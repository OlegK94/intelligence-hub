---
title: DoktorLib Automatisierungs-Pipeline
type: entity
tags: [automation, saas, workflow, doktorlib, project, tally, make, salesforce, notion, dust-agent, aktiv, onboarding, lead-management]
sources: ["raw/00-MOC/🏠 Home.md", "raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-13
updated: 2026-06-15
summary: Aktives Automatisierungsprojekt bei DoktorLib — End-to-End-Pipeline (Tally → Make → Salesforce/Notion → Dust Agent) zur Automatisierung von Inbound-Lead-Discovery & Onboarding für Arztpraxen, ersetzt das manuelle Excel-KEB; Priorität 2 Stand Juni 2026
---

# DoktorLib Automatisierungs-Pipeline

## Überblick

Die DoktorLib Automatisierungs-Pipeline ist ein aktives Arbeitsprojekt ([[Oleg Personal Context|Olegs]] Priorität 2 Stand Juni 2026) zur Automatisierung des End-to-End-**Discovery & Onboarding-Flows** für Inbound-Leads (Arztpraxen) bei [[DoktorLib]]. Die Pipeline kombiniert No-Code- und KI-Tools, um manuelle Dateneingabe zu eliminieren und den bestehenden Excel-basierten KEB (Kundenerfassungsbogen) zu ersetzen.

> Für die vollständige Architektur, Build-Phasen und Quellendetails siehe [[DoktorLib Automation Pipeline Source Detail]].

## Projektstatus

- **Status:** 🟡 In Bau (In Entwicklung)
- **Priorität:** 2 von 6 aktiven Prioritäten
- **Nächster Schritt:** Zuerst das Tally-Intake-Formular bauen (der Input definiert den Output des Dust Agents)
- **Quelle erstellt:** 2026-05-08

## Das zu lösende Problem

| Problem | Detail |
|---|---|
| Späte Datenerfassung | Praxis-Stammdaten werden erst beim Demo-Call erfasst — zu spät |
| Unstrukturierte Discovery-Notizen | Freitext in Salesforce → nicht skalierbar |
| Manueller KEB | Excel-basierter Kundenerfassungsbogen → fehleranfällig, fragmentiert |
| Keine einheitliche Datenquelle | Deployment erhält Excel → keine verknüpfte Übergabe |

## Technologie-Stack

| Tool | Rolle |
|---|---|
| [[Tally]] | Formular-Builder — Intake-Formular (vor Demo) + IT-Audit-Formular |
| [[Make]] | Automatisierungs-Middleware — leitet Daten von Tally an SF und Notion weiter |
| [[Salesforce]] | Langfristiges Daten-Backbone — primäres System of Record |
| [[Notion]] | Projektplanungs-DB — sekundäre Ebene für die Deployment-Ansicht |
| [[Dust Agent]] | KI-Agent — liest Salesforce-Daten, generiert KEB automatisch |

> ⚠️ **Korrektur gegenüber früherer Version:** Die ursprüngliche Entity-Seite beschrieb Tally und Dust als alternative Optionen. Das Quelldokument (siehe [[DoktorLib Automation Pipeline Source Detail]]) stellt klar, dass **beide** in komplementären Phasen eingesetzt werden — Tally zur Datenerfassung (Phase 1), Dust zur KEB-Generierung (Phase 3).

## Ziel-Flow

```
Inbound Lead
    ↓
[TALLY] Intake Form (vor Demo)
    ↓
[MAKE] → [SALESFORCE] + [NOTION DB]
    ↓
Demo-Call (Validierung only)
    ↓
IT-Partner → [TALLY] Audit Form
    ↓
[MAKE] → Salesforce + Notion
    ↓
Vertragsunterzeichnung
    ↓
[DUST AGENT] → KEB automatisch generiert
    ↓
Deployment erhält Notion-Link (kein Excel)
```

## Build-Phasen

1. **Phase 1 — Tally-Intake-Formular:** Felder definieren (Praxistyp, Fachrichtung, Software, Labore, IT-Infrastruktur, Gerätelandschaft), DSGVO-konformes Setup
2. **Phase 2 — Make-Automatisierung:** Trigger bei Tally-Einreichung → SF Lead/Opportunity + Notion-DB-Seite erstellen, mit Fehlerbehandlung
3. **Phase 3 — Dust Agent (KEB-Generator):** Prompt-Design, SF-Dateneingabestruktur, KEB-Ausgabeformat, Trigger bei Vertragsunterzeichnung
4. **Phase 4 — Deployment-Übergabe:** Notion-Vorlage für die Deployment-Ansicht, linkbasierte Übergabe ersetzt Excel

## Getroffene Grundsatzentscheidungen

- **Salesforce = langfristiges Daten-Backbone** (nicht nur Notion)
- **Tally = DSGVO-konform** für Praxisstruktur-Daten (EU-Hosting Belgien ✅; keine Patientendaten)
- **Dust = interne KI-Plattform** zur KEB-Generierung
- **Excel-KEB = vollständig ersetzt** (nicht optimiert)

## Kontext

Dieses Projekt ist Teil von [[Oleg Personal Context|Olegs]] übergeordneter Tätigkeit bei [[DoktorLib]] im B2B-SaaS-Vertrieb für Arztpraxen. Die Automatisierung wirkt sich direkt auf den Übergabeprozess von Sales → Deployment aus und reduziert den manuellen Aufwand in jeder Phase.

Der DSGVO-Hinweis zu [[Tally]] ist wesentlich: Die Erhebung von Praxisstruktur-Daten (Praxisstruktur, keine Patientendaten) ist unter der DSGVO mit entsprechender Formular-Kennzeichnung zulässig. Das EU-Hosting in Belgien erfüllt die Anforderungen an den Datenspeicherort.

## Verwandte Seiten

- [[DoktorLib Automation Pipeline Source Detail]] — vollständiges Quelldokument mit Architektur
- [[DoktorLib]] — übergeordnetes Unternehmen
- [[Oleg Personal Context]] — Projektverantwortlicher
- [[MOC Strategie und Business]] — strategische MOC
- [[MOC Tech und Setup]] — technischer Stack-Kontext
- [[Tally]] — Konzept des Formular-Builder-Tools
- [[Make]] — Konzept der Automatisierungs-Middleware
- [[Salesforce]] — CRM-Backbone-Konzept
- [[Notion]] — Projektplanungsebene
- [[Dust Agent]] — KI-KEB-Generator
- [[Kundenerfassungsbogen]] — zu automatisierendes Artefakt