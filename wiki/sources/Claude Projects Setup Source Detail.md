---
title: Claude Projects Setup Quelldokument-Detail
type: source
tags: [claude, anthropic, AI, setup, tools, productivity, projects, LLM, deutsch, no-code, make, tally, notion, salesforce, dust]
sources: ["raw/Privat/Tech/Claude Projects Setup.md"]
created: 2026-06-07
updated: 2026-06-07
summary: Quelldokument mit Details zu Olegs 7 Claude-KI-Projekten — Struktur, Rollen, Unterscheidung zwischen kontext- und aufgabengetriebenen Projekten, Instruction-Schema, globale Nutzerpräferenzen und No-Code-Tech-Stack (Make, Tally, Notion, Salesforce, Dust)
---

# Claude Projects Setup — Quelldokument-Detail

## Überblick

Dieses Quelldokument (Status: Aktiv, 7 Projekte, erstellt 2026-06-07) erfasst die vollständige Konfiguration von [[Oleg Personal Context|Olegs]] [[Claude Projects Setup]] innerhalb der Claude-KI-Plattform von Anthropic. Es definiert die Projektstruktur, die Unterscheidung zwischen kontext- und aufgabengetriebenen Projekten, das Instruction-Schema, globale Nutzerpräferenzen sowie den zugrundeliegenden No-Code-Tech-Stack.

> Für die Entitätszusammenfassung und den allgemeinen Kontext siehe [[Claude Projects Setup]].

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

### Bedeutung

Die kontext-getriebenen Projekte (**Café** und **Performance & Leben**) entsprechen direkt Olegs zwei Lebensbereichen mit der höchsten Kontinuität:
- **Café** ↔ [[Café Berlin Partnership Hai]] — laufender, mehrmonatiger Planungsprozess, der sitzungsübergreifendes Gedächtnis erfordert
- **Performance & Leben** ↔ [[Health Protocol Master]] — akkumuliertes Gesundheits-Tracking, Metriken und Protokollentwicklung

Die aufgabengetriebenen Projekte entsprechen klar abgegrenzten Arbeitsbereichen: [[DoktorLib Automation Pipeline]] (Tech & Code, Strategie & Business), Kommunikations-Outputs (Texte & Kommunikation), Markenarbeit (Creative & Brand) und Analysen (Research & Analyse).

## Schema je Projekt-Instruction

Jede Projekt-Instruction folgt einem standardisierten 6-teiligen Schema:

1. **Zweck** — Zweck des Projekts
2. **Kontext** — Hintergrundinformationen (wo relevant)
3. **Fokus** — Umfang und Schwerpunktbereiche
4. **Rolle** — Rollenzuweisung mit explizitem Mindset
5. **Output-Standard** — Anforderungen an Qualität und Format der Deliverables
6. **Nie** — Explizite Verbote (Never-do-Liste)

Dieses Schema sorgt für Konsistenz und verhindert, dass Claude innerhalb des jeweiligen Projektkontexts auf Standardverhalten zurückfällt (z. B. neutrale Zusammenfassungen, Consulting-Sprech).

## Globale Nutzerpräferenzen

Diese Präferenzen gelten **projektübergreifend**, unabhängig von der Eingabesprache:

| Präferenz | Detail |
|---|---|
| **Sprache** | Deutsch always — unabhängig von Input-Sprache |
| **Ton** | Direkt, präzise — kein Consulting-Sprech |
| **Deliverables** | Vollständig, sofort verwendbar |
| **Keine Zusammenfassungen** | Keine neutralen Zusammenfassungen |
| **Kein Prompt-Echo** | Keine Einleitungssätze die den Prompt wiederholen |
| **Annahmen** | Immer explizit markieren |

### Übereinstimmung mit der Wiki-Architektur

Die Präferenz für **sofort verwendbare Deliverables** spiegelt direkt die eigene Designphilosophie des Wikis wider — Entitäts- und Quellseiten sind für die unmittelbare Nutzung strukturiert, nicht für narratives Lesen. Das Prinzip **„Annahmen explizit markieren"** findet sich im gesamten Wiki in `⚠️ Assumption [A]`-Callouts (z. B. [[Cyprus Relocation Detail]]).

## Tech-Stack (DoktorLib / No-Code)

Die Quelle listet folgende Tools unter einer gemeinsamen Überschrift:

| Tool | Wiki-Seite |
|---|---|
| [[Make]] | Automation-Middleware |
| [[Tally]] | Formular-Builder |
| [[Notion]] | Projektplanung / Wissensmanagement |
| [[Salesforce]] | CRM / Daten-Backbone |
| [[Dust Agent]] | KI-Agenten-Plattform |

> **Hinweis:** Diese Tech-Stack-Auflistung kombiniert Tools aus [[DoktorLib Automation Pipeline]] (Make, Tally, Salesforce, Notion, Dust) mit allgemeinen Wissensmanagement-Tools (Notion). Die Bezeichnung „DoktorLib / No-Code" in der Quelle deutet darauf hin, dass dieser Stack sowohl beruflichen (DoktorLib) als auch persönlichen No-Code-Projekten dient.

## Querverweise zu anderen Wiki-Seiten

- Die Entitätsseite **Claude Projects Setup** hatte zuvor unbekannte Details vermerkt (Anzahl der Projekte, spezifische Anwendungsfälle) — dieses Quelldokument löst alle drei offenen Punkte auf: **7 Projekte**, spezifisch definierte Rollen je Projekt und Anwendungsfälle in den Bereichen Creative, Strategie, Tech, Performance und Café.
- Das **Café-Projekt** ist context-driven → konsistent damit, dass [[Café Berlin Partnership Hai]] die höchste Priorität mit Bedarf an kontinuierlichem State ist
- **Performance & Leben** ist context-driven → konsistent mit [[Health Protocol Master]] als sich entwickelndem Langzeitprotokoll
- Die Rolle in **Tech & Code** lautet „Senior Solution Architect (No-Code only)" → unterstützt direkt [[DoktorLib Automation Pipeline]] als aktives No-Code-Bauprojekt

## Verwandte Seiten

- [[Claude Projects Setup]] — Entitätsseite (mit vollständigen Details aktualisiert)
- [[MOC Tech und Setup]] — übergeordnete MOC
- [[Oleg Personal Context]] — Vault-Inhaber und Claude-Nutzer
- [[Café Berlin Partnership Hai]] — zugeordnet zum Café (context-driven) Projekt
- [[Health Protocol Master]] — zugeordnet zum Performance & Leben (context-driven) Projekt
- [[DoktorLib Automation Pipeline]] — zugeordnet zu Tech & Code + Strategie & Business (task-driven) Projekten
- [[Make]] — No-Code-Tool im Stack
- [[Tally]] — No-Code-Tool im Stack
- [[Notion]] — No-Code-Tool im Stack
- [[Salesforce]] — No-Code-Tool im Stack
- [[Dust Agent]] — KI-Tool im Stack