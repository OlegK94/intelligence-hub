# Intelligence Hub — LLM Wiki Schema

This vault follows [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources are compiled once into a persistent, interlinked markdown wiki. The LLM maintains the wiki; the human curates sources and asks questions.

## Vault purpose

Personal knowledge base spanning:

- **Strategie & Business (privat)** — OK Capital, Wagglz, Cafe Berlin, Versicherungen
- **Performance & Leben** — health protocols, Hyrox, supplements, body composition
- **Tech & Setup (privat)** — tooling, privacy stack
- **Finanzen (privat)** — accounts, taxes, cash flow, company structures
- **Recherchen** — ad-hoc research threads

**Nicht in diesem Vault:** Doctolib-Arbeit, Firmen-Automations, aktive Relocation (Someday).

## Directory layout

```
raw/          Immutable source documents (never modify)
wiki/         LLM-generated, interlinked knowledge (you maintain this)
outputs/      Derived artifacts from queries (notes, slides, charts)
tools/        CLI scripts the LLM can shell out to
templates/    Obsidian Templater templates
```

### raw/ conventions

```
raw/
  inbox/       Drop zone for new sources awaiting ingest
  assets/      Images and attachments
  data/        Structured exports (CSV, wearable data)
  MOC/         Vault home & navigation (dashboard.md)
  Privat/      Personal
  Business/    Wagglz/, Cafe/, OK-Capital/
  _archiv/     Excluded topics
```

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
- When new data contradicts old claims, add `## Contradictions / Updates` — do not silently overwrite.

## Operations

### 1. Ingest

```bash
python3 tools/ingest.py                       # process raw/inbox/
python3 tools/ingest.py --file raw/path/to.md # single file
python3 tools/ingest.py --scope clippings     # process Clippings/
python3 tools/ingest.py --scope raw           # all un-ingested under raw/
```

### 2. Query

```bash
python3 tools/query.py "How do my health protocols relate to Hyrox?"
python3 tools/query.py "Compare OK Capital vs Wagglz tax structure" --output slides
```

### 3. Research Sprint (Power Research)

Fuer tiefgruendige Recherchen mit Primaerquellen, Gegenpositionen und Konfidenz-Scores:

```bash
# Neue Frage - volles Research-Protokoll
python3 tools/research_sprint.py "Was ist der beste NAD+-Precursor fuer den EU-Markt?"

# Vergleich zweier Optionen
python3 tools/research_sprint.py "NR vs NMN vs Trigonellin" --type comparison

# Deep Dive mit Slides-Output
python3 tools/research_sprint.py "Koelner Liste Zertifizierungsprozess" --output slides
```

**Research Sprint Qualitaetsstandard:**
- Jeder Claim: Quelle + Konfidenz (HOCH/MITTEL/NIEDRIG)
- Aktiv Gegenpositionen suchen - nicht nur bestaetigen
- Regulatory-Kontext bei allem, was EU/DE-Markt betrifft
- Ergebnis immer in `wiki/syntheses/` oder `wiki/comparisons/` ablegen

**Konfidenz-Skala:**
- HOCH: Meta-Analyse, RCT, repliziert, offizielle Behoerde
- MITTEL: 1-2 Studien, Expert-Konsens, Industriestandard
- NIEDRIG: Anekdote, Tier-Studie, vorlaeufig, eine Quelle

### 4. Search

```bash
python3 tools/search.py "supplement stack"
python3 tools/search.py "Wagglz" -c hub-business
python3 tools/search.py "Hyrox" -c hub-privat
```

### 5. Lint

```bash
python3 tools/lint.py
python3 tools/lint.py --fix
```

### 6. Status

```bash
python3 tools/status.py
```

## Visualisierung

```bash
# Dashboard in Obsidian oeffnen
# -> raw/MOC/dashboard.md (Dataview Live-Abfragen)

# Slides aus Research generieren
python3 tools/research_sprint.py "Thema" --output slides
# -> outputs/slides/YYYY-MM-DD-slug.md (Marp-Format)

# Template fuer neue Research Sprints
# -> templates/research-sprint.md (Templater)

# Template fuer Praesentationen
# -> templates/marp-slide-deck.md
```

## outputs/ conventions

```
outputs/
  notes/     Markdown answer documents (dated filenames)
  slides/    Marp slide decks (.md with marp frontmatter)
  charts/    Matplotlib images (.png)
```

Good outputs get filed back into `wiki/syntheses/` or `wiki/comparisons/`.

## Obsidian setup

- Vault root = this directory.
- Attachment folder: `raw/assets/`
- Plugins enabled: Dataview, Templater, Excalidraw, Kanban, Tasks, Marp, Obsidian Git, Periodic Notes, Terminal.
- Dashboard: `raw/MOC/dashboard.md`
- View the wiki graph to see connections and orphan hubs.

## Agent behavior

- **You write the wiki.** The user rarely edits wiki pages directly.
- **Raw is sacred.** Never modify `raw/`.
- **Compound knowledge.** Every ingest and query should make the wiki richer.
- **Read index first.** On every query, start with `wiki/index.md`.
- **Prefer filing over chat.** Answers worth keeping become wiki pages or `outputs/`.
- **Research standard:** Immer Konfidenz-Score, immer Gegenpositionen, immer Quellen.
- **Co-evolve this schema.** Update CLAUDE.md when conventions change.

## Environment

```bash
export ANTHROPIC_API_KEY="..."
export WIKI_MODEL="claude-sonnet-4-6"   # optional override
pip install -r requirements.txt
```
