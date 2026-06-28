TAGS: [project-management, automation, notion, doktorlib, database, collaboration]
SOURCES: ["raw/raw/_archiv/Work/DoktorLib Automation Pipeline.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: Notion — Project-Management und Operator-Sichtbarkeits-System in DoktorLib Automation Pipeline; DB-Seite pro Praxis; synchronisiert mit Salesforce (Make Automation); Link-Übergabe an Deployment-Team statt Excel

---

# Notion (DoktorLib Context)

## Überblick

**Notion** ist die **Operator-sichtbare Projektplanung und Datenorganisation** in der [[DoktorLib Automation Pipeline]]. Es bietet eine benutzerfreundliche Ansicht auf die Salesforce-Daten.

## Struktur

### Database: Praxen / Leads
- **Seite pro Praxis:** Eine Notion-Seite pro Lead/Opportunity
- **Felder:** Mirror von Salesforce (Praxisname, Typ, Software, Audit-Daten, etc.)
- **Synchronisation:** Make schreibt initial (Intake Form → Notion); Salesforce bleibt Quelle

### Deployment-Vorlage
- **Zweck:** Standardisierte Ansicht für Deployment-Team
- **Inhalte:**
  - Praxis-Übersicht
  - Technische Anforderungen (aus Phase 1 + 3)
  - KEB (generiert von Dust Agent, Phase 4)
  - Deployment-Checkliste

## Vorteile gegenüber Excel

| Aspekt | Excel | Notion |
|---|---|---|
| **Echtzeit-Sync** | Manual | Automatisch (Make) |
| **Kollaboration** | Dateien-Sharing | Native Real-Time Collaboration |
| **Single Source of Truth** | Nein (viele Kopien) | Ja (Salesforce Quelle, Notion Replica) |
| **Deployment-Ansicht** | Manuelle KEB-Erstellung | Dust-generierte KEB in Notion |

## Abhängigkeiten

- [[DoktorLib Automation Pipeline]] — Parent-Projekt
- [[Make]] — schreibt zu Notion (Phase 2 + 3)
- [[Salesforce]] — Quelle-System (Notion ist Read-Replica)
- [[Dust Agent]] — KEB wird in Notion-Seite eingefügt

---

*Entität erstellt: 2026-06-17*
