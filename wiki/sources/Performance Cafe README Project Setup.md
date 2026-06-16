---
title: Performance Cafe README Project Setup
type: source
tags: [performance-cafe, longevity-coffee, project-setup, obsidian, cursor, claude-code, workflow, regulatorik, novel-food, NMN, urolithin-a, spermidine, NAC, IP, patents]
sources: ["raw/Business/PerformanceCafe/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Project setup README for Performance Café longevity coffee brand — 3-step Obsidian/Cursor/Claude Code workflow, research module priority order, full file structure, and critical decision blockers (NMN Novel Food, Amazentis patent, NAC masking, CMO certification)
---

# Performance Café — README Project Setup

## Overview

This source document is the `README.md` for the [[Performance Coffee Brand]] project vault (path: `raw/Business/PerformanceCafe/`). It defines the **toolchain setup**, **research module execution workflow**, and **critical pre-prototype decision blockers**.

> For the full project context, master brief, and AI instructions, see [[Performance Coffee Brand CLAUDE Project Context]].
> For the entity summary of the brand concept, see [[Performance Coffee Brand]].

## Tagline

**"Perform now. Live longer."**

## 3-Step Toolchain Setup

### 1. Obsidian Vault
- Open the `performance-cafe/` folder as an Obsidian Vault
- All `.md` files appear in sidebar immediately
- Wikilinks between research modules work automatically
- Dataview plugin: Module status table from frontmatter

### 2. Cursor IDE
- Open folder in Cursor
- `.cursor/rules/performance_cafe.mdc` auto-loads as project context
- Every AI request in Cursor knows: product, target audience, critical blockers

### 3. Claude Code
- `CLAUDE.md` is read automatically at session start
- Full project context available from first prompt
- Run: `cd performance-cafe && claude`

## Workflow Patterns

### Research Module Execution (Claude Code)

```bash
# Single module
claude "Arbeite Modul 1 (Ingredienzen Datenbank) aus.
Lies research/00_master_brief.md für den vollständigen Auftrag.
Schreibe Ergebnisse nach research/02_ingredienzen_db.md"

# Priority: Regulatorik first (BLOCKER)
claude "Kläre den EU Novel Food Status für NMN, Urolithin A und Spermidine.
Schreibe Ergebnisse nach research/06_regulatorik.md"

# Cross-module linkage
claude "Lies research/02_ingredienzen_db.md und research/06_regulatorik.md.
Identifiziere alle Inhaltsstoffe mit regulatorischen Blocker.
Aktualisiere CLAUDE.md mit den Erkenntnissen."
```

### Cursor (@-References)
```
@research/02_ingredienzen_db.md Welche Inhaltsstoffe haben Patent-Konflikte?
@research/06_regulatorik.md Erstelle eine Prioritätsliste der regulatorischen Risiken
@models/unit_economics.py Fülle die Rohstoffpreise aus @models/ingredient_db.csv
```

## Research Module Priority Order

| Priority | File | Status | Reason |
|----------|------|--------|--------|
| 1 | `research/06_regulatorik.md` | ⚠️ KRITISCH | Determines which ingredients are allowed |
| 2 | `legal/ip_landscape.md` | ⚠️ KRITISCH | Amazentis + Chromadex patents |
| 3 | `research/02_ingredienzen_db.md` | — | Only useful after Regulatorik |
| 4 | `research/03_kaffee_specs.md` | — | Coffee base specifications |
| 5 | `research/04_marktanalyse.md` | — | Market analysis |
| 6 | `research/05_prototyp_partner.md` | — | Prototype partner identification |
| 7 | `research/07_business_case.md` | — | Only after COGS data from modules 1+4 |
| 8 | `models/unit_economics.py` | — | Only after raw material prices known |

**Key sequencing logic:**
- Regulatorik first → determines allowed ingredient stack
- IP landscape second → determines licensing cost structure
- Ingredient DB only after regulatorik (no point researching blocked ingredients)
- Business case last → requires COGS data from upstream modules

## Full File Structure

```
performance-cafe/
├── CLAUDE.md                      ← Claude Code master context
├── README.md                      ← this document
├── .cursor/rules/
│   └── performance_cafe.mdc       ← Cursor AI context
├── research/
│   ├── 00_master_brief.md         ← Full research brief (Module 0)
│   ├── 01_longevity_science.md    ← Longevity science (Module 0)
│   ├── 02_ingredienzen_db.md      ← Ingredient DB (Module 1) ⭐
│   ├── 03_kaffee_specs.md         ← Coffee specs (Module 2)
│   ├── 04_marktanalyse.md         ← Market analysis (Module 3)
│   ├── 05_prototyp_partner.md     ← Prototype partner (Module 4)
│   ├── 06_regulatorik.md          ← Regulatory (Module 5) ⚠️
│   └── 07_business_case.md        ← Business case (Module 6)
├── brand/
│   └── naming_brief.md            ← Naming (Module 7)
├── legal/
│   ├── ip_landscape.md            ← IP landscape (Module 8) ⚠️
│   └── entity_structure.md        ← GmbH, trademark registration
├── models/
│   ├── unit_economics.py          ← COGS + margin calculation
│   └── ingredient_db.csv          ← Structured ingredient DB
└── ops/
    ├── supplier_list.md           ← Raw material suppliers
    └── certification_roadmap.md   ← Kölner Liste → Informed Sport → NSF
```

## Critical Pre-Prototype Decisions

| Question | Blocks | File |
|----------|--------|------|
| [[NMN]] EU Novel Food Status 2025? | Stack decision | `research/06_regulatorik.md` |
| [[Amazentis]] Patent [[Urolithin A]] — Lizenz? | Stack + costs | `legal/ip_landscape.md` |
| [[NAC]] Geruchs-Maskierung — how? | Prototype | `research/05_prototyp_partner.md` |
| Lebensmittel vs. NEM — which path? | Regulatory + marketing | `research/06_regulatorik.md` |
| Kölner Liste CMO-Anforderungen? | CMO selection | `ops/certification_roadmap.md` |

### Decision Details

**NMN Novel Food:** NMN may be classified as a Novel Food under EU Regulation 2015/2283, which would require pre-market authorization before inclusion in a food/supplement product sold in the EU. This is the single most critical ingredient blocker.

**Amazentis/Urolithin A Patent:** [[Amazentis]] holds patents on [[Urolithin A]] (sold as MITOPURE). Using Urolithin A may require licensing from Amazentis — impacting COGS and viability. See [[Urolithin A]].

**Chromadex/NMN Patent:** [[Chromadex]] holds relevant patents on [[NMN]] (Tru Niagen / NR). Patent landscape overlaps with NMN sourcing from certain manufacturers.

**NAC Odor:** [[NAC]] (N-Acetyl Cysteine) has a strong sulfurous odor that is difficult to mask in food/beverage formats — a formulation challenge for the coffee format.

**Lebensmittel vs. NEM:** Whether to classify the product as a food (Lebensmittel) or food supplement (Nahrungsergänzungsmittel / NEM) determines label claims, dosing allowances, and marketing options.

**Kölner Liste:** The [[Kölner Liste]] is the German anti-doping certification for supplements. CMO (Contract Manufacturing Organization) compliance with Kölner Liste is a prerequisite for the sports/performance market.

## Related Pages

- [[Performance Coffee Brand]] — entity page for the brand concept
- [[Performance Coffee Brand CLAUDE Project Context]] — master brief and AI context
- [[NMN]] — Novel Food blocker
- [[Urolithin A]] — Amazentis patent blocker
- [[NAC]] — formulation challenge
- [[Spermidine]] — Novel Food candidate
- [[Amazentis]] — patent holder for Urolithin A
- [[Chromadex]] — patent holder for NMN/NR
- [[Kölner Liste]] — anti-doping certification
- [[Longevity Stack Ingredients]] — full ingredient framework
- [[EU Novel Food Regulation]] — regulatory framework
- [[Chlorogenic Acid]] — key coffee compound
- [[Bryan Johnson]] — market benchmark (Blueprint gap)
