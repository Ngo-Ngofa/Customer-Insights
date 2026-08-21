# The company, Bramble

*Fictional body and skincare brand built for the dashboard prototype. Everything here is invented: names, products, suppliers, retailers and figures. Nothing is drawn from any real company's data.*

---

## 1. At a glance

| | |
|---|---|
| **Name** | Bramble (placeholder, changeable in one place) |
| **What it sells** | Body and skincare, body wash, body lotion, hand care, a small face range, lip balm |
| **The twist** | The bottles are refillable. You buy a pump bottle once, then top it up from refill pouches |
| **Founded** | 2022, so currently in year four |
| **Markets** | UK primary, small Ireland and EU shipping |
| **Revenue** | £9.34m a year |
| **Team** | ~40 people, customer service team of 6 |

### Why this shape

Two deliberate choices, both about making sure the dashboard has something real to find.

**Refill pouches** give us a durable item (the bottle and its pump) and a consumable (the pouch), which behave completely differently when they go wrong. A pump that stops working after four months is a different kind of problem from a pouch that arrives leaking, and the fit between the two creates a third category that belongs to neither.

**A face range alongside body products** gives us a high-value, high-emotion product line next to a cheap, high-volume one. Complaints about a £28 moisturiser (didn't work, broke me out, irritated my skin) look nothing like complaints about a £6 lip balm (melted in the post). A dashboard that handles both is doing something useful.

---

## 2. Product range

24 active SKUs across five lines.

### 2.1 Body wash

Refillable 300ml pump bottle, topped up from 500ml pouches.

| SKU | Product | DTC price | Retail RRP |
|---|---|---|---|
| `BOW-BOTL-STD-300` | Body wash bottle, 300ml, includes first fill | £14.00 | £15.00 |
| `BOW-POUC-FIG-500` | Refill pouch, Fig & Vetiver, 500ml | £9.00 | £10.00 |
| `BOW-POUC-SEA-500` | Refill pouch, Sea Salt, 500ml | £9.00 | £10.00 |
| `BOW-POUC-UNS-500` | Refill pouch, Unscented, 500ml | £9.00 | £10.00 |

### 2.2 Body lotion

Refillable 250ml pump bottle, topped up from 400ml pouches.

| SKU | Product | DTC price | Retail RRP |
|---|---|---|---|
| `LOT-BOTL-STD-250` | Body lotion bottle, 250ml, includes first fill | £16.00 | £17.00 |
| `LOT-POUC-FIG-400` | Refill pouch, Fig & Vetiver, 400ml | £11.00 | £12.00 |
| `LOT-POUC-SEA-400` | Refill pouch, Sea Salt, 400ml | £11.00 | £12.00 |
| `LOT-POUC-UNS-400` | Refill pouch, Unscented, 400ml | £11.00 | £12.00 |

### 2.3 Hand care

| SKU | Product | DTC price | Retail RRP |
|---|---|---|---|
| `HAW-BOTL-STD-250` | Hand wash bottle, 250ml, includes first fill | £12.00 | £13.00 |
| `HAW-POUC-LEM-500` | Refill pouch, Lemon & Thyme, 500ml | £8.00 | £9.00 |
| `HAW-POUC-FIG-500` | Refill pouch, Fig & Vetiver, 500ml | £8.00 | £9.00 |
| `HAW-POUC-UNS-500` | Refill pouch, Unscented, 500ml | £8.00 | £9.00 |
| `HAC-TUBE-UNS-50` | Hand cream, 50ml (not refillable) | £9.00 | £10.00 |

### 2.4 Face, the value driver

Not refillable. Around a third of revenue.

| SKU | Product | DTC price | Retail RRP |
|---|---|---|---|
| `FAC-MOIS-NRM-50` | Daily moisturiser, Normal/Combination, 50ml | £28.00 | £30.00 |
| `FAC-MOIS-DRY-50` | Daily moisturiser, Dry, 50ml | £28.00 | £30.00 |
| `FAC-MOIS-SEN-50` | Daily moisturiser, Sensitive, 50ml | £28.00 | £30.00 |
| `FAC-CLNS-ALL-150` | Gentle cleanser, 150ml | £20.00 | £22.00 |
| `FAC-SERU-ALL-30` | Hydrating serum, 30ml | £34.00 | £36.00 |

### 2.5 Lip balm

Cheap and high volume. Included because it behaves completely differently in the data.

| SKU | Product | DTC price | Retail RRP |
|---|---|---|---|
| `LIP-STCK-MIN-8` | Lip balm, Mint, 8g | £6.00 | £7.00 |
| `LIP-STCK-BER-8` | Lip balm, Berry, 8g | £6.00 | £7.00 |
| `LIP-STCK-UNS-8` | Lip balm, Unscented, 8g | £6.00 | £7.00 |

### 2.6 Kits and gifts

| SKU | Product | DTC price | Retail RRP |
|---|---|---|---|
| `KIT-BOD-STR` | Body starter kit, wash and lotion bottles | £28.00 | £30.00 |
| `KIT-GFT-FACE` | Face gift set, cleanser and moisturiser | £44.00 | £48.00 |
| `KIT-GFT-TRIO` | Gift trio, hand wash, hand cream, lip balm | £26.00 | £28.00 |

### Subscription

Refill pouches only. Every 4, 8 or 12 weeks, at **10% off** the DTC price. Average subscription order is £24.60.

---

## 3. Costs and margins

Unit cost is landed cost, ingredients, packaging, filling and inbound freight. Trade price is what retailers pay, at 52% of RRP.

| SKU | DTC price | Unit cost | DTC margin | Trade price | Trade margin |
|---|---|---|---|---|---|
| `BOW-BOTL-STD-300` | £14.00 | £3.60 | 74% | £7.80 | 54% |
| `BOW-POUC-*-500` | £9.00 | £1.80 | 80% | £5.20 | 65% |
| `LOT-BOTL-STD-250` | £16.00 | £4.10 | 74% | £8.84 | 54% |
| `LOT-POUC-*-400` | £11.00 | £2.30 | 79% | £6.24 | 63% |
| `HAW-BOTL-STD-250` | £12.00 | £3.20 | 73% | £6.76 | 53% |
| `HAW-POUC-*-500` | £8.00 | £1.60 | 80% | £4.68 | 66% |
| `HAC-TUBE-UNS-50` | £9.00 | £1.90 | 79% | £5.20 | 63% |
| `FAC-MOIS-NRM-50` | £28.00 | £5.20 | 81% | £15.60 | 67% |
| `FAC-MOIS-DRY-50` | £28.00 | £5.40 | 81% | £15.60 | 65% |
| `FAC-MOIS-SEN-50` | £28.00 | £5.60 | 80% | £15.60 | 64% |
| `FAC-CLNS-ALL-150` | £20.00 | £3.80 | 81% | £11.44 | 67% |
| `FAC-SERU-ALL-30` | £34.00 | £6.90 | 80% | £18.72 | 63% |
| `LIP-STCK-*-8` | £6.00 | £1.10 | 82% | £3.64 | 70% |
| `KIT-BOD-STR` | £28.00 | £7.20 | 74% | £15.60 | 54% |
| `KIT-GFT-FACE` | £44.00 | £8.60 | 80% | £24.96 | 66% |
| `KIT-GFT-TRIO` | £26.00 | £5.90 | 77% | £14.56 | 59% |

Bottles carry the lowest margin, which is deliberate and typical, you take the hit on the bottle to win the customer, and make it back on years of refills. It also means a bottle failure is disproportionately expensive: you've already paid to acquire that customer and haven't yet earned it back.

---

## 4. Revenue

| Channel | Revenue | Share | Note |
|---|---|---|---|
| **Own website, subscription** | £3,578,640 | 38% | 18,500 DTC orders a month at £26 average, 62% of that value on subscription |
| **Own website, one-off** | £2,193,360 | 24% | |
| **Retail** | £2,818,200 | 30% | At trade price. Equivalent to £5.42m at RRP. ~42,700 units a month |
| **Marketplace** | £752,000 | 8% | Reduced range |
| **Total** | **£9,342,200** | | |

**Rough split by product line:** Face 32% · Body wash 22% · Body lotion 18% · Hand care 16% · Kits 7% · Lip 5%.

### Retail partners (fictional)

| Partner | Type | Range carried |
|---|---|---|
| **Halden's** | National pharmacy chain, ~700 stores | 14 SKUs including the face range |
| **Marlow's** | Grocery multiple | 8 SKUs, body and hand only |
| **Bexley & Co** | Department store | Face range and gift sets |
| **Independents** | ~180 health and refill shops | Varies |

Retail sells a slightly different product. Bottles are sold in cartons with a first fill included, pouches are stocked more thinly, and there is no subscription. That difference alone generates complaints DTC customers never have, most obviously "I bought the bottle here and now I can't find the refills".

---

## 5. Supply chain

Four separate supply points, which matters because it gives problems somewhere specific to trace back to.

| Site | Makes | Lines |
|---|---|---|
| **Fillmore (Midlands)** | Body wash, body lotion, hand wash, bulk fill | A, B |
| **Kestrel Pack (Netherlands)** | Refill pouches, converting and filling | P1, P2 |
| **Costa Norte (Portugal)** | Bottles, pumps and closures, moulding | C |
| **Aldworth Labs (Sussex)** | Face range and lip balm | D |

### Batch codes

Format `YYWW-L`, year, week, line. So `2612-A` is week 12 of 2026 on line A.

This is more important than it looks. If the dashboard is going to catch a problem early, it has to be able to get from "customers are unhappy" to "units from one specific production run", and that only works if there's a batch code to group them by. Realistically, customers almost never quote it unprompted, the service team has to ask, and often can't get it because the pouch has already been thrown away. That gap is itself worth showing.

---

## 6. Scale

**These are modelled estimates, not measurements.**

| Measure | Estimate |
|---|---|
| Customers ever | ~121,000 |
| Active subscribers | ~29,000 |
| DTC orders per month | ~18,500 |
| Retail units sold per month | ~42,700 |
| **Customer service contacts per month** | **~4,500** (about 150 a day) |
|, email | ~2,250 |
|, live chat | ~1,500 |
|, phone | ~750 |
| Trustpilot reviews per month | ~220 |
| Google reviews per month | ~40 |
| Product reviews on our own website | ~480 |
| Post-contact satisfaction responses per month | ~180 |

The three kinds of review are worth keeping apart, because they are about different things:

| Source | Where it lives | What it's mostly about |
|---|---|---|
| **Trustpilot** | Public, third-party | Everything. Delivery and service, but heavily product too |
| **Google** | Public, third-party | The brand in general. Low volume, often very short |
| **Product reviews** | Our own website, on each product page, collected by a review widget and shown to shoppers | The product itself, always tied to a specific SKU |

The important difference is **attribution, not subject matter**. Trustpilot reviews talk about products just as much as service, but they aren't attached to a SKU, so a product fault mentioned there has to be inferred from the text. Website product reviews are attached to a SKU by definition.

That means neither source owns product problems, and watching only one of them will miss things. It's also the strongest argument for the cross-source view: a genuine product fault should surface in Trustpilot, in product reviews and in support tickets at roughly the same time, and that agreement across three independent places is what separates a real problem from noise.

That's a contact rate of roughly 243 per 1,000 DTC orders, about 24%. High for a straightforward retailer, normal for a subscription business, because a large share of contacts are people wanting to skip a delivery, change their frequency, update a card or cancel. Those aren't complaints at all, and separating them from complaints is one of the first jobs the dashboard has to do.

Over the 18 months of history the dashboard will show, that works out at roughly 81,000 service contacts and 4,700 public reviews.

**Team sizing check:** most contacts aren't worked from scratch. Subscription admin, delivery chasing and return requests are handled with macros and automation in two or three minutes. Only the substantive contacts take real time.

| | Share | Volume | Handling time | Monthly hours |
|---|---|---|---|---|
| Macro or automation handled | 60% | 2,700 | ~3 min | 135 |
| Worked by an agent | 40% | 1,800 | ~11 min | 330 |
| **Total** | | **4,500** | | **465** |

At 133 productive hours per agent per month that's 3.5 agents, so the team is **4 people**, costing roughly **£128,000 a year**.

---

## 7. What things cost when they go wrong

This is what turns the dashboard from interesting into useful. Without it, the dashboard can only say *"complaints about this are up 40%"*. With it, it can say *"this is costing about £14,000 a month, and catching it three weeks earlier would have saved £35,000"*.

### Cost to handle a contact

Based on a loaded agent cost of £32,000 a year and 1,600 productive hours, which is £0.33 a minute. The loaded figure adds 25% for helpdesk software, quality checking and management.

| Type | Handling time | Concurrency | Labour cost | Fully loaded |
|---|---|---|---|---|
| Macro or automation handled | 3 min | 1 | £1.00 | **£1.25** |
| Email, worked | 11 min | 1 | £3.67 | **£4.59** |
| Live chat, worked | 12 min | 2 | £2.00 | **£2.50** |
| Phone | 18 min | 1 | £6.00 | **£7.50** |

The gap between £1.25 and £7.50 is the reason the dashboard has to weight themes rather than count them. Two thousand subscription skips cost less to serve than three hundred phone complaints.

### Cost to put something right

| Item | Cost |
|---|---|
| Replacement product | unit cost, £1.60 to £6.90 |
| Outbound postage | £3.20 |
| Pick and pack | £1.10 |
| Goodwill credit, when given | £6.00 average, on ~30% of complaints |
| Return handling, when we ask for it back | £2.90 |

Opened personal care can't go back into stock, so a returned item is a write-off, not a recovery. That makes "replace, don't ask for it back" the cheaper option in most cases, a policy the dashboard can help test.

### What a customer costs to get, and how long they take to pay it back

| | |
|---|---|
| Blended acquisition cost | **£34.00** |
| Paid-only acquisition cost | £44.00 (about 70% of new customers come through paid) |
| First order value | £31.00, higher than repeat, because it usually includes a bottle |
| First order gross margin | 72%, lower than repeat, because bottles are the thin-margin item |
| **First order gross profit** | **£22.32** |
| Repeat order value | £24.60 |
| Repeat order gross margin | 79% |
| **Repeat order gross profit** | **£19.43** |

**A first order does not pay for itself.** At £22.32 of gross profit against £34 of acquisition cost, a new customer is £11.68 in the red the moment they've been served. The CAC is recovered on the **second order**.

| Customer type | When CAC is recovered | Elapsed time |
|---|---|---|
| Subscriber, 8-week cadence | Order 2 | ~8 weeks (1.8 months) |
| One-off buyer, ~16-week gap | Order 2 | ~16 weeks (3.7 months) |

Around **42% of new customers never place a second order**. Every one of those is a £11.68 loss, not a small profit.

### The true cost of losing a customer

| | |
|---|---|
| Lifetime gross profit (1 first order + 7.6 repeats) | £170.02 |
| Less acquisition cost | −£34.00 |
| **Lifetime net contribution** | **£136.02** |
| LTV to CAC ratio | 5.0 : 1 |

What it actually costs when someone leaves depends entirely on when they leave:

| They leave after order | Gross profit earned | Net position | **Contribution lost** |
|---|---|---|---|
| 1 | £22.32 | −£11.68 | **£147.70** |
| 2 | £41.75 | £7.75 | **£128.26** |
| 3 | £61.19 | £27.19 | **£108.83** |
| 4 | £80.62 | £46.62 | **£89.40** |
| 6 | £119.49 | £85.49 | **£50.53** |
| 8 | £158.36 | £124.36 | **£11.66** |

**This is the most commercially important table in the document.** A bad experience on someone's first order costs nearly three times as much as the identical experience on their sixth, because on order one you're still carrying unrecovered acquisition cost as well as forfeiting the whole future relationship.

It has a direct consequence for the dashboard: the same complaint is not worth the same amount. A leaking pouch in a first delivery is a £148 problem; the same leaking pouch on order six is a £51 problem. So the dashboard needs to know **which order in the relationship a complaint arrived on**, and weight the money accordingly. That turns "40 complaints about leaking pouches" into "£4,100 of lost contribution, and it's concentrated in new customers", which is a completely different conversation, and points at a completely different fix.

It also justifies a panel we hadn't discussed: **complaints by order number**. If problems cluster on first orders, the acquisition spend is being poured into a leaking bucket.

### Cost of a retail problem

A withdrawal from a single retailer runs to roughly £18,000, stock uplift, the retailer's admin charge, replacement stock, and logistics. That excludes the harder-to-price risk of losing the listing at the next range review.

### Cost of a falling review score

Left as an assumption to test rather than a fixed number, because the honest answer is that it depends. The mechanism is real, a Trustpilot score falling from 4.6 to 4.3 measurably affects conversion, but the size of the effect varies enormously by category and traffic source. The dashboard should show the score trend and let you set your own sensitivity rather than assert a figure it can't stand behind.

---

## 8. Worked example, what early detection is actually worth

**The problem:** batch `2612-A` of body lotion refill pouches has a weak seal. About a third leak in transit. 14,000 pouches in the batch, shipping over six weeks, reaching retail from week three onwards.

| | Caught end of week 2 | Caught end of week 6 |
|---|---|---|
| Units shipped | 4,700 | 14,000 |
|, of which into retail | 0 | 4,100 |
| Faulty units in customers' hands | ~1,600 | ~4,800 |
| Customer complaints | ~670 | ~2,000 |
| Handling and replacement | £8,390 | £24,990 |
| Subscribers lost | 62 | 130 |
| Contribution lost with them, at £105 each | £6,510 | £13,650 |
| Retail withdrawal |, | £18,000 |
| Remaining stock | 9,300 units quarantined and re-sealed, £5,580 | nothing left to save |
| **Total cost** | **£20,480** | **£56,640** |

**Catching it four weeks earlier is worth about £36,200 on this one batch.**

The £105 figure is the average contribution lost per cancelling customer, taken from the table above and weighted towards orders two to five, refill pouches are mostly bought by people already a few orders in. If the same fault had hit a first-order product like a starter kit, that figure would be nearer £148 and the whole example would be about a third more expensive.

The stock line is the part most people miss. Catch it early and the remaining 9,300 pouches are a rework job at about 60p a unit. Catch it late and they've all shipped, so there's nothing left to save, you've simply converted good inventory into complaints.

For context, the whole customer service team costs roughly £128,000 a year. One batch caught four weeks early pays for about a third of it.

---

## 9. Themes and complaints

*To be filled in next, from your real-world experience. Everything above exists to support this section.*

---

## 10. Anonymisation

Brand, product, scent, retailer and supplier names are all invented. Volumes, prices and costs are illustrative estimates built to be internally consistent, not drawn from any real company. All customer names, emails and order references in the demo dataset will be generated.
