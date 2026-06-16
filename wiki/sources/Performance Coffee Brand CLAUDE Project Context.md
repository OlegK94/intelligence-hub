---
title: Performance Coffee Brand CLAUDE Project Context
type: source
tags: [business, coffee, functional-beverage, longevity, biohacking, supplement, berlin, oleg, project-context, claude-code, NMN, urolithin-a, spermidine, chlorogenic-acid, trigonellin, hyrox, blueprint, bryan-johnson]
sources: ["raw/Business/PerformanceCafe/CLAUDE.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Claude Code project context file for the Performance Coffee Brand — functional coffee / longevity-stack instant sachet concept targeting athletes, executives, and biohackers; white space identified in Bryan Johnson's Blueprint product lineup
---

# Performance Coffee Brand — CLAUDE Project Context

## Overview

This source document is the persistent project context file (`CLAUDE.md`) for the **Performance Coffee Brand** — a functional beverage startup concept being developed by [[Oleg Personal Context|Oleg]] from Berlin. It serves as the session-initialization file for Claude Code sessions, maintaining project state across interactions.

> For the entity summary and strategic positioning, see [[Performance Coffee Brand]].
> For the founder profile, see [[Oleg Personal Context]].

## Product Summary

- **Name:** Performance Coffee Brand (Arbeitstitel — final name: see `brand/naming_brief.md`)
- **Category:** Functional Coffee / Performance Beverage with Longevity-Stack
- **Kernversprechen (Core Promise):** *Perform now. Live longer.*
- **MVP Format:** Instant-Sachet (Stick-Pack)
- **Scale Path:** RTD Can → Nespresso-kompatible Kapsel

## Strategic White Space

**[[Bryan Johnson]]'s Blueprint** (blueprint.bryanjohnson.com) sells NO coffee.

Blueprint current product range:
- Longevity Mix Pulver
- Ceremonial Matcha
- Super Shrooms
- Ashwagandha+Rhodiola
- NAC+Ginger+Curcumin
- Essential Capsules
- Creatine
- Omega-3
- Collagen

**Gap identified:** Bryan Johnson removed coffee from his personal protocol, but his community **continues drinking coffee** and seeks a Blueprint-compatible product. The white space = *"The Longevity Coffee Blueprint doesn't make."*

Quality reference bar (Blueprint standard): *"Science-backed, precision-dosed, every ingredient fought for its life, no pixie-dusting, no BS."*

## Target Audience (3 Segments)

| Segment | Use Case |
|---|---|
| **Athleten** (Hyrox, CrossFit, Triathlon) | Pre-Workout + Longevity-Stack |
| **Business / Executive** | Morning Deep Work, sustained energy without crash |
| **Biohacker / Blueprint-Follower** | Daily NMN, Urolithin A, Spermidine intake |

**Founder Context:** Oleg Kober, Berlin. Sales at Doctolib GmbH. 188cm, 96.7kg, 20.3% KF, active Hyrox athlete. Aerobic capacity as primary limiter. Reference framework: [[Bryan Johnson]], [[Andrew Huberman]], Peter Attia.

## Known Critical Points

### Regulatory Issues

| Ingredient | Issue |
|---|---|
| **NMN** | EU Novel Food status 2025/2026 unclear → must clarify BEFORE stack decision |
| **Urolithin A** | Amazentis/Timeline Nutrition holds Mitopure patent → license or find alternative |
| **Spermidine** (wheat germ) | Novel Food status in Germany — to be checked |
| **NR (Nicotinamide Riboside)** | Chromadex NIAGEN patent → IP check required |
| **Huperzin A** | **Banned as food ingredient in Germany** |

### Certification Priority

1. **[[Kölner Liste]]** — DACH standard, cheapest option, immediately sensible
2. **[[Informed Sport]]** — pan-European, for EU scaling
3. **[[NSF Certified for Sport]]** — only relevant for US expansion

### Sensory / Production Challenges

| Issue | Solution |
|---|---|
| NAC: sulfur smell | Flavorist for masking — mandatory |
| Curcumin: hydrophobic | Liposomal or micellar form for solubility |
| NMN/NR: oxidation-sensitive | Protective gas sealing in sachet |
| Mushroom extracts: bitter | Roast degree + coffee base as natural masking |
| Roast preference | **Light/Medium Roast**: maximizes chlorogenic acid + trigonellin |

### Coffee as Longevity Ingredient

- **Trigonellin** in coffee = natural NMN precursor (2024 research)
- **Chlorogenic acid:** AMPK activation, insulin sensitivity
- **Light Roast** maximizes both compounds
- **Vietnamese Robusta:** highest caffeine content + highest chlorogenic acid

## Module Status

| # | Module | Status | File |
|---|---|---|---|
| 0 | Longevity Science Fundamentals | ✅ Complete | `research/01_longevity_science.md` |
| 1 | Ingredient Database | ⬜ Empty | `research/02_ingredienzen_db.md` |
| 2 | Coffee Specification | ⬜ Empty | `research/03_kaffee_specs.md` |
| 3 | Market Analysis + Competition | ⬜ Empty | `research/04_marktanalyse.md` |
| 4 | Prototype Partners | ⬜ Empty | `research/05_prototyp_partner.md` |
| 5 | Regulatory + IP | ⬜ Empty | `research/06_regulatorik.md` |
| 6 | Business Case + Unit Economics | ⬜ Empty | `research/07_business_case.md` |
| 7 | Brand & Naming | ⬜ Empty | `brand/naming_brief.md` |
| 8 | IP & Patent Landscape | ⬜ Empty | `legal/ip_landscape.md` |
| 9 | Unit Economics Model | ⬜ Empty | `models/unit_economics.py` |

**Key Blocker:** Regulatory module (5) must precede stack decision — especially NMN Novel Food status.

## Project File Structure

```
performance-cafe/
├── CLAUDE.md                    ← source document (this page)
├── .cursor/rules/
│   └── performance_cafe.mdc
├── research/
│   ├── 00_master_brief.md
│   ├── 01_longevity_science.md  ← COMPLETE
│   ├── 02_ingredienzen_db.md
│   ├── 03_kaffee_specs.md
│   ├── 04_marktanalyse.md
│   ├── 05_prototyp_partner.md
│   ├── 06_regulatorik.md
│   └── 07_business_case.md
├── brand/
│   ├── naming_brief.md
│   └── positioning.md
├── legal/
│   ├── ip_landscape.md
│   └── entity_structure.md
├── models/
│   ├── unit_economics.py
│   └── ingredient_db.csv
└── ops/
    ├── supplier_list.md
    └── certification_roadmap.md
```

## Working Conventions

- **Language:** Always respond in German
- **Format:** Markdown with Frontmatter (`status`, `priority`, `date`, `modul`)
- **Quality Standard:** Concrete companies, dosages, prices, contacts — no generalities
- **Sources:** Use web_search, prefer 2024/2025 data
- **Output:** Always write to the corresponding module file, not just chat
- **Blockers:** Explicitly mark module dependencies
- **Questions:** Clarify briefly, don't silently optimize

## Related Pages

- [[Performance Coffee Brand]] — entity summary page
- [[Bryan Johnson]] — white space reference and quality benchmark
- [[Andrew Huberman]] — scientific framework reference
- [[Oleg Personal Context]] — founder
- [[Longevity Stack Ingredients]] — ingredient science concept
- [[Functional Beverage Market]] — market context
- [[NMN]] — key regulatory blocker ingredient
- [[Urolithin A]] — patented ingredient (Mitopure)
- [[Chlorogenic Acid]] — coffee longevity compound
- [[Trigonellin]] — NMN precursor in coffee
- [[Kölner Liste]] — primary certification target
- [[Daily Protocol Checklist]] — Oleg's personal stack (cross-reference: `*[[Performance Coffee]] | [[Supplement Stack]]*`)
