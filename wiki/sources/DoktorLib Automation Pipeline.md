TAGS: [doktorlib, automation, tech, discovery, onboarding, leads, arztpraxen, tally, make, salesforce, notion, dust, keb, integration]
SOURCES: ["raw/raw/_archiv/Work/DoktorLib Automation Pipeline.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: Automation Pipeline für Discovery & Onboarding-Flow von Inbound-Leads (Arztpraxen); Stack: Tally (Intake Form), Make (Workflow Automation), Salesforce (Data Backbone), Notion (Projektplanung), Dust Agent (KEB-Generator); Ist-Zustand Problemanalyse (manuelle KEB Excel, späte Datenerfassung); Ziel-Architektur 4 Build-Phasen; entscheidend: Tally-Formstruktur vor Dust-Prompt-Entwicklung

---

# DoktorLib Automation Pipeline

## Überblick

Dieses Quelldokument beschreibt die **Automatisierung des Discovery & Onboarding-Flows** für Inbound-Leads (Arztpraxen) bei DoktorLib. Das Ziel ist maximale Automatisierung mit **minimaler manueller Dateneingabe**, wobei **Salesforce als Long-Term Data Backbone** dient.

> Verbindung: [[MOC Tech & Setup]] | [[MOC Strategie & Business]]

---

## Problem-Analyse (Ist-Zustand)

| Problem | Impact | Lösung |
|---|---|---|
| Praxisbasisdaten zu spät erfasst (erst im Demo-Call) | Discovery-Phase verliert Zeit; fehlerhafte Annahmen | Tally Intake Form vor Demo |
| Discovery Notes als Freitext in Salesforce | Nicht skalierbar; schwer zu standardisieren | Strukturierte Form-Felder |
| KEB (Kundenerfassungsbogen) = manuell Excel | Fehleranfällig; redundante Dateneingabe | Dust Agent Auto-Generierung aus SF |
| Deployment erhält Excel-Datei | Keine Single Source of Truth; Synchronisations-Fehler | Notion-Link-Übergabe (statt Excel) |

---

## Ziel-Architektur (4 Phasen)

```
Inbound Lead
    ↓
[PHASE 1] TALLY Intake Form (vor Demo)
    ├─ Praxistyp, Fachrichtung
    ├─ Aktuelle Software, Labore
    └─ IT-Infrastruktur, Gerätelandschaft
    ↓
[PHASE 2] MAKE Automation
    ├─ Trigger: Tally Form Submission
    ├─ Aktion 1: Salesforce Lead/Opportunity + Felder
    └─ Aktion 2: Notion DB-Seite + Synchronisation
    ↓
Demo-Call (nur Validierung + Discovery Notes manuell in SF)
    ↓
IT-Partner → [PHASE 3] TALLY Audit-Formular (separates)
    ↓
[MAKE] Automation: Audit-Daten → Salesforce + Notion
    ↓
Vertragsunterzeichnung
    ↓
[PHASE 4] DUST AGENT: SF-Daten lesen → KEB automatisch generieren
    ├─ Input: Salesforce-Struktur (definiert in Phase 1–3)
    └─ Output: KEB im Standard-Format
    ↓
Deployment erhält Notion-Link (kein Excel mehr)
```

---

## Stack-Komponenten

### 1. **Tally** — Intake-Formular
- **Zweck:** Strukturierte Datenerfassung vor dem Demo
- **DSGVO:** EU-Hosting (Belgien) ✅
- **Felder (Phase 1 zu definieren):**
  - Praxistyp (Hausarzt, Facharzt, Zahnmedizin, etc.)
  - Fachrichtung
  - Aktuelle Software / EHR-System
  - Laboranbindungen
  - IT-Infrastruktur (On-Prem vs. Cloud)
  - Gerätelandschaft (RöKiste, Ultraschall, etc.)

**Abhängigkeit:** Phase 1 MUSS Formstruktur definieren, bevor Dust-Prompt (Phase 4) geschrieben wird.

### 2. **Make** — Workflow Automation
- **Trigger:** Tally Form Submission
- **Aktion 1:** Salesforce
  - Lead oder Opportunity erstellen
  - Felder befüllen (Praxistyp, Software, etc.)
- **Aktion 2:** Notion
  - Neue DB-Seite erstellen
  - Felder synchronisieren (Bidirektional?)
- **Error Handling:** Benachrichtigungs-Mechanismus bei Fehler

### 3. **Salesforce** — Data Backbone
- **Zweck:** Long-Term-System für Lead/Opportunity-Verwaltung
- **Struktur:** Lead → Demo → Opportunity → Contract → Deployment
- **Integration:** Make schreibt zu SF; Dust liest aus SF
- **Stage-Change:** Trigger für Dust-Agent (Vertragsunterzeichnung)

### 4. **Notion** — Projektplanung
- **Zweck:** Operator-sichtbare Projektplanung
- **Struktur:** DB-Seiten (eine pro Lead/Praxis)
- **Synchronisation:** Make schreibt initial; SF bleibt Quelle
- **Deployment-Ansicht:** Vorlage für Handover an Deployment-Team

### 5. **Dust Agent** — KEB-Generator
- **Zweck:** Automatische Generierung des Kundenerfassungsbogens (KEB)
- **Input:** Salesforce-Datensätze (alle Felder aus Phase 1–3)
- **Output:** Strukturierter KEB (Feldliste TBD)
- **Trigger:** Vertragsunterzeichnung (SF Stage-Change oder manuell)
- **Abhängigkeit:** Dust-Prompt-Struktur hängt vollständig von Phase-1-Tally-Formstruktur ab

---

## Build-Phasen (Detailliert)

### Phase 1: Tally Intake Form

**Deliverables:**
- [ ] Feldliste finalisieren (Praxistyp, Software, etc.)
- [ ] Tally-Formular bauen + Test
- [ ] DSGVO-Beschriftung prüfen
- [ ] Bestätigungsmail-Template
- [ ] Webhook-Setup für Make (Tally → Make Trigger)

**Entscheidung erforderlich:**
- Welche Felder sind **Pflicht** vs. Optional?
- Dropdown-Listen (vordefinierte Werte) oder Freitexte?
- Bedingte Logik (z.B. „Falls Zahnmedizin → weitere Zahnmedizin-spezifische Felder")?

### Phase 2: Make Automation

**Deliverables:**
- [ ] Make-Scenario bauen (Tally Trigger)
- [ ] Salesforce-Aktion (Lead/Opportunity Create + Felder mappen)
- [ ] Notion-Aktion (DB-Seite Create + Felder mappen)
- [ ] Error Handling (Slack / Email Notification)
- [ ] Test mit Dummy-Submissionen

**Entscheidung erforderlich:**
- Salesforce: Lead oder direkt Opportunity?
- Notion: Bidirektionale Sync oder nur One-Way (SF → Notion)?
- Welche Felder in Notion-Ansicht sichtbar?

### Phase 3: IT-Partner Audit-Formular + Make Extension

**Deliverables:**
- [ ] Separates Tally Audit-Formular für IT-Partner
- [ ] Make-Scenario erweitern: Audit-Daten → SF + Notion
- [ ] Audit-Felder definieren (Hardware-Inventar, Netzwerk-Spec, etc.)
- [ ] Zugriffs-Verwaltung (IT-Partner erhält Audit-Form-Link)

### Phase 4: Dust Agent KEB-Generator

**Deliverables:**
- [ ] Dust-Agent-Prompt schreiben
  - Input: SF-Datenstruktur (alle Felder aus Phase 1–3)
  - Output: KEB-Feldliste finalisieren
- [ ] KEB-Template bauen (Standard-Format)
- [ ] Trigger-Logik (SF Stage-Change vs. manuell)
- [ ] Test mit echten SF-Datensätzen

**Abhängigkeit:** Dust-Prompt kann ERST geschrieben werden, wenn Phase 1–3 Feldstrukturen final sind.

---

## Kritische Entscheidung

> **Frage:** Tally-Formstruktur zuerst bauen ODER Dust Agent Prompt schreiben?

**Antwort: TALLY ZUERST**

Begründung:
1. **Input definiert Output** — Ohne Tally-Feldstruktur ist Dust-Prompt sinnlos
2. **Waterfall-Abhängigkeit:** Phase 1 → Phase 2 → Phase 3 → Phase 4
3. **Tally-Felder = Dust-Prompt Input-Spec**

**Empfehlung:**
1. Phase 1 finalisieren (Tally-Felder, Form-Struktur)
2. Phase 2 aufbauen (Make Automation)
3. Phase 3 parallel starten (IT-Partner Audit-Form)
4. Phase 4 erst beginnen, wenn Phase 1–3 Feldstrukturen final sind

---

## Weitere Überlegungen

### Datenqualität
- Tally-Validierung (z.B. E-Mail-Format, Telefon-Format) direkt im Formular
- Make Error Handling bei Duplikaten (Praxis existiert bereits in SF?)
- Notion-Ansicht: Visualisierung von Daten-Gaps (wo Felder NULL sind)

### Skalierbarkeit
- Wie viele Leads/Monat erwartet?
- Braucht Make eine Rate-Limiting-Strategie?
- Sollte Dust-Agent Batch-Generierungen unterstützen (KEB für mehrere Praxen)?

### Single Source of Truth
- Aktuell: Salesforce = SSOT
- Notion ist Read-Replica (für Operator-Sichtbarkeit)
- Bei Konflikten: SF gewinnt (Notion wird nicht zurückgeschrieben)

---

## Verknüpfungen

- [[MOC Tech & Setup]] — Übergeordneter Tech-Index
- [[Tally]] — Formular-Tool-Entität (zu erstellen)
- [[Make]] — Workflow-Automation-Tool-Entität (zu erstellen)
- [[Salesforce]] — CRM-System-Entität (zu erstellen)
- [[Notion]] — Project-Management-Tool-Entität (zu erstellen)
- [[Dust Agent]] — KI-Plattform-Entität (zu erstellen)
- [[KEB — Kundenerfassungsbogen]] — Deliverable-Entität (zu erstellen)

---

*Quelldokument erstellt: 2026-06-17*
*Status: Architektur-Design Phase; bereit für Phase-1-Umsetzung*
