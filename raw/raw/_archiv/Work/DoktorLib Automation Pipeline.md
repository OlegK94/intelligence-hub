---
tags: [doktorlib, automation, tech, aktiv]
status: In Bau
stack: [Tally, Make, Salesforce, Notion, Dust]
created: 2026-05-08
---

# ⚙️ DoktorLib — Automation Pipeline

## Ziel
Maximale Automatisierung des Discovery & Onboarding-Flows für Inbound-Leads (Arztpraxen). Minimale manuelle Dateneingabe. Salesforce als Long-Term-Backbone.

## Ist-Zustand (Problem)
- Praxisbasisdaten werden zu spät erfasst (erst im Demo-Call)
- Discovery Notes als Freitext in Salesforce → nicht skalierbar
- KEB (Kundenerfassungsbogen) = manuell ausgefülltes Excel → fehleranfällig
- Deployment erhält Excel-Datei → kein Single Source of Truth

## Ziel-Architektur

```
Inbound Lead
    ↓
[TALLY] Intake Form (vor Demo)
    ↓
[MAKE] Automation
    ↓              ↓
[SALESFORCE]   [NOTION DB]
(Daten-Backbone)  (Projektplanung)
    ↓
Demo-Call (nur Validierung + Discovery Notes manuell in SF)
    ↓
IT-Partner → separates [TALLY] Audit-Formular
    ↓
[MAKE] schreibt Audit-Daten → Salesforce + Notion
    ↓
Vertragsunterzeichnung
    ↓
[DUST AGENT] liest alle SF-Daten → generiert KEB automatisch
    ↓
Deployment erhält Notion-Link (kein Excel mehr)
```

## Build-Phasen

### Phase 1 — Tally Intake Form
- [ ] Felder definieren: Praxistyp, Fachrichtung, aktuelle Software, Labore, IT-Infrastruktur, Gerätelandschaft
- [ ] DSGVO-konforme Formularbeschriftung (Tally, EU-Hosting Belgien ✅)
- [ ] Automatische Weiterleitung / Bestätigungsmail

### Phase 2 — Make Automation
- [ ] Trigger: Tally Form Submission
- [ ] Aktion 1: Salesforce — neues Lead/Opportunity erstellen + Felder befüllen
- [ ] Aktion 2: Notion — neue DB-Seite erstellen + Felder synchronisieren
- [ ] Error Handling: Benachrichtigung bei Fehler

### Phase 3 — Dust Agent (KEB-Generator)
- [ ] Dust Agent Prompt schreiben
- [ ] Input: Salesforce-Daten (Struktur definieren)
- [ ] Output: KEB im Standard-Format (Felder: [noch zu definieren])
- [ ] Trigger: Vertragsunterzeichnung (manuell oder automatisch via SF-Stage-Change)

### Phase 4 — Deployment Handover
- [ ] Notion-Template für Deployment-Ansicht bauen
- [ ] Link-Übergabe statt Excel

## Entscheidungen (getroffen)
- **Salesforce** = Long-Term Data Backbone (nicht nur Notion)
- **Tally** = DSGVO-konform für Praxisstruktur-Daten (kein Patientendaten-Problem)
- **Dust** = interne KI-Plattform für KEB-Generierung
- **Excel KEB** = wird abgelöst, nicht optimiert

## Nächster Schritt
**Entscheiden:** Tally-Formstruktur zuerst bauen ODER Dust Agent Prompt schreiben?
→ Empfehlung: Tally zuerst (Input definiert den Output — ohne Feldstruktur kein sinnvoller Dust Prompt)

---
*Verknüpft: [[MOC Tech & Setup]] | [[MOC Strategie & Business]]*
