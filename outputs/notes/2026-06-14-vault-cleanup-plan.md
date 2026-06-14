---
title: Vault Cleanup Plan — raw/ Duplicate Analysis
type: synthesis
tags: [vault-maintenance, cleanup, duplicates]
created: 2026-06-14
updated: 2026-06-14
summary: Full audit of duplicate and redundant files in raw/, with deletion and consolidation recommendations.
---

# Vault Cleanup Plan — raw/ Duplicate Analysis

Generated: 2026-06-14

---

## Overview

The `raw/` directory contains **108 markdown files** across **49 directories**. The vault has accumulated multiple parallel directory structures — legacy numbered folders (`00-MOC/`, `01-Strategie-Business/`, etc.), interim import folders (`Finanzdaten/ObsidianVault/`, `Finanzdaten/Obsidian_Vault/`, `Cafe/`), and the canonical target structure (`Privat/`, `Business/`, `MOC/`, `inbox/`).

**Summary of findings:**

| Category | Count |
|---|---|
| Total .md files | 108 |
| Files with exact duplicates (same md5sum) | 98 (49 pairs/groups) |
| Files that are unique (no duplicate) | 10 |
| Near-duplicate groups (same topic, different content) | 3 |
| Empty files | 1 (`inbox/2026-06-13.md`) |
| Non-markdown files needing attention | 5 |

The canonical structure per CLAUDE.md is:
```
raw/
  inbox/          # drop zone
  Privat/         # personal docs
  Business/       # company docs
  MOC/            # navigation
  assets/         # attachments
  data/           # structured exports
```

All other top-level folders (`00-MOC/`, `01-Strategie-Business/`, `02-Performance-Leben/`, `03-Tech-Setup/`, `04-Recherchen/`, `05-Inbox/`, `Cafe/`, `Finanzdaten/`) are legacy or interim and can be retired after cleanup.

---

## Exact Duplicate Pairs (identical md5sum — safe to delete one copy)

The files listed in the "Legacy / Redundant" column are the copies that should be deleted. The "Canonical" column shows the keeper.

| # | Filename | Canonical Path | Legacy / Redundant Path(s) |
|---|---|---|---|
| 1 | `Blutbild Panel.md` | `raw/Privat/Performance/_vault/Blutbild Panel.md` | `raw/Finanzdaten/ObsidianVault/Performance/Blutbild Panel.md` |
| 2 | `Supplement Stack.md` | `raw/Privat/Performance/Supplement Stack.md` | `raw/02-Performance-Leben/Supplement Stack.md` |
| 3 | `📥 Offene Actions.md` | `raw/inbox/📥 Offene Actions.md` | `raw/05-Inbox/📥 Offene Actions.md` |
| 4 | `Hyrox Prep.md` | `raw/Privat/Performance/_vault/Hyrox Prep.md` | `raw/Finanzdaten/ObsidianVault/Performance/Hyrox Prep.md` |
| 5 | `Health Protocol — Master.md` | `raw/Privat/Performance/Health Protocol — Master.md` | `raw/02-Performance-Leben/Health Protocol — Master.md` |
| 6 | `Allianz Insurance Consolidation.md` | `raw/Privat/Versicherungen/Allianz Insurance Consolidation.md` | `raw/01-Strategie-Business/Allianz Insurance Consolidation.md` |
| 7 | `P2 Diesen Monat.md` | `raw/Privat/Finanzen/Aufgaben/P2 Diesen Monat.md` | `raw/Finanzdaten/Obsidian_Vault/Aufgaben/P2 Diesen Monat.md` |
| 8 | `Password Manager Migration.md` | `raw/Privat/Tech/Password Manager Migration.md` | `raw/03-Tech-Setup/Password Manager Migration.md` |
| 9 | `Cyprus Relocation Tracker.md` | `raw/Privat/Auswandern/Cyprus Relocation Tracker.md` | `raw/inbox/Cyprus Relocation Tracker.md` |
| 10 | `cafe_masterplan_2026.md` | `raw/Business/Cafe/cafe_masterplan_2026.md` | `raw/Cafe/cafe_masterplan_2026.md` |
| 11 | `MOC Tech & Setup.md` | `raw/Privat/MOC/MOC Tech & Setup.md` | `raw/00-MOC/MOC Tech & Setup.md` |
| 12 | `Doctolib 2026.md` | `raw/Privat/Finanzen/Einnahmen/Doctolib 2026.md` | `raw/Finanzdaten/Obsidian_Vault/Einnahmen/Doctolib 2026.md` |
| 13 | `🏠 Home.md` | `raw/MOC/🏠 Home.md` | `raw/00-MOC/🏠 Home.md` |
| 14 | `Hyrox — 10-Week Training.md` | `raw/Privat/Performance/Hyrox — 10-Week Training.md` | `raw/02-Performance-Leben/Hyrox — 10-Week Training.md` |
| 15 | `P1 Diese Woche.md` | `raw/Privat/Finanzen/Aufgaben/P1 Diese Woche.md` | `raw/Finanzdaten/Obsidian_Vault/Aufgaben/P1 Diese Woche.md` |
| 16 | `00 MOC Finanzen.md` | `raw/Privat/Finanzen/00 MOC Finanzen.md` | `raw/Finanzdaten/Obsidian_Vault/00 MOC Finanzen.md` |
| 17 | `3D Body Scan — Scaneca Mai 2026.md` | `raw/Privat/Performance/3D Body Scan — Scaneca Mai 2026.md` | `raw/02-Performance-Leben/3D Body Scan — Scaneca Mai 2026.md` |
| 18 | `GESAMTANALYSE Archiv.md` | `raw/Privat/Finanzen/Archiv/GESAMTANALYSE Archiv.md` | `raw/Finanzdaten/Obsidian_Vault/Archiv/GESAMTANALYSE Archiv.md` |
| 19 | `MOC Performance & Leben.md` | `raw/Privat/MOC/MOC Performance & Leben.md` | `raw/00-MOC/MOC Performance & Leben.md` |
| 20 | `Wagglz Finom 2026.md` | `raw/Business/Wagglz/Finanzen/Konten/Wagglz Finom 2026.md` | `raw/Finanzdaten/Obsidian_Vault/Konten/Wagglz Finom 2026.md` |
| 21 | `Privacy & Tech Stack.md` | `raw/Privat/Tech/Privacy & Tech Stack.md` | `raw/03-Tech-Setup/Privacy & Tech Stack.md` |
| 22 | `ESt 2025.md` | `raw/Privat/Finanzen/Steuern/ESt 2025.md` | `raw/Finanzdaten/Obsidian_Vault/Steuern/ESt 2025.md` |
| 23 | `Master Prompt – Gesamtanalyse.md` | `raw/Privat/Finanzen/Master Prompt – Gesamtanalyse.md` | `raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md` |
| 24 | `Cyprus Relocation.md` | `raw/Privat/Auswandern/Cyprus Relocation.md` | `raw/01-Strategie-Business/Cyprus Relocation.md` |
| 25 | `Claude Session – Finanzen.md` | `raw/Privat/Finanzen/Templates/Claude Session – Finanzen.md` | `raw/Finanzdaten/ObsidianVault/Templates/Claude Session – Finanzen.md` |
| 26 | `OK Capital Finom 2026.md` | `raw/Business/OK-Capital/Finanzen/Konten/OK Capital Finom 2026.md` | `raw/Finanzdaten/Obsidian_Vault/Konten/OK Capital Finom 2026.md` |
| 27 | `Wagglz GF-Gehalt 2025.md` | `raw/Business/Wagglz/Finanzen/Einnahmen/Wagglz GF-Gehalt 2025.md` | `raw/Finanzdaten/Obsidian_Vault/Einnahmen/Wagglz GF-Gehalt 2025.md` |
| 28 | `Café Berlin — Partnership Hai.md` | `raw/Business/Cafe/Café Berlin — Partnership Hai.md` | `raw/01-Strategie-Business/Café Berlin — Partnership Hai.md` |
| 29 | `OK Capital UG.md` (v1 — 35 lines) | `raw/Business/OK-Capital/OK Capital UG.md` | `raw/Finanzdaten/Obsidian_Vault/Unternehmen/OK Capital UG.md` |
| 30 | `OK Capital UG — Finance Vault.md` | `raw/Business/OK-Capital/OK Capital UG — Finance Vault.md` | `raw/Finanzdaten/ObsidianVault/Finance/OK Capital UG.md` *(different filename)* |
| 31 | `Claude Session – Performance.md` | `raw/Privat/Finanzen/Templates/Claude Session – Performance.md` | `raw/Finanzdaten/ObsidianVault/Templates/Claude Session – Performance.md` |
| 32 | `TEMPUR Matratzenkauf.md` | `raw/Privat/Recherchen/TEMPUR Matratzenkauf.md` | `raw/04-Recherchen/TEMPUR Matratzenkauf.md` |
| 33 | `P0 Sofort.md` | `raw/Privat/Finanzen/Aufgaben/P0 Sofort.md` | `raw/Finanzdaten/Obsidian_Vault/Aufgaben/P0 Sofort.md` |
| 34 | `GESAMTANALYSE_Oleg_Kober_2025-2026.md` | `raw/Privat/Finanzen/Archiv/GESAMTANALYSE_Oleg_Kober_2025-2026.md` | `raw/Finanzdaten/GESAMTANALYSE_Oleg_Kober_2025-2026.md` |
| 35 | `Wagglz GmbH — Finance Vault.md` | `raw/Business/Wagglz/Wagglz GmbH — Finance Vault.md` | `raw/Finanzdaten/ObsidianVault/Finance/Wagglz GmbH.md` *(different filename)* |
| 36 | `VW Konsumkredit.md` | `raw/Privat/Finanzen/Ausgaben/VW Konsumkredit.md` | `raw/Finanzdaten/Obsidian_Vault/Ausgaben/VW Konsumkredit.md` |
| 37 | `Fixkosten Übersicht.md` | `raw/Privat/Finanzen/Ausgaben/Fixkosten Übersicht.md` | `raw/Finanzdaten/Obsidian_Vault/Ausgaben/Fixkosten Übersicht.md` |
| 38 | `00 Finanz-Übersicht.md` | `raw/Privat/Finanzen/00 Finanz-Übersicht.md` | `raw/Finanzdaten/ObsidianVault/Finance/00 Finanz-Übersicht.md` |
| 39 | `ALG I Progressionsvorbehalt.md` | `raw/Privat/Finanzen/Steuern/ALG I Progressionsvorbehalt.md` | `raw/Finanzdaten/Obsidian_Vault/Steuern/ALG I Progressionsvorbehalt.md` |
| 40 | `Finanz-Home.md` / `Home.md` | `raw/Privat/MOC/Finanz-Home.md` | `raw/Finanzdaten/ObsidianVault/Home.md` *(different filename, identical content)* |
| 41 | `Körper & Scan.md` | `raw/Privat/Performance/_vault/Körper & Scan.md` | `raw/Finanzdaten/ObsidianVault/Performance/Körper & Scan.md` |
| 42 | `Consorsbank Girokonto 0250120493.md` | `raw/Privat/Finanzen/Konten/Consorsbank Girokonto 0250120493.md` | `raw/Finanzdaten/Obsidian_Vault/Konten/Consorsbank Girokonto 0250120493.md` |
| 43 | `Rehabilitation Plan.md` | `raw/Privat/Finanzen/Rehabilitation Plan.md` | `raw/Finanzdaten/ObsidianVault/Finance/Rehabilitation Plan.md` |
| 44 | `ALG I 2025.md` | `raw/Privat/Finanzen/Einnahmen/ALG I 2025.md` | `raw/Finanzdaten/Obsidian_Vault/Einnahmen/ALG I 2025.md` |
| 45 | `MOC Strategie & Business.md` | `raw/Business/MOC/MOC Strategie & Business.md` | `raw/00-MOC/MOC Strategie & Business.md` |
| 46 | `Claude Projects Setup.md` | `raw/Privat/Tech/Claude Projects Setup.md` | `raw/03-Tech-Setup/Claude Projects Setup.md` |
| 47 | `Wagglz GmbH.md` (v1 — 76 lines) | `raw/Business/Wagglz/Wagglz GmbH.md` | `raw/Finanzdaten/Obsidian_Vault/Unternehmen/Wagglz GmbH.md` |
| 48 | `00 Performance-Übersicht.md` | `raw/Privat/Performance/_vault/00 Performance-Übersicht.md` | `raw/Finanzdaten/ObsidianVault/Performance/00 Performance-Übersicht.md` |

**Total: 48 redundant files safe to delete (all confirmed exact md5sum matches).**

---

## Near-Duplicate Groups (same topic, different content — requires manual review)

These file groups share a topic/name but contain **different content**. Both versions contain unique information that should be merged into the wiki before either is archived.

### Group A — OK Capital UG (two divergent versions)

| Version | Path | Size | Focus |
|---|---|---|---|
| v1 (canonical) | `raw/Business/OK-Capital/OK Capital UG.md` | 35 lines | Operational detail: bank account, monthly costs, structure diagram. Updated 2026-06-12. |
| v2 (analysis) | `raw/Finanzdaten/ObsidianVault/Finance/OK Capital UG.md` | 52 lines | Analytical: open insolvency questions, required documents, strategic options. Created 2026-06-13. |

**Key differences:** v2 contains insolvency risk checklist and document TODO list not present in v1. v1 has concrete bank balances and cost figures not in v2. Neither is a strict superset. Both should be ingested into the wiki before archiving v2.

### Group B — Wagglz GmbH (two divergent versions)

| Version | Path | Size | Focus |
|---|---|---|---|
| v1 (canonical) | `raw/Business/Wagglz/Wagglz GmbH.md` | 76 lines | Operational: Sofortmaßnahmen, monthly transfer history, running costs 2026, status as of Jun 2026. Updated 2026-06-12. |
| v2 (analysis) | `raw/Finanzdaten/ObsidianVault/Finance/Wagglz GmbH.md` | 56 lines | Analytical: Kapitaltransfer-Historie, insolvency questions, required documents. Created 2026-06-13. |

**Key differences:** v1 has concrete financial figures (Fehlbetrag 27.926,89 €, Rangrücktritt status, monthly transfers). v2 has VW-Bank loan origin story and document checklist. Complement each other — merge into wiki before archiving v2.

### Group C — `raw/Finanzdaten/Privat/CLAUDE.md`

| Path | Notes |
|---|---|
| `raw/Finanzdaten/Privat/CLAUDE.md` | Standalone file — appears to be an older or partial vault configuration. Does not duplicate any other file by content. |

**Recommendation:** Read and compare with `/home/user/intelligence-hub/CLAUDE.md` (root). If superseded, archive in `raw/_archiv/`.

---

## Unique Files (no duplicates — keep as-is)

These files exist only once and have no duplicate anywhere in `raw/`:

| Path | Notes |
|---|---|
| `raw/inbox/00-Master-Context.md` | Master context document — likely important, awaiting ingest |
| `raw/inbox/2026-06 Finance Monthly.md` | June 2026 monthly finance note — awaiting ingest |
| `raw/inbox/2026-06-13.md` | **Empty file** (md5sum `d41d8cd9...` = empty). Safe to delete. |
| `raw/01-Strategie-Business/DoktorLib Automation Pipeline.md` | Unique content — no canonical equivalent found |
| `raw/Business/OK-Capital/OK Capital UG — Finance Vault.md` | Unique name; content duplicates `raw/Finanzdaten/ObsidianVault/Finance/OK Capital UG.md` — see Near-Duplicate Group A |
| `raw/Business/Wagglz/Wagglz GmbH — Finance Vault.md` | Unique name; content duplicates `raw/Finanzdaten/ObsidianVault/Finance/Wagglz GmbH.md` — see Near-Duplicate Group B |
| `raw/README.md` | Vault root README |
| `raw/data/README.md` | Data folder README |
| `raw/Finanzdaten/Privat/CLAUDE.md` | Orphan config file — see Near-Duplicate Group C |
| `raw/Privat/Auswandern/Cyprus Relocation Tracker.md` | *Note: this IS duplicated in inbox — listed in exact duplicates table above (row 9)* |

---

## Non-Markdown Files

| Path | Type | Action |
|---|---|---|
| `raw/Finanzdaten/.~lock.Finanzanalyse_Oleg_Kober_2019-2026.xlsx#` | LibreOffice lock file (stale) | Delete — lock file from a previous session, not an actual document |
| `raw/articles/Unbenannt.base` | Unknown `.base` format | Review and convert or archive |
| `raw/inbox/Unbenannt.base` | Unknown `.base` format | Review and convert or archive |
| `raw/inbox/Unbenannt 1.base` | Unknown `.base` format | Review and convert or archive |
| `raw/inbox/Unbenannt 2.base` | Unknown `.base` format | Review and convert or archive |
| `raw/assets/Image.jpg` | Image attachment | Keep in `raw/assets/` — correct location |

---

## Canonical Structure Recommendation

After cleanup, `raw/` should contain only these top-level directories:

```
raw/
  inbox/          # active drop zone — only unprocessed items
  Privat/         # all personal docs
  Business/       # all company docs (Wagglz/, OK-Capital/, Cafe/)
  MOC/            # navigation only (🏠 Home.md)
  assets/         # images and attachments
  data/           # CSV / wearable exports
  README.md
```

**Directories to retire (delete after removing duplicates):**

| Legacy Directory | Canonical Replacement |
|---|---|
| `raw/00-MOC/` | `raw/MOC/` and `raw/Privat/MOC/` and `raw/Business/MOC/` |
| `raw/01-Strategie-Business/` | `raw/Business/` + `raw/Privat/` subdirs |
| `raw/02-Performance-Leben/` | `raw/Privat/Performance/` |
| `raw/03-Tech-Setup/` | `raw/Privat/Tech/` |
| `raw/04-Recherchen/` | `raw/Privat/Recherchen/` |
| `raw/05-Inbox/` | `raw/inbox/` |
| `raw/Cafe/` | `raw/Business/Cafe/` |
| `raw/Finanzdaten/` | `raw/Privat/Finanzen/`, `raw/Business/OK-Capital/Finanzen/`, `raw/Business/Wagglz/Finanzen/` |

**Note on `raw/Privat/Finanzen/Wagglz GF-Gehalt 2025.md`:** This file appears in `raw/Finanzdaten/Obsidian_Vault/Einnahmen/` and `raw/Business/Wagglz/Finanzen/Einnahmen/`. No `Privat/Finanzen/Einnahmen/Wagglz GF-Gehalt 2025.md` exists — the canonical copy is the one under `raw/Business/Wagglz/`.

---

## Where New Documents Should Be Placed

| Document Type | Drop Location |
|---|---|
| New sources for quick ingest | `raw/inbox/` |
| Personal finance docs | `raw/Privat/Finanzen/` (with appropriate subfolder) |
| Performance / health docs | `raw/Privat/Performance/` |
| Tech setup docs | `raw/Privat/Tech/` |
| Insurance docs | `raw/Privat/Versicherungen/` |
| Research/research threads | `raw/Privat/Recherchen/` |
| Relocation planning | `raw/Privat/Auswandern/` |
| Wagglz company docs | `raw/Business/Wagglz/` |
| OK Capital docs | `raw/Business/OK-Capital/` |
| Café Berlin docs | `raw/Business/Cafe/` |
| Obsidian web clippings | `raw/inbox/` (then triage) |
| Images and attachments | `raw/assets/` |
| CSV / data exports | `raw/data/` |

---

## Recommended Cleanup Sequence

1. **Ingest near-duplicates first** — run ingest on Group A and Group B files to capture all unique content into the wiki before any files are removed.
2. **Delete the 48 exact-duplicate files** in the Legacy column of the exact duplicates table.
3. **Delete the empty file** `raw/inbox/2026-06-13.md`.
4. **Delete the stale lock file** `raw/Finanzdaten/.~lock.Finanzanalyse_Oleg_Kober_2019-2026.xlsx#`.
5. **Review `.base` files** in `raw/inbox/` and `raw/articles/` — determine if they contain importable content.
6. **Review `raw/Finanzdaten/Privat/CLAUDE.md`** — compare with root CLAUDE.md and archive if superseded.
7. **Remove empty legacy directories** after all files are cleared from them.
8. **Run `python3 tools/lint.py`** to catch any orphaned wiki links pointing to deleted paths.
9. **Run `bash scripts/qmd-sync.sh`** to rebuild the search index.
