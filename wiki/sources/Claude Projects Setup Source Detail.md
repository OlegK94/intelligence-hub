---
title: Claude Projects Setup Source Detail
type: source
tags: [claude, anthropic, AI, setup, tools, productivity, projects, LLM, deutsch, no-code, make, tally, notion, salesforce, dust]
sources: ["raw/03-Tech-Setup/Claude Projects Setup.md"]
created: 2026-06-07
updated: 2026-06-07
summary: Source document detailing Oleg's 7 Claude AI Projects — structure, roles, context-driven vs task-driven distinction, instruction schema, global preferences, and no-code tech stack (Make, Tally, Notion, Salesforce, Dust)
---

# Claude Projects Setup — Source Detail

## Overview

This source document (status: Aktiv, 7 Projekte, created 2026-06-07) captures the full configuration of [[Oleg Personal Context|Oleg]]'s [[Claude Projects Setup]] within Anthropic's Claude AI platform. It defines the project structure, the distinction between context-driven and task-driven projects, the instruction schema, global user preferences, and the underlying no-code tech stack.

> For the entity summary and general context, see [[Claude Projects Setup]].

## Projektstruktur (7 Projekte)

| Projekt | Typ | Rolle |
|---|---|---|
| Creative & Brand | Task-driven | Creative Director + Brand Strategist |
| Performance & Leben | Context-driven | Elite Performance Coach + Life Advisor |
| Texte & Kommunikation | Task-driven | Senior Communication Strategist |
| Research & Analyse | Task-driven | World-Class Analyst |
| Tech & Code | Task-driven | Senior Solution Architect (No-Code only) |
| Strategie & Business | Task-driven | Elite Stratege + Operator |
| Café | Context-driven | Gastro-Entrepreneur + Business Builder |

## Unterschied: Context-driven vs. Task-driven

| Typ | Projekte | Eigenschaft |
|---|---|---|
| **Context-driven** | Café, Performance & Leben | Akkumulieren Kontext über Zeit — persistenter State |
| **Task-driven** | Creative & Brand, Texte & Kommunikation, Research & Analyse, Tech & Code, Strategie & Business | Deliverable-orientiert — wenig State |

### Significance

The context-driven projects (**Café** and **Performance & Leben**) map directly to Oleg's two highest-continuity life domains:
- **Café** ↔ [[Café Berlin Partnership Hai]] — ongoing multi-month planning process requiring memory across sessions
- **Performance & Leben** ↔ [[Health Protocol Master]] — accumulated health tracking, metrics, and protocol evolution

The task-driven projects align with discrete workstreams: [[DoktorLib Automation Pipeline]] (Tech & Code, Strategie & Business), communications outputs (Texte & Kommunikation), brand work (Creative & Brand), and analysis (Research & Analyse).

## Schema je Projekt-Instruction

Each project instruction follows a standardized 6-part schema:

1. **Zweck** — Purpose of the project
2. **Kontext** — Background context (where relevant)
3. **Fokus** — Scope and focus areas
4. **Rolle** — Role assignment with explicit Mindset
5. **Output-Standard** — Deliverable quality and format requirements
6. **Nie** — Explicit prohibitions (never-do list)

This schema ensures consistency and prevents Claude from reverting to default behaviors (e.g., neutral summaries, consulting-speak) within each project context.

## Global User Preferences

These preferences apply **across all projects** regardless of input language:

| Preference | Detail |
|---|---|
| **Language** | Deutsch always — unabhängig von Input-Sprache |
| **Tone** | Direkt, präzise — kein Consulting-Sprech |
| **Deliverables** | Vollständig, sofort verwendbar |
| **No summaries** | Keine neutralen Zusammenfassungen |
| **No prompt echo** | Keine Einleitungssätze die den Prompt wiederholen |
| **Assumptions** | Immer explizit markieren |

### Alignment with Wiki Architecture

The preference for **sofort verwendbare Deliverables** (immediately usable outputs) directly mirrors the wiki's own design philosophy — entity and source pages are structured for immediate reference, not narrative reading. The **"Annahmen explizit markieren"** principle is reflected throughout the wiki in `⚠️ Assumption [A]` callouts (e.g., [[Cyprus Relocation Detail]]).

## Tech Stack (DoktorLib / No-Code)

The source lists the following tools under a combined heading:

| Tool | Wiki Page |
|---|---|
| [[Make]] | Automation middleware |
| [[Tally]] | Form builder |
| [[Notion]] | Project planning / knowledge management |
| [[Salesforce]] | CRM / data backbone |
| [[Dust Agent]] | AI agent platform |

> **Note:** This tech stack listing combines tools from [[DoktorLib Automation Pipeline]] (Make, Tally, Salesforce, Notion, Dust) with general knowledge management tools (Notion). The label "DoktorLib / No-Code" in the source suggests this stack serves both work (DoktorLib) and personal no-code projects.

## Cross-References to Other Wiki Pages

- **Claude Projects Setup** entity page previously noted unknown details (number of projects, specific use cases) — this source resolves all three unknowns: **7 projects**, specific roles defined per project, and use cases spanning creative, strategy, tech, performance, and café.
- **Café project** is context-driven → consistent with [[Café Berlin Partnership Hai]] being the top priority requiring continuous state
- **Performance & Leben** is context-driven → consistent with [[Health Protocol Master]] as an evolving long-term protocol
- **Tech & Code** role is "Senior Solution Architect (No-Code only)" → directly supports [[DoktorLib Automation Pipeline]] which is the active no-code build project

## Related Pages

- [[Claude Projects Setup]] — entity page (updated with full detail)
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — vault owner and Claude user
- [[Café Berlin Partnership Hai]] — mapped to Café (context-driven) project
- [[Health Protocol Master]] — mapped to Performance & Leben (context-driven) project
- [[DoktorLib Automation Pipeline]] — mapped to Tech & Code + Strategie & Business (task-driven) projects
- [[Make]] — no-code tool in stack
- [[Tally]] — no-code tool in stack
- [[Notion]] — no-code tool in stack
- [[Salesforce]] — no-code tool in stack
- [[Dust Agent]] — AI tool in stack
