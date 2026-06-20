---
title: Tally
type: concept
tags: [tool, form-builder, no-code, automation, dsgvo, doktorlib, tech-stack]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: No-Code-Formularbuilder, der in der DoktorLib Automation Pipeline zur DSGVO-konformen Datenerfassung von Arztpraxen eingesetzt wird; EU-gehostet in Belgien
---

# Tally

## Überblick

**Tally** ist ein No-Code-Formularbuilder, der in der [[DoktorLib Automation Pipeline]] als primäre Datenerfassungsschicht für eingehende Leads (Arztpraxen) verwendet wird. Im Pipeline-Prozess übernimmt er zwei unterschiedliche Formularfunktionen:

1. **Intake-Formular** — erfasst die Stammdaten der Praxis vom Lead *vor* dem Demo-Call
2. **IT-Audit-Formular** — ein separates Formular, das vom IT-Partner nach der Demo ausgefüllt wird

## Warum Tally gewählt wurde

- **DSGVO-konform:** Entspricht den Anforderungen der Datenschutz-Grundverordnung
- **EU-Hosting:** Server befinden sich in Belgien → erfüllt die EU-Anforderungen zur Datenhaltung
- **Kein Patientendatenrisiko:** Erfasst ausschließlich Praxisstrukturdaten (keine Patientenakten)
- **No-Code:** Ermöglicht die Formularerstellung ohne Entwicklerbeteiligung

## Rolle in der Pipeline

```
[TALLY Intake-Formular] → [MAKE] → Salesforce + Notion
[TALLY IT-Audit-Formular] → [MAKE] → Salesforce + Notion
```

Tally fungiert als **Eingabeschicht**; [[Make]] leitet die Daten nachgelagert weiter.

## Integrationspunkte

| Nachgelagertes Tool | Art der Verbindung |
|---|---|
| [[Make]] | Auslöser: Formularübermittlung startet Make-Szenario |
| [[Salesforce]] | Über Make: erstellt/aktualisiert Lead oder Opportunity |
| [[Notion]] | Über Make: erstellt neue Datenbankseite |

## Geplante Felder im Intake-Formular

(Stand Quelldokument — noch nicht finalisiert)
- Praxistyp (practice type)
- Fachrichtung (medical specialty)
- Aktuelle Software (current software)
- Labore (labs)
- IT-Infrastruktur
- Gerätelandschaft (device landscape)

## Verwandte Seiten

- [[DoktorLib Automation Pipeline]] — primärer Nutzungskontext
- [[DoktorLib Automation Pipeline Source Detail|DoktorLib Automation Pipeline Quelldetail]] — vollständige Quelle
- [[Make]] — Automatisierungs-Middleware, ausgelöst durch Tally
- [[Salesforce]] — nachgelagertes Datenziel
- [[Notion]] — nachgelagerte Projektebene
- [[DoktorLib]] — Organisation, die Tally verwendet