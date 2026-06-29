---
title: Wagglz UX Playbook — Adopt & Optimize
type: synthesis
tags: [wagglz, ux, playbook, wettbewerb, best-practice, roadmap, doctolib, provet-cloud, vetera, petleo]
sources: ["[[Doctolib Software Screenshots 2026-06]]", "[[Provet Cloud + Vetera Screenshots 2026-06]]", "[[PetLeo App Screenshots 2026-06]]"]
created: 2026-06-29
updated: 2026-06-29
summary: Konsolidiertes Build-Playbook aus 162 analysierten Wettbewerber-Screenshots — pro Modul: was Wagglz 1:1 übernimmt (ADOPT), besser macht (OPTIMIZE) und als Alleinstellung baut (DIFFERENZIEREN)
---

# Wagglz UX Playbook — Adopt & Optimize

Cross-Competitor-Synthese aus **162 analysierten Screenshots**: [[Doctolib Software Screenshots 2026-06|Doctolib]] (47, Humanmedizin-Goldstandard DE), [[Provet Cloud + Vetera Screenshots 2026-06|Provet Cloud + Vetera]] (113, Veterinär #1 global + DACH), [[PetLeo App Screenshots 2026-06|PetLeo]] (2, Tierhalter-App).

Leitfrage (Oleg): *„Was übernehmen wir, was optimieren wir — um wirklich die beste Software zu bauen?"*

**Legende:** 🟢 ADOPT (bewährt, 1:1 bauen) · 🔵 OPTIMIZE (haben sie, Wagglz macht es besser) · 🟣 DIFFERENZIEREN (kaum/keiner hat es — Wagglz-Alleinstellung) · Status ggü. Wagglz CLAUDE.md §10.

---

## 1. Kalender / Terminplanung
**Best Practice:** Doctolib + Provet — Behandler-Spalten, Farbcodierung nach Terminart, Tag/Woche/Monat-Toggle, Auslastungs-Zähler (gebucht/Kapazität), Staff-Checkbox-Filter, Drag&Drop-Reschedule + Warteliste.

| Verdikt | Maßnahme | Wagglz-Bezug |
|---|---|---|
| 🟢 ADOPT | Behandler-Spalten + Farbcodierung nach Terminart + Staff-Filter | `KalenderWochenansicht.tsx` (Tag/Woche/Monat ✅ vorhanden) |
| 🟢 ADOPT | **Auslastungs-Zähler pro Tag/Woche** (z.B. 10/78) | fehlt → ergänzen |
| 🔵 OPTIMIZE | **Drag&Drop-Reschedule + Warteliste** für No-Show-Gap-Filling | Roadmap |
| 🟣 DIFFERENZIEREN | Fantastical-inspirierte „Anstehende Termine"-Leiste (schon gebaut ✅) | bereits Wagglz-Vorteil |

## 2. Dashboard / Triage
**Best Practice:** Provet „Recent consultations" + Digital Whiteboard + Triage Board (Priorität en route/arrived/waiting); Doctolib Patientennavigator (Raum-Kanban Wartezimmer→Sprechzimmer).

| Verdikt | Maßnahme | Wagglz-Bezug |
|---|---|---|
| 🟢 ADOPT | Konsultations-Liste mit Status-Tabs + Status-Chips | `TriageDashboard.tsx` ✅ gebaut |
| 🔵 OPTIMIZE | **Raum-Kanban** (Drag Patient → Behandlungsraum) als Eskalation | Roadmap (Premium) |
| 🟣 DIFFERENZIEREN | **Digital Whiteboard / Treatment Sheets** für stationäre Tiere (Medikations-Zeitraster + Overdue-Flags) | fehlt komplett — hoher Wert für Kliniken |

## 3. Behandlungsdoku / Patientenakte (EHR)
**Best Practice:** Doctolib + Provet — **3-Spalten-Workspace**: links Stammdaten/Anamnese-Akkordeon, Mitte Verlauf-Timeline (Filter-Chips) + Doku, rechts **Aktions-Hub** (Termin/Rezept/Labor/Nachricht/Aufgabe). Tabs Overview/Notes/Diagnoses/Lab/Treatment/Discharge. Diagnose-Flags (akut/dauer + V/Z/A/G + Lateralität R/L/B).

| Verdikt | Maßnahme | Wagglz-Bezug |
|---|---|---|
| 🟢 ADOPT | **3-Spalten-Layout** + Tab-Struktur der Behandlung | Behandlungsdoku (§10 #3) — Pattern übernehmen |
| 🟢 ADOPT | **Aktions-Hub-Sidebar** rechts (alle Patient-Aktionen gebündelt) | Tierakte |
| 🟢 ADOPT | **Verlauf-Filter-Chips** (Bericht/Bildgebung/Labor/Verordnung/Abrechnung) | Tierakte |
| 🟢 ADOPT | **Diagnosemodell mit Flags**: Typ (akut/dauer/anamnestisch) + Sicherheit (V/Z/A/G) + Lateralität (R/L/B) | DB-Enum — bei Tieren essenziell (OP links/rechts, Verdacht) |
| 🔵 OPTIMIZE | Vitalwerte mit Optimal-Range pro Spezies (Provet zeigt Range bei Temp) | speziesabhängige Referenzbereiche |
| 🟣 DIFFERENZIEREN | ICD-10 → **Vet-Diagnosekatalog** (speziesgerecht) | GOT/TÄHAV-nativ |

## 4. KI-Features (Wagglz Feature #7 — größter Hebel)
**Best Practice:** Provet + Doctolib — **AI Scribe** (Audio→strukturierte SOAP-Note, Template-getrieben, Human-Review vor Speichern), **AI Patient-History-Summary** (1-Klick), **AI Discharge** (editierbar), **KI-Abrechnungsvorschläge** (Ziffern automatisch), **KI-Telefonassistent** (Anruf→Zusammenfassung+Transkript→Aufgabe). Provet monetarisiert AI Scribe £30/Vet/Mo + „AI Governance: kein LLM-Training/-Speicherung".

| Verdikt | Maßnahme | Wagglz-Bezug |
|---|---|---|
| 🟢 ADOPT | **AI Scribe**: Recording-Karte (Pause/Done/Timer) → Template-Doku → Human-in-Loop-Freigabe | §10 #7 + §3 (Human-in-Loop ✅ konform) |
| 🟢 ADOPT | **AI History Summary** (1-Klick) + **AI Discharge** (editierbar im Editor) | Tierakte |
| 🟣 DIFFERENZIEREN | ⭐ **KI-GOT-Abrechnungsvorschläge** (KI liest Behandlung → schlägt GOT-Ziffern vor) — Provet/Vetera haben das NICHT für GOT | massiver DACH-Vorteil |
| 🟣 DIFFERENZIEREN | ⭐ **KI-Telefonassistent** (Tierhalter ruft an → Anliegen erfasst → Inbox→Aufgabe) | kein Vet-Wettbewerber hat es |
| 🟢 ADOPT | **„AI Governance: kein LLM-Training" offensiv vermarkten** (DSGVO/eu-west-1) | §3 Privacy-Guardrails |

## 5. GOT-Abrechnung / Kasse
**Best Practice:** Doctolib — Ziffern-Tabelle (Ziffer|Menge|Faktor|Gesamt), benutzerdef. **Ziffernketten/Leistungsbündel** (1-Klick-Sets), Diagnose-zu-Rechnung-Checkbox, PDF-Vorschau, Zahlungsart (Bar/Karte/EC) + Auto-„bezahlt" + Quittung, USt-ID/MwSt. Provet Pay — **Pay-by-Link (SMS/Email)**, Card-on-File, Split-Invoices, Recurring Billing.

| Verdikt | Maßnahme | Wagglz-Bezug |
|---|---|---|
| 🟢 ADOPT | **GOT-Zifferntabelle** Ziffer/Menge/Faktor/Gesamt + Inline-Edit | §10 #4 (GOT-Faktor NUMERIC(3,1) ✅) |
| 🟢 ADOPT | ⭐ **GOT-Leistungsbündel/Ziffernketten** (Impfung/Kastration als 1-Klick-Set) — größter Zeit-Hebel | neu |
| 🟢 ADOPT | **Kassen-POS-Flow**: PDF-Vorschau → Zahlungsart Bar/Karte → Auto-„bezahlt" + Quittung | B2C-Direktzahlung (≠ GKV-Quartal) |
| 🟢 ADOPT | **USt-ID + MwSt.** (Tierarzt USt-pflichtig in DE!) | Pflicht, §7 |
| 🔵 OPTIMIZE | **Pay-by-Link (SMS/Email)** + Card-on-File | Roadmap |
| 🟢 ADOPT | Rechnungsstatus-Pipeline (Entwurf→Ausgestellt→Bezahlt→Inkasso) + „Erinnern"/Mahnwesen | Rechnungen |

## 6. Tierhalter-Portal / E-Pet-Pass (Wagglz Kern-Differenzierer)
**Best Practice:** **PetLeo** (mobile Tierhalter-App) — digitale Patienten-Aufnahme (Pre-Visit-Wizard), granulare DSGVO-Consent-Checkboxen, **EU-Heimtierausweis-Scan → Auto-Import**. Vetera „Digitales Wartezimmer", Provet „pre-visit forms".

| Verdikt | Maßnahme | Wagglz-Bezug |
|---|---|---|
| 🟣 DIFFERENZIEREN | ⭐ **EU-Heimtierausweis-Scan** → Chip-Nr./Impfungen/Signalement auto-importieren | §2 „Electronic Pet Passport" — weder Vetera noch Provet haben es |
| 🟢 ADOPT | **Mobile Pre-Visit-Aufnahme-Wizard** (Fortschrittsbalken) — Tierhalter füllt vor Termin aus | `app/portal/` |
| 🟢 ADOPT | **Granulare DSGVO-Consent** (Folgebehandlung / Datenweitergabe Labore+Verrechnungsstellen) + Datenschutz-Download | §7 TÄHAV/DSGVO |
| 🔵 OPTIMIZE | Vollwertiges Portal (eigene Tiere, Termine, Rechnungen, Nachrichten) — geht über Provet/Vetera/Doctolib Self-Service hinaus | §10 #5 ✅ teils gebaut |
| 🟣 DIFFERENZIEREN | Wärmerer B2C-Ton fürs Portal (PetLeo: Teal/Creme/Coral) bewusst anders als B2B-Vet-Chrome | Design-Entscheidung |

## 7. Fehlende Module (alle Wettbewerber haben sie, Wagglz nicht)
| Verdikt | Modul | Quelle |
|---|---|---|
| 🔵 OPTIMIZE | **Aufgaben-/To-Do mit Mitarbeiter-Zuweisung + Fälligkeit** | Doctolib |
| 🔵 OPTIMIZE | **Recalls** (Impf-/Vorsorge-Erinnerung) + **Warteliste** | Doctolib/Vetera |
| 🔵 OPTIMIZE | **Lager/Inventory mit Auto-Reorder + Verfalls-Alerts** | Provet + Vetera |
| 🔵 OPTIMIZE | **Labor-Integration** (IDEXX/Heska): Auftrag→Ergebnis | Provet + Vetera |
| 🔵 OPTIMIZE | **PACS / Röntgen-Bildarchiv (DICOM)** | Provet + Vetera |
| 🔵 OPTIMIZE | **Dokumenten-Smartphone-Scan** + KI-Vorklassifizierung | Doctolib |
| 🔵 OPTIMIZE | **Geräte-Schnittstellen-Registry** (Ultraschall/Analysegeräte) | Doctolib (GDT/LDT) + Vetera |
| 🟣 DIFFERENZIEREN | **Health Plans / Wellness-Abos** (Recurring Revenue) | Provet |
| 🔵 OPTIMIZE | **Video-Sprechstunde** | Vetera/Provet |
| 🔵 OPTIMIZE | **Auto-Dublettenmerge** + Import/Export (Migration/DSGVO Art. 20) | Doctolib |
| 🔵 OPTIMIZE | **Multi-Standort/Filialsysteme** (eine DB) | Vetera + Provet |

## 8. Design / Trust / Go-to-Market
| Verdikt | Maßnahme | Quelle |
|---|---|---|
| 🟢 ADOPT | **Slide-over Drawer** für Details, Modal nur Kurzaktionen | alle 3 (= CLAUDE.md ✅) |
| 🟢 ADOPT | **DSGVO/Compliance offensiv vermarkten** (ISO/SOC2/Passwordless/Data-Ownership-Badges) | Provet — Wagglz-Stärke (Frankfurt) |
| 🟢 ADOPT | **Vorlagen-System** (Doku-Templates pro Behandlungsart, manuell vs. KI-Modus) | Doctolib + Provet |
| 🟢 ADOPT | **Dokument-Branding** pro Praxis (Logo/Kopf/Fuß) — Mandantenfähigkeit | Doctolib |
| 🔵 OPTIMIZE | **Pay-per-Vet-Pricing** + risikofreies **Pilot (3 Mo. gratis)** | Provet |
| 🟢 ADOPT | **Lifecycle-Narrativ** (Before/Check-in/Consult/Checkout/After) + Zielgruppen-Landings + In-App-Produkttour | Provet/Vetera (Marketing) |
| 🔵 OPTIMIZE | **Moderneres UI** (Slate/Indigo, tracking-tight, Whitespace) vs. Vetera „enterprise-grau" / Doctolib dicht | Wagglz-Designsystem §2 |

---

## Die 7 höchstpriorisierten Wagglz-Wetten (Impact × Differenzierung)
1. ⭐ **KI-GOT-Abrechnungsvorschläge** — kein Vet-Wettbewerber hat es; DACH-Killer.
2. ⭐ **EU-Heimtierausweis-Scan** (Tierhalter-Onboarding) — echte Alleinstellung.
3. ⭐ **AI Scribe** (Audio→GOT-konforme Behandlungsnotiz, Human-in-Loop) — Tischeinsatz vs. Provet.
4. **3-Spalten-Tierakte + Aktions-Hub** — bewährtes EHR-Pattern, sofort bauen.
5. **GOT-Leistungsbündel** (1-Klick-Ziffernketten) — größter Effizienz-Hebel im Alltag.
6. **Kassen-POS-Flow** (Bar/Karte + Quittung + USt) — Wagglz ist B2C-Direktzahlung.
7. **Vollwertiges Tierhalter-Portal** (Tiere/Termine/Rechnungen/Nachrichten + E-Pet-Pass) — strukturelle Differenzierung vs. alle.

## Verbindungen
- Quell-Teardowns: [[Doctolib Software Screenshots 2026-06]], [[Provet Cloud + Vetera Screenshots 2026-06]], [[PetLeo App Screenshots 2026-06]]
- Wettbewerber: [[Provet Cloud]], [[Vetera]], [[Petleo]], [[Nordhealth]]
- Produkt: [[Wagglz]], [[Wagglz App UI Screens]]
