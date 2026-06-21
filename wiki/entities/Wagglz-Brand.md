# Wagglz Brand Identity

**Typ:** Brand Design System
**Designer:** Julia Akenteva
**Datum:** Juni/Juli 2024
**Dokument:** `Wagglz_Design_Concept.pdf` (12 Seiten)
**Status:** Aktiv — wird in Wagglz-App implementiert

---

## Farben (bestätigt aus Design Concept PDF)

| Name | Hex | Pantone | Verwendung |
|------|-----|---------|-----------|
| **Ultramarine** (Primary) | `#2E54CE` | Pantone 2132C | Hauptfarbe, Sidebar, Buttons, Highlights |
| **Lime** (Accent) | `#CCFFB0` | Pantone 372C | Akzente, CTA-Highlights, aktive Indikatoren |
| **Lila / Lavender** (Secondary) | `#A6A6FF` | Pantone 2705C | Sekundäre UI-Elemente, Tags |

### Tints (offiziell aus Design System)
| Tint | Hex | Basis |
|------|-----|-------|
| Lime Light | `#E6FFD9` | Lime 60% |
| Lime Lightest | `#F9FFF3` | Lime 20% |
| Lavender Mid | `#C3C3FF` | Lila 60% |
| Lavender Light | `#F6F6FF` | Lila 10% |

---

## Typografie

**Primärschrift:** Poppins (Google Fonts / SIL Open Font License)

| Gewicht | Verwendung |
|---------|-----------|
| Black (900) | Display-Überschriften |
| Medium (500) | Subtitel, Nav-Labels |
| Regular (400) | Fließtext |
| Light (300) | Captions, Metadaten |

Alle 9 Gewichte (100–900) im ZIP `Wagglz-20260619T195338Z-3-001.zip` unter `Wagglz/Fonts/`.

---

## Logomark

### Wortmarke "Wagglz"
- Eigene Bubble-Schrift (kein Standardfont)
- Das "W" zeigt einen stilisierten Hundekopf — Ohren als W-Bögen, Punkte = Augen, Strich = Nase
- Trailing "~" am Ende = Wag/Schwanzwedeln-Symbol
- Farbvarianten: Ultramarine auf Lavender · Lime auf Ultramarine · Lavender auf Ultramarine

### Icon (W-Logomark allein)
- Isoliertes W-Hundegesicht-Icon auf Lavender-Hintergrund
- Verwendbar als App-Icon, Favicon, Social-Avatar

### Dateiformate verfügbar
| Format | Datei | Verwendung |
|--------|-------|-----------|
| SVG | `Wagglz_Logo.svg` | Web, App, skalierbar |
| EPS | `Wagglz_Logo.eps` | Print, Druck |
| AI | `Wagglz_Logo.ai` | Adobe Illustrator Quelldatei |
| PNG | `Wagglz_Logo-01/02/03/04.png` | Social Media, Web |
| JPG | Raster-Versionen | Preview |

---

## Taglines (aus Designdokumenten)

- **"We get Tails wagging"** — primäre Brand-Tagline (Investoren-Pitch)
- **"Making tails happy"** — Billboard / Out-of-Home
- **"Best care for best friends"** — Outdoor-Werbung / Poster

---

## Historischer Kontext: Pivot-Geschichte

Das ursprüngliche Wagglz-Konzept (2024) war ein **Dogwalking-Abo-Service** — kein Tierarzt-PIMS:

| Aspekt | Original 2024 | Aktuell (2025+) |
|--------|---------------|-----------------|
| Produkt | Dogwalking-Abo | Tierarzt-PIMS |
| MVP | Berlin Dogwalker | Web-App für Tierärzte |
| Zielgruppe | Hundebesitzer | Tierärzte + Praxen |
| Preise | €280–525/Mo (Abo) | Noch zu definieren |
| Domain | wagglz.de | wagglz.de |

Das Brand-System (Farben, Logo, Fonts) blieb beim Pivot erhalten — funktioniert für beide Use Cases perfekt.

---

## Social Media Assets (verfügbar im ZIP)

| Plattform | Format | Datei |
|-----------|--------|-------|
| LinkedIn | Cover 1584×396 | `Wagglz_LinkedIn_Cover_1584x396_1/2.jpg` |
| LinkedIn | Personal Cover | `Wagglz_LinkedIn_Cover_Personal_1/2.jpg` |
| LinkedIn | Avatar | `Wagglz_Li_Avatar_1/2/3/4.png+jpg` |
| Facebook | Cover 851×315 | `Wagglz_FB_851x315_1.jpg` |
| Facebook | Mobile | `Wagglz_FB_Mobil_1/2.jpg` |
| Google | Profil | `Wagglz_Google.jpg`, `Wagglz_Google_2/3.png` |

---

## Visitenkarten

**Oleg Kober — CEO**
- Telefon: +49 174 9306055
- E-Mail: olegkober@wagglz.de
- Domain: wagglz.de
- Design: Ultramarine-Blue Karte, W-Logomark (groß), weiße Schrift
- Dateien: `Wagglz_BC.ai`, `Wagglz_BC.pdf`, `Wagglz_BC_Curves.ai`

---

## Was davon in der App verwendet wird

| Asset | Status | Details |
|-------|--------|---------|
| Farben | ✅ Implementiert | In `globals.css` als CSS-Variablen |
| Poppins (9 Gewichte) | ✅ Implementiert | Originale TTF aus ZIP in `public/fonts/` |
| SVG-Logo | ✅ Implementiert | `public/wagglz-logo.svg` → Sidebar |
| W-Icon | ⏳ TODO | Als Favicon + App-Icon |
| Tagline | ⏳ TODO | In Marketing-Seiten / Onboarding |
| LinkedIn Cover | ⏳ TODO | Für Social Media Launch |

---

## Quellen
- `raw/Wagglz-20260619T195338Z-3-001.zip` → `Wagglz/Design Concept/Wagglz_Design_Concept.pdf`
- `raw/Wagglz-20260619T195338Z-3-001.zip` → `Wagglz/Presentation Template/Original_Wagglz_GmbH_Investoren_Präsentation.pptx`
- Designer: Julia Akenteva (Juni/Juli 2024)
