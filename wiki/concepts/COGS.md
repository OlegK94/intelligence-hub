TAGS: [cogs, cost-of-goods-sold, unit-economics, pricing, waterfall, inhaltsstoffe, verpackung, manufacturing, fulfillment]
SOURCES: ["raw/Business/PerformanceCafe/recherche/06_Kalkulation_Pricing.md"]
CREATED: 2026-06-14
UPDATED: 2026-06-17
SUMMARY: Cost of Goods Sold (COGS) — Waterfall-Struktur von Rohmaterial bis versendeter Einheit; Inhaltsstoffe + Kaffee + Verpackung + Co-Packing Fee + Fulfillment; zentrales Input für Pricing-Entscheidungen und Break-even-Analysen
---

# COGS — Cost of Goods Sold

## Überblick

**COGS (Cost of Goods Sold)** ist die Summe aller direkten Kosten zur Herstellung einer verkauftsfähigen Einheit. Es ist das zentrale Metrik für:
- **Kalkulation von Verkaufspreisen** (RRP = COGS ÷ (1 − Ziel-Margin))
- **Break-even-Analyse** (COGS vs. Contribution Margin)
- **Scenario-Modellierung** (MOQ-Sensitivität, Supplier-Variationen)

## COGS-Waterfall-Struktur (Performance Coffee Beispiel)

```
Inhaltsstoffe pro Portion (Stack A)
  L-Theanin 200 mg              €0,05
  L-Tyrosine 500 mg             €0,04
  B-Vitamin-Premix              €0,03
  Ashwagandha KSM-66            €0,06
  ─────────────────────────────
  Subtotal Inhaltsstoffe        €0,18

+ Kaffee (Blend 12–15g)         €0,12
+ Verpackung (Primary Sachet)   €0,08
+ Verpackung (Outer Box, Share) €0,04
  ─────────────────────────────
  = Manufacturing Baseline      €0,42

+ Co-Packing Fee (pro Unit)     €0,08
+ Inbound Shipping zu Warehouse €0,02
  ─────────────────────────────
  = Fulfillment-Ready COGS      €0,52

+ Fulfillment (3PL Pick-Pack)   €0,05
+ Outbound Shipping (DACH avg)  €0,04
  ─────────────────────────────
  = FINAL COGS (delivered)      €0,61
```

**Zielbereich Performance Coffee:** €0,45–0,65 pro Portion (je nach MOQ, Supplier-Variation)

## Komponenten-Details

### 1. Rohzutaten (Raw Materials)
Basis-Inhaltsstoffe für Stack A:
- **L-Theanin:** ~€0,03–0,07 / 200mg (je nach Supplier + MOQ)
- **L-Tyrosine:** ~€0,02–0,05 / 500mg
- **B-Vitamine (Premix):** ~€0,02–0,05 / Portion
- **Ashwagandha KSM-66:** ~€0,04–0,08 / 300–600mg
- **Kaffee (Rohbohne + Röstung):** ~€0,08–0,15 / 12–15g

**Sourcing-Strategie:** ≥3 Quotes pro Zutat (Alibaba, GlobalSources, lokale Distributor)

### 2. Verpackung (Packaging)

#### Primary Packaging
- **Sachet (Aluminium-Verbundfolie):** €0,06–0,10 pro Stück
  - Material (Folie + Druckkosten + Dichtung)
  - Bedruckung mit Logo/Inhaltsstoffe
- **Kapsel-Blister (falls Kapsel-SKU):** €0,08–0,12 pro 2er-Pack

#### Secondary Packaging
- **Outer Box (Karton):** €0,03–0,06 pro Einheit (bei 30–60er Multipack)
  - Includes: Design, Druck, Montage, Lagerstabilität
- **Shipper Box (für direkte Kunden):** €0,50–1,00 pro Bestellung (aber über viele Units amortisiert)

### 3. Manufacturing (Co-Packing Fee)

Die **Co-Packing-Gebühr** ist der Charge-Preis des CMO (Contract Manufacturer):
- **Typisch:** €0,05–0,12 pro Unit (je nach MOQ + Komplexität)
- **Includes:** Mischen, Kapsulierung (falls zutreffend), Qualitätskontrolle, Etikettierung
- **MOQ-abhängig:**
  - 500 Units: €0,10–0,12 / Unit (höher)
  - 1.000 Units: €0,07–0,09 / Unit
  - 5.000+ Units: €0,05–0,07 / Unit

### 4. Logistik

#### Inbound Logistics (Rohstoffe → CMO Warehouse)
- Typisch €0,01–0,03 pro Unit (in Großmengen-Batches)
- Inklusive: Supplier-Versand + Customs (falls Import)

#### Outbound Logistics (CMO/Warehouse → Kunde)
- **Shopify DTC:** €3–5 pro Bestellung durchschnittlich (500g–1kg Paket)
  - über ~15–30 Sachets = €0,15–0,30 pro Unit
  - **Aber:** Subscription-Bundles (30+ Units) senken Durchschnitt auf €0,03–0,05 / Unit
- **3PL Fulfillment Fee:** €0,50–1,50 pro Bestellung (Pick-Pack-Label) — auch über Units amortisiert

**Abkürzung:** Vereinfachter COGS setzt oft "Fulfillment" auf einen pauschalen %-Aufschlag (z.B. +15% auf Manufacturing COGS).

## MOQ-Sensitivität (Szenario-Analyse)

Minimale Bestellmenge hat großen Impact auf Unit-COGS:

| MOQ | Ingredienzen | Verpackung | CMO-Fee | Gesamtkost COGS | Break-even Beeinflussung |
|---|---|---|---|---|---|
| **500 Units** | €0,20 (höher) | €0,13 (höher) | €0,10 | €0,63–0,68 | ~1.900 Units/Mo |
| **1.000 Units** | €0,18 | €0,12 | €0,08 | €0,52–0,58 | ~1.470 Units/Mo |
| **5.000+ Units** | €0,17 | €0,10 | €0,06 | €0,42–0,48 | ~667 Units/Mo |

**Insight:** MOQ ist ein kritischer Lever — Unterschied zwischen 500 und 5.000 ist ~€0,15–0,20 pro Unit. Bei 60% Bruttomarge bedeutet das RRP-Unterschied von €0,35–0,50 pro Unit.

## Benchmark-Vergleiche

| Brand | Format | Est. COGS | RRP | Bruttomarge |
|---|---|---|---|---|
| **DRYLL** | Stick 7g | €0,50–0,65 | €0,99–1,33 | 35–50% / 50–60% (Sub) |
| **Bulletproof** | Kapseln 2er | €0,60–0,80 | €1,30–1,50 | 45–55% |
| **Kimera** | Sachets | €0,35–0,45 | €0,65–0,75 | 60–70% (aggressive Kosten) |
| **Braineffect** | Sticks | €0,45–0,60 | €1,10–1,30 | 50–65% |
| **Performance Coffee (Ziel)** | Sachets | €0,45–0,65 | €1,20–1,80 | 55–65% |

## Pricing-Rückwärts: Von RRP zu COGS

Typisches Pricing-Modell:

```
Ziel-Bruttomarge: 60%
Zielpreis RRP: €1,50
─────────────────────
Max COGS = RRP × (1 − Margin %)
Max COGS = €1,50 × (1 − 0,60) = €0,60
```

**Wenn COGS > €0,60:** RRP muss erhöht oder Margin akzeptiert reduziert werden.

## Variabilität & Sensitivität

COGS ist **nie fix** — abhängig von:
- **Supplier-Verhandlungen:** Bulk-Rabatte, Vertragsbedingungen
- **Rohstoff-Volatilität:** Kaffeepreise schwanken mit Börse
- **Wechselkurs:** EUR/USD für importierte Inhaltsstoffe
- **Logistik-Kosten:** Shipping-Preise ändern sich saisonal
- **Produktionseffizienz:** Ausschussquoten, Rüstzeiten beeinflussen CMO-Fee

**Best Practice:** COGS in 3 Szenarien modellieren (pessimistisch/base/optimistisch).

## Integration mit Unit Economics

COGS ist die Grundlage für:

| Metrik | Formel |
|---|---|
| **Contribution Margin** | RRP − COGS |
| **Bruttomarge %** | (RRP − COGS) ÷ RRP |
| **Break-even Units/Mo** | Fixkosten ÷ Contribution Margin |
| **Payback Period** | MOQ-Kosten ÷ (Contribution Margin × Orders/Monat) |

Siehe [[Unit Economics]] für vollständige Integration.

## Verwandte Seiten

- **[[Unit Economics]]** — Break-even, Szenario-Modellierung
- **[[06 Kalkulation & Pricing Performance Coffee]]** — Detaillierte COGS-Quelldokumentation
- **[[CMO Sourcing Performance Coffee]]** — Co-Packing-Partner-Evaluierung
- **[[Pricing]]** — RRP-Festlegung basierend auf COGS
- **[[Performance Coffee Brand]]** — Projekt-Kontext
