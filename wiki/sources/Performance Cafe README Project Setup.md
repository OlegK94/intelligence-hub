---
title: Performance Café README Projekt-Setup
type: source
tags: [performance-cafe, longevity-coffee, project-setup, obsidian, cursor, claude-code, workflow, regulatorik, novel-food, NMN, urolithin-a, spermidine, NAC, IP, patents]
sources: ["raw/Business/PerformanceCafe/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Projekt-Setup-README für die Performance Café Longevity-Kaffee-Marke — 3-stufiger Obsidian/Cursor/Claude Code Workflow, Prioritätsreihenfolge der Forschungsmodule, vollständige Dateistruktur und kritische Entscheidungsblocker (NMN Novel Food, Amazentis-Patent, NAC-Maskierung, CMO-Zertifizierung)
---

# Performance Café — README Projekt-Setup

## Überblick

Dieses Quelldokument ist die `README.md` für den [[Performance Coffee Brand|Performance Café]]-Projekt-Vault (Pfad: `raw/Business/PerformanceCafe/`). Es definiert das **Toolchain-Setup**, den **Workflow zur Ausführung der Forschungsmodule** und **kritische Entscheidungsblocker vor dem Prototyp**.

> Für den vollständigen Projektkontext, das Master-Briefing und die KI-Anweisungen siehe [[Performance Coffee Brand CLAUDE Project Context]].
> Für die Entitätszusammenfassung des Markenkonzepts siehe [[Performance Coffee Brand]].

## Tagline

**„Perform now. Live longer."**

## 3-stufiges Toolchain-Setup

### 1. Obsidian Vault
- Öffne den Ordner `performance-cafe/` als Obsidian Vault
- Alle `.md`-Dateien erscheinen sofort in der Seitenleiste
- Wikilinks zwischen Forschungsmodulen funktionieren automatisch
- Dataview-Plugin: Modulstatus-Tabelle aus dem Frontmatter

### 2. Cursor IDE
- Ordner in Cursor öffnen
- `.cursor/rules/performance_cafe.mdc` wird automatisch als Projektkontext geladen
- Jede KI-Anfrage in Cursor kennt: Produkt, Zielgruppe, kritische Blocker

### 3. Claude Code
- `CLAUDE.md` wird automatisch beim Sitzungsstart gelesen
- Vollständiger Projektkontext ab der ersten Eingabe verfügbar
- Ausführen: `cd performance-cafe && claude`

## Workflow-Muster

### Ausführung der Forschungsmodule (Claude Code)

```bash
# Einzelnes Modul
claude "Arbeite Modul 1 (Ingredienzen Datenbank) aus.
Lies research/00_master_brief.md für den vollständigen Auftrag.
Schreibe Ergebnisse nach research/02_ingredienzen_db.md"

# Priorität: Regulatorik first (BLOCKER)
claude "Kläre den EU Novel Food Status für NMN, Urolithin A und Spermidine.
Schreibe Ergebnisse nach research/06_regulatorik.md"

# Cross-module linkage
claude "Lies research/02_ingredienzen_db.md und research/06_regulatorik.md.
Identifiziere alle Inhaltsstoffe mit regulatorischen Blocker.
Aktualisiere CLAUDE.md mit den Erkenntnissen."
```

### Cursor (@-Referenzen)
```
@research/02_ingredienzen_db.md Welche Inhaltsstoffe haben Patent-Konflikte?
@research/06_regulatorik.md Erstelle eine Prioritätsliste der regulatorischen Risiken
@models/unit_economics.py Fülle die Rohstoffpreise aus @models/ingredient_db.csv
```

## Prioritätsreihenfolge der Forschungsmodule

| Priorität | Datei | Status | Begründung |
|-----------|-------|--------|------------|
| 1 | `research/06_regulatorik.md` | ⚠️ KRITISCH | Bestimmt, welche Inhaltsstoffe zugelassen sind |
| 2 | `legal/ip_landscape.md` | ⚠️ KRITISCH | Amazentis- und Chromadex-Patente |
| 3 | `research/02_ingredienzen_db.md` | — | Nur sinnvoll nach der Regulatorik |
| 4 | `research/03_kaffee_specs.md` | — | Kaffee-Basisspezifikationen |
| 5 | `research/04_marktanalyse.md` | — | Marktanalyse |
| 6 | `research/05_prototyp_partner.md` | — | Identifikation von Prototyp-Partnern |
| 7 | `research/07_business_case.md` | — | Erst nach COGS-Daten aus Modulen 1+4 |
| 8 | `models/unit_economics.py` | — | Erst nach Kenntnis der Rohstoffpreise |

**Zentrale Ablauflogik:**
- Regulatorik zuerst → bestimmt den zulässigen Inhaltsstoff-Stack
- IP-Landschaft als zweites → bestimmt die Lizenzkosten-Struktur
- Inhaltsstoff-Datenbank erst nach der Regulatorik (keine Recherche zu blockierten Inhaltsstoffen)
- Business Case zuletzt → erfordert COGS-Daten aus den vorgelagerten Modulen

## Vollständige Dateistruktur

```
performance-cafe/
├── CLAUDE.md                      ← Claude Code Master-Kontext
├── README.md                      ← dieses Dokument
├── .cursor/rules/
│   └── performance_cafe.mdc       ← Cursor KI-Kontext
├── research/
│   ├── 00_master_brief.md         ← Vollständiges Forschungs-Briefing (Modul 0)
│   ├── 01_longevity_science.md    ← Longevity-Wissenschaft (Modul 0)
│   ├── 02_ingredienzen_db.md      ← Inhaltsstoff-Datenbank (Modul 1) ⭐
│   ├── 03_kaffee_specs.md         ← Kaffee-Spezifikationen (Modul 2)
│   ├── 04_marktanalyse.md         ← Marktanalyse (Modul 3)
│   ├── 05_prototyp_partner.md     ← Prototyp-Partner (Modul 4)
│   ├── 06_regulatorik.md          ← Regulatorik (Modul 5) ⚠️
│   └── 07_business_case.md        ← Business Case (Modul 6)
├── brand/
│   └── naming_brief.md            ← Namensgebung (Modul 7)
├── legal/
│   ├── ip_landscape.md            ← IP-Landschaft (Modul 8) ⚠️
│   └── entity_structure.md        ← GmbH, Markenanmeldung
├── models/
│   ├── unit_economics.py          ← COGS + Margenberechnung
│   └── ingredient_db.csv          ← Strukturierte Inhaltsstoff-Datenbank
└── ops/
    ├── supplier_list.md           ← Rohstofflieferanten
    └── certification_roadmap.md   ← Kölner Liste → Informed Sport → NSF
```

## Kritische Entscheidungen vor dem Prototyp

| Frage | Blockiert | Datei |
|-------|-----------|-------|
| [[NMN]] EU Novel Food Status 2025? | Stack-Entscheidung | `research/06_regulatorik.md` |
| [[Amazentis]]-Patent [[Urolithin A]] — Lizenz? | Stack + Kosten | `legal/ip_landscape.md` |
| [[NAC]] Geruchs-Maskierung — wie? | Prototyp | `research/05_prototyp_partner.md` |
| Lebensmittel vs. NEM — welcher Weg? | Regulatorik + Marketing | `research/06_regulatorik.md` |
| Kölner Liste CMO-Anforderungen? | CMO-Auswahl | `ops/certification_roadmap.md` |

### Details zu den Entscheidungen

**NMN Novel Food:** NMN könnte gemäß EU-Verordnung 2015/2283 als Novel Food eingestuft werden, was eine Vorabgenehmigung vor der Markteinführung eines Lebensmittel- oder Nahrungsergänzungsmittelprodukts in der EU erfordern würde. Dies ist der einzel kritischste Inhaltsstoff-Blocker.

**Amazentis/Urolithin A Patent:** [[Amazentis]] hält Patente auf [[Urolithin A]] (vertrieben als MITOPURE). Die Verwendung von Urolithin A kann eine Lizenzierung von Amazentis erfordern — was COGS und Wirtschaftlichkeit beeinflusst. Siehe [[Urolithin A]].

**Chromadex/NMN Patent:** [[Chromadex Niagen Bioscience]] hält relevante Patente auf [[NMN]] (Tru Niagen / NR). Die Patentlandschaft überschneidet sich mit der NMN-Beschaffung bei bestimmten Herstellern.

**NAC-Geruch:** [[NAC]] (N-Acetylcystein) hat einen starken schwefeligen Geruch, der in Lebensmittel- und Getränkeformaten schwer zu maskieren ist — eine Formulierungsherausforderung für das Kaffeeformat.

**Lebensmittel vs. NEM:** Die Einstufung des Produkts als Lebensmittel oder Nahrungsergänzungsmittel (NEM) bestimmt die zulässigen Aussagen auf dem Etikett, die Dosierungsspielräume und die Marketingmöglichkeiten.

**Kölner Liste:** Die [[Kölner Liste]] ist die deutsche Antidoping-Zertifizierung für Nahrungsergänzungsmittel. Die Einhaltung der Kölner Liste durch den CMO (Contract Manufacturing Organization) ist eine Voraussetzung für den Sport- und Performance-Markt.

## Verwandte Seiten

- [[Performance Coffee Brand]] — Entitätsseite für das Markenkonzept
- [[Performance Coffee Brand CLAUDE Project Context]] — Master-Briefing und KI-Kontext
- [[NMN]] — Novel Food-Blocker
- [[Urolithin A]] — Amazentis-Patent-Blocker
- [[NAC]] — Formulierungsherausforderung
- [[Spermidine]] — Novel Food-Kandidat
- [[Amazentis]] — Patentinhaber für Urolithin A
- [[Chromadex Niagen Bioscience]] — Patentinhaber für NMN/NR
- [[Kölner Liste]] — Antidoping-Zertifizierung
- [[Longevity Stack Ingredients]] — vollständiges Inhaltsstoff-Framework
- [[EU Novel Food Regulation]] — regulatorischer Rahmen
- [[Chlorogenic Acid]] — wichtige Kaffeeverbindung
- [[Bryan Johnson]] — Markt-Benchmark (Blueprint-Lücke)