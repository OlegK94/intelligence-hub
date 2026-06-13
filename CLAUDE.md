# Intelligence Hub — LLM Wiki Schema

This vault follows [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources are compiled once into a persistent, interlinked markdown wiki. The LLM maintains the wiki; the human curates sources and asks questions.

## Vault purpose

Personal knowledge base spanning:

- **Strategie & Business (privat)** — OK Capital, Wagglz, Café Berlin, Versicherungen
- **Performance & Leben** — health protocols, Hyrox, supplements, body composition
- **Tech & Setup (privat)** — tooling, privacy stack
- **Finanzen (privat)** — accounts, taxes, cash flow, company structures
- **Recherchen** — ad-hoc research threads

**Nicht in diesem Vault:** Doctolib-Arbeit, Firmen-Automations, aktive Relocation (Someday in paar Jahren).

## Directory layout

```
raw/          Immutable source documents (never modify — read only)
wiki/         LLM-generated, interlinked knowledge (you maintain this)
outputs/      Derived artifacts from queries (notes, slides, charts)
tools/        CLI scripts the LLM can shell out to
```

### raw/ conventions

- Sources are **immutable**. Never edit, move, or delete files in `raw/`.
- Drop new material anywhere under `raw/`, or use `raw/inbox/` for items awaiting first ingest.
- Images and attachments live in `raw/assets/`.
- Web clippings from Obsidian Web Clipper go to `Clippings/` or `raw/inbox/`.
- Supported ingest types: `.md`, `.txt`, `.pdf` (text extracted if possible).

### wiki/ conventions

```
wiki/
  index.md       Catalog of all pages (updated on every ingest)
  log.md         Append-only chronological activity log
  entities/      People, companies, products, places
  concepts/      Ideas, frameworks, protocols, definitions
  sources/       One summary page per ingested raw document
  syntheses/     Cross-cutting analyses and evolving theses
  comparisons/   Side-by-side evaluations
```

#### Page format

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

#### index.md rules

Organize by category (Entities, Concepts, Sources, Syntheses, Comparisons). Each entry:

```
- [[Page Name]] — one-line summary (updated YYYY-MM-DD)
```

#### log.md rules

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

## Operations

### 1. Ingest

When the user adds a source or says "ingest":

1. Read the raw file(s) — do not modify them.
2. Read `wiki/index.md` and scan existing wiki pages for overlap.
3. Create or update:
   - A `wiki/sources/` page summarizing the raw document
   - Relevant `wiki/entities/` and `wiki/concepts/` pages
   - Cross-links across the wiki
4. Update `wiki/index.md`.
5. Append to `wiki/log.md`.
6. Record the source in `wiki/.ingest_manifest.json` (via CLI).

CLI (preferred for automation):

```bash
python3 tools/ingest.py                          # process raw/inbox/
python3 tools/ingest.py --file raw/path/to.md    # single file
python3 tools/ingest.py --scope clippings        # process Clippings/
python3 tools/ingest.py --scope raw            # all un-ingested under raw/
```

Or ask the agent to ingest conversationally — same workflow, same outputs.

### 2. Query

When the user asks a question:

1. Read `wiki/index.md` first to locate relevant pages.
2. Run `python3 tools/search.py "query"` (QMD hybrid search across wiki/raw/outputs; BM25 fallback).
3. Read the top-matching pages (use `qmd get <path>` for full excerpts when QMD is installed).
4. Synthesize an answer with citations to `[[wiki pages]]`.
4. Write output to `outputs/notes/`, `outputs/slides/` (Marp), or `outputs/charts/` (matplotlib).
5. **File valuable answers back into the wiki** as new synthesis/comparison pages.
6. Append to `wiki/log.md`.

CLI:

```bash
python3 tools/query.py "How do my health protocols relate to Hyrox training?"
python3 tools/query.py "Compare OK Capital vs Wagglz tax structure" --output slides
```

### 3. Lint

Periodically (or on request) health-check the wiki:

- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Concepts mentioned but lacking dedicated pages
- Missing cross-references
- Gaps fillable via web search

CLI:

```bash
python3 tools/lint.py
python3 tools/lint.py --fix   # let LLM propose and apply fixes
```

### 4. Search

Hybrid local search via [QMD](https://github.com/tobi/qmd) (BM25 + vectors + reranking). Falls back to naive wiki BM25 if QMD is not installed.

```bash
python3 tools/search.py "supplement stack"              # hybrid (best)
python3 tools/search.py "Wagglz" -c hub-wiki           # wiki only
python3 tools/search.py "Fixkosten" --engine search    # keyword only (fast)
python3 tools/search.py "health" --engine bm25         # legacy wiki-only

# QMD setup (once) + re-index after ingest
bash scripts/qmd-setup.sh
bash scripts/qmd-setup.sh --embed   # download models + semantic search
bash scripts/qmd-sync.sh            # after ingest / wiki edits
```

QMD collections: `hub-wiki`, `hub-raw`, `hub-outputs`. Index lives in `~/.cache/qmd/` (not in git).

## outputs/ conventions

```
outputs/
  notes/     Markdown answer documents (dated filenames)
  slides/    Marp slide decks (.md with marp frontmatter)
  charts/    Matplotlib images (.png)
```

Filename pattern: `YYYY-MM-DD-short-slug.md` or `.png`.

Good outputs get filed back into `wiki/syntheses/` or `wiki/comparisons/`.

## Obsidian setup

- Vault root = this directory.
- Attachment folder: `raw/assets/`
- Hotkey: "Download attachments for current file" after web clipping.
- Plugins already installed: Dataview, Templater, Excalidraw, Kanban.
- View the wiki graph to see connections and orphan hubs.

## Agent behavior

- **You write the wiki.** The user rarely edits wiki pages directly.
- **Raw is sacred.** Never modify `raw/`.
- **Compound knowledge.** Every ingest and query should make the wiki richer.
- **Read index first.** On every query, start with `wiki/index.md`.
- **Prefer filing over chat.** Answers worth keeping become wiki pages or `outputs/`.
- **Co-evolve this schema.** Update CLAUDE.md when conventions change.

## Environment

```bash
export ANTHROPIC_API_KEY="..."
export WIKI_MODEL="claude-sonnet-4-6"   # optional override
pip install -r requirements.txt
```
