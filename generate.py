"""
Bramble - synthetic signal generator.

Produces 78 weeks of customer signals across six sources, then aggregates them
into the shapes the dashboard needs. Five real problems are planted in the data
so the dashboard has something genuine to find.
"""
import json, math, random, datetime as dt
from collections import defaultdict

random.seed(20260818)

WEEKS = 78
END = dt.date(2026, 8, 16)                       # week ending Sunday
week_start = [END - dt.timedelta(weeks=WEEKS - 1 - i) for i in range(WEEKS)]

# ---------------------------------------------------------------- products
SKUS = {
 "BOW-BOTL-STD-300": ("Body wash bottle 300ml",        "Body wash",   14.00, 3.60, 0.055),
 "BOW-POUC-FIG-500": ("Body wash refill - Fig",         "Body wash",    9.00, 1.80, 0.085),
 "BOW-POUC-SEA-500": ("Body wash refill - Sea Salt",    "Body wash",    9.00, 1.80, 0.070),
 "BOW-POUC-UNS-500": ("Body wash refill - Unscented",   "Body wash",    9.00, 1.80, 0.055),
 "LOT-BOTL-STD-250": ("Body lotion bottle 250ml",       "Body lotion", 16.00, 4.10, 0.045),
 "LOT-POUC-FIG-400": ("Body lotion refill - Fig",       "Body lotion", 11.00, 2.30, 0.075),
 "LOT-POUC-SEA-400": ("Body lotion refill - Sea Salt",  "Body lotion", 11.00, 2.30, 0.060),
 "LOT-POUC-UNS-400": ("Body lotion refill - Unscented", "Body lotion", 11.00, 2.30, 0.045),
 "HAW-BOTL-STD-250": ("Hand wash bottle 250ml",         "Hand care",   12.00, 3.20, 0.050),
 "HAW-POUC-LEM-500": ("Hand wash refill - Lemon",       "Hand care",    8.00, 1.60, 0.065),
 "HAW-POUC-FIG-500": ("Hand wash refill - Fig",         "Hand care",    8.00, 1.60, 0.045),
 "HAW-POUC-UNS-500": ("Hand wash refill - Unscented",   "Hand care",    8.00, 1.60, 0.035),
 "HAC-TUBE-UNS-50":  ("Hand cream 50ml",                "Hand care",    9.00, 1.90, 0.040),
 "FAC-MOIS-NRM-50":  ("Moisturiser - Normal/Comb",      "Face",        28.00, 5.20, 0.055),
 "FAC-MOIS-DRY-50":  ("Moisturiser - Dry",              "Face",        28.00, 5.40, 0.040),
 "FAC-MOIS-SEN-50":  ("Moisturiser - Sensitive",        "Face",        28.00, 5.60, 0.045),
 "FAC-CLNS-ALL-150": ("Gentle cleanser 150ml",          "Face",        20.00, 3.80, 0.045),
 "FAC-SERU-ALL-30":  ("Hydrating serum 30ml",           "Face",        34.00, 6.90, 0.035),
 "LIP-STCK-MIN-8":   ("Lip balm - Mint",                "Lip",          6.00, 1.10, 0.030),
 "LIP-STCK-BER-8":   ("Lip balm - Berry",               "Lip",          6.00, 1.10, 0.025),
 "LIP-STCK-UNS-8":   ("Lip balm - Unscented",           "Lip",          6.00, 1.10, 0.020),
 "KIT-BOD-STR":      ("Body starter kit",               "Kits",        28.00, 7.20, 0.020),
 "KIT-GFT-FACE":     ("Face gift set",                  "Kits",        44.00, 8.60, 0.010),
 "KIT-GFT-TRIO":     ("Gift trio",                      "Kits",        26.00, 5.90, 0.010),
}
SKU_LIST = list(SKUS)
SKU_W = [SKUS[s][4] for s in SKU_LIST]

# ---------------------------------------------------------------- themes
# code: (label, category, base share of all signals, severity 1-4, product-linked, resolution cost band)
T = {
 "EFF-01": ("Doesn't work at all",                    "Efficacy & results",      0.0090, 2, 1, "replace"),
 "EFF-02": ("Doesn't work as well as I hoped",        "Efficacy & results",      0.0150, 1, 1, "none"),
 "EFF-03": ("Worked before, doesn't now",             "Efficacy & results",      0.0055, 3, 1, "replace"),
 "EFF-04": ("Wrong product for my skin type",         "Efficacy & results",      0.0080, 1, 1, "refund"),
 "EFF-05": ("Stained clothing or bedding",            "Efficacy & results",      0.0035, 3, 1, "refund"),
 "EFF-06": ("Left residue, didn't rinse off",         "Efficacy & results",      0.0045, 2, 1, "none"),
 "EFF-07": ("Ran out far faster than expected",       "Efficacy & results",      0.0055, 2, 1, "replace"),
 "RXN-01": ("Rash, irritation or burning",            "Reactions & safety",      0.0060, 4, 1, "refund"),
 "RXN-02": ("Breakout or spots",                      "Reactions & safety",      0.0065, 3, 1, "refund"),
 "RXN-03": ("Allergic reaction to known ingredient",  "Reactions & safety",      0.0020, 4, 1, "refund"),
 "RXN-04": ("Didn't realise it contained X",          "Reactions & safety",      0.0025, 3, 1, "refund"),
 "RXN-05": ("Reaction needing medical attention",     "Reactions & safety",      0.0006, 4, 1, "refund"),
 "RXN-06": ("Eye irritation or ingestion",            "Reactions & safety",      0.0012, 4, 1, "refund"),
 "RXN-07": ("Reaction in a child",                    "Reactions & safety",      0.0008, 4, 1, "refund"),
 "SEN-01": ("Scent too strong",                       "Sensory",                 0.0110, 1, 1, "none"),
 "SEN-02": ("Scent too weak or fades",                "Sensory",                 0.0125, 1, 1, "none"),
 "SEN-03": ("Scent different from before",            "Sensory",                 0.0050, 3, 1, "replace"),
 "SEN-04": ("Smells off or unpleasant",               "Sensory",                 0.0075, 2, 1, "replace"),
 "SEN-05": ("Texture gritty, lumpy or separated",     "Sensory",                 0.0040, 3, 1, "replace"),
 "SEN-06": ("Texture too thin or too thick",          "Sensory",                 0.0055, 2, 1, "none"),
 "SEN-07": ("Colour looks wrong or has changed",      "Sensory",                 0.0030, 3, 1, "replace"),
 "SEN-08": ("Simply don't like the scent",            "Sensory",                 0.0140, 1, 1, "none"),
 "DES-01": ("Pump doesn't work or has stopped",       "Design & usability",      0.0085, 3, 1, "replace"),
 "DES-02": ("Pump dispenses too much or too little",  "Design & usability",      0.0045, 2, 1, "none"),
 "DES-03": ("Bottle too big or awkward",              "Design & usability",      0.0035, 1, 1, "none"),
 "DES-04": ("Doesn't stand up properly",              "Design & usability",      0.0030, 1, 1, "none"),
 "DES-05": ("Pouch hard to open, spills when refilling","Design & usability",    0.0075, 2, 1, "none"),
 "DES-06": ("Cap or closure doesn't seal",            "Design & usability",      0.0040, 3, 1, "replace"),
 "DES-07": ("Packaging feels cheap or flimsy",        "Design & usability",      0.0030, 1, 1, "none"),
 "DES-08": ("Label unclear or hard to read",          "Design & usability",      0.0020, 1, 1, "none"),
 "DES-09": ("Too much packaging, not recyclable",     "Design & usability",      0.0030, 2, 0, "none"),
 "CON-01": ("Arrived leaking",                        "Condition on arrival",    0.0135, 3, 1, "replace"),
 "CON-02": ("Arrived damaged or broken",              "Condition on arrival",    0.0150, 3, 1, "replace"),
 "CON-03": ("Arrived opened or used",                 "Condition on arrival",    0.0045, 3, 1, "replace"),
 "CON-04": ("Seal broken or missing",                 "Condition on arrival",    0.0050, 3, 1, "replace"),
 "CON-05": ("Underfilled, less than stated",          "Condition on arrival",    0.0040, 3, 1, "replace"),
 "CON-06": ("At or past best-before date",            "Condition on arrival",    0.0030, 2, 1, "replace"),
 "CON-07": ("Outer box damaged, product fine",        "Condition on arrival",    0.0060, 1, 0, "none"),
 "DEL-01": ("Not delivered",                          "Order & delivery",        0.0400, 2, 0, "replace"),
 "DEL-02": ("Delayed",                                "Order & delivery",        0.0700, 1, 0, "none"),
 "DEL-03": ("Lost in transit",                        "Order & delivery",        0.0180, 2, 0, "replace"),
 "DEL-04": ("Items missing from order",               "Order & delivery",        0.0260, 2, 0, "replace"),
 "DEL-05": ("Wrong items received",                   "Order & delivery",        0.0170, 2, 0, "replace"),
 "DEL-06": ("Delivered to wrong address",             "Order & delivery",        0.0110, 2, 0, "replace"),
 "DEL-07": ("Marked delivered but not received",      "Order & delivery",        0.0230, 2, 0, "replace"),
 "DEL-08": ("Courier problem, no card left",          "Order & delivery",        0.0130, 1, 0, "none"),
 "DEL-09": ("Tracking not updating",                  "Order & delivery",        0.0180, 1, 0, "none"),
 "SUB-01": ("Wants to cancel",                        "Subscription & billing",  0.0420, 2, 0, "churn"),
 "SUB-02": ("Wants to pause, skip or delay",          "Subscription & billing",  0.0850, 1, 0, "none"),
 "SUB-03": ("Wants to change frequency or products",  "Subscription & billing",  0.0400, 1, 0, "none"),
 "SUB-04": ("Didn't realise it was a subscription",   "Subscription & billing",  0.0130, 3, 0, "refund"),
 "SUB-05": ("Charged the wrong amount",               "Subscription & billing",  0.0110, 3, 0, "refund"),
 "SUB-06": ("Charged twice",                          "Subscription & billing",  0.0075, 3, 0, "refund"),
 "SUB-07": ("Payment failed",                         "Subscription & billing",  0.0230, 1, 0, "none"),
 "SUB-08": ("Arrives too often, too much product",    "Subscription & billing",  0.0160, 2, 0, "churn"),
 "SUB-09": ("Discount code didn't apply",             "Subscription & billing",  0.0120, 2, 0, "refund"),
 "SUB-10": ("Can't manage my subscription",           "Subscription & billing",  0.0105, 2, 0, "none"),
 "RFD-01": ("Refund not received",                    "Returns & refunds",       0.0180, 3, 0, "none"),
 "RFD-02": ("Refund slower than expected",            "Returns & refunds",       0.0150, 2, 0, "none"),
 "RFD-03": ("Refund amount wrong",                    "Returns & refunds",       0.0075, 3, 0, "refund"),
 "RFD-04": ("How do I return this",                   "Returns & refunds",       0.0300, 1, 0, "none"),
 "RFD-05": ("Return label problem",                   "Returns & refunds",       0.0110, 2, 0, "none"),
 "RFD-06": ("Unhappy with refund decision",           "Returns & refunds",       0.0075, 3, 0, "refund"),
 "AVL-01": ("Out of stock online",                    "Availability",            0.0120, 2, 1, "none"),
 "AVL-02": ("Can't find refills in store",            "Availability",            0.0105, 2, 1, "none"),
 "AVL-03": ("Product or variant discontinued",        "Availability",            0.0050, 2, 1, "none"),
 "AVL-04": ("Where can I buy this",                   "Availability",            0.0090, 1, 0, "none"),
 "AVL-05": ("Price differs between channels",         "Availability",            0.0040, 1, 0, "none"),
 "AVL-06": ("Not available in my country",            "Availability",            0.0035, 1, 0, "none"),
 "SVC-01": ("No reply, had to chase",                 "Service experience",      0.0090, 3, 0, "churn"),
 "SVC-02": ("Slow response",                          "Service experience",      0.0080, 2, 0, "none"),
 "SVC-03": ("Unhelpful or rude",                      "Service experience",      0.0040, 3, 0, "churn"),
 "SVC-04": ("Had to repeat myself",                   "Service experience",      0.0045, 2, 0, "none"),
 "SVC-05": ("Problem still not resolved",             "Service experience",      0.0060, 3, 0, "churn"),
 "VAL-01": ("Not enough product for the price",       "Price & value",           0.0080, 2, 1, "none"),
 "VAL-02": ("Overpriced for what it is",              "Price & value",           0.0070, 1, 1, "none"),
 "VAL-03": ("Refill isn't cheap enough",              "Price & value",           0.0040, 2, 1, "none"),
 "VAL-04": ("Delivery charge too high",               "Price & value",           0.0050, 1, 0, "none"),
 "VAL-05": ("Price has gone up",                      "Price & value",           0.0035, 2, 0, "none"),
 "PRA-01": ("Loves the product",                      "Praise",                  0.2050, 0, 1, "none"),
 "PRA-02": ("Loves the scent",                        "Praise",                  0.1310, 0, 1, "none"),
 "PRA-03": ("Works well for sensitive skin",          "Praise",                  0.0680, 0, 1, "none"),
 "PRA-04": ("Praise for service or an agent",         "Praise",                  0.0810, 0, 0, "none"),
 "PRA-05": ("Praise for packaging or sustainability", "Praise",                  0.0550, 0, 0, "none"),
 "PRA-06": ("Fast delivery",                          "Praise",                  0.1020, 0, 0, "none"),
}

FAULT_FLAG = {  # themes whose rise implies a real product or process fault
 "EFF-03":2,"EFF-05":1,"EFF-06":1,"EFF-07":2,"SEN-03":2,"SEN-05":2,"SEN-07":2,"SEN-06":1,
 "DES-01":2,"DES-02":1,"DES-05":1,"DES-06":1,"CON-01":2,"CON-02":1,"CON-03":1,"CON-04":2,
 "CON-05":2,"CON-06":1,"DEL-04":1,"DEL-05":1,"VAL-01":1,
}

SOURCES = ["Support - email","Support - chat","Support - phone",
           "Trustpilot","Product reviews","Google"]

# how each theme distributes across sources (support-weighted vs review-weighted)
def source_mix(code):
    cat = T[code][1]
    if cat in ("Subscription & billing","Returns & refunds","Service experience"):
        return [0.46,0.31,0.15,0.05,0.01,0.02]
    if cat in ("Order & delivery",):
        return [0.40,0.28,0.13,0.15,0.02,0.02]
    if cat in ("Condition on arrival",):
        return [0.36,0.22,0.10,0.20,0.10,0.02]
    if cat in ("Praise",):
        return [0.06,0.04,0.01,0.38,0.44,0.07]
    if cat in ("Efficacy & results","Sensory","Design & usability","Price & value"):
        return [0.18,0.11,0.05,0.26,0.38,0.02]
    if cat in ("Reactions & safety",):
        return [0.42,0.18,0.16,0.14,0.09,0.01]
    return [0.30,0.20,0.10,0.22,0.15,0.03]

# ---------------------------------------------------------------- volume
BASE_WEEKLY = 830          # signals per week, all sources
def seasonal(i):
    d = week_start[i]
    wk = d.isocalendar()[1]
    s = 1 + 0.16*math.sin((wk-14)/52*2*math.pi)          # summer/winter swing
    if wk in (48,49,50,51): s *= 1.30                     # christmas peak
    if wk in (1,2,3):       s *= 1.18                     # january returns
    growth = 1 + 0.0028*i                                 # slow business growth
    return s*growth

CAMPAIGN_WEEK = 58          # decoy: big promo, all volumes rise together

# ---------------------------------------------------------------- planted problems
INCIDENTS = [
 dict(id="INC-1", name="Body lotion pouch seal failure",
      theme=["CON-01","CON-04","DES-05"], mult=[7.5,4.0,1.8],
      skus=["LOT-POUC-FIG-400","LOT-POUC-SEA-400","LOT-POUC-UNS-400"],
      start=64, ramp=1, length=8, batch="2612-A", shape="spike",
      note="Weak seal on batch 2612-A. Pouches leak in transit."),
 dict(id="INC-2", name="Hand wash pump failures",
      theme=["DES-01","DES-02"], mult=[4.2,2.0],
      skus=["HAW-BOTL-STD-250"], start=52, ramp=9, length=26, batch="2604-C",
      shape="ramp", note="Moulding change at Costa Norte. Pumps seize after ~6 weeks of use."),
 dict(id="INC-3", name="Moisturiser reformulation",
      theme=["SEN-03","EFF-03","SEN-06"], mult=[5.0,3.4,2.2],
      skus=["FAC-MOIS-NRM-50","FAC-MOIS-DRY-50"], start=44, ramp=3, length=18,
      batch="2548-D", shape="step", note="Emollient supplier switched. Texture and scent changed."),
 dict(id="INC-4", name="Sensitive moisturiser reactions",
      theme=["RXN-01","RXN-02","RXN-05"], mult=[6.0,3.5,4.0],
      skus=["FAC-MOIS-SEN-50"], start=70, ramp=1, length=6, batch="2620-D",
      shape="spike", note="Preservative overdose suspected on batch 2620-D."),
 dict(id="INC-5", name="Christmas courier backlog",
      theme=["DEL-02","DEL-01","DEL-07"], mult=[2.6,1.9,1.8],
      skus=[], start=48, ramp=1, length=4, batch=None, shape="spike",
      note="Known seasonal courier failure. Should NOT alert as a new problem."),
]

def incident_factor(inc, i):
    off = i - inc["start"]
    if off < 0 or off >= inc["length"]: return 0.0
    if inc["shape"] == "spike":
        peak = inc["length"]*0.35
        return math.exp(-((off-peak)**2)/(2*(inc["length"]*0.30)**2))
    if inc["shape"] == "ramp":
        return min(1.0, off/max(1,inc["ramp"]))
    if inc["shape"] == "step":
        return 1.0 if off >= inc["ramp"] else off/max(1,inc["ramp"])
    return 0.0

# ---------------------------------------------------------------- cost model
CAC = 34.00
LIFETIME_NET = 136.02
FIRST_GP, REPEAT_GP = 22.32, 19.43
def contribution_lost(order_no):
    cum = FIRST_GP + (order_no-1)*REPEAT_GP
    return max(0.0, LIFETIME_NET - (cum - CAC))

COST_HANDLE = {"Support - email":4.59,"Support - chat":2.50,"Support - phone":7.50,
               "Trustpilot":0.90,"Product reviews":0.40,"Google":0.90}
COST_MACRO = 1.25
POSTAGE, PICKPACK, GOODWILL = 3.20, 1.10, 6.00

ORDER_BANDS = [(1,0.19),(2,0.14),(3,0.13),(4,0.11),(5,0.10),(6,0.09),(7,0.08),(8,0.16)]

# ---------------------------------------------------------------- generate
rows = []
for i in range(WEEKS):
    total = BASE_WEEKLY*seasonal(i)
    if i == CAMPAIGN_WEEK: total *= 1.55
    if i == CAMPAIGN_WEEK+1: total *= 1.22
    for code,(label,cat,share,sev,prodlinked,costband) in T.items():
        lam = total*share*random.uniform(0.86,1.14)
        extra_note, extra_batch, extra_skus = None, None, None
        for inc in INCIDENTS:
            if code in inc["theme"]:
                f = incident_factor(inc,i)
                if f > 0:
                    m = inc["mult"][inc["theme"].index(code)]
                    lam *= 1 + (m-1)*f
                    if f > 0.25:
                        extra_note, extra_batch, extra_skus = inc["id"], inc["batch"], inc["skus"]
        n = max(0, int(random.gauss(lam, math.sqrt(max(lam,1))*1.15)))
        if n == 0: continue
        mix = source_mix(code)
        for si,src in enumerate(SOURCES):
            k = int(round(n*mix[si]*random.uniform(0.8,1.2)))
            if k <= 0: continue
            for _ in range(k):
                if extra_skus and random.random() < 0.72:
                    sku = random.choice(extra_skus); batch = extra_batch
                elif prodlinked:
                    sku = random.choices(SKU_LIST, weights=SKU_W)[0]
                    batch = f"{random.choice(['25','26'])}{random.randint(1,52):02d}-{random.choice('ABCPD')}"
                else:
                    sku, batch = None, None
                order_no = random.choices([b[0] for b in ORDER_BANDS],
                                          weights=[b[1] for b in ORDER_BANDS])[0]
                is_support = src.startswith("Support")
                macro = is_support and cat in ("Subscription & billing","Returns & refunds") \
                        and random.random() < 0.78
                # 1. team time. real, but already sitting in payroll
                c_handle = COST_MACRO if macro else COST_HANDLE[src]
                # 2. putting it right: replacement or refund, plus any goodwill
                c_redress = 0.0
                if costband == "replace" and random.random() < 0.62:
                    unit = SKUS[sku][3] if sku else 2.50
                    c_redress = unit + POSTAGE + PICKPACK
                    if random.random() < 0.26: c_redress += GOODWILL
                elif costband == "refund" and random.random() < 0.55:
                    unit = SKUS[sku][2] if sku else 18.00
                    c_redress = unit + PICKPACK
                    if random.random() < 0.22: c_redress += GOODWILL
                # 3. customers who leave because of it
                churn_p = {0:0.0,1:0.004,2:0.010,3:0.025,4:0.050}[sev]
                if costband == "churn": churn_p += 0.090
                churn_p *= 0.55                      # only subscribers can cancel
                churned = random.random() < churn_p
                c_churn = contribution_lost(order_no) if churned else 0.0
                cost = c_handle + c_redress + c_churn
                # sentiment
                if sev == 0:   sent = random.uniform(0.62,0.99)
                elif sev == 1: sent = random.uniform(-0.45,0.10)
                elif sev == 2: sent = random.uniform(-0.62,-0.10)
                elif sev == 3: sent = random.uniform(-0.85,-0.30)
                else:          sent = random.uniform(-1.00,-0.55)
                sent = max(-1,min(1,sent+random.gauss(0,0.09)))
                rating = None
                if src in ("Trustpilot","Product reviews","Google"):
                    rating = max(1,min(5,round(3.25+sent*1.95+random.gauss(0,0.40))))
                elif is_support and random.random() < 0.11:
                    rating = max(1,min(5,round(3.35+sent*1.7+random.gauss(0,0.55))))
                rows.append(dict(w=i,code=code,cat=cat,src=src,sku=sku,batch=batch,
                                 order=order_no,cost=round(cost,2),
                                 c_handle=round(c_handle,2),c_redress=round(c_redress,2),
                                 c_churn=round(c_churn,2),sent=round(sent,3),
                                 rating=rating,churn=int(churned),inc=extra_note,sev=sev,
                                 support=int(is_support)))

print(f"generated {len(rows):,} signals over {WEEKS} weeks")

# ---------------------------------------------------------------- aggregate
def agg(keyfn):
    d = defaultdict(lambda: dict(n=0,cost=0.0,sent=0.0,churn=0,rat_n=0,rat_s=0,
                                 ch=0.0,rd=0.0,cn=0.0,sup=0,red_n=0,
                                 pos=0,neu=0,neg=0))
    for r in rows:
        k = keyfn(r)
        if k is None: continue
        a = d[k]; a["n"] += 1; a["cost"] += r["cost"]; a["sent"] += r["sent"]; a["churn"] += r["churn"]
        a["ch"] += r["c_handle"]; a["rd"] += r["c_redress"]; a["cn"] += r["c_churn"]
        a["sup"] += r["support"]
        if r["sent"] > 0.2: a["pos"] += 1
        elif r["sent"] < -0.2: a["neg"] += 1
        else: a["neu"] += 1
        if r["c_redress"] > 0: a["red_n"] += 1
        if r["rating"]: a["rat_n"] += 1; a["rat_s"] += r["rating"]
    return d

by_week        = agg(lambda r: r["w"])
by_week_theme  = agg(lambda r: (r["w"], r["code"]))
by_week_cat    = agg(lambda r: (r["w"], r["cat"]))
by_week_src    = agg(lambda r: (r["w"], r["src"]))
by_theme_sku   = agg(lambda r: (r["code"], r["sku"]) if r["sku"] else None)
by_week_sku    = agg(lambda r: (r["w"], r["sku"]) if r["sku"] else None)
by_theme_order = agg(lambda r: (r["code"], r["order"]))
by_theme_src   = agg(lambda r: (r["code"], r["src"]))
by_week_theme_src = agg(lambda r: (r["w"], r["code"], r["src"]))
by_theme_batch = agg(lambda r: (r["code"], r["batch"]) if r["batch"] else None)
by_order       = agg(lambda r: r["order"])

# --- compact array packing (keeps the baked-in file small) ---
CATS = sorted({v[1] for v in T.values()})

def series(d, keys, field, rnd=0):
    """{key: [value per week]}"""
    out = {}
    for k in keys:
        arr = []
        for i in range(WEEKS):
            v = d.get((i,k))
            if not v: arr.append(0); continue
            if field == "n":    arr.append(v["n"])
            elif field == "cost": arr.append(int(round(v["rd"]+v["cn"])))
            elif field == "handle": arr.append(int(round(v["ch"])))
            elif field == "redress": arr.append(int(round(v["rd"])))
            elif field == "churncost": arr.append(int(round(v["cn"])))
            elif field == "rednum": arr.append(v["red_n"])
            elif field == "support": arr.append(v["sup"])
            elif field == "pos": arr.append(v["pos"])
            elif field == "neu": arr.append(v["neu"])
            elif field == "neg": arr.append(v["neg"])
            elif field == "sent": arr.append(round(v["sent"]/v["n"], 2))
            elif field == "churn": arr.append(v["churn"])
            elif field == "rat":  arr.append(round(v["rat_s"]/v["rat_n"],2) if v["rat_n"] else 0)
        out[k] = arr
    return out

def topmap(d, outer, inner_limit=8):
    """{outer: {inner: n}} keeping the biggest few"""
    tmp = defaultdict(dict)
    for (a,b),v in d.items():
        tmp[a][b] = v["n"]
    return {a: dict(sorted(m.items(), key=lambda x:-x[1])[:inner_limit]) for a,m in tmp.items() if a in outer}

THEME_KEYS = list(T)
orders_wk = [int(18500/4.33*seasonal(i)*random.uniform(0.97,1.03)) for i in range(WEEKS)]

# per-theme, per-source weekly counts, only for themes that can signal a fault
FAULT_THEMES = [k for k in THEME_KEYS if FAULT_FLAG.get(k,0) or T[k][3] >= 3]
wts = {}
for code in FAULT_THEMES:
    wts[code] = [[by_week_theme_src.get((i,code,s),{"n":0})["n"] for s in SOURCES] for i in range(WEEKS)]

out = dict(
    targets=dict(positive=0.72, review=4.3, contact_rate=105, redress_pct=0.021),
    meta=dict(weeks=WEEKS, week_start=[d.isoformat() for d in week_start],
              orders=orders_wk, cats=CATS, sources=SOURCES,
              generated=dt.datetime.now().isoformat()),
    themes={k:[v[0],v[1],v[3],FAULT_FLAG.get(k,0)] for k,v in T.items()},
    skus={k:[v[0],v[1],v[2],v[4]] for k,v in SKUS.items()},
    units_month=83400,
    incidents=[dict(id=i["id"],name=i["name"],note=i["note"],batch=i["batch"],
                    start=i["start"],length=i["length"],themes=i["theme"],skus=i["skus"])
               for i in INCIDENTS],
    tot=dict(
        n   =[by_week[i]["n"] for i in range(WEEKS)],
        cost=[int(round(by_week[i]["rd"]+by_week[i]["cn"])) for i in range(WEEKS)],
        handle=[int(round(by_week[i]["ch"])) for i in range(WEEKS)],
        redress=[int(round(by_week[i]["rd"])) for i in range(WEEKS)],
        churncost=[int(round(by_week[i]["cn"])) for i in range(WEEKS)],
        rednum=[by_week[i]["red_n"] for i in range(WEEKS)],
        support=[by_week[i]["sup"] for i in range(WEEKS)],
        contacts=[int(round(by_week[i]["n"]*0.82)) for i in range(WEEKS)],
        pos=[by_week[i]["pos"] for i in range(WEEKS)],
        neu=[by_week[i]["neu"] for i in range(WEEKS)],
        neg=[by_week[i]["neg"] for i in range(WEEKS)],
        rat_n=[by_week[i]["rat_n"] for i in range(WEEKS)],
        sent=[round(by_week[i]["sent"]/by_week[i]["n"],3) for i in range(WEEKS)],
        rat =[round(by_week[i]["rat_s"]/by_week[i]["rat_n"],2) for i in range(WEEKS)],
        churn=[by_week[i]["churn"] for i in range(WEEKS)],
    ),
    theme_n    = series(by_week_theme, THEME_KEYS, "n"),
    theme_cost = series(by_week_theme, THEME_KEYS, "cost"),
    theme_sent = series(by_week_theme, THEME_KEYS, "sent"),
    theme_churn= series(by_week_theme, THEME_KEYS, "churn"),
    cat_n      = series(by_week_cat,  CATS,   "n"),
    cat_cost   = series(by_week_cat,  CATS,   "cost"),
    src_n      = series(by_week_src,  SOURCES,"n"),
    src_sent   = series(by_week_src,  SOURCES,"sent"),
    src_rat    = series(by_week_src,  SOURCES,"rat"),
    src_pos    = series(by_week_src,  SOURCES,"pos"),
    src_neg    = series(by_week_src,  SOURCES,"neg"),
    src_neu    = series(by_week_src,  SOURCES,"neu"),
    cat_sent   = series(by_week_cat,  CATS,   "sent"),
    cat_pos    = series(by_week_cat,  CATS,   "pos"),
    cat_neg    = series(by_week_cat,  CATS,   "neg"),
    sku_n      = series(by_week_sku,  SKU_LIST,"n"),
    sku_cost   = series(by_week_sku,  SKU_LIST,"cost"),
    theme_sku  = topmap(by_theme_sku,  set(THEME_KEYS), 6),
    theme_batch= topmap(by_theme_batch,set(FAULT_THEMES), 6),
    theme_src  = {k:[by_theme_src.get((k,s),{"n":0})["n"] for s in SOURCES] for k in THEME_KEYS},
    theme_order= {k:[by_theme_order.get((k,o),{"n":0})["n"] for o in range(1,9)] for k in THEME_KEYS},
    order_cost = {str(o):[by_order[o]["n"], int(round(by_order[o]["cost"]))] for o in range(1,9)},
    week_theme_src = wts,
)

with open("/root/customer-insight-dashboard/data/aggregates.json","w") as f:
    json.dump(out,f,separators=(",",":"))
import os
print("aggregates.json", round(os.path.getsize('/root/customer-insight-dashboard/data/aggregates.json')/1024), "KB")
