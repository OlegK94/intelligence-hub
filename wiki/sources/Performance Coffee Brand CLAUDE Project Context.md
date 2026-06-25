---
title: Performance Coffee Brand CLAUDE Projektkontext
type: source
tags: [business, coffee, functional-beverage, longevity, biohacking, supplement, berlin, oleg, project-context, claude-code, NMN, urolithin-a, spermidine, chlorogenic-acid, trigonellin, hyrox, blueprint, bryan-johnson]
sources: ["raw/Business/PerformanceCafe/CLAUDE.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Claude Code Projektkontextdatei für die Performance Coffee Brand — funktionaler Kaffee / Longevity-Stack Instant-Sachet-Konzept für Athleten, Führungskräfte und Biohacker; identifizierte Marktlücke im Blueprint-Produktportfolio von Bryan Johnson
---

# Performance Coffee Brand — CLAUDE Projektkontext

## Überblick

Dieses Quelldokument ist die persistente Projektkontextdatei (`CLAUDE.md`) für die **Performance Coffee Brand** — ein Konzept für ein funktionales Getränke-Startup, das von [[Oleg Personal Context|Oleg]] aus Berlin entwickelt wird. Es dient als Initialisierungsdatei für Claude Code-Sitzungen und sichert den Projektstatus zwischen den einzelnen Interaktionen.

> Für die Entitätszusammenfassung und strategische Positionierung siehe [[Performance Coffee Brand]].
> Für das Gründerprofil siehe [[Oleg Personal Context]].

## Produktzusammenfassung

- **Name:** Performance Coffee Brand (Arbeitstitel — finaler Name: siehe `brand/naming_brief.md`)
- **Kategorie:** Funktionaler Kaffee / Performance-Getränk mit Longevity-Stack
- **Kernversprechen (Core Promise):** *Perform now. Live longer.*
- **MVP-Format:** Instant-Sachet (Stick-Pack)
- **Skalierungspfad:** RTD Can → Nespresso-kompatible Kapsel

## Strategische Marktlücke

**[[Bryan Johnson]]'s Blueprint** (blueprint.bryanjohnson.com) verkauft KEINEN Kaffee.

Aktuelles Blueprint-Produktsortiment:
- Longevity Mix Pulver
- Ceremonial Matcha
- Super Shrooms
- Ashwagandha+Rhodiola
- NAC+Ginger+Curcumin
- Essential Capsules
- Creatine
- Omega-3
- Collagen

**Identifizierte Lücke:** Bryan Johnson hat Kaffee aus seinem persönlichen Protokoll gestrichen, aber seine Community **trinkt weiterhin Kaffee** und sucht nach einem Blueprint-kompatiblen Produkt. Die Marktlücke = *„Der Longevity-Kaffee, den Blueprint nicht herstellt."*

Qualitätsreferenz (Blueprint-Standard): *„Wissenschaftlich fundiert, präzise dosiert, jede Zutat hat sich ihren Platz verdient — kein Pixie-Dusting, kein Unsinn."*

## Zielgruppe (3 Segmente)

| Segment | Anwendungsfall |
|---|---|
| **Athleten** (Hyrox, CrossFit, Triathlon) | Pre-Workout + Longevity-Stack |
| **Business / Executive** | Morgendliche Deep Work, anhaltende Energie ohne Crash |
| **Biohacker / Blueprint-Follower** | Tägliche Einnahme von NMN, Urolithin A, Spermidine |

**Gründerkontext:** Oleg Kober, Berlin. Vertrieb bei Doctolib GmbH. 188 cm, 96,7 kg, 20,3 % KF, aktiver Hyrox-Athlet. Aerobe Kapazität als primärer Leistungslimiter. Referenzrahmen: [[Bryan Johnson]], [[Andrew Huberman]], Peter Attia.

## Bekannte kritische Punkte

### Regulatorische Probleme

| Zutat | Problem |
|---|---|
| **NMN** | EU Novel Food-Status 2025/2026 unklar → muss VOR der Stack-Entscheidung geklärt werden |
| **Urolithin A** | Amazentis/Timeline Nutrition hält Mitopure-Patent → Lizenz einholen oder Alternative finden |
| **Spermidine** (Weizenkeime) | Novel Food-Status in Deutschland — zu prüfen |
| **NR (Nicotinamide Riboside)** | Chromadex NIAGEN-Patent → IP-Prüfung erforderlich |
| **Huperzin A** | **In Deutschland als Lebensmittelzutat verboten** |

### Zertifizierungspriorität

1. **[[Kölner Liste]]** — DACH-Standard, günstigste Option, sofort sinnvoll
2. **[[Informed Sport]]** — europaweit, für EU-Skalierung
3. **[[NSF Certified for Sport]]** — nur für US-Expansion relevant

### Sensorische / Produktionstechnische Herausforderungen

| Problem | Lösung |
|---|---|
| NAC: Schwefelgeruch | Flavorist zur Maskierung — zwingend erforderlich |
| Curcumin: hydrophob | Liposomale oder mizellare Form für Löslichkeit |
| NMN/NR: oxidationsempfindlich | Schutzgasversiegelung im Sachet |
| Pilzextrakte: bitter | Röstgrad + Kaffeebasis als natürliche Maskierung |
| Röstpräferenz | **Hell/Medium Roast**: maximiert Chlorogensäure + Trigonellin |

### Kaffee als Longevity-Zutat

- **Trigonellin** in Kaffee = natürlicher NMN-Vorläufer (Forschung 2024)
- **Chlorogensäure:** AMPK-Aktivierung, Insulinsensitivität
- **Helle Röstung** maximiert beide Verbindungen
- **Vietnamesischer Robusta:** höchster Koffeingehalt + höchste Chlorogensäure

## Modulstatus

| # | Modul | Status | Datei |
|---|---|---|---|
| 0 | Longevity Science Grundlagen | ✅ Abgeschlossen | `research/01_longevity_science.md` |
| 1 | Zutaten-Datenbank | ⬜ Leer | `research/02_ingredienzen_db.md` |
| 2 | Kaffeespezifikation | ⬜ Leer | `research/03_kaffee_specs.md` |
| 3 | Marktanalyse + Wettbewerb | ⬜ Leer | `research/04_marktanalyse.md` |
| 4 | Prototyp-Partner | ⬜ Leer | `research/05_prototyp_partner.md` |
| 5 | Regulatorik + IP | ⬜ Leer | `research/06_regulatorik.md` |
| 6 | Business Case + Unit Economics | ⬜ Leer | `research/07_business_case.md` |
| 7 | Marke & Naming | ⬜ Leer | `brand/naming_brief.md` |
| 8 | IP & Patentlandschaft | ⬜ Leer | `legal/ip_landscape.md` |
| 9 | Unit Economics Model | ⬜ Leer | `models/unit_economics.py` |

**Zentraler Blocker:** Das Regulatorik-Modul (5) muss vor der Stack-Entscheidung abgeschlossen sein — insbesondere der NMN Novel Food-Status.

## Projektdateistruktur

```
performance-cafe/
├── CLAUDE.md                    ← Quelldokument (diese Seite)
├── .cursor/rules/
│   └── performance_cafe.mdc
├── research/
│   ├── 00_master_brief.md
│   ├── 01_longevity_science.md  ← ABGESCHLOSSEN
│   ├── 02_ingredienzen_db.md
│   ├── 03_kaffee_specs.md
│   ├── 04_marktanalyse.md
│   ├── 05_prototyp_partner.md
│   ├── 06_regulatorik.md
│   └── 07_business_case.md
├── brand/
│   ├── naming_brief.md
│   └── positioning.md
├── legal/
│   ├── ip_landscape.md
│   └── entity_structure.md
├── models/
│   ├── unit_economics.py
│   └── ingredient_db.csv
└── ops/
    ├── supplier_list.md
    └── certification_roadmap.md
```

## Arbeitskonventionen

- **Sprache:** Immer auf Deutsch antworten
- **Format:** Markdown mit Frontmatter (`status`, `priority`, `date`, `modul`)
- **Qualitätsstandard:** Konkrete Unternehmen, Dosierungen, Preise, Kontakte — keine Verallgemeinerungen
- **Quellen:** web_search verwenden, bevorzugt Daten aus 2024/2025
- **Output:** Immer in die entsprechende Moduldatei schreiben, nicht nur in den Chat
- **Blocker:** Modulabhängigkeiten explizit kennzeichnen
- **Rückfragen:** Kurz klären, nicht stillschweigend optimieren

## Verwandte Seiten

- [[Performance Coffee Brand]] — Entitätszusammenfassungsseite
- [[Bryan Johnson]] — Referenz für die Marktlücke und Qualitätsmaßstab
- [[Andrew Huberman]] — wissenschaftlicher Referenzrahmen
- [[Oleg Personal Context]] — Gründer
- [[Longevity Stack Ingredients]] — Zutaten-Wissenschaftskonzept
- [[Functional Beverage Market]] — Marktkontext
- [[NMN]] — wichtigste regulatorisch kritische Zutat
- [[Urolithin A]] — patentierte Zutat (Mitopure)
- [[Chlorogenic Acid]] — Longevity-Verbindung in Kaffee
- [[Trigonellin]] — NMN-Vorläufer in Kaffee
- [[Kölner Liste]] — primäres Zertifizierungsziel
- [[Daily Protocol Checklist]] — Olegs persönlicher Stack (Querverweise: `*[[Performance Coffee]] | [[Supplement Stack]]*`)