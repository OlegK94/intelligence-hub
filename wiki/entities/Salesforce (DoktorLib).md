TAGS: [crm, data-backbone, automation, salesforce, doktorlib, lead-management]
SOURCES: ["raw/raw/_archiv/Work/DoktorLib Automation Pipeline.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: Salesforce — Long-Term Data Backbone für DoktorLib Automation Pipeline; speichert Lead/Opportunity-Daten; Quelle für Dust Agent (KEB-Generierung); Stage-Change triggert Dust-Automation

---

# Salesforce (DoktorLib Context)

## Überblick

**Salesforce** ist die **zentrale Datenbank und Long-Term Data Backbone** der [[DoktorLib Automation Pipeline]]. Es speichert alle strukturierten Daten über Leads (Arztpraxen) und koordiniert die nachgelagerten Automationen.

## Datenstruktur

### Lead / Opportunity-Objekt
| Feld | Quelle | Verwendung |
|---|---|---|
| Praxisname | Tally Intake Form | Lead-Identifikation |
| Praxistyp | Tally Intake Form | Segmentierung |
| Aktuelle Software | Tally Intake Form | Discovery-Kontext |
| IT-Infrastruktur | Tally Intake Form | Deployment-Planung |
| Demo-Notizen | Manuell (Demo-Call) | Sales-Context |
| Audit-Daten | Tally Audit Form | Technical Planning |
| Stage | Sales-Process | Lead → Opp → Contract → Deployment |

## Automatisierungen

### Phase 2: Lead/Opportunity-Erstellung
- Make schreibt neu erfasste Leads/Opportunities aus Tally-Form

### Phase 4: KEB-Generierung
- **Trigger:** Stage-Change (Vertragsunterzeichnung)
- **Action:** Dust Agent liest SF-Datensatz → generiert KEB automatisch
- **Quelle:** Alle Felder aus Phase 1–3 Tally-Forms + manuell eingegeben Discovery-Notes

## Abhängigkeiten

- [[DoktorLib Automation Pipeline]] — Parent-Projekt
- [[Make]] — schreibt zu SF (Phase 2 + 3)
- [[Dust Agent]] — liest aus SF (Phase 4)
- [[Notion]] — Read-Replica für Operator-Sichtbarkeit

---

*Entität erstellt: 2026-06-17*
