TAGS: [doctolib, automation, tech, workflow, tally, make, salesforce, notion, dust-agent, no-code, lead-generation, inbound, sales-ops]
SOURCES: ["raw/raw/_archiv/Work/Doctolib Automation Pipeline.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: DoktorLib Automation Pipeline für Inbound-Lead-Discovery & Onboarding; Tally Intake Form (praxisbasisdaten) → Make Automation (Trigger: Form Submission) → Salesforce (Lead/Opportunity erstellen) + Notion (Projektplanung) → Dust Agent KEB-Generator (nach Vertragsunterzeichnung); Ziel: minimale manuelle Dateneingabe, Single Source of Truth in Salesforce, automatische Kundenerfassungsbogen (KEB)-Generierung; Status: In Bau; Abhängigkeiten: Tally-Formstruktur → Make Flows → Dust Prompt-Definition; nächste Schritte: Phase 1 (Tally-Formular) prioritär vor Phase 3 (Dust Agent).
summary: Automation Pipeline für Doctolib Arztpraxen-Onboarding; Tally → Make → Salesforce + Notion → Dust KEB-Generator; minimale manuelle Dateneingabe; Single Source of Truth in Salesforce; Status: In Bau; Phasen: 1 (Tally Form), 2 (Make Flows), 3 (Dust Agent), 4 (Notion Handover)
SUMMARY_DE: Automation Pipeline für Doctolib Inbound-Leads (Arztpraxen); Workflow: Tally Intake Form → Make Automation → Salesforce (Lead/Opportunity) + Notion (Projektplanung) → Dust Agent KEB-Generator; Ziel: minimale manuelle Dateneingabe, Single Source of Truth, automatische Kundenerfassungsbogen; Status: In Bau; 4 Phasen geplant; nächster Schritt: Tally-Formstruktur definieren vor Dust-Prompt-Arbeit.

# DoktorLib — Automation Pipeline

## Überblick

Die **DoktorLib Automation Pipeline** ist ein strukturiertes System zur automatisierten Erfassung und Verarbeitung von Inbound-Leads (Arztpraxen) im [[Doctolib]]-Kontext. Das Ziel ist **maximale Automatisierung bei minimaler manueller Dateneingabe**, mit [[Salesforce]] als zentraler Data Backbone und automatischer Generierung von Kundenerfassungsbögen (KEB) durch einen [[Dust Agent]].

> **Status:** In Bau  
> **Stakeholder:** Doctolib Operations Team  
> **Tech-Stack:** [[Tally]] (Forms) → [[Make]] (Automation) → [[Salesforce]] (Daten-Backbone) + [[Notion]] (Projektplanung) → [[Dust Agent]] (KEB-Generator)

---

## Problem (Ist-Zustand)

| Problem | Impact | Quelle |
|---|---|---|
| **Praxisbasisdaten zu spät erfasst** | Erst im Demo-Call statt vor dem Call | Manueller Prozess |
| **Discovery Notes als Freitext in SF** | Nicht skalierbar; Datenqualität schwach | SF-Feldnutzung |
| **KEB = manuelles Excel** | Fehleranfällig; keine Automatisierung | Excel-Datei-Workflow |
| **Deployment erhält Excel, nicht Single Source of Truth** | Doppelte Dateneingabe; Versionskonflikt | Keine Integration |

---

## Ziel-Architektur

```
Inbound Lead (Arztpraxis)
    ↓
[TALLY] Intake Form
(vor Demo-Call; Praxistyp, Fachrichtung, 
aktuelle Software, Labore, IT-Infrastruktur, Geräte)
    ↓
[MAKE] Automation Trigger
(Form Submission erkannt)
    ↓              ↓
[SALESFORCE]   [NOTION DB]
(Lead/Opportunity) (Projektplanung + Sync)
    ↓
Demo-Call
(nur Validierung + Discovery Notes manuell in SF)
    ↓
IT-Partner → [TALLY] Audit-Formular
(separate Datenerfassung)
    ↓
[MAKE] Automation
(Audit-Daten → SF + Notion)
    ↓
Vertragsunterzeichnung
    ↓
[DUST AGENT] KEB-Generator
(liest SF-Daten; generiert KEB automatisch)
    ↓
Deployment erhält Notion-Link
(kein Excel mehr; Single Source of Truth)
```

**Kernhebel:** Tally-Formular-Struktur definiert den gesamten Down-Stream (Make, SF-Felder, Dust-Prompt-Input). → **Input definiert Output.**

---

## Build-Phasen

### Phase 1 — Tally Intake Form (Priorität 1)
**Deliverable:** Funktionales Tally-Formular mit DSGVO-konformer Beschriftung

- [ ] **Feldbestandteile:**
  - Praxistyp (Einzelpraxis, Gemeinschaftspraxis, Klinik)
  - Fachrichtung(en) (Allgemeinmedizin, Zahnmedizin, Gastroenterologie, etc.)
  - Aktuelle Software (Medistar, Turbomed, CompuGroup, etc.)
  - Labore (Anzahl; intern/extern)
  - IT-Infrastruktur (Windows/Mac, Netzwerk-Topologie)
  - Gerätelandschaft (Drucker, Scanner, Telefone, Fax)
  - Kontaktperson (Name, E-Mail, Telefon)

- [ ] **DSGVO-Konformität:**
  - Datenschutzerklärung im Formular
  - Belgien-Hosting verifizieren (Tally: ✅ EU-konform)
  - Cookie-Hinweise (falls Frontend-Landing)

- [ ] **Submission-Handling:**
  - Automatische Bestätigungsmail an Lead
  - Webhook an Make (oder API-Polling)

**Abhängigkeit:** Keine (MVP kann mit Skeleton-Feldern starten)  
**Timeline:** 1 Woche (Form-Design + Deployment)

---

### Phase 2 — Make Automation Flows (abhängig: Phase 1)
**Deliverable:** Error-tolerante Automation mit Fehlerbenachrichtigungen

- [ ] **Trigger:** Tally Form Submission (Webhook oder API-Polling)

- [ ] **Aktion 1: Salesforce Lead/Opportunity erstellen**
  - Mapped: Tally-Felder → SF-Felder (Standard: Lead | Account | Opportunity)
  - Error Handling: Benachrichtigung bei SF-API-Fehler (z.B. Duplikat-Deduplizierung)
  - Filter: Nur vollständige Formulare verarbeiten

- [ ] **Aktion 2: Notion Database Seite erstellen**
  - Sync: Tally-Felder → Notion Properties
  - Verknüpfung: Notion-Seite-ID speichern in SF (für Bidirektionalität)
  - Template: Standard-Projekt-Kanban (Status: "Intake erfasst" → "Demo geplant" → ...)

- [ ] **Error Handling & Notifications:**
  - Slack/E-Mail bei fehlgeschlagenem SF-Sync
  - Retry-Logik (3× mit exponentieller Verzögerung)
  - DLQ (Dead Letter Queue) für fehlerhafte Records

**Abhängigkeit:** Phase 1 (Tally-Formstruktur festgelegt)  
**Timeline:** 2 Wochen (Flow-Design + Testing)

---

### Phase 3 — Dust Agent KEB-Generator (abhängig: Phase 2 + SF-Daten-Struktur)
**Deliverable:** Automatisch generierte, SF-Daten-basierte Kundenerfassungsbögen

- [ ] **Dust Agent Prompt schreiben**
  - Input: Salesforce Lead/Opportunity Record (JSON)
  - Template: Standard-KEB-Format (Felder: siehe unten)
  - Output-Format: Markdown oder PDF (TBD)

- [ ] **SF-Daten-Struktur für Dust:**
  ```
  {
    "Lead": {
      "Name": "...",
      "Praxistyp": "...",
      "Fachrichtung": ["...", "..."],
      "AktuellerSoftware": "...",
      "LaboranzahlIntern": 2,
      "ITInfrastruktur": "...",
      "Geraete": ["...", "..."]
    },
    "DemoCall": {
      "Datum": "2026-06-20",
      "Notes": "Discovery Notes (Freitext)"
    }
  }
  ```

- [ ] **KEB-Template-Felder (noch zu definieren):**
  - Praxis-Überblick (Typ, Größe, Fachrichtung)
  - Aktuelle IT-Landschaft
  - Integrationsanforderungen (Labore, Drucker, etc.)
  - Go-Live-Vorbereitung
  - Benutzerverwaltung-Plan
  - Schulungs-Anforderungen

- [ ] **Trigger:**
  - Manuell: Button "KEB generieren" in SF-UI
  - Automatisch: Nach Vertragsunterzeichnung (SF-Stage-Change zu "Contract Signed") ← Kann Phase 4+ sein

**Abhängigkeit:** Phase 2 (SF-Daten verfügbar); KEB-Feldstruktur-Finalisierung  
**Timeline:** 3 Wochen (Prompt-Engineering + Validierung)

---

### Phase 4 — Deployment Handover (abhängig: Phase 3)
**Deliverable:** Notion-basierte Deployment-View statt Excel-Export

- [ ] **Notion-Template für Deployment-Ansicht:**
  - Relation zu Projekt-Kanban
  - KEB-Generator-Output einbetten (als Seite oder Doc)
  - Deployment-Checklisten-Integration
  - Zugriff für Deployment-Team freigeben

- [ ] **Link-Übergabe-Prozess:**
  - Excel-KEB wird **nicht mehr** an Deployment gesendet
  - Stattdessen: Notion-Link zur Live-Seite
  - Notion → Single Source of Truth (keine Versions-Duplikate)

**Abhängigkeit:** Phase 3 (KEB-Generator funktioniert)  
**Timeline:** 2 Wochen (Notion-Template-Design)

---

## Entscheidungen (getroffen)

| Entscheidung | Begründung |
|---|---|
| **Salesforce = Long-Term Data Backbone** | nicht Notion (Notion ist Project-View, nicht Data-Backbone); SF hat bessere Audit-Trails und Compliance |
| **Tally für Praxisstruktur-Daten** | DSGVO-konform (Belgien ✅); kein Patientendaten-Problem (nur Praxisbasisstruktur) |
| **Dust Agent für KEB-Generierung** | Interne KI-Plattform; kostengünstiger als externe LLM-API auf Dauer |
| **Excel KEB wird abgelöst** | nicht optimiert; stattdessen Notion-Link als Single Source of Truth |

---

## Entscheidungspfad: Nächster Schritt

**Frage:** Tally-Formstruktur zuerst bauen ODER Dust Agent Prompt schreiben?

**Empfehlung:** **Tally-Formular zuerst (Phase 1).**

**Begründung:**
- Phase 1 definiert die **Input-Struktur**, die Phase 2 (Make) und Phase 3 (Dust) direkt determiniert
- Dust Agent Prompt ist ohne finalisierte SF-Feldbestandteile nicht sinnvoll schreibbar
- Tally-Form ist MVP-ready und kann sofort mit "Intake erfasst"-Trigger starten
- Parallel dazu: Dust-Prompt-Outline schreiben (nicht implementieren); auf Phase 2 warten

---

## Abhängigkeits-DAG

```
Phase 1: Tally Intake Form (unabhängig)
    ↓
Phase 2: Make Automation (abhängig: Phase 1)
    ↓                         ↓
Phase 3: Dust Agent      Phase 4: Notion Handover (abhängig: Phase 3)
```

---

## Verknüpfungen

- **[[Doctolib]]** — Produkt-Kontext
- **[[Tally]]** — Form-Building-Plattform
- **[[Make]]** — Automation-Plattform
- **[[Salesforce]]** — CRM & Data Backbone
- **[[Notion]]** — Projektplanung + Output-Zielort
- **[[Dust Agent]]** — KEB-Generator KI-Plattform
- **[[MOC Tech & Setup]]** — Übergeordnetes No-Code-Automation-Index

---

*Quelldokument: raw/raw/_archiv/Work/Doctolib Automation Pipeline.md*  
*Status: In Bau*  
*Zuletzt aktualisiert: 2026-06-17*
