---
title: "06 — Kalkulation & Pricing"
module: "06"
status: Entwurf
created: 2026-06-14
updated: 2026-06-14
parent: recherche/00_Auftragsbrief.md
summary: COGS, Margen, RRP, Subscription-Pricing, Break-even-Analyse
---

# 06 — Kalkulation & Pricing

## Ziel

Verteidigbares COGS-Modell aufbauen, RRP und Subscription-Pricing festlegen und Break-even-Volumen berechnen. `modelle/unit_economics.py` und `modelle/inhaltsstoffe_db.csv` als quantitativer Backbone.

## Leitfragen

- [ ] COGS pro Portion nach Format (Inhaltsstoffe + Kaffee + Verpackung + CM + inbound Ship)?
- [ ] Ziel-Bruttomarge % (Benchmark: DRYLL €0,99–1,31/Portion retail)?
- [ ] RRP für SKU #1 — Einmalkauf vs. Subscription (10–25 % Discount)?
- [ ] Break-even Units/Monat bei Fixkosten (Shopify, Content, minimal Ops)?
- [ ] Impact Verlustvortrag (~€150k) auf effektive Steuer auf frühe Profite?
- [ ] Sensitivität: MOQ 500 vs. 1k vs. 5k auf Unit-COGS?

## Abschnitte

### Kostenstruktur-Überblick

<!-- TODO: Waterfall — Inhaltsstoff → Kaffee → Pack → CM Fee → Fulfillment → COGS -->

### Inhaltsstoffkosten

<!-- TODO: Pro Portion aus inhaltsstoffe_db.csv; bei Angeboten aktualisieren -->

**Stack-A-Platzhalter (recherche_noetig):**
- L-Theanine 200 mg
- L-Tyrosine 500 mg
- B-Vitamin-Premix NRV
- Kaffee 12–15 g/Portion (Blend TBD)

### Verpackungskosten

<!-- TODO: Primary + Secondary + Shipper; MOQ-Breaks -->

### Manufacturing & Co-Packing

<!-- TODO: CM Fee pro Unit bei Prototyp vs. Scale -->

### Fulfillment & Versand

<!-- TODO: DACH avg. Ship Cost; 3PL Pick-Pack Fee -->

### Pricing-Strategie

<!-- TODO: RRP, Subscription Tiers, Launch Promo -->

**Benchmarks (aus [[01_Markt_Wettbewerb]] §7):**
- DRYLL Sticks: ~€0,99/Portion (Subscription), €1,20–1,33 Einmalkauf
- Specialty Coffee DE: €14–24/250g → €0,50–0,80/Portion
- Bulletproof EU: ~€1,30/Portion (22 Servings/€30)
- Kimera: ~€0,65–0,75/Portion
- **Performance Coffee Ziel:** €1,20–1,80/Portion RRP → 55–65% Bruttomarge bei €0,45–0,65 COGS

### Margen-Szenarien

<!-- TODO: unit_economics.py ausführen — 3 Szenarien dokumentieren (pessimistisch/base/optimistisch) -->

### Break-even-Analyse

<!-- TODO: Fixkosten/Monat ÷ Contribution Margin = Break-even Units -->

### Steuer & Verlustvortrag

<!-- TODO: GmbH Profit-Szenario mit Verlustvortrag -->

## Deliverables

- [ ] Gefüllte `inhaltsstoffe_db.csv` Kosten-Spalten (≥5 Quotes)
- [ ] `unit_economics.py` Szenario-Output hier gespeichert
- [ ] Pricing-Empfehlung für SKU #1
- [ ] Break-even-Chart

## Verknüpfungen

- Auftragsbrief: [[00_Auftragsbrief]]
- Lieferkette: [[03_Lieferkette_Produktion]]
- GTM: [[07_Vermarktung_Operations]]
- Modell: `../modelle/unit_economics.py`, `../modelle/inhaltsstoffe_db.csv`
