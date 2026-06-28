---
title: "Performance Coffee Unit Economics Model"
type: synthesis
tags: [performance-cafe, unit-economics, cogs, pricing, break-even, financial-model]
sources: ["[[06 Kalkulation & Pricing Performance Coffee]]", "[[04 Marktanalyse & Wettbewerb (Quelldokument)]]", "[[00 Auftragsbrief Performance Coffee]]"]
created: 2026-06-17
updated: 2026-06-17
summary: Integrated unit economics synthesis for Performance Coffee Phase 1 DTC launch; COGS €0,45–0,65, RRP €1,50 (base case), contribution margin €0,95, break-even ~1.470 sachets/month, 3 scenarios (pessimistic/base/optimistic), subscription model 15–25% discount, 6-month KPI targets (500 orders, €25k revenue, 25% repeat rate)
---

# Performance Coffee Unit Economics Model

## Executive Summary

The **Performance Coffee Unit Economics Model** integrates cost-of-goods-sold (COGS), pricing benchmarks, and break-even analysis to answer the core business question: **At what volume does Phase 1 become profitable?**

### Key Figures (Base Case)

| Metric | Value | Notes |
|---|---|---|
| **COGS per Sachet** | €0,55 | Ingredients + packaging + fulfillment; 1,000 MOQ |
| **RRP Einmalkauf** | €1,50 | Retail recommended price |
| **RRP Abo** | €1,35 | 10% discount; target 45% subscription mix |
| **Blended RRP** | €1,43 | (€1,50 × 55% one-time) + (€1,35 × 45% abo) |
| **Contribution Margin** | €0,88 | RRP − COGS (before fixed costs) |
| **Gross Margin %** | 59% | €0,88 ÷ €1,50 |
| **Fixed Costs/Month** | €1,400 | Shopify, content, ops (minimal Phase 1) |
| **Break-even Units/Month** | 1,591 | €1,400 ÷ €0,88 contribution |
| **Break-even Revenue/Month** | €2,386 | 1,591 units × €1,50 avg RRP |

---

## COGS Waterfall (Base Case, 1,000 MOQ)

### Ingredients per Sachet (~10g)

| Component | Dosage | Unit Cost | Portion Cost |
|---|---|---|---|
| L-Theanin | 200 mg | €2,00/g | €0,040 |
| L-Tyrosine | 500 mg | €0,15/g | €0,075 |
| Alpha-GPC | 200 mg | €1,50/g | €0,030 |
| Koffein | 130 mg | €0,20/g | €0,026 |
| B-Vitamin Premix | NRV | €0,50/portion | €0,050 |
| Ashwagandha KSM-66 | 400 mg | €0,08/g | €0,032 |
| **Inhaltsstoff-Summe** | — | — | **€0,253** |

### Kaffee (12g roasted, SCA ≥80)

| Component | Dosage | Unit Cost | Portion Cost |
|---|---|---|---|
| Grün-Bohnen (Specialty) | 12g | €0,08/g | €0,096 |
| Röstung + QA | — | €0,05/g | €0,060 |
| Kaffee-Summe | — | — | **€0,156** |

### Verpackung (Primary + Secondary)

| Component | Unit Cost | Notes |
|---|---|---|
| Sachet (Aluminium Foil, 1–2 color print) | €0,080 | Alu-laminat, Aroma-valve, Heat-seal |
| Outer Box (Karton 4-er oder 30-er) | €0,040 | Druck + Montage |
| Shipper (für Lagerung, amortisiert) | €0,015 | Großmengen-Verpackung |
| **Verpackung-Summe** | — | **€0,135** |

### Manufacturing + Fulfillment

| Component | Unit Cost | Notes |
|---|---|---|
| Co-Packing Fee (CMO) | €0,040 | Fill, seal, QA per unit |
| Inbound Shipping (Deutschland) | €0,010 | 1k-unit-batch, 2-week lead |
| 3PL Pick-Pack-Ship (DHL) | €0,045 | ~€2,00/order = €0,20 per 4,4 sachets avg |
| Return Management | €0,010 | 2% return rate buffer |
| **Mfg + Fulfillment-Summe** | — | **€0,105** |

### COGS Total

```
Ingredients:        €0,253
Kaffee:             €0,156
Verpackung:         €0,135
Mfg + Fulfillment:  €0,105
─────────────────
COGS per Sachet:    €0,649
```

**Adjusted for base case assumption (1,000 MOQ optimism):** €0,55 per sachet (vs. €0,65 conservative).

---

## Pricing Scenarios

### Scenario A: Pessimistisch (Small MOQ, High COGS)

**Assumptions:**
- MOQ 500 Units → ingredient prices higher, packaging inefficiency
- COGS: €0,65/sachet
- RRP unchanged: €1,50 (competitive)
- No subscription discount pricing

| Metric | Value |
|---|---|
| **COGS** | €0,65 |
| **RRP (1x)** | €1,50 |
| **Contribution Margin** | €0,85 |
| **Gross Margin %** | 57% |
| **Fixed Costs** | €1,800 (higher ops/stress) |
| **Break-even Units/Month** | 2,118 |
| **Break-even Revenue** | €3,176 |
| **First-Year Profitability** | Limited; ~€500 EBIT if 100 customers/month reached |

---

### Scenario B: Base Case (1,000 MOQ)

**Assumptions:**
- MOQ 1,000 Units → standard supplier pricing
- COGS: €0,55/sachet
- RRP 1x: €1,50; Abo: €1,35 (10% discount)
- Mixed subscription: 45% abo, 55% one-time
- Blended effective RRP: €1,43

| Metric | Value |
|---|---|
| **COGS** | €0,55 |
| **Blended RRP** | €1,43 |
| **Contribution Margin** | €0,88 |
| **Gross Margin %** | 59% |
| **Fixed Costs** | €1,400 (lean ops) |
| **Break-even Units/Month** | 1,591 |
| **Break-even Revenue** | €2,275 |
| **First-Year Profitability** | ~€8k–€12k EBIT at 3,000 units/month steady-state |

---

### Scenario C: Optimistisch (5,000 MOQ, Scale)

**Assumptions:**
- MOQ 5,000 Units → bulk ingredient pricing, packaging economy
- COGS: €0,45/sachet
- RRP 1x: €1,50; Abo: €1,30 (13% discount)
- Mixed subscription: 50% abo, 50% one-time
- Blended effective RRP: €1,40

| Metric | Value |
|---|---|
| **COGS** | €0,45 |
| **Blended RRP** | €1,40 |
| **Contribution Margin** | €0,95 |
| **Gross Margin %** | 68% |
| **Fixed Costs** | €1,200 (ops leverage) |
| **Break-even Units/Month** | 1,263 |
| **Break-even Revenue** | €1,768 |
| **First-Year Profitability** | ~€15k–€20k EBIT at 4,000 units/month scale |

---

## 6-Month KPI Dashboard (Phase 1 Target)

| Metric | Month 1 | Month 3 | Month 6 | Rationale |
|---|---|---|---|---|
| **Cumulative Orders** | 50 | 200 | 500 | Friends & Family → Influencer → Organic |
| **Monthly Run Rate** | 50 | 200 | 300 | (Steady-state by Month 6) |
| **Revenue (cumulative)** | €2,500 | €10,000 | €25,000 | Blended RRP €1,43 |
| **Revenue (monthly M6)** | — | — | €4,290 | 300 orders × €1,43 |
| **CAC (Customer Acquisition Cost)** | €35 | €28 | €22 | Costs reduce as owned channels scale |
| **Repeat Rate %** | 10% | 20% | 25% | Standard subscription conversion |
| **Abo-Anteil (% of orders)** | 20% | 35% | 45% | Growing retention focus |
| **Gross Profit Margin %** | >55% | >58% | >60% | COGS stays €0,55; RRP mix improves |
| **Profitability** | −€1,300 (month loss) | −€500 (month loss) | +€900 (month profit) | Break-even ~Month 4–5 (1,591 units reached) |

---

## Break-even Sensitivity Analysis

### Variable: COGS

| COGS | Contribution | Break-even Units | Break-even Months to Profit |
|---|---|---|---|
| **€0,45** | €1,05 | 1,333 | 3–4 months |
| **€0,55** (Base) | €0,95 | 1,474 | 4–5 months |
| **€0,65** | €0,85 | 1,647 | 5–6 months |
| **€0,75** | €0,75 | 1,867 | 6–8 months |

### Variable: Fixed Costs

| Fixed Costs/Month | Break-even Units | Profitability Window |
|---|---|---|
| **€800** | 842 | Rapid (Month 2–3) |
| **€1,200** | 1,263 | Fast (Month 3–4) |
| **€1,400** (Base) | 1,474 | Standard (Month 4–5) |
| **€1,800** | 1,895 | Slow (Month 5–6) |

### Variable: RRP (Blended, Subscription Mix)

| RRP | COGS | Margin | Break-even | Monthly Revenue @Break-even |
|---|---|---|---|---|
| **€1,20** | €0,55 | €0,65 | 2,154 units | €2,585 |
| **€1,43** (Base) | €0,55 | €0,88 | 1,591 units | €2,275 |
| **€1,60** | €0,55 | €1,05 | 1,333 units | €2,133 |
| **€1,80** | €0,55 | €1,25 | 1,120 units | €2,016 |

---

## Subscription Model Impact

### Abo Pricing Strategy

| Tier | Price | Discount | Target Mix | LTV Impact |
|---|---|---|---|---|
| **One-time** | €1,50 | — | 55% | CAC €35 = 2.1x ROI |
| **Monthly Abo** | €1,35 | 10% | 30% | LTV €50+ (12-month) |
| **Quarterly Abo** | €1,30 | 13% | 10% | LTV €52+ (12-month) |
| **Annual Abo** | €1,25 | 17% | 5% | LTV €55+ (12-month) |

### Repeat Rate Conversion

**Assumption:** 25% of one-time customers convert to abo within 90 days.

```
Month 1: 50 one-time → 10% abo (from email nurture) = 5 recurring
Month 3: 200 total one-time (cumulative) → 25% convert = 50 recurring
Month 6: 500 total one-time → 25% convert = 125 recurring

Blended Revenue Impact:
  Month 1: (50 × 1x × €1,50) + (5 × abo × €1,35) = €82,50 (avg per order €1,47)
  Month 6: (300 × 1x × €1,50) + (125 × abo × €1,35) = €619,50 (avg per order €1,43)
```

---

## Dependency Chains

### To Execute Pricing Model:
1. ✅ **Modul 00 (Auftragsbrief)** — Stack A defined
2. ⏳ **Modul 01 (Ingredienzen DB)** — Supplier costs required
3. ⏳ **Modul 03 (Kaffee-Spec)** — Roast & sourcing costs required
4. ⏳ **Modul 04 (Marktanalyse)** — Competitor RRP benchmarks
5. ⏳ **CMO Sourcing** — Packaging + co-packing fee quotes

### To Validate Break-even:
1. ✅ **Modul 00** — Fixed-cost assumptions (Shopify, content, ops)
2. ⏳ **Modul 07 (Vermarktung & Ops)** — CAC estimates per channel

---

## Risks & Sensitivities

| Risk | Impact | Mitigation |
|---|---|---|
| **COGS Overrun (€0,65 vs. €0,55)** | Break-even +200 units/month; profit delayed 1–2 months | Lock supplier quotes Q3 2026; negotiate volume rebates |
| **RRP Pressure (market forces €1,20)** | Break-even +500 units/month; low margin | Differentiate via positioning; avoid race-to-bottom |
| **CAC Inflation (€35 → €50)** | LTV:CAC ratio drops to 1.2x (bad); abo focus critical | Owned channel development (email, content, community) |
| **Repeat Rate Lower (10% vs. 25%)** | Abo revenue 50% lower; profitability 2–3 months delayed | Product quality + NPS focus; retention marketing |
| **Fulfillment Costs Rise (€0,045 → €0,070)** | COGS +€0,025; break-even +200 units | Negotiate 3PL SLA; self-fulfill initially if <100 orders/mo |

---

## Links to Related Pages

- [[06 Kalkulation & Pricing Performance Coffee]] — COGS waterfall detail
- [[04 Marktanalyse & Wettbewerb (Quelldokument)]] — Pricing benchmarks (DRYLL, Kimera, Bulletproof)
- [[07 Vermarktung & Operations (Quelldokument)]] — CAC assumptions, KPI dashboard
- [[Performance Coffee DTC Playbook]] — Execution roadmap
- [[00 Auftragsbrief Performance Coffee]] — Phase structure, timeline
