---
title: Wagglz App Wireframes 2025
type: source
tags: [wagglz, wireframes, ux, design, onboarding, kalender, marketing, referenz]
sources: ["raw/assets/wagglz-tier/7RI3XqEc3RR6znirkakZcm/ (19 Dateien)"]
created: 2026-06-30
updated: 2026-06-30
summary: Frühe Wagglz-Wireframes und UX-Referenzen aus 2024/2025 — Onboarding-Wizard, Kalender, Marketing-Landing, Demo-Form sowie Inspirationsquellen (Fantastical, Defcon/Linear)
---

# Wagglz App Wireframes 2025

Vollständige Inventur der **19 Assets** in `raw/assets/wagglz-tier/7RI3XqEc3RR6znirkakZcm/` — frühe Wagglz-Wireframes (Low-Fidelity, schwarz/weiß) aus 2024–2025 sowie Design-Referenzscreenshots.

---

## A) Wagglz Onboarding-Wizard (9 Screens, `01-*.png`)

**Wireframe-Serie: „Create an account" — 6-stufiger Links-Wizard**

| Screen | Schritt | Inhalt |
|--------|---------|--------|
| `01-1` | **Business Information** | Typ wählen: „Create a praxis profile" / „Create a clinic profile" — 2 Radio-Cards, Next-Button |
| `01-2` | Business Information (Detail) | Weitere Geschäftsdaten |
| `01-3` | Business Information (3) | — |
| `01-4` | **Contact Details** | Kontaktangaben |
| `01-5` | **Veterinarian Information** | Tierarzt-Stammdaten |
| `01-6` | **Operating Information** | Betriebszeiten etc. |
| `01-7` | **Technical Requirements** | Hardware/Software-Anforderungen |
| `01-8` | **Add Employee Profiles** | Mitarbeiter anlegen |
| `01-9` | Add Employee Profiles (Fortsetzung) | — |

**Navbar:** Logo + DE/EN-Toggle — kein Wagglz-Logo, noch Platzhalter.

**Wizard-Design:** Vertikale Fortschrittsleiste links (Kreis-Nummern 1–6), Content rechts. Genau das Pattern, das heute als `OnboardingWizard` in Wagglz-App (`app/(auth)/onboarding/`) gebaut ist ✅.

**Wagglz-Learning:** Original-Vision bestätigt: Praxis vs. Klinik als erste Entscheidung — relevante Unterscheidung für spätere Multi-Standort/Triage-Board-Features (Provet Pro-Tier).

---

## B) Wagglz Marketing-Website Wireframes (`arrange-a-demo.png`, `arrange-a-demo-2.png`)

**Frühe Landing-Page mit Demo-Request-Flow:**

**`arrange-a-demo.png`** — Hauptseite:
- Navbar: Logo-Placeholder + **„Pet Owners"**-Button (CTA für Tierhalter-Portal) + DE/EN-Toggle
- Hero: Grau-Overlay, „Headline" + Lorem-ipsum — Platzhalter
- Sektion „Let's get town to business!": Formular mit Feldern Practice name*, Practice Adresse, E-Mail*, Phone*, First/Last Name*, Role, Desired appointment, Desired time, Privacy Policy-Checkbox + **„Arrange a demo"**-CTA (schwarzer Pill-Button)

**`arrange-a-demo-2.png`** — Erfolgsseite nach Absenden:
- „Thank you for your request" + „Go to the homepage"-Link

**Wagglz-Learning:**
- „Pet Owners"-Button in Navbar von Anfang an als eigene Zielgruppe geplant → bestätigt Tierhalter-Portal als Kern-Differenzierer
- DE/EN bilingual von Beginn an — spricht für internationale Ambition (DACH + UK?)
- Einfache Demo-Form statt Self-Serve-Onboarding — frühes B2B-Sales-Modell

---

## C) Design-Referenz-Screenshots (Inspirationsquellen)

### `fantastical.png` — Fantastical macOS (Dark Mode, Feb 2021)
- Linke Sidebar: Mini-Monatskalender + farbcodierte Terminliste mit „TODAY/TOMORROW/MONDAY..." — **die „Anstehende Termine"-Leiste**, die in Wagglz CLAUDE.md §10 als „Fantastical-inspiriert ✅ gebaut" vermerkt ist
- Hauptbereich: Wochenansicht Mo–Sa, farbige Terminblöcke
- **Direkte Wagglz-Inspiration** für die Kalender-Sidebar (schon implementiert)

### `calendar-week.png` — „Defcon systems" (Linear/Projekt-Tool-Stil, Okt 2024)
- Multi-Person-Kalender: Spalten pro Teammitglied (Mitchel Fleen, Mandy Harley, Hank Williams, Joanna Salem, Hanna Rodrigues)
- Farbcodierte Events (grün/rosa/blau/orange/grau)
- **Referenz für Behandler-Spalten-Kalender** (Provet-Pattern ADOPT — noch nicht gebaut in Wagglz)

### `wireframe-1.png` — Früher Wagglz-App-Kalender (Feb 2025)
- Einfache Wochenansicht Mo–Sa, 22–27 Feb 2025
- „Martin Musterman" als Platzhalter-Patient (8:00 Uhr Dienstag + Mittwoch, 8:30 Mittwoch)
- Sidebar: My Calendar + My Task — sehr minimales Wireframe
- Zeigt den Ausgangszustand vor der aktuellen `KalenderWochenansicht.tsx`-Implementierung

---

## D) UI-Elemente

| Datei | Inhalt |
|-------|--------|
| `frame.png` | „Praxis Registration" — schwarzer Pill-Button |
| `frame-2.png` | „Banking payment details?" — dunkelgrauer Pill-Button |
| `1.png` | (weitere UI-Element) |
| `a4-1.png` | (A4-Format-Mockup) |
| `Image.jpg` | (Referenzbild in `raw/assets/`) |

---

## WhatsApp-Screenshots (frühe App-Demos, `WhatsApp Image 2024-06-*.jpeg`)

6 WhatsApp-Bilder vom 05.–06. Juni 2024 — sehr frühe App-Demo-Screens, die per WhatsApp geteilt wurden. Nicht einzeln analysiert (niedrige Auflösung, interne Kommunikation).

---

## Konsolidierte Wagglz-Learnings (Wireframe-Analyse)

1. **Kontinuität bestätigt:** Onboarding-Wizard (6 Schritte), Tierhalter-Portal und Kalender waren von Beginn an die 3 Kern-Flows — heute alle implementiert ✅.
2. **Behandler-Spalten-Kalender** (Defcon-Referenz) steht noch aus → ADOPT aus CLAUDE.md §10 Roadmap.
3. **Fantastical-Sidebar** als explizite Design-Inspiration dokumentiert — Differenzierer gegenüber Provet/Vetera.
4. **DE/EN bilingual** war früh im Design — für UK-Expansion relevant.
5. **Frühes Demo-Form-Modell** (kein Self-Serve) wurde inzwischen durch direktes Onboarding ersetzt.

## Verbindungen
- [[Wagglz]], [[Wagglz App UI Screens]]
- Wettbewerb: [[Wagglz UX Playbook — Adopt & Optimize]]
- Kalender: `components/kalender/KalenderWochenansicht.tsx`
- Onboarding: `app/(auth)/onboarding/`
