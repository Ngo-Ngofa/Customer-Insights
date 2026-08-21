# Bramble Customer Insight

A working prototype of a customer insight dashboard for a consumer brand. It pulls customer feedback from six places, turns free text into something countable, spots problems while they are still small, and puts a pound figure against them.

Everything here runs on generated data for a fictional company. No real customer data of any kind was used.

**[Open the dashboard](dashboard.html)** (single file, opens in any browser, no server needed)

![Overview](screenshots/01-overview.png)

---

## The problem it solves

A consumer brand hears from its customers in six or seven different places at once. Support tickets, phone calls, emails, Trustpilot, Google, reviews on its own product pages. Each one has its own inbox, its own dashboard and its own version of the truth, and none of them talk to each other.

The result is that a genuine product fault, say a batch of refill pouches with a weak seal, shows up as a slight uptick in three separate systems that nobody is looking at together. By the time it is obvious it has been shipping for six weeks.

This dashboard is built to catch that in week two.

## What it does

**Brings six sources into one shape** without trying to match customers between them. A Trustpilot reviewer is never linked to a caller. The join is the theme, not the person, which removes the hardest problem in this space entirely.

**Turns text into something countable** by asking every source the same fixed set of questions. What is this about, which product, how do they feel, how serious is it, which order in the relationship were they on.

**Knows what normal looks like** for each theme individually and flags what is running outside it, measured as a share of all feedback rather than a raw count so a busy week does not set off every alarm.

**Puts money against it,** so themes can be ranked by cost rather than volume. This matters more than it sounds. Around a third of contacts are people wanting to skip a delivery, so a dashboard ranked by count shows that at the top every single week and never surfaces the product fault.

## What is on screen

Two tabs.

### What customers are saying

The standing picture. Six figures across the top, each with a target or a comparison so you can tell good from bad, then a ranked breakdown of what customers are talking about, how each source feels, which products are generating complaints, and a feed of what people actually said.

### Needs attention

![Needs attention](screenshots/03-alerts-live.png)

What is running outside its usual range right now, a twelve month log of every alert raised, and the theme matrix plotting every theme by size against feeling.

### Drilling in

Clicking any theme opens the investigation view: volume against its own usual range, which source picked it up first, which products and production batches it is concentrated in, and the verbatims behind it.

![Theme drill down](screenshots/04-theme-drilldown.png)

Clicking the cost tile shows the full calculation rather than asserting a number.

![Cost breakdown](screenshots/05-cost-breakdown.png)

## How the detection works

Each theme is compared against its own recent history, not a global threshold. Delivery delays are seasonally spiky every December, leaking pouches are not, and one threshold cannot serve both.

The measure is share of all feedback. The normal range is the median of the previous thirteen weeks plus or minus 2.6 times a robust spread measure, which ignores past spikes rather than being widened by them. A theme with no history flags on volume and speed instead. Safety themes flag at a much lower bar and never wait their turn.

The strongest signal is corroboration: a real fault shows up in support, in reviews and on Trustpilot at roughly the same time, and the dashboard shows how many independent sources each alert appears in.

Full formulas are in [04-architecture.md](04-architecture.md).

## How the money works

Three things kept separate rather than blended.

| | |
|---|---|
| Team time | £1.25 when a macro handles it up to £7.50 for a phone call. Reported outside the headline, because it sits in payroll whatever happens |
| Putting it right | Replacement or refund, plus postage and pick and pack, plus goodwill on about a quarter of cases |
| Customers who leave | Lifetime contribution not yet earned. £147.70 if they go after one order, £11.66 after eight |

That last line is the important one. A problem on someone's first order costs about thirteen times what the same problem costs on their eighth, because the acquisition cost is still unrecovered and the whole future relationship is forfeited. It is why the extraction captures which order a customer was on.

## The data

There is no live connection. `pipeline/generate.py` produces 78 weeks of feedback across six sources with realistic volumes, seasonality, product mix, sentiment and cost.

Five real problems are planted in it so the detection has something true to find:

| | What it tests |
|---|---|
| A weak seal on one batch of body lotion pouches | A sharp spike, traceable to a batch code |
| Hand wash pumps seizing after a moulding change | A slow ramp rather than a spike |
| A moisturiser reformulation | A subtle shift across two related themes at once |
| A reaction cluster on the sensitive moisturiser | Low volume, high severity, the safety route |
| A Christmas courier backlog and a promotion week | Two decoys that should **not** read as new problems |

## Running it

```
# open the dashboard
open dashboard.html

# regenerate the data and rebuild
python3 pipeline/generate.py
python3 -c "
tpl=open('pipeline/template.html').read()
data=open('data/aggregates.json').read()
open('dashboard.html','w').write(tpl.replace('/*__DATA__*/', data))"
```

No dependencies beyond Python 3. The dashboard is one self contained HTML file with the data baked in, about 250KB, and needs no build step and no server.

## Repository

```
README.md              this file
01-company.md          the fictional company: products, SKUs, pricing, costs, unit economics
02-themes.md           the theme taxonomy, 12 categories and about 70 themes
03-brand.md            palette, typography and UI rules
04-architecture.md     how the real systems would connect, with formulas
dashboard.html         the prototype, single file
data/aggregates.json   generated dataset, pre aggregated
pipeline/generate.py   the data generator
pipeline/verbatims.py  sample customer wording per theme
pipeline/template.html the dashboard source, before the data is inlined
screenshots/           images used in this readme
```

## Design notes

**It has to explain itself.** There is no help page and no explanatory captions under charts. Every metric label states what is being counted and over what period, and every figure has a target or a comparison so you can tell whether it is good. If a chart needs a note to make sense, the chart is wrong.

**Sources are never blended into one number.** Public reviews and support tickets disagree by design, and averaging them hides exactly the thing you want to see.

**Ranked by cost, not volume.** Otherwise subscription admin drowns everything.

**Alerts explain themselves.** Each one shows the usual range in plain numbers, how many sources see it, which product and batch, and what it has cost. An alert nobody can act on gets ignored within a fortnight.

## Status

Prototype. The front end, the detection and the cost model are real code running on generated data. Nothing is connected to a live system. [04-architecture.md](04-architecture.md) sets out what connecting it would involve and roughly what each phase would take.

![Dark mode](screenshots/06-dark-mode.png)
