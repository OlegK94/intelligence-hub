---
title: "00 Auftragsbrief — Performance Coffee Brand"
type: source
tags: [performance-cafe, modul-00, auftragsbrief, project-scope, research, timeline, stakeholder, dependencies, cli-code-workflow]
sources: ["raw/Business/PerformanceCafe/recherche/00_Auftragsbrief.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Modul 00 — Performance Coffee Brand Auftragsbrief; Projekt-Scope: DTC-Launch DACH Tier 1 (Stack A) Phase 1, Event-Sampling Phase 2, Longevity-Wirkstoffe Phase 3; Stakeholder: Oleg (Strategie/Brand), Hai (Operations); Markenname Aevum „Perform Now. Live Longer."; Research-Submodule 01–08 mit Claude Code-Workflows; Deliverables, Timeline, Budget-Richtlinien; Abhängigkeits-DAG
---

# 00 Auftragsbrief — Performance Coffee Brand

## Überblick

Dies ist das **Modul 00 (Auftragsbrief)** für das **[[Performance Coffee Brand]]-Projekt** von [[Oleg Personal Context|Oleg]] und [[Hai — Co-Founder Performance Coffee|Hai]]. Der Auftragsbrief definiert den Projekt-Scope, Stakeholder, Research-Submodule (Modul 01–08), Deliverables und Timeline.

> **Status:** Leitdokument; verbindet alle Forschungsmodule (01–08)
> **Zielgruppe:** Research-Team, Claude Code, Projektverantwortliche

## Projekt-Scope & Vision

### Marke & Positionierung
- **Markenname:** [[Aevum — Performance Coffee Markenname|Aevum]]
- **Tagline:** „Perform Now. Live Longer."
- **Positionierung:** Premium-Performance-Coffee mit funktionellen Inhaltsstoffen (Tier 1) und Longevity-Wirkstoffen (Tier 3)
- **Zielmarkt primär:** DACH (Deutschland, Österreich, Schweiz)
- **Zielkunde:** Biohacker, Fitnessenthusiasten, Health-Conscious Professionals, Bryan Johnson-inspirierte Community

### Phase-Struktur

| Phase | Zeitrahmen | SKU | Kanal | Ziele |
|---|---|---|---|---|
| **Phase 1 (Tier 1: Stack A)** | 2026 Q3–Q4 | Kaffeesachets + optional Kapseln-Duo-Pack | DTC Shopify DE primär | 500+ Kunden, 25% Repeat-Rate, Break-even Unit-Economics |
| **Phase 2 (Event + B2B)** | 2026 Q4–2027 Q2 | Stack A + Sampling-SKU | Event-Sampling (Hyrox, Gym-Partner) + Wholesale B2B | 5.000+ kumulativ, Gym-Partner-Netzwerk, Amazon DE Listing |
| **Phase 3 (Longevity)** | 2027+ | Stack A + Stack B (NMN/Urolithin A/Spermidin — abhängig von Zulassung/Lizenzen) | DTC + Retail (dm/Rossmann Phase 2+) | Niche-Leadership, Longevity-Marke-Differenzierung, Retail-Distribution |

### Stack-Definition

**Stack A (Tier 1 — Launch-ready):**
- L-Theanin 200 mg
- L-Tyrosine 500 mg
- Alpha-GPC (eingeschränktes Novel Food, vorsicht)
- Koffein 70–200 mg (je nach Format)
- B-Vitamine (B6, B12, B5 NRV)
- Ashwagandha KSM-66 300–600 mg
- Kaffee-Blend (12–15 g/Portion, spezialisierter Röstung)

**Stack B/C (Tier 2/3 — Phase 3, abhängig von Zulassung):**
- NMN (Chromadex-Patent, EFSA-Positiv Mai 2026, EC-Autorisierung ausstehend)
- Urolithin A (Amazentis Novel Food proprietär, bis ~2034 geschützt)
- Spermidin (nur Weizenkeimextrakt, ≤6 mg/Tag, NEM-only)
- Weitere Longevity-Wirkstoffe (Post-2027 Evaluierung)

## Stakeholder & Rollen

| Stakeholder | Rolle | Verantwortung |
|---|---|---|
| **[[Oleg Personal Context\|Oleg]]** | Mitgründer (50%) | Strategie, Brand, Business Model, Finanzen, Go-to-Market |
| **[[Hai — Co-Founder Performance Coffee\|Hai]]** | Mitgründer (50%) | Operations, Fulfillment, B2B-Beziehungen, CM-Management |
| **[[SP STB]]** (Steuerberater) | Finanzen-Advisor | Entity-Struktur, Verlustvortrag-Optimization, ESt-Integration |
| **Externe Partner TBD** | CMO, Supplier, Marketer | Prototyping, CM, Logistics, Growth-Marketing |

## Research-Submodule (01–08) & Claude Code Workflow

Jedes Modul ist ein **verwalteter Platzhalter** mit explizitem Claude Code-Auftrag:

```
Arbeite Modul [N] ([Titel]) aus.
Lies recherche/00_Auftragsbrief.md für den vollständigen Auftrag.
Schreibe alle Ergebnisse nach recherche/_archiv/[N]_[slug].md.
Nutze web_search für aktuelle Daten (2024/2025).
Quellenangaben am Ende jedes Abschnitts.
```

| Modul | Titel | Status | Deliverable | Abhängigkeit |
|---|---|---|---|---|
| **01** | Ingredienzen Datenbank | ⏳ Claude Code | inhaltsstoffe_db.csv (≥5 Quotes/Zutat) + Kostenanalyse | Modul 00 |
| **02** | Produkt & Rezeptur | ⏳ Modul 01 | Stack-A-Formulierung Final, Packaging-Spec | Modul 01 |
| **03** | Kaffee-Spezifikation | ⏳ Claude Code | Blend-Definition, Roaster-Quotes, SCA-Score-Analyse | Modul 00 |
| **04** | Marktanalyse & Wettbewerb | ⏳ Claude Code | Competitor-Matrix, TAM/SAM/SOM, Pricing-Benchmarks (DRYLL, Four Sigmatic, etc.) | Modul 00 |
| **04-alt** | Prototyp-Partner | ⏳ Claude Code | CMO-Kandidaten, Sensory-Test-Protokoll, Lead-Times | Modul 00 |
| **05** | Recht & Regulatorik | ⏳ Parallel | Novel Food-Compliance, Health Claims, Entity-Struktur, Co-Founder-Vereinbarung | Modul 00 |
| **06** | Kalkulation & Pricing | ⏳ Modul 01, 03 | COGS-Waterfall, RRP-Empfehlung, Break-even-Analyse, unit_economics.py | Modul 01, 03 |
| **07** | Vermarktung & Operations | ⏳ Modul 06 | DTC-Launch-Plan, Channel-Mix, KPI-Dashboard, Fulfillment-Strategie | Modul 06 |
| **08** | IP & Patent-Landschaft | ⏳ Claude Code | Markenname-Registrierung (Aevum EUIPO), Patent-FTO-Analyse, Lizenzierungskosten | Modul 00 |

## Abhängigkeits-DAG (vereinfacht)

```
Modul 00 (Auftragsbrief)
├── Modul 01 (Ingredienzen DB) ← Claude Code
│   └── Modul 02 (Produkt & Rezeptur)
│       └── Modul 06 (Kalkulation & Pricing)
│           └── Modul 07 (Vermarktung & Ops)
├── Modul 03 (Kaffee-Spec) ← Claude Code
│   └── Modul 06 (Kalkulation & Pricing)
├── Modul 04 (Marktanalyse) ← Claude Code
│   └── Modul 07 (Vermarktung & Ops)
├── Modul 04-alt (Prototyp-Partner) ← Claude Code
│   └── Modul 02, 06
├── Modul 05 (Recht & Regulatorik) — Parallel
│   └── Alle nachgelagerten Module
└── Modul 08 (IP & Patent) ← Claude Code
    └── Modul 05 (Regulatory-Kontext)
```

## Deliverables (Final)

### Pro-Modul Deliverables (siehe oben)

### Cross-Modul Deliverables
- **Performance Coffee Business Model Canvas** (A1-Poster)
- **Go-to-Market Timeline** (Gantt-Chart)
- **Financial Model** (unit_economics.py + Excel)
- **Risk Register & Mitigation-Plan**
- **Competitive Positioning-Deck** (5–10 Slides für Hai-Diskussion)

## Timeline & Milestones

| Milestone | Zieldatum | Abhängigkeit |
|---|---|---|
| **Modul 01–04 Claude Code ausgeführt** | 2026-06-30 | Auftragsbrief vorhanden |
| **Stack A Formulierung Final** | 2026-07-15 | Modul 01 + 02 |
| **CMO-Quotes eingegangen** | 2026-07-30 | Modul 01 + 02 + 03 |
| **Prototyp-Batch bestellt (500–1.000 Units)** | 2026-08-15 | CMO-Quote OK, Funding vorhanden |
| **Prototyp-Sensory-Tests durchgeführt** | 2026-09-15 | Prototyp erhalten |
| **Shopify MVP gestartet** (Friends & Family) | 2026-10-01 | Modul 07 + Formulation Final |
| **Phase 1 Public Launch (Modul 07)** | 2026-10-15 | MVP + Compliance OK |
| **Phase 2 Trigger erreicht (500 Kunden)** | 2026-Q4 oder 2027-Q1 | Launch erfolgreich |

## Budget-Richtlinien (illustrativ)

| Bereich | Budgetrahmen | Quelle |
|---|---|---|
| **Research & Development** | €3.000–5.000 | Prototyping, Sensory Tests, Gründungskosten |
| **Modul 01–08 Recherche** | €0 (Claude Code intern) | Dieses Projekt |
| **EUIPO Markenname-Registrierung** | €500–1.000 | Aevum Trademark |
| **Phase 1 DTC Launch (Shopify, Ads, Content)** | €5.000–10.000 | Erste 3 Monate |
| **Erste Batch Production (1.000 Units @ €0,55 COGS)** | €550–650 | Manufacturing + Fulfillment Setup |
| **Phase 2 Event-Sampling (Hyrox, Gym)** | €3.000–5.000 | Sampling + Logistics |

**Gesamtbudget Phase 1:** ~€10.000–15.000 (excl. Co-Founder-Gehalt)

> ⚠️ **Anmerkung:** Olegs persönliche Finanz-Situation ([[00 Finanz-Übersicht]]) zeigt Dispo €-1.405 und Ersparnisse €1,10. Die [[Rehabilitation Plan|3-Phasen-Finanzielle-Rehabilitation]] muss parallel laufen, um Phase-1-Funding zu sichern. Mögliche Quellen: Eigenkapital nach July Commission, Angel-Investor, Bank-Darlehen via [[SP STB]]-Netzwerk.

## Spezielle Anmerkungen

### Entity-Struktur-Entscheidung (offen)
Die Performance Coffee Brand kann unter:
- **Wagglz GmbH** (bestehende Gesellschaft, Brand-Separation via Markenname möglich)
- **Neue GmbH** (Performance Coffee GmbH o.ä., saubere Struktur, separate Haftung)

gegründet werden. Siehe [[05 Recht & Regulatorik (EU Lebensmittel/Supplements)]] für Vor/Contra. **Entscheidung erforderlich vor Co-Founder-Vereinbarung mit Hai.**

### Verlustvortrag Wagglz (~€150k)
Der Verlusvortrag von [[Wagglz GmbH]] kann das Performance Coffee-Business steuerlich begünstigen, **wenn** die Gewinne unter der Wagglz GmbH-Dachstruktur anfallen. Siehe [[SP STB]] für Optimierungsstrategien.

### Amazentis & Chromadex Lizenzierungen
Phase 3 ist **blockiert** durch:
- Amazentis Urolithin A Lizenzkosten (unbekannt, proprietary)
- Chromadex NMN Patent-Status post-EFSA (EC-Autorisierung ausstehend)

Diese müssen **parallel** mit Start der Phase-1-Recherche evaluiert werden.

## Verknüpfungen

- **[[Performance Coffee Brand]]** — übergeordnete Projekt-Entität
- **[[Aevum — Performance Coffee Markenname]]** — Markenname
- **[[Modul 01–08 (je einzeln)]** — Research-Submodule (siehe Tabelle oben)
- **[[Hai — Co-Founder Performance Coffee]]**, **[[Oleg Personal Context]]** — Stakeholder
- **[[00 Finanz-Übersicht]]**, **[[Rehabilitation Plan]]** — Finanz-Kontext
- **[[SP STB]]** — Advisor (Entity, Steuern)
- **[[Amazentis]]**, **[[Chromadex]]** — Lizenzierungs-Partner Phase 3
