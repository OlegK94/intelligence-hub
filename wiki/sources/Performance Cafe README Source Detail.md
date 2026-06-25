---
title: Performance Cafe README Quelldokument-Detail
type: source
tags: [performance-cafe, projekt-setup, workflow, obsidian, cursor, claude-code, regulatorik, novel-food, ip, COGS, CMO, blocker, dateistruktur, prioritaeten]
sources: ["raw/Business/PerformanceCafe/README.md"]
created: 2026-06-16
updated: 2026-06-16
summary: Projekt-Setup-Dokument für Performance Café — beschreibt Obsidian/Cursor/Claude-Code-Workflow, Prioritätsreihenfolge der Research-Module, vollständige Dateistruktur und kritische Entscheidungsmatrix (NMN Novel Food, Amazentis-Patent, NAC-Geruch, Kölner Liste)
---

# Performance Cafe — README Quelldokument-Detail

## Überblick

Dieses Quelldokument (`raw/Business/PerformanceCafe/README.md`) ist das Einstiegsdokument für das [[Performance Coffee Brand]]-Projekt. Es definiert den technischen Workflow (Obsidian + Cursor + Claude Code), die Prioritätsreihenfolge der Research-Module und eine Tabelle kritischer Vorab-Entscheidungen.

> Zur Hauptprojektentität siehe [[Performance Coffee Brand]].
> Zu kritischen IP-Blockern siehe [[Amazentis]] und [[Chromadex Niagen Bioscience]].
> Zur Regulatorik siehe [[EU Novel Food Regulation]] und [[Performance Cafe Regulatorik Modul 5]].

---

## Tool-Setup (3 Schritte)

| Tool | Konfiguration |
|---|---|
| **Obsidian** | Ordner als Vault öffnen → alle `.md`-Dateien erscheinen in der Sidebar |
| **Cursor** | `.cursor/rules/performance_cafe.mdc` wird automatisch als Projektkontext geladen |
| **Claude Code** | Liest `CLAUDE.md` zu Beginn jeder Session; Start mit `claude` im Projektordner |

---

## Research-Modul-Workflow

### Einzelmodul (Claude Code)
```bash
claude "Arbeite Modul 1 (Ingredienzen Datenbank) aus.
Lies research/00_master_brief.md für den vollständigen Auftrag.
Schreibe Ergebnisse nach research/02_ingredienzen_db.md"
```

### Regulatorik-Priorität (Blocker zuerst)
```bash
claude "Kläre den EU Novel Food Status für NMN, Urolithin A und Spermidine.
Schreibe Ergebnisse nach research/06_regulatorik.md"
```

### Module verknüpfen
```bash
claude "Lies research/02_ingredienzen_db.md und research/06_regulatorik.md.
Identifiziere alle Inhaltsstoffe mit regulatorischen Blocker.
Aktualisiere CLAUDE.md mit den Erkenntnissen."
```

---

## Prioritätsreihenfolge der Module

| Priorität | Datei | Status | Begründung |
|---|---|---|---|
| **1** | `research/06_regulatorik.md` | ⚠️ KRITISCH | Bestimmt welche Stoffe erlaubt sind |
| **2** | `legal/ip_landscape.md` | ⚠️ KRITISCH | Amazentis + Chromadex Patente |
| **3** | `research/02_ingredienzen_db.md` | Abhängig | Erst nach Regulatorik sinnvoll |
| **4** | `research/03_kaffee_specs.md` | — | Kaffee-Spezifikationen |
| **5** | `research/04_marktanalyse.md` | — | Marktanalyse |
| **6** | `research/05_prototyp_partner.md` | — | Prototyp-Partner |
| **7** | `research/07_business_case.md` | Abhängig | Erst wenn COGS-Daten aus Modul 1+4 vorliegen |
| **8** | `models/unit_economics.py` | Abhängig | Erst wenn Rohstoffpreise bekannt |

---

## Dateistruktur

```
performance-cafe/
├── CLAUDE.md                      ← Claude Code Kontext (master)
├── README.md                      ← Projekt-Setup (diese Quelle)
├── .cursor/rules/
│   └── performance_cafe.mdc       ← Cursor AI Kontext
├── research/
│   ├── 00_master_brief.md         ← vollständiger Research-Auftrag
│   ├── 01_longevity_science.md    ← Modul 0
│   ├── 02_ingredienzen_db.md      ← Modul 1 ⭐
│   ├── 03_kaffee_specs.md         ← Modul 2
│   ├── 04_marktanalyse.md         ← Modul 3
│   ├── 05_prototyp_partner.md     ← Modul 4
│   ├── 06_regulatorik.md          ← Modul 5 ⚠️
│   └── 07_business_case.md        ← Modul 6
├── brand/
│   └── naming_brief.md            ← Modul 7
├── legal/
│   ├── ip_landscape.md            ← Modul 8 ⚠️
│   └── entity_structure.md        ← GmbH, Markenanmeldung
├── models/
│   ├── unit_economics.py          ← COGS + Margin Kalkulation
│   └── ingredient_db.csv          ← Strukturierte Inhaltsstoff-DB
└── ops/
    ├── supplier_list.md           ← Rohstoff-Lieferanten
    └── certification_roadmap.md   ← Kölner Liste → Informed Sport → NSF
```

---

## Kritische Vorab-Entscheidungen (vor Prototyp klären)

| Frage | Blocker für | Datei | Wiki-Seite |
|---|---|---|---|
| NMN EU Novel Food Status 2025? | Stack-Entscheidung | `research/06_regulatorik.md` | [[NMN]] / [[EU Novel Food Regulation]] |
| Amazentis Patent Urolithin A — Lizenz? | Stack + Kosten | `legal/ip_landscape.md` | [[Amazentis]] |
| NAC Geruchs-Maskierung — wie? | Prototyp | `research/05_prototyp_partner.md` | [[NAC]] |
| Lebensmittel vs. NEM — welcher Weg? | Regulatorik + Marketing | `research/06_regulatorik.md` | [[Performance Cafe Regulatorik Modul 5]] |
| Kölner Liste CMO-Anforderungen? | CMO-Auswahl | `ops/certification_roadmap.md` | [[Kölner Liste]] |

---

## Verknüpfte Wiki-Seiten

### Bereits existierende Entitäten (bestätigt durch dieses Dokument)
- [[Amazentis]] — IP-Blocker Urolithin A, Priorität 2
- [[Performance Coffee Brand]] — Hauptprojektentität
- [[Aevum Brand]] — Markenname (aus Naming-Modul)
- [[Blueprint von Bryan Johnson]] — Markt-Benchmark

### Referenzierte aber noch zu erstellende Seiten
- [[Performance Cafe Regulatorik Modul 5]] — `research/06_regulatorik.md`
- [[Performance Cafe IP Landscape Modul 8]] — `legal/ip_landscape.md`
- [[Performance Cafe Ingredienzen DB Modul 1]] — `research/02_ingredienzen_db.md`
- [[Performance Cafe Business Case Modul 6]] — `research/07_business_case.md`
- [[Kölner Liste]] — Zertifizierungsstandard für CMO-Auswahl
- [[NMN]] — Novel Food Status 2025 kritisch
- [[NAC]] — Geruchs-Maskierungsproblem im Prototyp
- [[Performance Cafe Unit Economics]] — `models/unit_economics.py`

---

## Widersprüche / Anmerkungen

Keine Widersprüche zu bestehenden Wiki-Inhalten gefunden. Dieses README bestätigt:
- Amazentis-Patent als kritischen Blocker (⚠️ Priorität 2) — konsistent mit [[Amazentis]]-Entitätsseite
- NMN Novel Food Status als kritischsten Blocker (⚠️ Priorität 1) — konsistent mit bestehenden Regulatorik-Seiten
- Chromadex-Patent als zweiten IP-Blocker — konsistent mit [[Chromadex Niagen Bioscience]]-Entitätsseite
