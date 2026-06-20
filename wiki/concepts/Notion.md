---
title: Notion
type: concept
tags: [tool, project-management, database, doktorlib, tech-stack, automation]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Projektplanungs- und Kollaborationstool, das als sekundäre Datenschicht in der DoktorLib-Pipeline eingesetzt wird — empfängt synchronisierte Daten aus Make und stellt die deployment-seitige Ansicht bereit, die die Excel-Übergabe ersetzt
---

# Notion

## Überblick

**Notion** ist ein flexibles All-in-one-Workspace-Tool für Notizen, Datenbanken, Wikis und Projektmanagement. In der [[DoktorLib Automation Pipeline]] fungiert Notion als **sekundäre Datenschicht** und **deployment-seitige Ansicht** — es ergänzt [[Salesforce]] (das primäre Datenfundament) durch eine zugänglichere Oberfläche für das Deployment-Team.

## Rolle in der DoktorLib-Pipeline

### Pipeline-Position

```
[TALLY] → [MAKE] → [NOTION DB] (synchronisiert parallel zu Salesforce)
                        ↓
              Deployment-Team greift auf Notion-Link zu
              (ersetzt Excel-Übergabe)
```

### Konkrete Einsatzbereiche

| Phase | Rolle von Notion |
|---|---|
| Phase 2 (Make-Automatisierung) | Empfängt Tally-Intake-Daten — neue DB-Seite wird pro Kunde angelegt |
| IT-Audit (Make) | IT-Audit-Daten werden mit bestehender Notion-Seite synchronisiert |
| Phase 4 (Deployment-Übergabe) | Deployment-spezifisches Notion-Template wird gebaut; Link wird statt Excel geteilt |

## Designentscheidung: Notion als Sekundär-, Salesforce als Primärsystem

Das Quelldokument positioniert Notion explizit als **Projektplanung**, während [[Salesforce]] der **Daten-Backbone** ist. Das bedeutet:
- Notion ist die *menschenlesbare, deployment-seitige* Schicht
- Salesforce ist die *System-of-Record-, integrationsseitige* Schicht
- Daten fließen von Tally → Make → **beide** Systeme parallel

## Vorteil bei der Deployment-Übergabe

Das zentrale Ergebnis des Notion-Einsatzes für das Deployment:
- **Vorher:** Das Deployment-Team erhält eine Excel-Datei (keine einheitliche Wahrheitsquelle, Versionierungsprobleme)
- **Nachher:** Das Deployment-Team erhält einen **Notion-Link** (stets aktuell, mit Live-Daten verknüpft)

## Build-Status (Offene Punkte)

- [ ] Notion-Template für Deployment-Ansicht bauen (build deployment view template)
- [ ] Link-Übergabe definieren (define link handover process)

## Verwandte Seiten

- [[DoktorLib Automation Pipeline]] — Pipeline-Kontext
- [[DoktorLib Automation Pipeline Source Detail|DoktorLib Automation Pipeline Quelldokument]] — vollständige Quelle
- [[Make]] — Automatisierungsschicht, die in Notion schreibt
- [[Salesforce]] — primärer Daten-Backbone (Notion ist sekundär)
- [[Tally]] — vorgelagerter Eingabe-Datenlieferant
- [[DoktorLib]] — Organisationskontext