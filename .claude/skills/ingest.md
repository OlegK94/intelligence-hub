# /ingest — Wiki Ingest

Ingest one or more raw sources into the wiki. Call with an optional file path or scope.

## Usage

```
/ingest                        # process raw/inbox/
/ingest raw/path/to/file.md   # single file
/ingest --scope clippings      # process Clippings/
/ingest --scope raw            # all un-ingested under raw/
```

## Steps (always in this order)

1. Read the raw file(s) — never modify raw/.
2. Read `wiki/index.md` to check for existing pages.
3. Create or update:
   - `wiki/sources/` — one summary page per raw document
   - `wiki/entities/` and `wiki/concepts/` — for people, places, products, ideas
   - Wikilinks across pages
4. Update `wiki/index.md` (append new entries under the right category).
5. Append one entry to `wiki/log.md`.
6. Record in `wiki/.ingest_manifest.json` via `python3 tools/ingest.py`.

## Rules

- Raw is sacred. Never edit files under `raw/`.
- Every wiki page needs YAML frontmatter (title, type, tags, sources, created, updated, summary).
- When new data contradicts existing claims, add `## Contradictions / Updates` — do not silently overwrite.
- Link liberally: `[[Page Name]]` for every entity or concept mentioned.
