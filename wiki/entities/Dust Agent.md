TAGS: [ai, automation, keb, document-generation, dust, doktorlib, llm]
SOURCES: ["raw/raw/_archiv/Work/DoktorLib Automation Pipeline.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: Dust Agent — Interne KI-Plattform für automatische Dokumentgenerierung; erzeugt KEB (Kundenerfassungsbogen) aus Salesforce-Daten; Trigger: Vertragsunterzeichnung (SF Stage-Change)

---

# Dust Agent

## Überblick

**Dust Agent** ist eine **interne KI-Plattform** (wahrscheinlich auf LLM-Basis), die in der [[DoktorLib Automation Pipeline]] die letzte Automatisierungs-Phase (Phase 4) umsetzt: **Automatische Generierung des Kundenerfassungsbogens (KEB)** aus strukturierten Salesforce-Daten.

## Zweck & Funktion

### KEB-Generierung (Phase 4)
- **Input:** Salesforce-Datensatz mit allen Feldern aus Phase 1–3
  - Praxistyp, Fachrichtung
  - Aktuelle Software, Laboranbindungen
  - IT-Infrastruktur, Gerätelandschaft
  - Audit-Daten
  - Discovery-Notes
- **Output:** Strukturierter KEB (Kundenerfassungsbogen) im Standard-Format
- **Format:** Notion-kompatibel oder PDF (TBD)

## Architektur

### Prompt-Struktur
```
Input: Salesforce-Objekt (Lead/Opportunity)
├─ Field: praxistyp = "Zahnarzt"
├─ Field: aktuelle_software = "Schiller ProfiDent"
├─ Field: it_infrastruktur = "On-Prem mit Windows Server 2019"
└─ ... (weitere Felder)

Processing: Dust Agent Prompt
├─ Feld-Mapping (SF-Felder → KEB-Kategorien)
├─ Kontext-Integration (Branchenbest-Practices)
└─ Standard-Format-Generierung

Output: KEB
├─ Administratives Setup
├─ Hardware-Anforderungen
├─ Software-Integration
├─ Mitarbeiter-Onboarding
└─ Compliance & Sicherheit
```

### Prompt-Design
- **Input-Spec:** Salesforce-Feldliste (definiert in Phase 1–3)
- **Output-Spec:** KEB-Feldliste (noch zu definieren)
- **Logik:** Konditionale Generierung (z.B. „Falls Zahnarzt → Zahnmedizin-spezifische KEB-Abschnitte")

## Trigger

- **Event:** SF Lead Stage-Change zu „Vertragsunterzeichnung" (oder manuell)
- **Aktion:** Dust Agent wird aufgerufen mit SF-Datensatz
- **Resultat:** KEB wird generiert und in Notion-Seite eingefügt

## Abhängigkeiten

- [[Salesforce]] — Input-Quelle
- [[Notion]] — Output-Ziel (KEB wird in Notion-Seite eingefügt)
- [[DoktorLib Automation Pipeline]] — Phase 4 / Parent-Projekt

## Kritische Abhängigkeit

⚠️ **Wichtig:** Dust-Agent-Prompt kann ERST geschrieben werden, wenn **Phase 1–3 Feldstrukturen finalisiert sind**. Das heißt:
1. Tally-Form-Feldliste MUSS definiert sein
2. Salesforce-Objektstruktur MUSS klar sein
3. KEB-Output-Format MUSS spezifiziert sein

Aktuell (2026-06-17): Phase 1–3 sind noch in Design-Phase; Dust-Prompt sollte **NACH** Phase 2–3-Umsetzung geschrieben werden.

---

*Entität erstellt: 2026-06-17*
