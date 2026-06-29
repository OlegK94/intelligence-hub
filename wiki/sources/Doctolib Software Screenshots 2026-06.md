---
title: Doctolib Software Screenshots 2026-06
type: source
tags: [doctolib, wettbewerb, ux, wagglz, praxissoftware, screenshots]
sources: ["raw/raw/Doctolib /IMG_3279.JPG … IMG_3325.JPG"]
created: 2026-06-28
updated: 2026-06-28
summary: 47 Screenshots aus dem Doctolib-Arztsoftware-Demo-Account (Oleg Kober, intern) — vollständige Modul-Inventur der deutschen Marktführer-Praxissoftware als UX-Referenz für Wagglz
---

# Doctolib Software Screenshots 2026-06

Set von **47 hochauflösenden Screenshots** (IMG_3279–IMG_3325, 5712×4284 px, abfotografiert vom MacBook-Display) aus dem **Doctolib-Praxissoftware-Demo-Account** von Oleg Kober. Oleg arbeitet bei Doctolib (source: [[Doctolib]]) und hat über den internen Demo-Account ("Oleg Kober (Demo)", Hausarzt/Allgemeinmediziner) die komplette Arzt-Software dokumentiert.

Dies ist die **direkteste verfügbare Wettbewerber-UX-Referenz** für Wagglz: Doctolib ist der dominierende Anbieter für deutsche Arztpraxen, voll DSGVO-/TI-konform, und zeigt den Goldstandard für Terminkalender, EHR, KI-Assistenz und Abrechnung im deutschen Markt. Wagglz überträgt diese Muster auf die **Tierarzt-Domäne** (source: [[Wagglz]]).

> **Hinweis zur Vault-Konvention:** `Doctolib-Arbeit` ist normalerweise *nicht* in diesem Vault (siehe CLAUDE.md). Diese Screenshots sind hier eine **Ausnahme als reine Wettbewerbs-/UX-Recherche für Wagglz** — keine Doctolib-Arbeitsinhalte, sondern Produkt-Teardown des Marktführers. Keine echten Patientendaten (Demo-Account mit Mustermann-Daten).

---

## Design-System (Doctolib)

| Element | Doctolib | Wagglz-Pendant |
|---------|----------|----------------|
| **Primärfarbe** | Doctolib-Blau `#1A6DFF`-ish, dunkelblaue Top-Bar | `--wagglz-blue #2E54CB` / `indigo-600` |
| **Logo** | „D"-Monogramm, geschwungene Schrift | „W"-Dog Icon |
| **Layout** | Fixe linke Icon-Sidebar (schmal) + Top-Suchleiste + Content | Collapsible Sidebar + TopBar |
| **Sidebar-Items** | Terminkalender, Patientennavigator, Aufgaben, Connect, Patientennachrichten, Patientenmanagement, E-Mails, Dokumentenimport, Abrechnung, Mehr | Kalender, Patienten, Behandlungen, Rechnungen, Nachrichten, Analytics, Übersicht |
| **Detail-Pattern** | **Slide-over Drawer von rechts** (kein zentriertes Modal für Detail) | ✅ identisch in CLAUDE.md vorgeschrieben |
| **CRUD** | Zentrierte Modals nur für kurze Aktionen (Besuch hinzufügen, Anhänge) | Drawer bevorzugt |
| **Status** | Farbcodierte Pills + Badges, Zähler an Icons (z.B. „180" Dokumente, „15" Aufgaben) | Status-Chips mit Dot-Indikatoren |

---

## Modul-Inventur (47 Screenshots)

### 1. Login & Account-Auswahl (IMG_3279–3280)
- **Account-Picker**: „Wählen Sie Ihren Account aus" — Multi-Account auf einem Gerät (Oleg Kober Demo, Max Mustermann, Cf Demo), je mit Fachrichtung. „+ Ein Konto hinzufügen / entfernen".
- **PIN-Login**: 4-stelliger PIN pro Account (schneller Wechsel ohne volles Passwort), „PIN-Code vergessen?".
- Rechte Seite: Marketing-Promo („KI-Telefonassistent, 3 Monate 100% Rabatt").
- **Wagglz-Learning:** Multi-Account + PIN-Schnellwechsel ist stark für **Praxen mit mehreren Behandlern an einem Empfangs-PC**. Wagglz hat aktuell nur Standard-Auth → PIN-Schnellwechsel als Praxis-Feature erwägen.

### 2. Terminkalender (IMG_3281)
- **Wochenansicht** mit Behandler-Spalten (Mo–Fr), View-Toggle: **Tagesliste · Tag · Woche · Monat** (exakt das Muster, das Wagglz gerade gebaut hat ✅).
- Farbcodierte Termin-Blöcke nach Terminart, „@"-Icon = Online gebucht, „P" = Patienten-Marker.
- Linke Spalte: „TERMIN SUCHEN" Button, Mini-Monatskalender, **Behandler-Filter** (Dr. König, Dr. Müller, Gynäkologe, Kinderarzt — Checkboxen), Patientenstatus-Filter, **Terminarten-Filter (25/25)**.
- Auslastungs-Zähler pro Tag: `10/78` (gebucht/Kapazität), Wochensumme `44/318`.
- „Aufgaben"-Zeile oben (15 Flags), „Sprechzeiten ändern", „Kalenderanzeige".
- **Wagglz-Learning:** ① **Auslastungs-Zähler pro Tag/Woche** (gebucht/Kapazität) fehlt Wagglz — sehr wertvoll für Praxis-Steuerung. ② **Behandler-Filter-Checkboxen** in der linken Spalte. ③ Online-gebucht-Marker am Termin.

### 3. Patientennavigator — Raum-Kanban (IMG_3282–3283)
- **Kanban-Board nach Räumen**: Wartezimmer · Sprechzimmer 1–4 · Impf-/Injektionsraum · Labor/Zytologie · U/Raum.
- Links: **„Bevorstehende Besuche (57)"** — Patientenkarten (Name, Geburtsdatum+Alter, Geschlecht, Grund „Akute Beschwerden/Notfall", Uhrzeit, Behandler). Farbiger linker Rand = Behandler/Dringlichkeit.
- „+ Besuch ohne Termin", „Kürzliche Patientenbesuche".
- **Modal „Besuch ohne Termin hinzufügen"**: Patientensuche, Terminkalender, Terminart, Behandlungsstation, Notiz.
- **Wagglz-Learning:** Das ist **das Triage-/Dashboard-Konzept** (vgl. Provet „Recent Consultations"). Wagglz `TriageDashboard` ist die Listen-Variante; **Doctolibs Raum-Kanban (Drag-Patient-in-Raum) ist die Premium-Eskalationsstufe** → Roadmap: Patienten per Drag&Drop zwischen Wartezimmer → Behandlungsraum ziehen.

### 4. Aufgaben (IMG_3284)
- Aufgabenliste mit Tabs: **Alle · Mir zugewiesen (20) · Heutige Aufgaben (15)**.
- Filter: Kategorien, Verantwortlich, Erstellt von, Terminkalender, Fälligkeitsdatum, Status.
- Spalten: Aufgabe · Patient:in · Verantwortlich · Erstellt von · Terminkalender · **Fälligkeitsdatum** (rot = überfällig).
- Flag-Indikatoren (rot/leer = Priorität), Kategorien: Sonstiges, Patient:in kontaktieren, Dokument, Befund, Termin.
- „AUFGABE HINZUFÜGEN", „Signaturliste", „Aufgabenliste drucken".
- **Wagglz-Learning:** **Vollwertiges Aufgaben-/To-Do-Modul mit Zuweisung an Mitarbeiter** fehlt Wagglz komplett. Für Praxisteam-Koordination (Rückrufe, Befunde einscannen, EKG nachholen) essenziell. Hoher Mehrwert, mittlerer Aufwand.

### 5. Patientennachrichten + KI-Telefonassistent (IMG_3285–3288) ⭐
- **Nachrichten-Inbox**: Patient · Datum · Kategorie · Vorschau · Nachrichtenprofil · Aufgaben · Status. Filter Offen/Kategorie/Behandler.
- Kategorien: Folgerezept anfragen, Befundbesprechung, Überweisungsschein, Arbeitsunfähigkeitsbescheinigung, neues Rezept …
- Jede Nachricht = **„Telefonische Anfrage"** → automatisch vom **KI-Telefonassistenten** erfasst.
- **Detail-Drawer**: Umschalter **„KI-Zusammenfassung" ↔ „Vollständiges Transkript"**:
  - *KI-Zusammenfassung*: strukturierte Bullet-Extraktion (Anliegen: Folgerezept · Medikament: Amoxicillin, Paracetamol, Nasenspray) + Disclaimer „möglicherweise unvollständig".
  - *Transkript*: vollständiger Dialog Assistent↔Patient + **Audio-Play-Button**.
- Aktionen: „Antwort an Patient:in", „Aufgabe erstellen", „Als Vorlage speichern", „Qualität der Anfrage bewerten".
- **Anhänge-Picker** mit Kategorie-Chips (Bericht, Bildgebung, Laborbefund, Verordnung, Abrechnung, Administratives …).
- **Wagglz-Learning:** ⭐ **KI-Telefonassistent ist Doctolibs Killer-Feature** (Promo: 3 Monate gratis). Patient ruft an → KI nimmt Anliegen auf → strukturierte Zusammenfassung + Transkript landet in der Inbox → Praxis macht Aufgabe draus. **Für Wagglz (Tierhalter ruft an: „Hund hat Durchfall, brauche Termin")** wäre das ein massiver Differenziator vs. Vetera/Provet, die das nicht haben.

### 6. Patientenmanagement (IMG_3289)
- Tabs: **Patienten · Zu benachrichtigen · Recalls · Warteliste · Patientenmitteilungen · Dokumente**.
- Liste: Name · Alter · Behandlungen · Letzter Termin · **Letzte Terminart** (farbcodiert). „11688 Patienten".
- „+ EINEN NEUEN PATIENTEN HINZUFÜGEN", **„PATIENTENKARTEN VERGLEICHEN"** (Dubletten-Merge).
- **Wagglz-Learning:** ① **„Recalls"** (Wiederbestellung/Erinnerung — z.B. Impfung fällig) als eigener Tab → für Tierarzt **Impf-Recall** Gold wert. ② **„Warteliste"**. ③ **Dubletten-Zusammenführung** von Patientenkarten.

### 7. Dokumentenimport (IMG_3290)
- Split-View: Links Dokumentenliste (180 Dokumente), Mitte PDF-Vorschau, **rechts Zuordnungs-Panel** (Patient:in, Art des Dokuments mit Kategorie-Baum).
- „Dokumente hierher ziehen / Dokument hochladen" + **„Über mein Smartphone hinzufügen"** (Scan per Handy).
- Kategorie-Baum: Bericht (Arztbrief, Krankenhausentlassungsbericht, OP-Bericht, Geburtsbericht, Histologie, Pränataldiagnostik), Bildgebung (Röntgen) …
- **Wagglz-Learning:** **Smartphone-Scan-Upload + KI-Vorklassifizierung** von Befunden. Für Tierarzt: Laborbefunde, Röntgen, Überweisungen scannen und automatisch dem Tier zuordnen.

### 8. Abrechnung (IMG_3291–3292)
- Tabs: **Umsatz · GKV-Abrechnung · Privatabrechnung**. Zeitraum-Toggle: Tag/Monat/**Quartal**/Jahr/Benutzerdefiniert.
- **Umsatz-Dashboard**: GKV-Umsatz Balkendiagramm (Budget vs. Ist), Scheine-Linienchart, Privatabrechnung-Aufteilung privat/IGeL. „EBM-Ziffern anzeigen" / „GOÄ-Ziffern anzeigen", „Budget eingeben".
- **Privatabrechnung-Liste**: Tabs Entwürfe/Offen(4)/An PVS gesendet/Bezahlt/Inkassofähig/Alle. Spalten Nr · Patient · Versand (Digital) · Art (IGeL) · Rechnungsverlauf · Status · Summe · „Erinnern". Export.
- **Wagglz-Learning:** ① **Umsatz-Dashboard mit Budget-Tracking** (Ist vs. Plan pro Quartal) → Wagglz Analytics. ② **Rechnungsstatus-Pipeline** (Entwurf → Ausgestellt → Bezahlt → Inkassofähig) + „Erinnern"-Mahnwesen. ③ GOÄ↔GOT: Doctolib GOÄ/EBM, Wagglz GOT — gleiche Mechanik.

### 9. Patientenkarte / EHR (IMG_3293–3299) ⭐
- **Linke Spalte (Akkordeon)**: Behandlung · Persönliche Daten · Verlauf · **Krankengeschichte** (Dauerdiagnosen 6, Akutdiagnosen 12/Quartal) · Operationen · Allergien (Bestätigt/Vermutet) · Familienanamnese · Gyn-Anamnese · **Lebensgewohnheiten** (Alkohol, Tabak, Drogen, Sport, Ernährung, Beruf, Wohnform) · Aktuelle Medikation · **Labor- & Vitalparameter** (Puls 180bpm, CRP, Temp, SpO₂) · Impfpass · Memo.
- **Mitte „Verlauf"**: chronologische Timeline der Behandlungen mit ICD-Diagnosen + Patientenhinweisen, **Filter-Chips** (Bericht, Bildgebung, Laborbefund, Verordnung, Abrechnung, Administratives). Schwangerschafts-Tracker.
- **Rechte Spalte (kontextuelle Aktionen)**: Patientennavigator (einchecken), **Zum Signieren** (eRezept), Abrechnung (Schein/IGeL-Rechnung erstellen), **Dokumente** (Rezept, Heilmittelverordnung, Überweisung, AU, Bescheinigung), **Termin** (Einen/Mehrere vereinbaren, Spontan buchen), Vernetzte Versorgung, Patient:in-Aktionen (Nachricht, Laborauftrag, Patientenakte exportieren, ePA öffnen, Patient löschen).
- **Krankengeschichte-Detail**: ICD-10-Suche („Code oder Etikett eingeben"), Diagnosesicherheit (DD/G), Codes G55.1, M51.1 … mit Datum.
- **Wagglz-Learning:** ⭐ **Das ist die Referenz für die Wagglz-Tierakte.** Dreispaltig: links strukturierte Stammdaten/Anamnese (Akkordeon), Mitte chronologischer Behandlungs-Verlauf mit Filter-Chips, rechts **kontextuelle Aktionen** (Rezept, Termin, Dokument — immer griffbereit). Wagglz Behandlungsdoku sollte exakt dieses 3-Spalten-Pattern adaptieren. **Dauer- vs. Akutdiagnosen** + ICD-10-Suche → für Tier: ICD-10-Vet/Diagnose-Katalog.

### 10. KI-Sprechstundenassistent / AI Scribe (IMG_3300–3302) ⭐⭐
- **„KI-Sprechstundenassistent"** Panel in der Behandlung:
  - **„Audio-Transkription · Starten"** — Ambient Recording des Arzt-Patient-Gesprächs.
  - **„Vorlage für den KI-Sprechstundenassistenten"** (Template-Auswahl, z.B. „Gesundheitsvorsorge – Check Up") — strukturiert die generierten Notizen.
  - Template-Struktur: **Konsultationsgrund · Anamnese · Untersuchung** [Erfasste Vitalzeichen: RR, Puls, Temp, Gewicht, Größe, BMI] …
  - **„✨ Dokumentation generieren"** — Audio → strukturierte Behandlungsnotiz.
- **KI-Abrechnungsvorschläge** (IMG_3302): rechtes Panel „IGeL", **„GOÄ-Ziffer hinzufügen"** (GOÄ-Katalog-Suche), **„Abrechnungsvorschläge (2)"** — KI schlägt Ziffern automatisch vor (Chips 1,3,5 … mit „Bestätigen (2/2)"). „MwSt.-Berechnung zu Ziffern", „Später fertigstellen", „Ausstellen".
- **Wagglz-Learning:** ⭐⭐ **Zwei KI-Killer-Features:**
  - **AI Scribe** (Audio → SOAP-Note): identisch zu Provet AI Scribe (£30/seat). Wagglz hat das in CLAUDE.md als Feature #7 „AI Scribe – voice → structured treatment note, Human-in-Loop". Doctolib zeigt das **Template-getriebene** Muster (Vorlage wählt Struktur) → genau so bauen, mit Human-in-Loop-Freigabe.
  - **KI-Abrechnungsvorschläge**: KI liest die Behandlung und schlägt GOÄ/GOT-Ziffern vor → Arzt bestätigt nur. **Für Wagglz GOT-Abrechnung ein enormer Differenziator** (automatische GOT-Ziffer-Vorschläge aus Behandlungstext).

### 11. Behandlungs-/Abrechnungsflow vertieft (IMG_3303–3311)
- **3-Spalten-Workspace während der Konsultation**: links Patientenakte, Mitte KI-Sprechstundenassistent + Verlauf/Dokumentation + Schwangerschafts-Tracker, rechts **Abrechnung** (IGeL, GOÄ-Ziffern).
- **KI-Abrechnungsvorschläge als Radio-Auswahl** (nicht nur Anzeige) → Arzt bestätigt Vorschläge (IMG_3303).
- **Diagnose-zu-Rechnung-Zuordnung per Checkbox** (IMG_3304): „Entfernen Sie die Diagnosen, die für diese Rechnung nicht relevant sind." ICD-10 inline mit Sicherheitskennzeichen „G".
- **GOÄ-Ziffern-Tabelle**: Spalten **Ziffer | Menge | Faktor | Gesamt** (z.B. Faktor 2,3), zeilenweise Edit/Delete (IMG_3305) — strukturell **identisch zum Wagglz-GOT-Modell** (Faktor NUMERIC(3,1)).
- **PDF-Rechnungsvorschau im Browser** vor Versand + Zahlungspanel: „bezahlt jetzt/später", **IBAN-fehlt-Warnung**, „senden/drucken" (IMG_3306).
- **Zahlungsbestätigung**: Zahlungsart-Dropdown (Überweisung, Girokarte/EC, Debit, Karte, **Bar**), Druck markiert Rechnung automatisch als „bezahlt" (IMG_3307).
- **Medikament/Rezept-Modul** (IMG_3308): PZN-Suche, Packungsgröße N1/N2, AVP, **Dosierungsschema (1-1-1)**, Wiederverordnung aus Historie (35 bisherige Rezepte).
- **Aktions-Hub-Sidebar** der Patientenakte (IMG_3309): alle Aktionen gebündelt — Termin, Nachricht, Laborauftrag, **Untersuchung mit Gerät**, Dokumente importieren, Aufgabe, Online-Buchung sperren.
- **Laborauftrag-Flow** (IMG_3310–3311): Laborverbindung wählen (IMD Berlin) → Stammdaten-Übermittlungs-Vorschau (Patient, Versicherung, BSNR) → „An Labor senden" (aktiviert erst bei vollständiger Auswahl).

### 12. Einstellungen / Admin-Konsole (IMG_3312–3325)
- **Aufgabenorientierte Settings-Startseite** (IMG_3312): Suche „Was möchten Sie heute tun?" + Quick-Action-Karten statt nur Menübaum. Navigation: Meine Praxis, Terminmanagement, Patientennachrichten, Personalisierung & Vorlagen, Abrechnung, Diagnosen, Erweiterte Einstellungen.
- **Vorlagen-Verwaltung** (IMG_3313): Tabelle Name | Art | **Anwendung (Manuelle Notizen vs. KI-Sprechstundenassistent)** | Verfasser | Aktiv-Toggle. Doku-Templates pro Behandlungsart.
- **Dokument-Branding** (IMG_3314): Logo/Kopf-/Fußzeile pro Dokumenttyp (Rechnung etc.).
- **Abrechnung-Admin**:
  - **Ziffernketten/Leistungsbündel** (IMG_3315): vordefinierte Ziffern-Kombis als 1-Klick-Sets (z.B. „Check Up", „Impfung & Wundversorgung"), getrennte Kataloge EBM/GOÄ.
  - PVS-Anbindung (IMG_3316), **USt-IdNr.** mit Format-Validierung (IMG_3317), KV-Automatik-Toggles (Dauerdiagnose-Übernahme etc., IMG_3318).
- **Diagnosen-Admin**:
  - **Kodierregelwerk** (IMG_3319): regelbasierte ICD-Plausibilität, Stammdaten-Versionierung.
  - **Diagnose-Kategorisierung** (IMG_3320): Akut / Dauer / Anamnestisch — Definitionen.
  - ICD-10-GM-Leitfaden + **Zusatzkennzeichen** (IMG_3321–3322): **V** Verdacht, **Z** Zustand-nach, **A** ausgeschlossen, **G** gesichert + **Seitenlokalisation R/L/B**.
- **Erweiterte Einstellungen**:
  - **Geräte-/Labor-Schnittstellen** (IMG_3323): Registry mit Verbindungstyp **GDT** (Geräte) / **LDT** (Labor), Aktiv-Status.
  - **Zugriffsrechte-Default** für neue Benutzer auf medizinische Daten (IMG_3324) → RLS-Default.
  - **Patientenbasis-Verwaltung** (IMG_3325): mehrere Mandanten-Datenbanken, **automatische Dublettenzusammenführung** mit Aktionsprotokoll, Import/Export-Tabs (Migration/DSGVO).
- **Wagglz-Learning (Block 11–12):** ① **GOT-Ziffern-Tabelle (Ziffer|Menge|Faktor|Gesamt) + Leistungsbündel** = wichtigster Abrechnungs-Hebel. ② **Kassen-/POS-Flow** (Zahlungsart Bar/Karte, Auto-„bezahlt", Quittung) — Wagglz ist B2C-Direktzahlung. ③ **USt-ID + MwSt.** (Tierarzt USt-pflichtig!). ④ **Aktions-Hub-Sidebar** in der Tierakte. ⑤ **Vorlagen-System mit KI-Modus** (= Wagglz Feature 7). ⑥ **Diagnosemodell mit Flags** (Typ akut/dauer/anamnestisch + V/Z/A/G + Lateralität R/L/B). ⑦ **Auto-Dublettenmerge** + **Geräte/Labor-Registry** (GDT/LDT → IDEXX/Röntgen).

---

## Top-Erkenntnisse für Wagglz (Priorisiert)

> Leitfrage (Oleg): „Was können wir **besser** machen oder **genau so**, um wirklich die beste Software zu bauen?"

### 🟢 GENAU SO übernehmen (bewährte Muster)
1. **3-Spalten-Patientenakte** (Stammdaten-Akkordeon | Verlauf-Timeline mit Filter-Chips | kontextuelle Aktionen rechts) — IMG_3293–3299.
2. **Kalender Tag/Woche/Monat + Auslastungs-Zähler** (gebucht/Kapazität pro Tag) — IMG_3281.
3. **Slide-over Drawer** für Details, Modal nur für Kurzaktionen (deckt sich mit Wagglz CLAUDE.md).
4. **Rechnungsstatus-Pipeline** (Entwurf→Ausgestellt→Bezahlt→Inkasso) + „Erinnern"-Mahnwesen — IMG_3292.
5. **Verlauf-Filter-Chips** (Bericht/Bildgebung/Labor/Verordnung/Abrechnung) in der Akte.
6. **GOT-Ziffern-Tabelle** Ziffer|Menge|Faktor|Gesamt mit Inline-Edit/Delete — IMG_3305 (= Wagglz GOT-Modell 1:1).
7. **Kassen-/POS-Flow**: PDF-Vorschau → Zahlungsart (Bar/Karte/EC) → Auto-„bezahlt" + Quittung — IMG_3306–3307.
8. **Aktions-Hub-Sidebar** in der Patientenakte (alle Aktionen gebündelt rechts) — IMG_3309.

### 🟡 KI-FEATURES als Differenziatoren (Wagglz-Chance)
6. ⭐⭐ **AI Scribe** (Audio→strukturierte Behandlungsnotiz, Template-getrieben, Human-in-Loop) — Wagglz Feature #7, Doctolib zeigt das Pattern.
7. ⭐⭐ **KI-GOT-Abrechnungsvorschläge** (KI liest Behandlung, schlägt GOT-Ziffern vor) — IMG_3302. Provet/Vetera haben das (noch) nicht für GOT.
8. ⭐ **KI-Telefonassistent** (Tierhalter ruft an → KI erfasst Anliegen → Zusammenfassung+Transkript in Inbox → Aufgabe) — IMG_3285–3287.

### 🔵 FEHLENDE MODULE in Wagglz (Roadmap)
9. **Aufgaben-/To-Do-Modul** mit Mitarbeiter-Zuweisung & Fälligkeit — IMG_3284.
10. **Recalls** (Impf-/Vorsorge-Erinnerung) + **Warteliste** im Patientenmanagement — IMG_3289.
11. **Patientennavigator als Raum-Kanban** (Drag Patient → Behandlungsraum) als Premium-Eskalation des TriageDashboard — IMG_3282.
12. **Dokumenten-Smartphone-Scan** mit KI-Vorklassifizierung — IMG_3290.
13. **Umsatz-Dashboard mit Budget-Tracking** (Ist vs. Plan/Quartal) — IMG_3291.
14. **Auto-Dubletten-Merge** von Patientenkarten mit Aktionsprotokoll — IMG_3289 / IMG_3325.
15. **GOT-Leistungsbündel/Ziffernketten** (1-Klick-Sets für Impfung/Kastration etc.) — IMG_3315.
16. **USt-ID + MwSt.-Konfiguration** (Tierarztleistungen sind in DE USt-pflichtig!) — IMG_3317 / IMG_3303.
17. **Vorlagen-System** (Doku-Templates pro Behandlungsart, manuell vs. KI-Modus) — IMG_3313.
18. **Diagnosemodell mit Flags**: Typ (akut/dauer/anamnestisch) + Sicherheit (V/Z/A/G) + Lateralität (R/L/B) — IMG_3320/3322.
19. **Medikament-/Rezeptmodul** mit Dosierungsschema + Wiederverordnung (§13 TÄHAV) — IMG_3308.
20. **Geräte-/Labor-Schnittstellen-Registry** (GDT/LDT → IDEXX/Röntgen/Ultraschall) — IMG_3323.
21. **Dokument-Branding** pro Praxis (Logo/Kopf/Fuß auf Rechnungen) — Mandantenfähigkeit — IMG_3314.
22. **Aufgabenorientierte Settings-Startseite** („Was möchten Sie tun?" + Quick-Cards) — IMG_3312.

### ⚪ WO WAGGLZ SCHON BESSER IST / SEIN KANN
- **Modernere UX**: Doctolib ist dicht/funktional aber „enterprise-grau". Wagglz kann mit Personio/Sportina-Designsprache (Slate+Indigo, `tracking-tight`, großzügiger Whitespace) frischer wirken.
- **Tierhalter-Portal**: Doctolib hat Patienten-Self-Service (Online-Buchung), aber Wagglz' vollwertiges **Tierhalter-Portal** (eigene Tiere, Termine, Rechnungen, Nachrichten, E-Pet-Pass) geht weiter.
- **GOT-nativ** (DE/AT-Tierarzt) statt GOÄ/EBM (Humanmedizin) — Wagglz spielt im Vet-Markt gegen Vetera/Provet, nicht Doctolib.

---

## Verbindungen
- Wettbewerber-Kontext: [[Provet Cloud]] (globaler Vet-Marktführer, hat AI Scribe), [[Vetera]] (DACH-Vet, GOT-nativ), [[Nordhealth]] (besitzt beide).
- Wagglz-Produkt: [[Wagglz]], [[Wagglz App UI Screens]].
- Person/Quelle: [[Doctolib]] (Olegs Arbeitgeber — Quelle des Demo-Zugangs).

## Quellen
- 47 Screenshots `raw/raw/Doctolib /IMG_3279.JPG`–`IMG_3325.JPG` (origin/main, 2026-06-28 ingested)
- 4 AppDev-Screenshots `raw/raw/Business/AppDev/` (Doctolib Onboarding/Preboarding-Kontext)
