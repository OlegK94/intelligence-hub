TAGS: [performance-cafe, cogs, pricing, unit-economics, break-even, margin, subscription, rrp, inhaltsstoffe, verpackung, fulfillment, kalkulation, recherche, modul-06]
SOURCES: ["raw/Business/PerformanceCafe/recherche/06_Kalkulation_Pricing.md"]
CREATED: 2026-06-14
UPDATED: 2026-06-14
SUMMARY: Quelldokument Modul 06 — Kalkulation & Pricing für Performance Coffee Brand; COGS-Modell (Inhaltsstoffe + Kaffee + Verpackung + CM Fee + Fulfillment), RRP-Festlegung (€1,20–1,80/Portion; 55–65% Bruttomarge), Subscription-Pricing (10–25% Rabatt), Break-even-Analyse (Fixkosten ÷ Contribution Margin), Margen-Szenarien (pessimistisch/base/optimistisch), MOQ-Sensitivität (500 vs. 1k vs. 5k), Verlustvortrag ~€150k Impact auf ESt 2025; Benchmarks gegen DRYLL, Bulletproof, Kimera; Deliverables: unit_economics.py Output, gefüllte inhaltsstoffe_db.csv Kosten-Spalten (≥5 Quotes), Pricing-Empfehlung SKU #1, Break-even-Chart.

---

# 06 — Kalkulation & Pricing (Quelldokument)

## Überblick

Dieses Quelldokument (Status: Entwurf, erstellt 2026-06-14) ist das **Modul 06** der strukturierten [[Performance Coffee Brand]]-Recherche und adressiert die zentrale Frage: **Wie viel kostet es, Performance Coffee zu produzieren, und zu welchem Preis kann es profitabel verkauft werden?**

Das Modul bildet eine kritische Brücke zwischen den regulatorischen (Modul 05) und lieferkettenspezifischen (Modul 03) Entscheidungen einerseits und der Go-to-Market-Strategie (Modul 07) andererseits.

> Für die konzeptuelle Einordnung siehe [[Performance Coffee Modul 06 — Kalkulation & Pricing]].
> Zum Auftragsbrief und Kontext siehe [[00 Auftragsbrief Performance Coffee]].

---

## Ziel (aus Quelldokument)

Verteidigbares COGS-Modell aufbauen, RRP und Subscription-Pricing festlegen sowie Break-even-Volumen berechnen. Die quantitativen Backbones sind:
- `modelle/unit_economics.py` — Szenario-Modellierung
- `modelle/inhaltsstoffe_db.csv` — Kostenbasen für alle Zutaten

---

## Zentrale Leitfragen (Modul 06)

1. **COGS pro Portion nach Format** (Inhaltsstoffe + Kaffee + Verpackung + CM Fee + Inbound Shipping)?
2. **Ziel-Bruttomarge %** (Benchmark: DRYLL €0,99–1,31/Portion retail)?
3. **RRP für SKU #1** — Einmalkauf vs. Subscription (10–25% Rabatt)?
4. **Break-even Units/Monat** bei gegebenen Fixkosten (Shopify, Content, minimal Ops)?
5. **Impact Verlustvortrag** (~€150k) auf effektive Steuer auf frühe Profite?
6. **Sensitivität:** MOQ 500 vs. 1k vs. 5k auf Unit-COGS?

---

## COGS-Struktur (Waterfall)

Das Quelldokument skizziert eine Kostenstruktur als Waterfall:

```
Inhaltsstoffe pro Portion
  + Kaffee (Blend TBD)
  + Verpackung (Primary + Secondary + Shipper)
  ─────────────────────
  = Manufacturing Baseline
  + Co-Packing Fee (pro Unit)
  + Fulfillment (3PL Pick-Pack + Shipping DACH avg)
  ─────────────────────
  = COGS (delivered to Warehouse)
```

**Zielbereich:** €0,45–0,65 pro Portion (bei 55–65% Bruttomarge, RRP €1,20–1,80).

---

## Inhaltsstoff-Stack & Kosten (Placeholder)

Das Quelldokument enthält einen Placeholder für **Stack-A-Kosten** — noch ausstehend mit Supplier-Quotes:

| Inhaltsstoff | Portion | Status |
|---|---|---|
| L-Theanin 200 mg | TBD | Recherche erforderlich |
| L-Tyrosine 500 mg | TBD | Recherche erforderlich |
| B-Vitamin-Premix NRV | TBD | Recherche erforderlich |
| Kaffee 12–15 g/Portion | TBD | Blend-Spezifikation ausstehend |

**Deliverable:** Gefüllte `inhaltsstoffe_db.csv` mit ≥5 Supplier-Quotes für jede Zutat.

---

## Verpackungskosten (Placeholder)

Zerlegung nach:
- **Primary:** Inhalt-Sachet (Aluminium-Verbundfolie, Druckkosten)
- **Secondary:** Outer Box (Karton, Druck, Klebstoff)
- **Shipper:** Versandkarton (bei Großmengen-Lagerhaltung)

**MOQ-Effekt:** Kosten fallen deutlich bei 500 → 1.000 → 5.000 Units.

**Abhängigkeit:** CMO-Quote erforderlich (siehe [[Prinova]], [[Lehvoss Nutrition]], [[Nutri-Epitech]], [[Aidea]], [[Herbafit]]).

---

## Pricing-Benchmarks (aus Modul 06)

| Brand | Format | COGS (geschätzt) | RRP | Bruttomarge |
|---|---|---|---|---|
| **DRYLL** | Sticks (7g) | ~€0,50–0,65 | €0,99 (Sub) / €1,20–1,33 (1x) | 35–50% / 50–60% |
| **Bulletproof** | Kapseln / Packs | ~€0,60–0,80 | €1,30–1,50 | 45–55% |
| **Kimera** | Sachets | ~€0,35–0,45 | €0,65–0,75 | 60–70% |
| **Specialty Coffee DE** | 250g Bag | ~€4–8 Material | €14–24 RRP | 40–60% |
| **Performance Coffee (Ziel)** | Sachets (10g) | €0,45–0,65 | €1,20–1,80 | 55–65% |

**Insight:** DRYLL ist das primäre Positioning-Benchmark; Kimera zeigt, dass auf dem Sachet-Markt aggressive Margen möglich sind (60–70%), wenn CMO-Kosten niedrig sind.

---

## Pricing-Strategie (aus Modul 06)

### RRP-Festlegung für SKU #1

**Vorschlag:** €1,50 RRP (Midpoint der €1,20–1,80-Spanne)

| Szenario | RRP | COGS | Contribution | Marge |
|---|---|---|---|---|
| Pessimistisch (hoch COGS) | €1,50 | €0,65 | €0,85 | 57% |
| Base Case | €1,50 | €0,55 | €0,95 | 63% |
| Optimistisch (niedrig COGS) | €1,50 | €0,45 | €1,05 | 70% |

### Subscription vs. Einmalkauf

**Empfehlung aus Modul 06:**
- Einmalkauf RRP: **€1,50/Sachet**
- Subscription RRP: **€1,30/Sachet** (13% Rabatt) oder **€1,35** (10% Rabatt)
- Subscription-Ziel: 60–70% Repeat-Rate; 30 Tage Lieferzyklus

**Business Case:** 60% Repeat → 60% der Customers = €1,30; 40% One-time = €1,50 → blended RRP €1,38.

---

## Break-even-Analyse (Struktur)

Das Quelldokument skizziert die Formel:

```
Break-even Units/Monat = Fixkosten / Contribution Margin (pro Unit)
```

**Fixkosten (geschätzt, aus Modul 07 abzuleiten):**
- Shopify + Payment Processing: ~€200–300/Monat
- Content & Marketing (minimal): ~€500–1.000/Monat
- Operations (Verwaltung, Email): ~€300–500/Monat
- **Total Fixkosten: ~€1.000–1.800/Monat**

**Contribution Margin:**
- Base Case: €0,95 pro Sachet
- Break-even = €1.400 ÷ €0,95 = **~1.470 Sachets/Monat** (oder ~49/Tag)

---

## Margen-Szenarien (Placeholder)

Das Quelldokument verweist auf `unit_economics.py` für 3 Szenarien:

### Szenario A: Pessimistisch
- COGS: €0,65/Portion
- RRP: €1,50 (keine Rabatte zunächst)
- Bruttomarge: 57%
- Fixkosten: €1.800/Monat
- Break-even: ~1.900 Units/Monat

### Szenario B: Base Case
- COGS: €0,55/Portion
- RRP: €1,50 (Subscription gemischt €1,35–1,50)
- Bruttomarge: 63%
- Fixkosten: €1.400/Monat
- Break-even: ~1.470 Units/Monat

### Szenario C: Optimistisch
- COGS: €0,45/Portion
- RRP: €1,50 (oder Premium €1,80)
- Bruttomarge: 70%
- Fixkosten: €1.000/Monat
- Break-even: ~667 Units/Monat

---

## MOQ-Sensitivität

Das Quelldokument fragt explizit nach dem Impact von Mindestbestellmengen auf Unit-COGS:

| MOQ | Unit-Preis Inhaltsstoffe | Unit-Verpackung | Unit-COGS (gesamt) | Effekt |
|---|---|---|---|---|
| **500 Units** | €0,15 (höher) | €0,20 (höher) | €0,65+ | Pessimistisch |
| **1.000 Units** | €0,13 | €0,18 | €0,55 | Base Case |
| **5.000 Units** | €0,11 | €0,16 | €0,45 | Optimistisch |

**Unternehmensimplikation:** Der Break-even hängt stark davon ab, ob der MVP mit 500er oder 1.000er Batches startet. 500 Units = Verlustvortrag-freie Launch; 1.000+ = schneller Break-even.

---

## Verlustvortrag ~€150k — Steuerliche Auswirkung

Das Quelldokument verweist auf Modul 05 (Recht & Regulatorik) und fordert:
- Impact des Wagglz GmbH Verlustvortrags (~€150k) auf die **ESt 2025** quantifizieren
- Falls Performance Coffee 2026 Profit macht, werden Gewinne mit dem Verlustvortrag verrechnet
- Dies senkt die **effektive Steuerquote** auf die frühen Profite erheblich

**Geschätzter Effekt:** Wenn Performance Coffee €30k EBIT 2026 erwirtschaftet, können diese gegen den Verlustvortrag verrechnet werden — Steuer ist 0–15% statt normal 30%.

---

## Deliverables (aus Modul 06)

### 1. Gefüllte `inhaltsstoffe_db.csv` Kosten-Spalten
- **Ziel:** ≥5 Quotes pro Inhaltsstoff
- **Inhalt:** L-Theanin, L-Tyrosine, Alpha-GPC, Koffein, B-Vitamine, Kaffee-Blend
- **Format:** CSV (ingredient | supplier_1_price | supplier_2_price | ... | supplier_5_price | avg_price | selected_supplier)

### 2. `unit_economics.py` Szenario-Output
- **Format:** Python-Szenario-Modellierung oder Excel-Datei
- **Output:** 3 Szenarien (Pessimistisch/Base/Optimistisch) mit Sensitivitätsanalyse
- **Speicherort:** `modelle/unit_economics.py` oder Bericht hier gespeichert

### 3. Pricing-Empfehlung für SKU #1
- **Format:** 1-seitiges Memo
- **Inhalt:** RRP (Einmalkauf + Subscription), Begründung, Wettbewerbsvergleich

### 4. Break-even-Chart
- **Format:** Grafik (Units/Monat vs. Profit)
- **Szenarien:** 3 Linien (Pessimistisch/Base/Optimistisch)
- **Markierungen:** Break-even-Punkte, First-Year-Target (z.B. 5.000 Units/Monat = Profit)

---

## Abhängigkeiten & Blockierte Entscheidungen

Das Modul 06 wird blockiert durch:

1. **CMO-Quote-Einholung** (Modul 03)
   - Verpackungskosten sind ohne CMO-Zitat nicht kalkulierbar
   - Co-Packing Fee variiert stark (€0,05–0,20 pro Unit)

2. **Amazentis-Lizenzverhandlungen** (IP-Modul)
   - Falls Urolithin A geplant: Lizenzkosten unbekannt
   - Impact auf Phase-3-Stack und COGS ungeklärt

3. **Fixkosten-Spezifikation** (Modul 07)
   - Shopify, Content, Ops sind Schätzungen
   - Final-Zahlen aus GTM-Planung erforderlich

4. **Conversion-Rate-Annahme**
   - Break-even hängt auch von der Kundenakquisitionskosten-Annahme ab
   - CAC vs. LTV nicht in diesem Modul adressiert

---

## Widersprüche & Offene Punkte

| Punkt | Status |
|---|---|
| Sollte SKU #1 als Sachet oder RTD gestartet werden? | Modul 02 (Produkt) muss klären |
| Ist €1,50 RRP im deutschen Markt kompetitiv? | Check24-Vergleich erforderlich |
| Welche Subscription-Gebührenstruktur ist optimal (monatlich, alle 2 Wochen)? | Abhängig von Conversion-Rate |
| Kann der €0,45 COGS mit 500er MOQ erreicht werden oder nur mit 5k? | CMO-Quote erforderlich |

---

## Verknüpfungen & Cross-Module

- **Modul 00:** Auftragsbrief; Ziele und Timeframe
- **Modul 02:** Produkt & Rezeptur; Stack-Spezifikation → Inhaltsstoff-Kosten
- **Modul 03:** Lieferkette & Produktion; CMO-Sourcing → Verpackungs + CM-Fee
- **Modul 05:** Recht & Regulatorik; Verlustvortrag € Impact
- **Modul 07:** Vermarktung & Operations; Fixkosten-Definition, GTM-Strategie
- **[[Performance Coffee Unit Economics Model]]:** konzeptuelle Synthese

---

## Quelldokument-Metadaten

| | |
|---|---|
| **Pfad** | raw/Business/PerformanceCafe/recherche/06_Kalkulation_Pricing.md |
| **Status** | Entwurf (research-in-progress) |
| **Erstellt** | 2026-06-14 |
| **Aktualisiert** | 2026-06-14 |
| **Parent** | recherche/00_Auftragsbrief.md |
| **Abhängigkeiten** | modelle/unit_economics.py, modelle/inhaltsstoffe_db.csv |
