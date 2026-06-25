# Finanzdaten — Duplicate Export Archive

**Status:** Archived duplicate tree (2026-06-14 audit). **Excluded from wiki ingest** — `tools/common.py` skips `raw/Finanzdaten/` on `--scope raw`.

This folder is a parallel copy of finance vault content, largely **byte-identical** to:

- `raw/Privat/Finanzen/`
- `raw/Business/Wagglz/Finanzen/`
- `raw/Business/OK-Capital/Finanzen/`

## Canonical source of truth

Edit and ingest from `raw/Privat/Finanzen/` and `raw/Business/*/Finanzen/` — not from here.

## Unique files (if any)

- `GESAMTANALYSE_Oleg_Kober_2025-2026.md` — duplicate of `raw/Privat/Finanzen/Archiv/`
- `ObsidianVault/` subtree — legacy export structure

Safe to delete this entire folder once confirmed no unique content remains. Audit found **52 duplicate MD5 groups** involving Finanzdaten paths.
