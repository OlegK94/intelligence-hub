# Intelligence Hub — LLM Wiki Schema

This vault follows [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources are compiled once into a persistent, interlinked markdown wiki. The LLM maintains the wiki; the human curates sources and asks questions.

**Detail conventions:** `docs/conventions.md` — page format, index/log rules, outputs, Obsidian, QMD, skills.

## Vault purpose

Personal knowledge base spanning:

- **Strategie & Business (privat)** — OK Capital, Wagglz, Café Berlin, Versicherungen
- **Performance & Leben** — health protocols, Hyrox, supplements, body composition
- **Tech & Setup (privat)** — tooling, privacy stack
- **Finanzen (privat)** — accounts, taxes, cash flow, company structures
- **Recherchen** — ad-hoc research threads

**Nicht in diesem Vault:** Doctolib-Arbeit, Firmen-Automations, aktive Relocation.

## Directory layout

```
raw/          Immutable source documents (never modify — read only)
wiki/         LLM-generated, interlinked knowledge (you maintain this)
outputs/      Derived artifacts from queries (notes, slides, charts)
tools/        CLI scripts the LLM can shell out to
docs/         Conventions, schemas, reference docs
.claude/      Claude Code config — settings, skills, hooks
```

### wiki/ structure

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

## Operations

### /ingest

Add a source → wiki. See `.claude/skills/ingest.md` for full steps.

```bash
python3 tools/ingest.py                          # process raw/inbox/
python3 tools/ingest.py --file raw/path/to.md    # single file
python3 tools/ingest.py --scope clippings        # process Clippings/
python3 tools/ingest.py --scope raw              # all un-ingested under raw/
```

### /query

Answer a question, write output, file back valuable answers.

```bash
python3 tools/query.py "question"
python3 tools/query.py "question" --output slides
```

### /lint

Health-check for contradictions, orphan pages, stale claims.

```bash
python3 tools/lint.py
python3 tools/lint.py --fix
```

### /audit

Audit Claude Code setup or wiki conventions. Produces Apple-style HTML report.

### Search

```bash
python3 tools/search.py "query"          # hybrid BM25/vector (best)
python3 tools/search.py "q" -c hub-wiki  # wiki only
```

## Agent behavior

- **You write the wiki.** The user rarely edits wiki pages directly.
- **Raw is sacred.** Never modify anything under `raw/`.
- **Compound knowledge.** Every ingest and query should make the wiki richer.
- **Read index first.** On every query, start with `wiki/index.md`.
- **Prefer filing over chat.** Answers worth keeping become wiki pages or `outputs/`.
- **Apple-style HTML** for visualizations — see `docs/conventions.md`.
- **Co-evolve this schema.** Update CLAUDE.md when conventions change.

## Environment

```bash
export ANTHROPIC_API_KEY="..."
export WIKI_MODEL="claude-sonnet-4-6"   # optional override
pip install -r requirements.txt
```
