TAGS: [automation, forms, intake, tally, dsgvo, tools, doktorlib]
SOURCES: ["raw/raw/_archiv/Work/DoktorLib Automation Pipeline.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: Tally — DSGVO-konformes Online-Formular-Tool; EU-Hosting (Belgien); verwendet in DoktorLib Automation Pipeline für Intake Form (Praxisbasisdaten) und Audit-Formular (IT-Partner)

---

# Tally

## Überblick

**Tally** ist ein Online-Formular-Builder-Tool, das in der [[DoktorLib Automation Pipeline]] für die **Intake-Form-Phase (Phase 1)** und **Audit-Formular-Phase (Phase 3)** eingesetzt wird.

## Eigenschaften

| Eigenschaft | Detail |
|---|---|
| **Typ** | Online-Formular-Builder |
| **DSGVO-Konformität** | ✅ Ja; EU-Hosting (Belgien) |
| **Integration** | Webhook-Support für Make Automation |
| **Kosten** | Free Tier + Paid Plans (TBD) |
| **Validierung** | Email-Format, Telefon-Format, bedingte Logik möglich |

## Einsatz in DoktorLib

### Phase 1: Intake Form
- **Zweck:** Strukturierte Datenerfassung vor Demo-Call
- **Felder:**
  - Praxistyp (Hausarzt, Facharzt, Zahnmedizin, etc.)
  - Fachrichtung
  - Aktuelle Software / EHR-System
  - Laboranbindungen
  - IT-Infrastruktur (On-Prem vs. Cloud)
  - Gerätelandschaft (RöKiste, Ultraschall, etc.)
- **Trigger:** Form Submission → Make Automation

### Phase 3: Audit-Formular
- **Zweck:** IT-Partner trägt detaillierte technische Anforderungen ein
- **Felder:** Hardware-Inventar, Netzwerk-Spec, etc. (TBD)
- **Trigger:** Form Submission → Make Automation → Salesforce + Notion

## Abhängigkeiten

- [[DoktorLib Automation Pipeline]] — Parent-Projekt
- [[Make]] — Nachgelagerte Automation
- [[Salesforce]] — Ziel-System für Daten
- [[Notion]] — Ziel-System für Daten

---

*Entität erstellt: 2026-06-17*
