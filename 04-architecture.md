# Architecture

How the prototype is built, and how the same thing would be wired to real systems.

---

## 1. The shape of the system

Six layers. Naming them separately matters, because "how do we connect Zendesk" and "how do we decide something is wrong" are different problems and get solved in different places.

| Layer | Does | The question it answers |
|---|---|---|
| **1 Sources** | HubSpot, Zendesk, Jiminny, email, Trustpilot, Google, product reviews | What data exists at all |
| **2 Ingestion** | Pulls on a schedule or receives a webhook | How does it get out, how often, what breaks |
| **3 Landing** | Raw copies, untouched, kept | Can we rebuild everything if a definition changes |
| **4 Modelling** | Reshapes everything into two tables | What common shape does this all fit into |
| **5 Enrichment** | Theme, sentiment, product, severity | How does text become countable |
| **6 Presentation** | The dashboard | What does somebody do on Monday |

Layer 3 looks like bureaucracy and is the one people regret skipping. Transform on the way in and you cannot re-run history when the theme list changes. Keep the raw copies and every definition downstream stays reversible.

---

## 2. Sources and how each one connects

| Source | Route out | Auth | Cadence | The catch |
|---|---|---|---|---|
| **HubSpot** CRM and tickets | CRM v3 object APIs, plus Webhooks v3 for change events | Private app token, or OAuth for a listed app | Webhook push with a nightly reconcile | Conversations and inbox data sit behind a weaker API than CRM objects. People assume it is all one thing and it is not |
| **Zendesk** tickets and CSAT | Incremental Exports API, cursor based, built for keeping an external copy in sync. Satisfaction Ratings endpoint for scores | API token or OAuth | Poll every 15 minutes on the cursor | CSAT response rates are in single digits, so it can never be the only satisfaction measure |
| **Jiminny** call transcripts | Jiminny API, or its HubSpot integration where the transcript already lands on the record | API key | Nightly batch | Long, messy text. Agent speech has to be separated from customer speech or the sentiment is meaningless |
| **Email** | Gmail API or Microsoft Graph | OAuth, service account for a shared mailbox | Poll or push subscription | Usually redundant. Only connect a mailbox that sits outside the helpdesk, or everything is double counted |
| **Trustpilot** | Business Units API, then Service Reviews and Product Reviews | API key on a business account | Hourly | Service reviews and product reviews are genuinely different objects with different shapes |
| **Google reviews** | Business Profile API, `accounts.locations.reviews.list` | OAuth, approval gated by Google | Hourly | Access is not automatic. The Places API alternative returns about five reviews, which is why a third party aggregation industry exists |
| **Website product reviews** | Review platform webhook on submission | Shared secret | Push | Question and form changes silently break trend lines |

### Orchestration

Webhook sources land straight into the landing store. Polled sources run on a scheduler holding a cursor per source. Every source also gets a nightly full reconcile, because webhooks get missed and nobody notices until a number looks wrong.

Freshness per source is written to a status table on every run. That table is what drives the source status chip in the dashboard header. If Trustpilot stops sending on Tuesday, sentiment quietly becomes wrong, and this is the only thing that would tell you.

### Build against buy

You would not hand write seven integrations. A managed pipeline tool covers HubSpot, Zendesk and Gmail off the shelf, and you hand roll only the two or three it does not support. That is a materially different cost and maintenance profile and worth saying out loud in any business case.

---

## 3. How sources become comparable

**Not by joining customers.** A Trustpilot reviewer is never matched to a caller. Identity resolution is the hardest problem in this space and this dashboard does not need it, because the join is the theme, not the person.

What makes sources comparable is that **every one of them is put through the same fixed set of questions**, and it is the answers that line up:

| Question asked of the text | Field | Type |
|---|---|---|
| What is this about | `theme` | fixed list, plus an emerging bucket |
| Which product | `sku` | SKU or null |
| How does the customer feel | `sentiment` | -1 to +1, with a confidence |
| How serious is it | `severity` | 1 to 4, safety words escalate automatically |
| What did they want | `intent` | refund, replacement, information, complaint, praise |
| Is this a repeat for them | `is_repeat` | boolean |
| Which order were they on | `order_no` | integer, this is what prices the complaint |

One contact can produce more than one answer. A call covering a billing query, a leaking pouch and praise for the agent is three records, not one. Getting that wrong is how a dashboard under counts the thing you most need to see.

Extraction runs where it is cheapest per source. Call transcripts already land in HubSpot through the Jiminny integration and can be processed there. Everything else is pulled as text and passed through the same prompt with the same output schema.

---

## 4. Data model

### `feedback` (one row per point raised)

| Field | Example |
|---|---|
| `feedback_id` | `zd_884213_2` |
| `source_system` | `zendesk` |
| `source_record_id` | `884213` |
| `occurred_at` | `2026-08-11T09:14Z` |
| `channel` | `phone`, `email`, `chat`, `review` |
| `direction` | `inbound`, `outbound` |
| `body_text` | the actual words |
| `rating_raw`, `rating_scale` | `4`, `1-5 CSAT` |
| `theme`, `theme_confidence` | `CON-01`, `0.91` |
| `sentiment`, `sentiment_confidence` | `-0.62`, `0.84` |
| `severity` | `3` |
| `intent` | `replacement` |
| `sku`, `batch_code` | `LOT-POUC-FIG-400`, `2612-A` |
| `order_no` | `2` |
| `region`, `language` | `UK`, `en` |
| `ingested_at` | pipeline timestamp |

### `theme` (reference)

Code, label, category, severity band, owning team, cost band, whether a rise implies a fault.

### `product` (reference)

SKU, name, line, price, unit cost, units sold per period. Units sold is what turns a raw complaint count into a rate.

---

## 5. Detection

Every theme is measured against **its own** history. A single global threshold would flag December delivery delays every year and miss a leaking pouch entirely.

The measure is **share of all feedback**, never raw count. A promotion that doubles contacts would otherwise light up every theme at once. The prototype includes exactly that as a decoy in week 58.

For theme *t* in week *i*:

```
share(i)   = count(t, i) / count(all, i)
window     = share(i-13) … share(i-1)
median     = median(window)
mad        = median(|share - median|)
sigma      = max(1.4826 * mad, median * 0.22, 0.00035)
upper      = median + 2.6 * sigma
flagged    = share(i) > upper AND count(t, i) >= 10
```

Median absolute deviation rather than standard deviation, because past spikes should not widen the band and hide the next one. The two floors stop a theme that normally sits at zero from flagging on a single record.

Three extra rules:

- **New themes.** No history means no baseline, so a theme with a near zero median flags on absolute volume and speed instead.
- **Safety.** Severity 4 themes flag at a much lower bar and never wait their turn.
- **Corroboration.** Appearing in three or more independent sources at once is the strongest signal that a problem is real rather than noise. The dashboard shows the source count on every alert.

Alerts are also tracked as runs, not as instants, which is what produces the twelve month alert log: when it was raised, its highest week, how long it ran, whether it is still going.

---

## 6. Cost model

Three separate things, deliberately not blended into one number.

**Team time** is real but sits in payroll whatever happens, so it is reported outside the headline total. £1.25 when a macro handles it, £2.50 chat, £4.59 email, £7.50 phone.

**Putting it right** is replacement or refund plus £3.20 postage and £1.10 pick and pack, with a £6 goodwill credit on roughly a quarter of cases.

**Customers who leave** is the expensive one, and it depends entirely on when they leave:

```
first order gross profit   = £22.32
repeat order gross profit  = £19.43
acquisition cost           = £34.00
lifetime net contribution  = £136.02

earned(n)   = 22.32 + (n - 1) * 19.43
lost(n)     = lifetime_net - (earned(n) - CAC)
```

Which gives £147.70 if they leave after one order and £11.66 after eight. A first order problem costs about thirteen times a late one, because you are still carrying unrecovered acquisition cost as well as forfeiting the future. That is why the extraction captures `order_no`, and why the dashboard can rank by money rather than volume.

Ranking by money is not cosmetic. Around a third of contacts are subscription admin, so a dashboard ranked by count shows "wants to skip a delivery" at the top every single week and never surfaces the product fault.

---

## 7. Governance

Call transcripts and support email are personal data, and in a personal care context they can become special category data by accident when a customer describes a skin reaction.

- PII redaction before any text reaches a language model
- Lawful basis and retention agreed per source, with call recording consent handled upstream
- Data residency fixed to the UK or EU
- Reaction records exportable for the product information file, since the Responsible Person has duties under the UK Cosmetics Regulation to review and report undesirable effects

---

## 8. Making it real

| Phase | Scope | Rough effort |
|---|---|---|
| **1** | Two sources, helpdesk and Trustpilot. Fixed theme list, no emerging bucket. Weekly refresh. Proves the extraction quality on real text | 3 to 4 weeks |
| **2** | All sources, daily refresh, alerting with the baseline model, cost model wired to real order and product data | 6 to 8 weeks |
| **3** | Emerging theme clustering, action logging, alert routing to owning teams | 4 to 6 weeks |

The thing to test first is phase 1, and specifically whether the extraction can reliably tell a preference from a fault. "The scent is weaker than I remember" and "the scent is a bit weak for me" are almost the same sentence and completely different problems. Everything else in this design is straightforward once that works.

---

## 9. The prototype

Everything above describes the real build. What is in this repository is a working front end on generated data.

- `pipeline/generate.py` builds 78 weeks of feedback across six sources, with five problems deliberately planted and one decoy
- Volumes, seasonality, product mix, sentiment and cost are all modelled rather than random
- The output is pre aggregated to about 200KB and baked into a single HTML file, so the dashboard opens from disk with no server
- The detection, the cost model and the drill downs are the real logic running on that data, not screenshots
