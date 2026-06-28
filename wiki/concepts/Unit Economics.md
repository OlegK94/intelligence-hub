TAGS: [unit-economics, break-even, contribution-margin, scenario-modelling, pricing, cogs, profitability, moq-sensitivity]
SOURCES: ["raw/Business/PerformanceCafe/recherche/06_Kalkulation_Pricing.md", "raw/Business/PerformanceCafe/recherche/_archiv/07_business_case.md"]
CREATED: 2026-06-14
UPDATED: 2026-06-17
SUMMARY: Unit Economics — Geschäftsmodell-Metriken zur Profitabilitäts-Analyse; Break-even-Units/Monat, Contribution Margin, MOQ-Sensitivität, Szenario-Modellierung (Pessimistisch/Base/Optimistisch); zentrale Metrik für Launch-Viability und Scale-Entscheidungen
---

# Unit Economics

## Überblick

**Unit Economics** sind die finanziellen Metriken pro verkaufter Einheit, die die **Profitabilität eines Geschäftsmodells** zeigen:
- Ist jede verkaufte Einheit profitabel?
- Bei welchem Volumen wird das Geschäft insgesamt profitabel (Break-even)?
- Wie empfindlich ist das Modell gegenüber Kosten-Variationen?

## Kernmetriken

### 1. Contribution Margin (Deckungsbeitrag)

```
Contribution Margin = Revenue per Unit − COGS per Unit
CM = RRP − COGS
```

**Beispiel Performance Coffee (Base Case):**
- RRP: €1,50
- COGS: €0,55
- **CM: €0,95**

**Interpretation:** Jedes verkaufte Sachet trägt €0,95 zu den Fixkosten/Gewinn bei.

### 2. Contribution Margin % (Prozentsatz)

```
CM % = (RRP − COGS) ÷ RRP × 100%
CM % = €0,95 ÷ €1,50 × 100% = 63%
```

**Benchmark:** Performance Coffee zielt auf 55–65% CM %; DRYLL erreicht 50–60%; Kimera 60–70%.

### 3. Break-even Analyse

**Break-even Units pro Monat:**

```
Break-even Units = Monthly Fixed Costs ÷ Contribution Margin
```

**Beispiel Performance Coffee (Base Case):**
- Fixkosten/Monat: ~€1.400 (Shopify €200–300, Content €500–1.000, Ops €300–500)
- CM: €0,95
- **Break-even = 1.400 ÷ 0,95 = 1.474 Units/Monat**

**Interpretation:** Bei 1.474 Sachets/Monat wird der Break-even erreicht (0 Gewinn/Verlust). Alles über 1.474 ist Gewinn.

### 4. Profitability Threshold (Gewinnschwelle)

Über Break-even hinaus:

```
Monatlicher Gewinn = (Units Verkauft − Break-even Units) × CM
```

**Beispiel:** 2.000 Units/Monat bei Break-even 1.474:
- Gewinn = (2.000 − 1.474) × €0,95 = **526 × €0,95 = €499,70/Monat**

### 5. Payback Period (für Anfangs-Investitionen)

```
Payback Period = MOQ Kosten ÷ (Monthly Units × CM)
```

**Beispiel:** MOQ 1.000 Units @ €550 COGS (gesamt):
- Monatliche Profitieren: 100 Units/Monat × €0,95 = €95/Monat
- **Payback = €550 ÷ €95 = 5,8 Monate**

## Szenario-Modellierung (Pessimistisch / Base / Optimistisch)

### Szenario A: Pessimistisch

- **COGS:** €0,65 (hohe Supplier-Kosten, kleine MOQ)
- **RRP:** €1,50 (Wettbewerber-getrieben)
- **CM:** €0,85 (56% Margin)
- **Fixkosten:** €1.800 (zusätzliche Content/Ads erforderlich)
- **Break-even:** 1.800 ÷ 0,85 = **2.118 Units/Monat**
- **Bewertung:** Riskant; langsamere Profitabilität

### Szenario B: Base Case

- **COGS:** €0,55 (realistische Supplier-Verhandlungen, 1k MOQ)
- **RRP:** €1,50 (Benchmark DRYLL-Position)
- **CM:** €0,95 (63% Margin)
- **Fixkosten:** €1.400 (realistisch für Launch)
- **Break-even:** 1.400 ÷ 0,95 = **1.474 Units/Monat**
- **Bewertung:** Robust; 500 Kunden/Monat erreichbar in Phase 1

### Szenario C: Optimistisch

- **COGS:** €0,45 (Bulk-Rabatte, 5k MOQ)
- **RRP:** €1,50 (oder sogar €1,80 Premium-Position)
- **CM:** €1,05 (70% Margin, oder €1,35 @ €1,80)
- **Fixkosten:** €1.000 (Lean Operations)
- **Break-even:** 1.000 ÷ 1,05 = **952 Units/Monat**
- **Bewertung:** Hervorragend; schneller Profitabilität und Scale-Spielraum

## MOQ-Sensitivität

Minimale Bestellmenge hat großen Impact auf Zeitlinie zu Break-even:

| MOQ | Unit-COGS | Payback bei 100 Units/Mo | Profitabilität erreicht |
|---|---|---|---|
| **500 Units @ €0,65** | €0,65 | 3,4 Monate | Monat 5–6 |
| **1.000 Units @ €0,55** | €0,55 | 5,8 Monate | Monat 7–8 |
| **5.000 Units @ €0,45** | €0,45 | 23,8 Monate | Monat 24–25 (zu lange!) |

**Insights:** 
- 500er MOQ ist **teurer per Unit** aber schneller zu Break-even (weniger Kapitalgebunden)
- 1.000er MOQ ist **optimal** (balanciert Unit-Cost und Payback-Zeit)
- 5.000er MOQ ist nur sinnvoll, wenn man >300 Units/Monat sicher verkaufen kann

## Subscription-Impact auf Unit Economics

Subscription-Modell verändert CM und Break-even:

### One-Time Purchase
- RRP: €1,50
- CM: €0,95 (63%)

### Subscription Monthly (15% Rabatt)
- RRP (Subscription): €1,28
- CM: €0,73 (57%)
- **Aber:** 60–70% Repeat-Rate bedeutet Lifetime Value (LTV) ist viel höher

**LTV Calculation (für langfristige Profitabilität):**
```
LTV = (Monthly CM × Durchschn. Abo-Monate) − CAC (Kundenakquisitionskosten)
```

Beispiel:
- Durchschn. Abo-Dauer: 6 Monate
- Monthly CM (Abo): €0,73
- **LTV = 0,73 × 6 = €4,38** (vs. One-Time €0,95)
- Selbst wenn CAC €3,00 ist: LTV − CAC = **€1,38 Gewinn pro Kunde**

## CAC vs. LTV Ratio (Akquisitions-Effizienz)

```
CAC (Customer Acquisition Cost) = Total Marketing Spend ÷ New Customers
LTV = (Monthly CM × Abo-Monate) − CAC

Health Ratio: LTV : CAC sollte ≥3:1 sein
```

**Beispiel DRYLL (geschätzt):**
- CAC: ~€15–20 (Meta Ads in DE)
- LTV: ~€4,38 (6 Monate Subscription) — **Problem: LTV < CAC!**
- **Lösung:** Längere durchschnittliche Abo-Dauer (12+ Monate) oder höhere Repeat-Rate

## Break-even Chart (Visualisierung)

```
Gewinn (€)
    ↑
    |              Szenario C (Optimistisch)
    |         /
  500 |        /
    |       /
    |      /┌─ Szenario B (Base)
    |     /─┘
  250 |    /   \
    |   /    ┌──────── Szenario A (Pessimistisch)
    0 |──┼─┼──┼────────
    |  ↓  ↓
 -250 | 952 1474 2118 Units/Monat
    |
   -€ Break-even Punkte
```

## Fehler & Fallstricke

| Fehler | Auswirkung | Vermeidung |
|---|---|---|
| **Fixkosten unterschätzt** | Break-even ist höher als geplant | Detaillierte Kostenprognose; +20% Puffer |
| **COGS nicht validiert** | CM ist niedriger als geplant | ≥3 Supplier-Quotes einholen |
| **Churn unterschätzt** | LTV ist viel niedriger | Historische Daten von Concurrents (DRYLL ~10–15% Monatlicher Churn) |
| **CAC nicht gemessen** | Unbekannt, ob Akquisition profitabel | Tracking-Pixel + UTM-Parameter von Tag 1 |
| **Saisonalität ignoriert** | Sommermonate sind langsam | Szenarien für Q2/Q3/Q4 trennen |

## Integrationen & Abhängigkeiten

- **[[COGS]]** — Unit-Kosten Basis
- **[[Pricing]]** — RRP-Festlegung
- **[[06 Kalkulation & Pricing Performance Coffee]]** — Detaillierte Unit-Economics-Quelldokumentation
- **[[Performance Coffee Brand]]** — Projekt-Kontext

## Verwandte Seiten

- **[[COGS]]** — Cost of Goods Sold Berechnung
- **[[Pricing]]** — RRP-Festlegung
- **[[Contribution Margin]]** — Deckungsbeitrag
- **[[Break-even]]** — Gewinnschwelle
- **[[CAC]]** — Customer Acquisition Cost
- **[[LTV]]** — Lifetime Value
