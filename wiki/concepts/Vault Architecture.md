---
title: Vault Architecture
type: concept
tags: [vault, architecture, workflow, ingest, raw, wiki, obsidian, meta]
sources: ["raw/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: The two-layer vault architecture separating immutable raw sources from the living wiki — raw/ contains original notes, wiki/ contains integrated knowledge; ingest script bridges them
---

# Vault Architecture

## Overview

The vault uses a **two-layer architecture** that strictly separates raw source material from integrated wiki knowledge. This pattern (similar to the Karpathy LLM Wiki approach) ensures that:
1. Original sources are preserved unchanged
2. Knowledge synthesis happens exclusively in the wiki layer
3. All wiki pages can be traced to specific source files

## Two-Layer Model

```
Layer 1: raw/           ← Immutable source material
         ↓
     python3 tools/ingest.py
         ↓
Layer 2: wiki/          ← Living, integrated knowledge base
```

### Layer 1 — raw/
- **Immutable after ingest** — files are never edited
- Organized by life/business domain (Privat, Business, _archiv)
- Contains original notes, exports, templates, and documents
- Includes `inbox/` as the staging area for new material
- See [[Raw Vault Structure README]] for the full directory map

### Layer 2 — wiki/
- **Living, updateable** — continuously refined and extended
- Organized by knowledge type:
  - `wiki/entities/` — specific people, places, companies, events
  - `wiki/concepts/` — ideas, methods, frameworks
  - `wiki/sources/` — one source summary page per raw file ingested
  - `wiki/syntheses/` — cross-source synthesis and analysis
  - `wiki/comparisons/` — structured comparisons
- Connected via [[Obsidian]] wikilinks throughout

## Ingest Workflow

1. **New content** arrives in `raw/inbox/`
2. **Ingest script** (`python3 tools/ingest.py`) processes the file
3. **Source summary page** created in `wiki/sources/` (one per raw file)
4. **Entity/concept pages** created or updated as needed
5. **Index updated** with new entries
6. **Raw file remains immutable** — wiki is the single point of truth

## Page Type Hierarchy

| Type | Purpose | Location |
|---|---|---|
| `source` | Summary of a single raw file | `wiki/sources/` |
| `entity` | Specific person, company, event, etc. | `wiki/entities/` |
| `concept` | Method, framework, idea | `wiki/concepts/` |
| `synthesis` | Cross-source analysis | `wiki/syntheses/` |
| `comparison` | Structured A vs B | `wiki/comparisons/` |

## Exclusion Zone

`raw/_archiv/` is explicitly excluded from active ingest. Content there (primarily old work history) should not generate wiki pages.

## Naming Conventions

- **Source pages:** Named after the raw file for traceability
- **Entity pages:** Human-readable proper names (people, companies, events)
- **Concept pages:** Topic name (e.g., "BMR and TDEE", "Brick Training")
- **No .md suffix** in wikilinks — Obsidian resolves automatically

## YAML Frontmatter Standard

Every wiki page uses:
```yaml
---
title: Human Readable Title
type: source|entity|concept|synthesis|comparison
tags: [tag1, tag2]
sources: ["raw/path/to/source.md"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
summary: One-line description
---
```

## Related Pages

- [[Raw Vault Structure README]] — the README that defines raw/ structure
- [[Oleg Personal Context]] — vault owner
- [[MOC Performance und Leben]] — performance MOC
- [[MOC Finanzen]] — finance MOC
- [[MOC Strategie und Business]] — business MOC
- [[MOC Tech und Setup]] — tech MOC
