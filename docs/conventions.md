# Intelligence Hub — Detailed Conventions

## wiki/ Page Format

Every wiki page starts with YAML frontmatter:

```yaml
---
title: Page Title
type: entity | concept | source | synthesis | comparison
tags: [tag1, tag2]
sources: ["raw/path/to/source.md"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
summary: One-line description for the index
---
```

Body rules:

- Wikipedia-style prose: lead paragraph, then sections.
- Heavy use of Obsidian wikilinks: `[[Page Name]]`.
- Cite raw sources inline: `(source: [[Source Page Name]])`.
- When new data contradicts old claims, add a `## Contradictions / Updates` section — do not silently overwrite.

## index.md rules

Organize by category (Entities, Concepts, Sources, Syntheses, Comparisons). Each entry:

```
- [[Page Name]] — one-line summary (updated YYYY-MM-DD)
```

## log.md rules

Append-only. Every operation gets one entry:

```
## [YYYY-MM-DD HH:MM] ingest | raw/path/to/file.md
- Created/updated: [[Page A]], [[Page B]]
- Notes: brief summary of what changed

## [YYYY-MM-DD HH:MM] query | "user question"
- Output: outputs/notes/2026-06-13-topic.md
- Filed back: [[New Synthesis Page]]

## [YYYY-MM-DD HH:MM] lint
- Found 3 orphan pages, 1 contradiction, 2 missing entity pages
```

## outputs/ conventions

```
outputs/
  notes/     Markdown answer documents (dated filenames)
  slides/    Marp slide decks (.md with marp frontmatter)
  charts/    Matplotlib images (.png)
```

Filename pattern: `YYYY-MM-DD-short-slug.md` or `.png`.

Good outputs get filed back into `wiki/syntheses/` or `wiki/comparisons/`.

Visualizations use Apple-style HTML: background `#F5F5F7`, accent `#0071E3`, SF Pro fonts, large numbers, generous whitespace.

## raw/ conventions

```
raw/
  inbox/       Drop zone for new sources awaiting ingest
  assets/      Images and attachments
  data/        Structured exports (CSV, wearable data)
  MOC/         Vault home & navigation
  Privat/      Personal — Performance, Tech, Finanzen, Versicherungen, Recherchen, Auswandern
  Business/    Wagglz/, Cafe/, OK-Capital/
  _archiv/     Excluded topics (e.g. work automations) — low ingest priority
```

- Sources are **immutable after ingest**. One-time vault migrations update paths in `.ingest_manifest.json`.
- Drop new material in `raw/inbox/`, or the relevant `Privat/` / `Business/` subfolder.
- Images and attachments live in `raw/assets/`.
- Web clippings from Obsidian Web Clipper go to `Clippings/` or `raw/inbox/`.
- Supported ingest types: `.md`, `.txt`, `.pdf` (text extracted if possible).
- **Nicht ingesten:** `_archiv/Work/` (Firmen-Automations), bulk PDF-Kontoauszüge — nur Monatsübersichten.

## Obsidian setup

- Vault root = this directory.
- Attachment folder: `raw/assets/`
- Hotkey: "Download attachments for current file" after web clipping.
- Plugins already installed: Dataview, Templater, Excalidraw, Kanban.
- View the wiki graph to see connections and orphan hubs.

## QMD Search

Hybrid local search via [QMD](https://github.com/tobi/qmd) (BM25 + vectors + reranking). Falls back to naive wiki BM25 if QMD is not installed.

```bash
python3 tools/search.py "supplement stack"              # hybrid (best)
python3 tools/search.py "Wagglz" -c hub-business       # business only
python3 tools/search.py "Hyrox" -c hub-privat          # personal only
python3 tools/search.py "health" --engine bm25         # legacy wiki-only

# QMD setup (once) + re-index after ingest
bash scripts/qmd-setup.sh
bash scripts/qmd-setup.sh --embed   # download models + semantic search
bash scripts/qmd-sync.sh            # after ingest / wiki edits
```

QMD collections: `hub-wiki`, `hub-privat`, `hub-business`, `hub-outputs`. Index lives in `~/.cache/qmd/` (not in git).

## Skills (Slash Commands)

- `/ingest` — see `.claude/skills/ingest.md`
- `/query` — see `.claude/skills/query.md`
- `/lint` — see `.claude/skills/lint.md`
- `/audit` — see `.claude/skills/audit.md`
