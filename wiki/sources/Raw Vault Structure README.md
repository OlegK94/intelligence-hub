---
title: Raw Vault Structure README
type: source
tags: [vault, structure, workflow, inbox, ingest, raw, architecture]
sources: ["raw/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Immutable README for the raw/ directory — defines folder structure for Privat, Business, and _archiv areas; documents the inbox → ingest → wiki workflow
---

# Raw Vault Structure — README

## Overview

This source document (`raw/README.md`) defines the directory structure and ingestion workflow for the raw/ folder, which serves as the immutable source layer for this wiki. Raw files are never edited after ingest — all knowledge integration happens in the wiki.

> This page is a structural/meta source. It does not contain personal data but provides the architectural map of all raw source areas.

## Folder Structure

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

1. Drop new notes/exports into `raw/inbox/`
2. Run `python3 tools/ingest.py`
3. Wiki pages are created/updated in `wiki/`
4. Raw files remain immutable

## Top-Level Area Descriptions

### raw/inbox/
Staging area for new notes before ingest. After ingest, files may remain here as a record or be archived.

### raw/assets/
Images and attachments referenced by raw documents.

### raw/data/
CSV exports from wearables and other data sources — structured data that feeds health/performance tracking.

### raw/MOC/
Vault-Home — top-level map of content (MOC = Map of Content).

### raw/Privat/
All personal content for [[Oleg Personal Context|Oleg]]. Sub-areas:

| Sub-folder | Content |
|---|---|
| `Performance/` | Health, [[Hyrox Competition]], [[Supplement Stack]], scans |
| `Tech/` | Tools, privacy, [[Apple Passwords]] / [[Proton Pass]] |
| `Finanzen/` | Privatkonten, [[ESt 2025]], [[Fixkosten Übersicht]] |
| `Versicherungen/` | Insurance policies |
| `Recherchen/` | Research notes |
| `Auswandern/` | [[Cyprus Relocation]] — someday, paused |

### raw/Business/
Business-related content. Sub-areas:

| Sub-folder | Content |
|---|---|
| `Wagglz/` | [[Wagglz GmbH]] — GmbH, Finanzen, BWAs |
| `Cafe/` | [[Café Berlin Partnership Hai]] — Masterplan, Decks |
| `OK-Capital/` | UG (OK-Capital), Finanzen |

### raw/_archiv/
Work-related topics — **not actively ingested**. Contains:
- `Work/` — e.g., Doctolib/DoktorLib work history

> ⚠️ **Ingest rule:** `_archiv/` content is explicitly excluded from active ingest. Do not create wiki pages from `_archiv/Work/` sources.

## Mapping to Wiki Areas

| Raw Area | Wiki Area |
|---|---|
| `raw/Privat/Performance/` | `wiki/entities/`, `wiki/concepts/` (health, performance) |
| `raw/Privat/Finanzen/` | `wiki/entities/` (finanzen, steuern) |
| `raw/Privat/Tech/` | `wiki/entities/` (tech stack) |
| `raw/Business/Wagglz/` | `wiki/entities/` (Wagglz GmbH) |
| `raw/Business/Cafe/` | `wiki/entities/`, `wiki/sources/` (café project) |
| `raw/Business/OK-Capital/` | `wiki/entities/` (OK-Capital UG) |
| `raw/inbox/` | → processed into all wiki areas |
| `raw/_archiv/` | ❌ Not ingested |

## Related Pages

- [[Oleg Personal Context]] — vault owner
- [[MOC Performance und Leben]] — performance area MOC
- [[MOC Finanzen]] — finance area MOC
- [[MOC Strategie und Business]] — business area MOC
- [[MOC Tech und Setup]] — tech area MOC
- [[Wagglz GmbH]] — business entity in raw/Business/Wagglz/
- [[Café Berlin Partnership Hai]] — business entity in raw/Business/Cafe/
- [[Performance Coffee Brand]] — business entity in raw/Business/PerformanceCafe/
- [[Cyprus Relocation]] — paused personal project
- [[Hyrox Competition]] — performance area content
- [[Supplement Stack]] — performance area content
- [[ESt 2025]] — finance area content
- [[Apple Passwords]] — tech area content
- [[Proton Pass]] — tech area content
