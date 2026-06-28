TAGS: [performance-cafe, cogs, pricing, unit-economics, break-even, margin, subscription, rrp, margin-szenarien, modul-06, recherche]
SOURCES: ["raw/Business/PerformanceCafe/recherche/06_Kalkulation_Pricing.md"]
CREATED: 2026-06-14
UPDATED: 2026-06-14
SUMMARY: Konzeptseite Modul 06 — zentrale Entscheidung: COGS-Modell (€0,45–0,65/Portion), RRP (€1,20–1,80; 55–65% Bruttomarge), Subscription-Pricing (10–25% Rabatt), Break-even (Fixkosten ÷ Contribution Margin), MOQ-Sensitivität; Benchmarks gegen DRYLL, Bulletproof, Kimera; Abhängigkeiten: CMO-Quote, Amazentis-Lizenz, Fixkosten (Modul 07); 4 Deliverables (inhaltsstoffe_db.csv, unit_economics.py, Pricing-Memo, Break-even-Chart)

---

# Performance Coffee Modul 06 — Kalkulation & Pricing

## Überblick

**Modul 06** beantwortet die zentrale Frage: **Wie wird Performance Coffee profitabel gemacht?** Es verbindet die produkt-technischen Entscheidungen (Modul 02), die lieferkettentechnischen Realitäten (Modul 03) und die regulatorischen Verpflichtungen (Modul 05) mit einer wasserdichten Finanzrechnung.

Das Modul hat vier konkrete Deliverables:
1. **Gefüllte `inhaltsstoffe_db.csv`** — alle Zutaten mit ≥5 Supplier-Quotes
2. **`unit_economics.py` Szenario-Output** — 3 Szenarien (pessimistisch/base/optimistisch)
3. **Pricing-Empfehlung SKU #1** — RRP + Subscription-Struktur
4. **Break-even-Chart** — visuelle Darstellung der Profitabilität

---

## Zentrale Metriken

### COGS-Zielbereich
**€0,45–0,65 pro Portion** (10g Sachet)

Zusammensetzung (geschätzt):
- Inhaltsstoffe: €0,08–0,12
- Kaffee: €0,10–0,15
- Verpackung: €0,15–0,20
- Co-Packing Fee: €0,05–0,10
- Fulfillment (3PL + Versand DACH): €0,07–0,10

### RRP-Zielbereich
**€1,20–1,80 pro Portion**

Motivation:
- DRYLL: €0,99–1,33 (Subscription vs. 1x)
- Bulletproof: €1,30–1,50
- Specialty Coffee: €0,50–0,80 (aber andere Kategorie)
- **Midpoint:** €1,50 (kompetitiv, Premium-Positionierung)

### Bruttomarge-Zielbereich
**55–65%**

Formula: (RRP – COGS) / RRP

| COGS | RRP €1,50 | Marge |
|---|---|---|
| €0,45 | €1,50 | 70% |
| €0,55 | €1,50 | 63% |
| €0,65 | €1,50 | 57% |

---

## Subscription-Pricing-Modell

### Empfehlung

| Modell | RRP | Rabatt | Repeat-Ziel |
|---|---|---|---|
| **Einmalkauf** | €1,50 | — | 40% (One-Time-Customers) |
| **Subscription (monatlich)** | €1,30 | 13% | 60% (Recurring) |
| **Blended Average** | €1,38 | — | 100% Kundenbasis |

### Business-Case-Logik

- **Subscription:** Höhere Kundenloyalität, vorhersehbarer Revenue
- **Einmalkauf:** Höhere Margen pro Transaktion, ggf. höhere CAC-Effizienz
- **Ziel:** 60/40 Split (Subscription/One-Time) nach 6 Monaten

---

## Break-even-Analyse

### Formel
```
Break-even Units/Monat = Fixkosten / Contribution Margin (pro Unit)
```

### Beispielrechnung (Base Case)

| Parameter | Wert |
|---|---|
| Fixkosten/Monat | €1.400 |
| RRP blended | €1,38 |
| COGS | €0,55 |
| Contribution Margin | €0,83 |
| **Break-even Units** | **~1.687 Sachets/Monat** |
| **Tagesquote** | **~56 Sachets/Tag** |

### Sensitivitätsanalyse (3 Szenarien)

| Szenario | COGS | Contribution | Fixkosten | Break-even Units/Monat |
|---|---|---|---|---|
| Pessimistisch | €0,65 | €0,73 | €1.800 | ~2.466 |
| Base Case | €0,55 | €0,83 | €1.400 | ~1.687 |
| Optimistisch | €0,45 | €0,93 | €1.000 | ~1.075 |

---

## Pricing-Benchmark-Vergleich

### DRYLL (Competitor #1)
- **Format:** 7g Stick-Pack (Ashwagandha, Theanin, Koffein Stack)
- **RRP:** €0,99 (Subscription) / €1,20–1,33 (1x)
- **COGS (geschätzt):** €0,50–0,65
- **Marge:** 35–50% (Sub) / 50–60% (1x)
- **Takeaway:** DRYLL ist aggressiv auf Preis, aber auf Subscription fokussiert

### Bulletproof (Competitor #2)
- **Format:** Brain Octane (Kapseln) oder Ready-to-Drink
- **RRP:** €1,30–1,50 (Kapseln), €2–3 (RTD)
- **Marge:** 45–55% (Kapseln)
- **Takeaway:** Premium-Positionierung + höhere Margen

### Kimera (Competitor #3)
- **Format:** Sachets (ähnlich wie unser MVP)
- **RRP:** €0,65–0,75
- **COGS (geschätzt):** €0,35–0,45 (aggressive Kostenkontrolle)
- **Marge:** 60–70%
- **Takeaway:** Kimera ist sehr kosteneffizient; Performance Coffee kann höher positionieren (€1,20–1,80)

### Performance Coffee (Ziel)
- **Format:** 10g Sachet (Stack A: L-Theanin 200mg, L-Tyrosine, Koffein, B-Vitamine)
- **RRP:** €1,50 (Midpoint der €1,20–1,80-Spanne)
- **COGS:** €0,55 (Base Case)
- **Marge:** 63%
- **Positionierung:** Premium über Kimera, kompetitiv mit Bulletproof, höher als DRYLL

---

## MOQ-Sensitivität

Die Unit-COGS hängt stark von der Batch-Größe ab:

| MOQ | Inhaltsstoff-Unit | Verpackung-Unit | CM Fee | Total COGS |
|---|---|---|---|---|
| **500 Units** (Mini-Batch) | €0,15 | €0,22 | €0,10 | €0,65+ |
| **1.000 Units** (Standard) | €0,13 | €0,19 | €0,08 | €0,55 |
| **5.000 Units** (Skalierung) | €0,11 | €0,16 | €0,06 | €0,45 |

**Entscheidungshilfe:**
- MVP mit 500er MOQ → höhere COGS, aber geringeres Kapital erforderlich
- Skalierung auf 5k MOQ → niedrigere COGS, aber €15–25k Lagerkosten + Demand-Risiko

---

## Margen-Szenarien (Detailliert)

### Szenario A: Pessimistisch (hochmargiges Risiko)
**Annahmen:**
- COGS: €0,65 (500er MOQ, schlechte Supplier-Quotes)
- RRP: €1,50 (kein Rabatt, volle Marge nötig)
- Fixkosten: €1.800/Monat (Full-Time-Gründer-Gehalt ~€800 + Shopify/Ops €1.000)
- Conversion Rate: 1% (sehr konservativ)

**Implikation:**
- Bruttomarge: 57%
- Break-even: ~2.466 Units/Monat (82 Units/Tag)
- First-Year-Target (3.000 Units/Monat) → €3.510 Brutto-Profit/Monat

**Risiko:** Hohe Unit-Kosten machen Profitabilität fragil; Subscription-Rabatt nicht möglich.

### Szenario B: Base Case (realistisch)
**Annahmen:**
- COGS: €0,55 (1k MOQ, mittlere Supplier-Quotes)
- RRP: €1,38 blended (Subscription €1,30 + 1x €1,50)
- Fixkosten: €1.400/Monat (Shopify, Freelancer Content, Admin)
- Conversion Rate: 1,5% (Organic + Organic Social)

**Implikation:**
- Bruttomarge: 63%
- Break-even: ~1.687 Units/Monat (56 Units/Tag)
- First-Year-Target (5.000 Units/Monat) → €4.150 Brutto-Profit/Monat
- 12 Monate → ~€50k EBIT (nach Fixkosten, vor Steuern + Verlustvortrag-Offset)

**Plausibilität:** Entspricht typischen DTC-Nutrition-Brands mit 1–2% Conversion im organischen Kanal.

### Szenario C: Optimistisch (scale-up)
**Annahmen:**
- COGS: €0,45 (5k MOQ, beste Supplier-Quotes)
- RRP: €1,50 (Subscription €1,35 durchgesetzt; 60/40 Mix)
- Fixkosten: €1.000/Monat (Gründer unbezahlt, nur Shopify/Tools)
- Conversion Rate: 2% (Instagram + Influencer-Seeding)

**Implikation:**
- Bruttomarge: 70%
- Break-even: ~1.075 Units/Monat (36 Units/Tag)
- First-Year-Target (10.000 Units/Monat) → €5.500 Brutto-Profit/Monat
- 12 Monate → ~€66k EBIT

**Plausibilität:** Erreichbar mit Influencer-Partnership (z.B. Huberman Lab Shoutout) oder Sponsorship.

---

## Verlustvortrag & Steuerliche Auswirkung

Das Quelldokument adressiert den Wagglz GmbH Verlustvortrag von ~€150k:

**Impact auf Performance Coffee ESt 2025:**
- Falls Performance Coffee 2026 als separate GmbH gegründet wird: **Kein direkter Impact** (Gewinne gehören neue Entität)
- Falls unter Wagglz GmbH fortgeführt: **Großer Impact** (€150k Verlustvortrag offset die ersten Gewinne)

**Steuereffekt (Base Case):**
- Performance Coffee 2026 EBIT: €50k
- Normale Körperschaftsteuer (30%): €15k
- Mit Verlustvortrag: €0 (€50k offset gegen €150k Vortrag)
- **Steuer-Einsparung: €15k in 2026**

**Strategie:** Gewinne der Performance Coffee unter Wagglz GmbH zu halten maximiert Verlustvortrag-Nutzung.

---

## Blockers & Abhängigkeiten

### 1. CMO-Quote erforderlich (blockiert Verpackung + CM Fee)
- Verpackungskosten sind ohne CMO-Zitat nicht genau kalkulierbar
- Varianz: €0,15–0,25 pro Unit möglich
- **Abhängig von:** [[Prinova]], [[Lehvoss Nutrition]], [[Nutri-Epitech]], [[Aidea]], [[Herbafit]] Responses

### 2. Amazentis-Lizenzverhandlung (blockiert Phase 3)
- Falls Urolithin A in Phase 3 geplant: Lizenzkosten unbekannt
- Könnte COGS um €0,10–0,20 erhöhen
- **Abhängig von:** IP-Modul (Modul 8) Ergebnisse

### 3. Fixkosten-Definition (blockiert Break-even)
- Shopify, Content, Ops sind Schätzungen
- Final-Zahlen müssen aus Modul 07 (GTM) abgeleitet werden
- **Abhängig von:** Vermarktungs- & Operations-Planung

### 4. Conversion-Rate-Annahme
- Break-even hängt auch von CAC und ROAS ab
- Organischer Kanal: 1–2% Conversion (optimistisch für Kalt-Traffic)
- Influencer-Kanal: 2–5% möglich
- **Abhängig von:** Early Traction + Audience-Testing

---

## Deliverable-Checkliste

- [ ] **`inhaltsstoffe_db.csv` gefüllt** — ≥5 Quotes pro Zutat (L-Theanin, L-Tyrosine, Alpha-GPC, Koffein, B-Vitamine, Kaffee-Blend)
- [ ] **`unit_economics.py` Szenario-Output** — 3 Szenarien mit Sensitivitätsanalyse
- [ ] **Pricing-Empfehlung SKU #1** — RRP €1,50, Subscription €1,30, Begründung
- [ ] **Break-even-Chart** — 3 Linien (Pessimistisch/Base/Optimistisch); Markierungen bei Break-even + First-Year-Target

---

## Verwandte Seiten

- [[Performance Coffee Brand]] — übergeordnetes Projekt
- [[00 Auftragsbrief Performance Coffee]] — Modul-Kontext
- [[02 Produkt & Rezeptur Performance Coffee]] — Stack A-Spezifikation
- [[03 Lieferkette & Produktion Performance Coffee]] — CMO Sourcing
- [[05 Recht & Regulatorik Performance Coffee]] — Verlustvortrag-Kontext
- [[07 Vermarktung & Operations Performance Coffee]] — Fixkosten-Definition
- [[Performance Coffee Unit Economics Model]] — konzeptuelle Synthese
- [[COGS Breakdown Performance Coffee]] — Waterfall-Analyse
- [[Performance Coffee Pricing Benchmark]] — Wettbewerber-Vergleich
- [[Modul 06 Quelldokument]] — raw Quelldokumentation
