---
title: PetLeo App Screenshots 2026-06
type: source
tags: [petleo, wettbewerb, ux, wagglz, tierhalter-app, onboarding, dsgvo, heimtierausweis]
sources: ["User-Upload 2026-06-29 (2 Screenshots)", "raw/Business/Wagglz/Wagglz Wettbewerber.md"]
created: 2026-06-29
updated: 2026-06-29
summary: Analyse der PetLeo Tierhalter-App (mobile, petrol/türkis) — digitale Patienten-Aufnahme mit DSGVO-Consent + EU-Heimtierausweis-Scan; direkte UX-Referenz für Wagglz' Tierhalter-Portal
---

# PetLeo App Screenshots 2026-06

Analyse der **PetLeo-Tierhalter-App** (mobile iOS, [[Petleo]] — pet.petleo.net), aufgenommen von Oleg. PetLeo ist die **Tierhalter-/Pet-Owner-facing App** — genau das Segment, das Wagglz' Kern-Differenzierer ist (Feature #5 Tierhalter-Portal + elektronischer Pet-Pass).

> ⚠️ **Unvollständig:** Laut Oleg gibt es eine ganze Serie PetLeo-Screenshots (die **petrol/türkisfarbenen** Mobile-Screens), die im Kamera-Ordner **mit den Doctolib-Screenshots gemischt** sind. **Diese sind NICHT ins Repo gesynct/gepusht** worden — der Ordner `raw/raw/Doctolib /` enthält ausschließlich die 47 Doctolib-Desktop-Fotos (alle 5712×4284 Querformat). Bisher liegen nur **2 PetLeo-Screenshots** (User-Upload) vor. Vollständige Analyse sobald der PetLeo-Ordner gepusht ist.

## Design-System (PetLeo)
- **Primärfarbe:** Petrol/Teal `#2D8A8F`-Ton (Hintergrund + Buttons)
- **Akzente:** Creme/Gelb (`#F2D98D`-Ton, sekundäre Buttons „Weiter") + **Pink/Coral** (Fortschrittsbalken + Links)
- **Stil:** Mobile-first, freundlich-verspielt (illustrative Icons), große Touch-Targets, viel Whitespace
- **Kontrast zu Wagglz:** Wagglz nutzt Slate/Indigo (B2B-premium); PetLeo ist wärmer/konsumiger (B2C-Tierhalter). Für Wagglz' **Tierhalter-Portal** (`app/portal/`) ist ein wärmerer, mobile-first Ton durchaus übertragbar.

## Erfasste Screens (2)

### 1. Digitale Patienten-Aufnahme — DSGVO-Consent (17:37)
- Header „Digitalen Patienten-Aufnahme" mit Zurück-Pfeil + **pinkem Fortschrittsbalken** (mehrstufiger Wizard).
- Titel „Bitte überprüfen Sie die Kundenregistrierungsdetails".
- **Feld „Haustier(e)"**: „Oleg" (editierbar, Stift-Icon).
- **Feld „Ort"**: „Tierarztpraxis | Dr. Oczipka" (Mindener Str. 22, 10589 Berlin).
- **DSGVO-Einwilligungstext** + 2 Opt-in-Checkboxen:
  1. „…dass die erhobenen Daten auch für **zukünftige Behandlungsverträge** genutzt werden dürfen." *(Pflicht)*
  2. „…dass die Daten im Rahmen **tierärztlicher Überweisungen** an andere Praxen/-kliniken, zur **Diagnostik an Untersuchungslabore** und zur **Abrechnung an Verrechnungsstellen** übermittelt werden."
- Button „Zustimmung erteilen" (Teal) + Link „Datenschutzerklärung und Anhänge herunterladen" (Pink).
- **Wagglz-Learning:** Das ist der **digitale Aufnahme-/Onboarding-Flow für den Tierhalter VOR dem Termin** (= Provets „Before Check-in" / pre-visit forms, aber mobil & DSGVO-nativ). Wagglz braucht genau diesen Consent-Flow: granulare Einwilligungen (Folgebehandlung / Datenweitergabe an Labore+Verrechnungsstellen) — deckt sich mit der Datenübermittlungs-Transparenz aus Doctolib (IMG_3311) und mit Wagglz §7 DSGVO/TÄHAV. **Direkt für `app/portal/` Onboarding übernehmen.**

### 2. EU-Heimtierausweis / Impfpass-Scan (17:34, „Neu")
- Teal Vollbild-Onboarding-Karte, Badge „Neu", Schließen-X.
- EU-Pass-Illustration + Titel „Wählen Sie die Art des Dokuments, das Sie besitzen" — „Besitzen Sie einen Heimtierausweis oder einen Impfpass?".
- **2 Auswahl-Karten:** „HEIMTIER-AUSWEIS" (blau-türkis EU-Pass, „DE 00 1234567") vs. „TIER IMPFPASS" (gelb).
- Hinweis: „Diese Angaben beziehen sich auf den blauen (EU-)Heimtierausweis. Für gelbe/orange Pässe bitte nur die Seitentitel vergleichen."
- Button „Weiter" (Creme/Gelb).
- **Wagglz-Learning:** ⭐ **EU-Heimtierausweis-Scan zur Auto-Befüllung der Tierdaten** (Chip-Nr., Impfungen, Signalement). Das ist exakt der **„Electronic Pet Passport"** aus Wagglz CLAUDE.md (§2 „Electronic Pet Passports", „Digital Anamnesis"). PetLeo zeigt den Einstieg: Pass-Typ wählen → scannen → Daten importieren. Killer-Feature fürs Tierhalter-Onboarding (spart manuelle Eingabe von Impfhistorie/Chip-Nr.). **Hohe Priorität für Wagglz-Differenzierung** — weder Vetera noch Provet zeigen einen tierhalterseitigen Pass-Scan.

## Top-Wagglz-Learnings (PetLeo = Tierhalter-Seite)
1. ⭐ **EU-Heimtierausweis-Scan** → Auto-Import von Chip-Nr./Impfungen/Signalement ins Tierprofil (Wagglz E-Pet-Pass).
2. ⭐ **Mobile digitale Patienten-Aufnahme** als mehrstufiger Wizard mit Fortschrittsbalken — Tierhalter füllt VOR dem Termin aus (entlastet Empfang, = Provet „pre-visit forms").
3. **Granulare DSGVO-Consent-Checkboxen** (Folgebehandlung / Datenweitergabe Labore+Verrechnungsstellen) mit Pflicht-Markierung + Datenschutz-Download.
4. **Wärmerer B2C-Ton** fürs Tierhalter-Portal (Teal/Creme/Coral, illustrativ) — bewusst anders als die B2B-Vet-Oberfläche.
5. **Praxis-Kontext sichtbar** (Tierhalter sieht „Tierarztpraxis Dr. Oczipka") — Multi-Praxis-Zuordnung im Portal.

## Verbindungen
- [[Petleo]] (Entity — Wettbewerber Booking + Tierhalter-App), [[Wagglz Wettbewerber]].
- Komplementär: [[Doctolib Software Screenshots 2026-06]] (Praxis-Seite), [[Provet Cloud + Vetera Screenshots 2026-06]] (Vet-PMS).
- Wagglz: [[Wagglz App UI Screens]], [[Wagglz]] — Tierhalter-Portal (`app/portal/`) + E-Pet-Pass.

## Offen
- **Vollständige PetLeo-Screenshot-Serie pushen** (die petrol/türkisen Mobile-Screens, gemischt mit den Doctolib-Fotos im Kamera-Ordner) → dann komplette Flow-Analyse (Registrierung, Tierprofil, Terminbuchung, Impfhistorie, Dokumente).

## Quellen
- 2 PetLeo-Screenshots (User-Upload 2026-06-29): „Digitale Patienten-Aufnahme" (17:37), „Heimtierausweis-Scan" (17:34)
- [[Petleo]] Entity / `raw/Business/Wagglz/Wagglz Wettbewerber.md`
