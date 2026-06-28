TAGS: [claude, setup, tools, ai-infrastructure, projects, task-driven, context-driven, preferences, doktorlib]
SOURCES: ["raw/raw/_archiv/legacy-numbered-folders/03-Tech-Setup/Claude Projects Setup.md"]
CREATED: 2026-06-07
UPDATED: 2026-06-14
SUMMARY: 7-Projekt-Struktur für Claude Assistants mit klarer Rollen-Definition (Creative & Brand, Performance & Leben, Texte & Kommunikation, Research & Analyse, Tech & Code, Strategie & Business, Café); Unterscheidung Context-driven vs. Task-driven; Global User Preferences (Deutsch, direkt, Deliverables-fokussiert); Tech Stack No-Code (Make, Tally, Notion, Salesforce, Dust)

---

# 🤖 Claude Projects Setup

## Überblick

Dieses Quelldokument dokumentiert die **7-Projekt-Struktur** für Claude Assistants, die als zentrale Intelligenz-Hub Systeme für verschiedene Geschäfts- und persönliche Domänen fungieren. Die Struktur basiert auf der **Karpathy LLM Wiki Pattern** — ein bewährter Ansatz zur Verwaltung spezialisierter Assistants mit klaren Rollen, Kontextanforderungen und Output-Standards.

## Projektstruktur (7 Projekte)

| Projekt | Typ | Rolle & Mindset |
|---|---|---|
| **Creative & Brand** | Task-driven | Creative Director + Brand Strategist; visuell + narrativ fokussiert |
| **Performance & Leben** | Context-driven | Elite Performance Coach + Life Advisor; akkumuliert Kontext über Zeit |
| **Texte & Kommunikation** | Task-driven | Senior Communication Strategist; Copywriting, Content, Messaging |
| **Research & Analyse** | Task-driven | World-Class Analyst; Datenquellen, Synthesen, Evidenz-basiert |
| **Tech & Code** | Task-driven | Senior Solution Architect (No-Code only); Automation, Workflows |
| **Strategie & Business** | Task-driven | Elite Stratege + Operator; Geschäftsmodell, GTM, Finanzen |
| **Café** | Context-driven | Gastro-Entrepreneur + Business Builder; Kontext über Monate |

## Context-driven vs. Task-driven

### Context-driven Projekte
**Merkmale:**
- Akkumulieren Kontext über längere Zeit
- Verfügen über umfassende Hintergrund-Information
- Continuity over Sessions ist kritisch
- State = notwendig und wertvoll

**Projekte:**
- **Performance & Leben** — Persönliche Optimierung, Health Protocol, Training-Logs, Biometrics
- **Café** — Unternehmens-Spezifika, Finanz-Historie, Stakeholder-Dynamiken, Markt-Evolution

**Best Practice:**
- Regelmäßige Context-Dumps (wöchentlich oder monatlich)
- [[MOC Performance & Leben]] + [[Performance-Übersicht]] als aktuelle Baselines
- Café-Kontext in separaten, verwalteten Files (z.B. Geschäftsmodell, Supplier-Database)

### Task-driven Projekte
**Merkmale:**
- Deliverable-fokussiert (spezifische Output pro Session)
- Wenig State-Akkumulation erforderlich
- Session-Isolation ist OK
- Context = Prompt + Auftragsbrief

**Projekte:**
- **Creative & Brand** — einzelne Brand-Kampagnen, Logo-Iterationen
- **Texte & Kommunikation** — einzelne Copy-Pieces, Content-Artikel
- **Research & Analyse** — einzelne Recherche-Aufträge, Benchmarks
- **Tech & Code** — einzelne Automation-Aufträge, No-Code-Flows
- **Strategie & Business** — einzelne Business-Cases, GTM-Pläne

**Best Practice:**
- Explizite Aufträge mit vollständigen Kontext-Files
- Deliverables sind selbständig (keine Abhängigkeit von Session-State)
- Re-Run ist jederzeit möglich

## Instruction Schema (je Projekt)

Jedes Projekt folgt einem **standardisierten 6-teil Instruction-Schema**:

```
1. ZWECK
   What ist dieser Assistant für? (1–2 Sätze)

2. KONTEXT
   Wo relevant: Business Context, User State, External Info
   (leer, wenn Task-driven und Kontext im Prompt gegeben)

3. FOKUS
   Was genau soll dieser Assistant NICHT tun?
   Was ist the Primary Outcome?

4. ROLLE (mit Mindset)
   Archetype, Tone, Decision-Making-Style
   z.B. "Du bist ein World-Class Analyst mit obsessivem Fokus auf Evidenz"

5. OUTPUT-STANDARD
   Format (Markdown, Excel, JSON), Struktur, Länge-Guideline
   z.B. "Alle Analysen strukturiert als [1] Executive Summary (5 Bullet Points) + [2] Detailed Findings + [3] Source References"

6. NIEMALS
   Explizite Verbote — was dieser Assistant niemals tun sollte
   z.B. "NIEMALS spekulativ antworten ohne Evidenz"
```

## Global User Preferences (alle Projekte)

Diese Preferences gelten für **alle 7 Projekte** und setzen globale Standards:

### Sprache
- ✅ **Deutsch always** — unabhängig von Input-Sprache oder Kontext
- Etablierte englische Fachbegriffe/Eigennamen bleiben englisch (z.B. Performance Coffee, Zone 2, NSDR, COGS, Hyrox, Blueprint, EFSA)

### Kommunikation
- ✅ **Direkt, präzise** — kein Consulting-Sprech, keine Weichspüler
- ✅ **Vollständige, sofort verwendbare Deliverables** — nicht „hier sind Ideen zu...", sondern „hier ist der fertige [Ding]"
- ❌ **Keine neutralen Zusammenfassungen** — Nehmt Positionen ein
- ❌ **Keine Einleitungssätze die den Prompt wiederholen** — Startet mit Output
- ✅ **Annahmen immer explizit markiert** — z.B. „⚠️ Annahme: Kaffee-Rohstoffe verfügbar in EU" oder „Anmerkung: TDEE-Schätzung ±10% Unsicherheit"

### Struktur
- Markdown-Frontmatter auf relevanten Output (YAML: title, type, tags, sources, created, updated, summary)
- Wikilinks [[Name]] wherever relevant
- Numbered lists (1/2/3) für Sequenzen, Bullet Points für Attribute

---

## Tech Stack (DoktorLib / No-Code)

Die 7 Projekte nutzen folgende **No-Code-Technologie-Basis**:

| Tool | Funktion | Kontext |
|---|---|---|
| **Make** (ehemals Integromat) | Workflow-Automation, API-Orchestrierung | Task-driven Automation |
| **Tally** | No-Code Form Builder | Customer-facing Datenerfassung (z.B. Performance Intake Forms) |
| **Notion** | CMS, Database, Project Management | Knowledge Base, MOCs, Intake Forms |
| **Salesforce** | CRM | Kundenverwaltung (falls B2B/DTC skaliert) |
| **Dust** | Claude-basierte Process Automation | Intelligente Workflows für Text-Heavy Prozesse |

**Philosophie:** Zero Backend Code — alles konfigurativ gelöst durch No-Code-Plattformen.

---

## Karpathy LLM Wiki Pattern

Dieses Setup folgt dem **Karpathy LLM Wiki Pattern** (Andrej Karpathy, OpenAI), der sich für persönliche KI-Assistants bewährt hat:

1. **Spezialisierte Projekte** mit klarer Rollen-Definition (statt generischer "Super-Assistant")
2. **Explizite Instructions** mit 6-teil Schema (Zweck, Kontext, Fokus, Rolle, Output, Niemals)
3. **Markdown + Wikilinks** als Interfacing-Sprache (Human-Lesbar, Versions-kontrollierbar)
4. **Regelmäßige Updates** des Context-Material (Weekly Dumps für Context-driven Projekte)
5. **Deliverable-Fokus** (nicht Exploration oder Brainstorm-Sessions)

---

## Verwandte Seiten

- [[MOC Tech & Setup]] — Technologie-Stack und Infrastruktur-Übersicht
- [[Performance & Leben (Claude Project)]] — Context-driven Project Detail
- [[Café (Claude Project)]] — Context-driven Project Detail
- [[Creative & Brand (Claude Project)]] — Task-driven Project Detail
- [[DoktorLib]] — No-Code-Framework und Toolset
- [[Global User Preferences]] — Detaillierte Kommunikations-Standards
