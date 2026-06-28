---
title: "Performance Coffee Brand — Archivierte Legacy-Recherche README"
type: source
tags: [performance-cafe, recherche, module-01-07, legacy, archive, claude-code, placeholder, 2026-06-14]
sources: ["raw/Business/PerformanceCafe/recherche/_archiv/README.md"]
created: 2026-06-14
updated: 2026-06-17
summary: "Quelldokument-Index der Legacy-Recherche-Placeholder (Modul 0–7) aus 2026-06-14; dokumentiert Modul-Verschiebung von leeren Claude-Code-Stubs zu aktiver 00–07-Struktur; Mapping: Modul 00 (Auftragsbrief) → 01 (Ingredienzen DB), 02 (Produkt), 03 (Lieferkette), 04 (Markt), 05 (Recht), 06 (Kalkulation), 07 (Vermarktung); Novel Food-Regulatorik nach recht/novel_food_longevity_wirkstoffe.md verschoben"
---

# Performance Coffee Brand — Archivierte Legacy-Recherche README

## Überblick

Dieses Quelldokument (`raw/Business/PerformanceCafe/recherche/_archiv/README.md`) dokumentiert die **Archivierungsstruktur der Legacy-Rechercheplatzhalter** für die [[Performance Coffee Brand]]-Recherche. Die Datei wurde am 2026-06-14 erstellt und zeigt, welche **älteren Claude-Code-Stubs** (Modul-Nummern 01–07) durch die neue **aktive 00–07-Modulstruktur** ersetzt wurden.

> Die **aktiven Quelldokumente** sind separat dokumentiert in [[02 Ingredienzen Datenbank Performance Coffee Quelldokument]], [[03 Kaffee-Spezifikation Performance Coffee Quelldokument]], etc.

## Archivierte Dateistruktur (Mapping-Tabelle)

| Datei (archiviert) | War Modul | Ersetzt durch | Neuer Scope |
|---|---|---|---|
| `01_longevity_science.md` | 0 | `01_Markt_Wettbewerb.md` | Anderer Fokus; Markt statt Wissenschaft |
| `02_ingredienzen_db.md` | 1 | `02_Produkt_Rezeptur.md` + raw `Inhaltsstoffe — Datenbank.md` | Ingredient sourcing + product formulation |
| `03_kaffee_specs.md` | 2 | `03_Lieferkette_Produktion.md` + raw `Kaffee — Rohstoffanalyse.md` | Coffee sourcing + supply chain |
| `04_marktanalyse.md` | 3 | `01_Markt_Wettbewerb.md` | Market analysis (jetzt Modul 01) |
| `05_prototyp_partner.md` | 4 | `03_Lieferkette_Produktion.md` + raw `Prototyp — Hersteller & Prompt.md` | Prototyping partner sourcing + CMO |
| `07_business_case.md` | 6 | `06_Kalkulation_Pricing.md` + `07_Vermarktung_Operations.md` | COGS + pricing + GTM |

## Modul-Neustrukturierung

### Alte Struktur (Legacy, 2026-06-14)

```
Modul 0: 01_longevity_science.md — Longevity science deep-dive
Modul 1: 02_ingredienzen_db.md — Ingredient database & sourcing
Modul 2: 03_kaffee_specs.md — Coffee specifications
Modul 3: 04_marktanalyse.md — Market analysis
Modul 4: 05_prototyp_partner.md — Prototyping partner research
Modul 5: (nicht dokumentiert hier; 06_regulatorik.md separat)
Modul 6: 07_business_case.md — Business case & COGS
```

### Neue Struktur (Aktiv, 2026-06-14 onwards)

```
Modul 00: 00_Auftragsbrief.md — Master brief; Stack A spec; compliance requirements
Modul 01: 01_Markt_Wettbewerb.md — Market analysis + competitor benchmarking
Modul 02: 02_Produkt_Rezeptur.md — Product formulation + ingredient integration
Modul 03: 03_Lieferkette_Produktion.md — Supply chain + CMO sourcing + coffee specs
Modul 04: 04_Prototyp_Partner.md — Prototyping partner evaluation + sensory protocol
Modul 05: 05_Recht_Regulatorik.md — Regulatory compliance + entity structure
Modul 06: 06_Kalkulation_Pricing.md — COGS model + RRP + subscription pricing
Modul 07: 07_Vermarktung_Operations.md — DTC launch strategy + KPI dashboard
```

## Novel Food-Regulatorik (Verschiebung)

Die Regulatorische Recherche zu **Novel Food und Longevity-Wirkstoffen** wurde aus der Legacy-Struktur auf die dedizierte Seite verschoben:

- **Zielseite:** `raw/Recht/novel_food_longevity_wirkstoffe.md`
- **Modul-Integration:** Teilweise in [[05 Recht Regulatorik EU Lebensmittel Supplements]], teilweise in [[Longevity Wirkstoffe Novel Food Status]]
- **Effekt:** Klare Trennung von Performance-Coffee-spezifischem Recht und globalem Longevity-Wirkstoffe-Überblick

## Status der Legacy-Dateien

| Datei | Status | Aktion |
|---|---|---|
| `01_longevity_science.md` | ✅ Archiviert | Nach `_archiv/` verschoben; Inhalte in [[Longevity Wirkstoffe Novel Food Status]] konsolidiert |
| `02_ingredienzen_db.md` | ✅ Archiviert | Nach `_archiv/` verschoben; Struktur in [[02 Ingredienzen Datenbank Performance Coffee Quelldokument]] überführt |
| `03_kaffee_specs.md` | ✅ Archiviert | Nach `_archiv/` verschoben; Struktur in [[03 Kaffee-Spezifikation Performance Coffee Quelldokument]] überführt |
| `04_marktanalyse.md` | ✅ Archiviert | Nach `_archiv/` verschoben; Struktur in [[04 Marktanalyse Wettbewerb Performance Coffee Quelldokument]] überführt |
| `05_prototyp_partner.md` | ✅ Archiviert | Nach `_archiv/` verschoben; Struktur in [[05 Prototyp-Partner Quelldokument]] überführt |
| `06_regulatorik.md` | ✅ Archiviert | Nach `raw/Recht/` verschoben; Struktur in [[05 Recht Regulatorik EU Lebensmittel Supplements]] überführt |
| `07_business_case.md` | ✅ Archiviert | Nach `_archiv/` verschoben; Struktur in [[06 Kalkulation Pricing Performance Coffee]] und [[07 Business Case Performance Coffee Quelldokument]] aufgesplittet |

## Claude Code — Auftrag der Legacy-Dateien

Alle Legacy-Dateien waren ursprünglich als **Claude Code-Aufträge** strukturiert:

```
Arbeite Modul N (Name) aus.
Lies recherche/00_Auftragsbrief.md für den vollständigen Auftrag.
Schreibe alle Ergebnisse nach recherche/_archiv/XX_name.md.
Nutze web_search für aktuelle Daten (2024/2025).
Quellenangaben am Ende jedes Abschnitts.
```

Diese Aufträge waren **nicht ausgeführt** — alle Legacy-Dateien waren bloße Platzhalter/Prompts, die auf Claude Code warteten.

## Neuer Auftragsfluss (2026-06-14 onwards)

Mit der neuen 00–07-Struktur:

1. **Modul 00 (Auftragsbrief)** wird zuerst finalisiert
2. **Module 01–07** werden parallel oder sequenziell ausgeführt
3. **Quelldokumente** werden direkt in `raw/Business/PerformanceCafe/recherche/` gespeichert (nicht in `_archiv/`)
4. **Wiki-Seiten** (`02 Ingredienzen Datenbank Performance Coffee Quelldokument`, etc.) dokumentieren den Research-Status in Echtzeit

## Verwandte Seiten

- [[Performance Coffee Brand]] — Projekt-Entität
- [[00 Auftragsbrief Performance Coffee]] — Modul 00; Master brief
- [[02 Ingredienzen Datenbank Performance Coffee Quelldokument]] — Modul 01 aktiv
- [[03 Kaffee-Spezifikation Performance Coffee Quelldokument]] — Modul 03 aktiv
- [[04 Marktanalyse Wettbewerb Performance Coffee Quelldokument]] — Modul 04 aktiv
- [[05 Prototyp-Partner Quelldokument]] — Modul 04-alt aktiv
- [[05 Recht Regulatorik EU Lebensmittel Supplements]] — Modul 05 aktiv
- [[06 Kalkulation Pricing Performance Coffee]] — Modul 06 aktiv
- [[07 Vermarktung Operations Quelldokument]] — Modul 07 aktiv
- [[Longevity Wirkstoffe Novel Food Status]] — Novel Food-Regulatorik (verschoben aus `06_regulatorik.md`)
- [[MOC Performance Coffee Brand]] — Master-Index aller Performance-Coffee-Seiten
