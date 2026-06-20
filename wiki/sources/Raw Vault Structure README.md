---
title: Raw Vault Struktur README
type: source
tags: [vault, structure, workflow, inbox, ingest, raw, architecture]
sources: ["raw/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Unveränderliches README für das raw/-Verzeichnis — definiert die Ordnerstruktur für die Bereiche Privat, Business und _archiv; dokumentiert den inbox → ingest → wiki Workflow
---

# Raw Vault Struktur — README

## Übersicht

Dieses Quelldokument (`raw/README.md`) definiert die Verzeichnisstruktur und den Ingest-Workflow für den raw/-Ordner, der als unveränderliche Quellschicht dieses Wikis dient. Raw-Dateien werden nach dem Ingest nie bearbeitet — die gesamte Wissensintegration findet im Wiki statt.

> Diese Seite ist eine strukturelle/Meta-Quelle. Sie enthält keine persönlichen Daten, sondern liefert die architektonische Übersicht aller rohen Quellbereiche.

## Ordnerstruktur

```
raw/
├── inbox/              # Neue Notizen → hier ablegen, dann ingest
├── assets/             # Bilder & Anhänge
├── data/               # CSV/Exports (Wearables, etc.)
├── MOC/                # Vault-Home
│
├── Privat/             # Alles Persönliche
│   ├── MOC/
│   ├── Performance/    # Health, Hyrox, Supplements, Scans
│   ├── Tech/           # Tools, Privacy, Password Manager
│   ├── Finanzen/       # Privatkonten, Steuern, Fixkosten
│   ├── Versicherungen/
│   ├── Recherchen/
│   └── Auswandern/     # Someday (pausiert)
│
├── Business/
│   ├── MOC/
│   ├── Wagglz/         # GmbH, Finanzen, BWAs
│   ├── Cafe/           # Café Berlin, Masterplan, Decks
│   └── OK-Capital/     # UG, Finanzen
│
└── _archiv/            # Work-Themen, nicht aktiv ingesten
    └── Work/           # z.B. Doctolib/DoktorLib
```

## Workflow

```
Datei in inbox/ → python3 tools/ingest.py → Wiki wächst in wiki/
```

1. Neue Notizen/Exporte in `raw/inbox/` ablegen
2. `python3 tools/ingest.py` ausführen
3. Wiki-Seiten werden in `wiki/` erstellt/aktualisiert
4. Raw-Dateien bleiben unveränderlich

## Beschreibung der Top-Level-Bereiche

### raw/inbox/
Staging-Bereich für neue Notizen vor dem Ingest. Nach dem Ingest können Dateien als Nachweis hier verbleiben oder archiviert werden.

### raw/assets/
Bilder und Anhänge, die von Raw-Dokumenten referenziert werden.

### raw/data/
CSV-Exporte von Wearables und anderen Datenquellen — strukturierte Daten für das Gesundheits- und Performance-Tracking.

### raw/MOC/
Vault-Home — übergeordnete Inhaltsübersicht (MOC = Map of Content).

### raw/Privat/
Alle persönlichen Inhalte für [[Oleg Personal Context|Oleg]]. Teilbereiche:

| Unterordner | Inhalt |
|---|---|
| `Performance/` | Gesundheit, [[Hyrox Competition]], [[Supplement Stack]], Scans |
| `Tech/` | Tools, Datenschutz, [[Apple Passwords]] / [[Proton Pass]] |
| `Finanzen/` | Privatkonten, [[ESt 2025]], [[Fixkosten Übersicht]] |
| `Versicherungen/` | Versicherungspolicen |
| `Recherchen/` | Recherchenotizen |
| `Auswandern/` | [[Cyprus Relocation]] — Someday, pausiert |

### raw/Business/
Geschäftliche Inhalte. Teilbereiche:

| Unterordner | Inhalt |
|---|---|
| `Wagglz/` | [[Wagglz GmbH]] — GmbH, Finanzen, BWAs |
| `Cafe/` | [[Café Berlin Partnership Hai]] — Masterplan, Decks |
| `OK-Capital/` | UG (OK-Capital), Finanzen |

### raw/_archiv/
Arbeitsbezogene Themen — **werden nicht aktiv ingested**. Enthält:
- `Work/` — z. B. Doctolib/DoktorLib Arbeitshistorie

> ⚠️ **Ingest-Regel:** Inhalte aus `_archiv/` sind explizit vom aktiven Ingest ausgeschlossen. Aus `_archiv/Work/`-Quellen werden keine Wiki-Seiten erstellt.

## Zuordnung zu Wiki-Bereichen

| Raw-Bereich | Wiki-Bereich |
|---|---|
| `raw/Privat/Performance/` | `wiki/entities/`, `wiki/concepts/` (Gesundheit, Performance) |
| `raw/Privat/Finanzen/` | `wiki/entities/` (Finanzen, Steuern) |
| `raw/Privat/Tech/` | `wiki/entities/` (Tech-Stack) |
| `raw/Business/Wagglz/` | `wiki/entities/` (Wagglz GmbH) |
| `raw/Business/Cafe/` | `wiki/entities/`, `wiki/sources/` (Café-Projekt) |
| `raw/Business/OK-Capital/` | `wiki/entities/` (OK-Capital UG) |
| `raw/inbox/` | → wird in alle Wiki-Bereiche verarbeitet |
| `raw/_archiv/` | ❌ Nicht ingested |

## Verwandte Seiten

- [[Oleg Personal Context]] — Vault-Inhaber
- [[MOC Performance und Leben]] — MOC des Performance-Bereichs
- [[MOC Finanzen]] — MOC des Finanzbereichs
- [[MOC Strategie und Business]] — MOC des Business-Bereichs
- [[MOC Tech und Setup]] — MOC des Tech-Bereichs
- [[Wagglz GmbH]] — Geschäftsentität in raw/Business/Wagglz/
- [[Café Berlin Partnership Hai]] — Geschäftsentität in raw/Business/Cafe/
- [[Performance Coffee Brand]] — Geschäftsentität in raw/Business/PerformanceCafe/
- [[Cyprus Relocation]] — pausiertes persönliches Projekt
- [[Hyrox Competition]] — Inhalt des Performance-Bereichs
- [[Supplement Stack]] — Inhalt des Performance-Bereichs
- [[ESt 2025]] — Inhalt des Finanzbereichs
- [[Apple Passwords]] — Inhalt des Tech-Bereichs
- [[Proton Pass]] — Inhalt des Tech-Bereichs