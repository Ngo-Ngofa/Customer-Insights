# Themes and complaints

*The theme list the dashboard trends. Two levels: 12 categories and around 70 themes.*

---

## 1. How it's organised

Two levels.

**Category**, 12 of them. This is what the top-level charts trend, and what a weekly meeting talks about.

**Theme**, around 70. This is what actually gets detected, alerted on and drilled into. A category is too coarse to act on; "Sensory is up 20%" tells you nothing, whereas "scent different from before, on one batch of body wash" tells you exactly what to do.

Every theme carries five attributes, because they're what make it useful rather than just a label:

| Attribute | Why it's there |
|---|---|
| **Fixed by** | Which team owns it. A theme nobody owns never gets fixed |
| **Fault signal** | Whether a rise in this theme suggests a real product or process fault, as opposed to normal grumbling. Marked ⚑ or ⚑⚑ |
| **Safety path** | Whether it has to escalate regardless of volume. Marked ⚠ |
| **Cost driver** | Replacement, refund, churn, or none. This is what lets the dashboard put money against a theme |
| **Order-number sensitive** | Whether it typically hits new customers, where the cost is nearly three times higher |

---

## 2. Four judgement calls

All four are arguable, and each one changes what the dashboard can detect.

**Pump and bottle failures moved out of Efficacy into Design & usability.** You had "the refill bottle is broken / the pump doesn't work" under Efficacy. I've moved it because the fix belongs to a different team and a different supplier, a pump failure traces to the moulding site in Portugal, not to the formulation. Leaving it under Efficacy would hide a pump supplier problem inside formulation noise, which is exactly the failure the dashboard exists to prevent.

**Skin reactions split out of Efficacy into their own category.** Under UK cosmetics rules the Responsible Person has obligations to review, report and act on undesirable effects and serious undesirable effects. A reaction is therefore not a complaint you triage by volume, a single serious one matters. It needs its own escalation route, not a place in a ranked list.

**"Damaged" and "opened or used" split out of Operational into Condition on arrival.** You had these grouped with delivery. The problem is that "damaged" can mean transit handling *or* a manufacturing fault, and telling those two apart is probably the single most valuable distinction in the whole taxonomy. Keeping them inside delivery would attribute a factory problem to the courier.

**"Smells off" stays an ordinary sensory theme.** I originally treated it as a spoilage signal, which was wrong, most of the time the customer simply doesn't like the smell. It only becomes a quality signal if the *volume* rises, or if the specific words used are spoilage words (rancid, sour, chemical) rather than dislike words. That's the same preference-versus-fault problem covered in section 5, and it's handled by the same rule rather than by a permanent flag.

---

## 3. Beyond the product

A complaint list drawn from experience tends to be strong on the product, which makes sense, that's what a personal care brand thinks about. What it doesn't cover is the large volume of contacts that aren't about the product at all. In a subscription business that's most of them.

Added categories: **Subscription & billing**, **Returns & refunds**, **Availability & where to buy**, **Service experience** (complaints about us), and **Praise**. Positive feedback matters more than it sounds, without it the dashboard can only measure how bad things are, never whether anything is good, and sentiment becomes meaningless.

---

## 4. The taxonomy

### EFF, Efficacy & results

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| EFF-01 | Doesn't work at all | Yours | NPD / Quality | |
| EFF-02 | Doesn't work as well as I hoped | Yours | Marketing / NPD | Often an expectation problem, not a product one |
| EFF-03 | Worked before, doesn't now | Yours | Quality | ⚑⚑ Strong reformulation or batch signal |
| EFF-04 | Wrong product for my skin type | Added | Marketing | Points at product guidance, not the product |
| EFF-05 | Stained clothing, bedding or towels | Yours | Quality / NPD | ⚑ |
| EFF-06 | Left residue, didn't rinse off | Added | NPD | ⚑ |
| EFF-07 | Ran out far faster than expected | Added | Ops / Quality | ⚑⚑ Classic underfill signal |

### RXN, Reactions & safety ⚠

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| RXN-01 | Rash, irritation or burning | Yours | Quality / RP | ⚠ |
| RXN-02 | Breakout or spots | Yours | Quality / RP | ⚠ |
| RXN-03 | Allergic reaction to a known ingredient | Yours | RP | ⚠ |
| RXN-04 | Didn't realise it contained X | Yours | Labelling / RP | ⚠ Labelling issue as much as a reaction |
| RXN-05 | Reaction needing medical attention | Added | RP, immediate | ⚠⚠ Potential serious undesirable effect |
| RXN-06 | Eye irritation or accidental ingestion | Added | RP | ⚠ |
| RXN-07 | Reaction in a child | Added | RP, immediate | ⚠⚠ |

### SEN, Sensory

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| SEN-01 | Scent too strong | Yours | NPD | Usually preference |
| SEN-02 | Scent too weak or fades | Yours | NPD | Usually preference |
| SEN-03 | Scent different from before | Yours | Quality | ⚑⚑ Reformulation or batch |
| SEN-04 | Smells off or unpleasant | Yours | NPD, or Quality if it spikes | Usually preference. Only a spoilage signal if it rises, or if the words are specific (rancid, sour, chemical) |
| SEN-05 | Texture gritty, lumpy or separated | Yours | Quality, urgent | ⚑⚑ |
| SEN-06 | Texture too thin or too thick | Yours | Quality | ⚑ |
| SEN-07 | Colour looks wrong or has changed | Yours | Quality | ⚑⚑ |
| SEN-08 | Simply don't like the scent | Added | Nobody | Noise. Must be separated from SEN-03 |

### DES, Design & usability

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| DES-01 | Pump doesn't work or has stopped working | Yours | Packaging / Costa Norte | ⚑⚑ |
| DES-02 | Pump dispenses too much or too little | Added | Packaging | ⚑ |
| DES-03 | Bottle too big or awkward to hold | Yours | Design | |
| DES-04 | Doesn't stand up properly | Yours | Design | |
| DES-05 | Pouch hard to open, spills when refilling | Added | Packaging / Kestrel | ⚑ Refill-model specific |
| DES-06 | Cap or closure doesn't seal | Added | Packaging | ⚑ |
| DES-07 | Packaging feels cheap or flimsy | Yours | Design | |
| DES-08 | Label unclear or hard to read | Added | Design / Labelling | |
| DES-09 | Too much packaging, or not recyclable | Added | Design | Brand risk more than service cost |

### CON, Condition on arrival

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| CON-01 | Arrived leaking | Yours | Quality / Packaging | ⚑⚑ Must be split: seal fault vs transit |
| CON-02 | Arrived damaged or broken | Yours | Ops / Logistics | ⚑ Same split |
| CON-03 | Arrived opened or used | Yours | Ops / Warehouse | ⚑ Often a returns-handling failure |
| CON-04 | Seal broken or missing | Added | Quality | ⚑⚑ |
| CON-05 | Underfilled, less product than stated | Added | Quality / Fillmore | ⚑⚑ |
| CON-06 | At or past best-before date | Added | Ops / Stock rotation | ⚑ |
| CON-07 | Outer box damaged, product fine | Added | Logistics | Low cost, high annoyance |

### DEL, Order & delivery

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| DEL-01 | Not delivered | Yours | Logistics | |
| DEL-02 | Delayed | Yours | Logistics | |
| DEL-03 | Lost in transit | Yours | Logistics | |
| DEL-04 | Items missing from order | Yours | Warehouse | ⚑ Pick accuracy |
| DEL-05 | Wrong items received | Yours | Warehouse | ⚑ Pick accuracy |
| DEL-06 | Delivered to the wrong address | Added | Logistics | |
| DEL-07 | Marked delivered but not received | Added | Logistics | |
| DEL-08 | Courier problem, no card left | Added | Logistics | |
| DEL-09 | Tracking not updating | Added | Logistics / Tech | Cheap to fix, drives avoidable contacts |

### SUB, Subscription & billing *(added category)*

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| SUB-01 | Wants to cancel | Added | CS / Retention | Churn |
| SUB-02 | Wants to pause, skip or delay | Added | Self-service | Highest volume theme in the business |
| SUB-03 | Wants to change frequency or products | Added | Self-service | |
| SUB-04 | Didn't realise it was a subscription | Added | Marketing / Tech | Reputationally dangerous |
| SUB-05 | Charged the wrong amount | Added | Tech / Finance | |
| SUB-06 | Charged twice | Added | Tech / Finance | |
| SUB-07 | Payment failed | Added | Tech | |
| SUB-08 | Arrives too often, I have too much | Added | Retention | Cadence mismatch, predicts cancellation |
| SUB-09 | Discount code didn't apply | Added | Tech / Marketing | |
| SUB-10 | Can't find how to manage my subscription | Added | Tech | Fully avoidable contact |

### RFD, Returns & refunds *(added category)*

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| RFD-01 | Refund not received | Added | Finance | |
| RFD-02 | Refund slower than expected | Added | Finance | |
| RFD-03 | Refund amount wrong | Added | Finance | |
| RFD-04 | How do I return this | Added | Self-service | |
| RFD-05 | Return label problem | Added | Logistics | |
| RFD-06 | Unhappy with the refund decision or policy | Added | CS / Policy | Escalation risk |

### AVL, Availability & where to buy *(added category)*

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| AVL-01 | Out of stock online | Added | Supply chain | |
| AVL-02 | Can't find refills in store | Added | Commercial / Retail | Retail-specific, hits the refill model directly |
| AVL-03 | Product or variant discontinued | Added | Commercial | |
| AVL-04 | Where can I buy this | Added | Marketing | Pre-sales, not a complaint |
| AVL-05 | Price differs between channels | Added | Commercial | |
| AVL-06 | Not available in my country | Added | Commercial | |

### SVC, Service experience *(added category)*

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| SVC-01 | No reply, had to chase | Added | CS | |
| SVC-02 | Slow response | Added | CS | |
| SVC-03 | Unhelpful or rude | Added | CS | |
| SVC-04 | Had to repeat myself, passed around | Added | CS | |
| SVC-05 | Problem still not resolved | Added | CS | Strong churn predictor |

### VAL, Price & value

| Code | Theme | Origin | Fixed by | Notes |
|---|---|---|---|---|
| VAL-01 | Not enough product for the price | Yours | Commercial | ⚑ Watch, can indicate underfill, not pricing |
| VAL-02 | Overpriced for what it is | Yours | Commercial / Marketing | |
| VAL-03 | Refill isn't enough cheaper than the bottle | Added | Commercial | Undermines the whole proposition |
| VAL-04 | Delivery charge too high | Added | Commercial | |
| VAL-05 | Price has gone up | Added | Commercial | Spikes after any price change |

### PRA, Praise *(added category)*

| Code | Theme | Origin | Notes |
|---|---|---|---|
| PRA-01 | Loves the product | Added | |
| PRA-02 | Loves the scent | Added | |
| PRA-03 | Works well for sensitive skin | Added | Useful counterweight to RXN volume |
| PRA-04 | Praise for service or a named agent | Added | |
| PRA-05 | Praise for packaging or sustainability | Added | |
| PRA-06 | Fast delivery | Added | |

---

## 5. The hardest judgement in the whole system

**Preference versus fault.** These two look almost identical in text and mean completely different things:

> *"The scent is much weaker than I remember."*, a fault signal. Something changed.
>
> *"The scent is a bit weak for me."*, a preference. Nothing changed.

The first, if it rises, means a reformulation or a bad batch. The second is constant background noise that will always be there.

Getting this wrong in either direction breaks the dashboard. Treat them all as faults and you get alerts every week that lead nowhere, and people stop looking. Treat them all as preference and you miss the reformulation.

This is why SEN-03 and SEN-08 are separate themes rather than one. The tell is nearly always a **comparison to a previous experience**: "than before", "used to", "not like the last one". That's the specific thing the extraction has to look for, and it's worth stating as an explicit rule rather than hoping a model picks it up.

The same split applies to VAL-01. "Not enough product for the price" is usually a pricing opinion, but if it rises sharply on one SKU it may be an underfill problem wearing a pricing complaint's clothes. Cross-checking it against CON-05 and EFF-07 is how you tell.

---

## 6. Reactions need their own route

Every other theme in this document is handled by volume, a few is normal, a spike matters. Reactions can't work that way, for two reasons.

**The regulatory one.** Under the UK Cosmetics Regulation the Responsible Person has duties to review, report and act on undesirable effects and serious undesirable effects. Serious ones carry reporting obligations to the authorities. A single case can trigger those duties; volume is irrelevant. Your RP will know the specifics, and the dashboard should support that process rather than try to replace it.

**The practical one.** Reactions are the only theme where a delay causes harm to a person rather than to a number.

So RXN themes get: immediate flagging regardless of volume, a record that can be exported for the product file, mandatory capture of product, batch and date, and a separate view that doesn't compete with the ranked lists. They appear in the trend charts like anything else, a rise in reactions on one batch is exactly the kind of thing the dashboard should catch, but they never wait their turn.

---

## 7. Where each theme shows up

Rough expected mix, modelled rather than measured.

**Support contacts, ~4,500 a month**

| Category | Share | Volume |
|---|---|---|
| Subscription & billing | 32% | ~1,440 |
| Order & delivery | 26% | ~1,170 |
| Returns & refunds | 11% | ~495 |
| Condition on arrival | 7% | ~315 |
| Efficacy & results | 5% | ~225 |
| Sensory | 4% | ~180 |
| Availability | 4% | ~180 |
| Design & usability | 3% | ~135 |
| Service experience | 3% | ~135 |
| Price & value | 2% | ~90 |
| Reactions & safety | 2% | ~90 |
| Praise | 1% | ~45 |

**This is the most important thing on the page.** Only about 21% of contacts are about the product at all. Everything else is subscription admin, delivery chasing and refunds.

Which means a dashboard that ranks themes by raw volume will show "wants to skip a delivery" at the top every single week, and will never show the product fault. That's how these dashboards die. It's the clearest argument for ranking by **cost** rather than count, and for putting the emerging-themes panel above the volume panel.

**Reviews** invert this completely, they skew heavily towards the product, roughly 45% product, 30% delivery, 15% service, 10% value. That inversion is useful: support tells you about your processes, reviews tell you about your products, and you need both.

---

## 8. What this means for the build

Four things fall out of the taxonomy:

- **Rank by money, not volume.** Otherwise subscription admin drowns everything.
- **Split "damaged" by cause.** Transit versus manufacturing. Without that split, factory faults get blamed on couriers.
- **Detect the comparison phrase.** "Different from before" is the single most valuable pattern in the text, because it's what separates a fault from a preference.
- **Reactions bypass the queue.** Always, regardless of volume.

---

## 9. Open questions

- Which themes are everyday noise and which are rare but serious? That ratio drives whether the demo data is believable
- Does the contact mix in section 7 match what a business this size actually sees?
