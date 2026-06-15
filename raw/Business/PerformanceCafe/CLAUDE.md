# Performance Coffee Brand — CLAUDE.md

Persistenter Projektkontext für Claude Code. Wird zu Beginn jeder Session gelesen.
Zuletzt aktualisiert: 2026-06-15

---

## Produkt

**Name:** Performance Coffee Brand (Arbeitstitel) — finaler Name siehe `brand/naming_brief.md`
**Kategorie:** Functional Coffee / Performance Beverage mit Longevity-Stack
**Kernversprechen:** Perform now. Live longer.
**MVP-Format:** Instant-Sachet (Stick-Pack)
**Skalierung:** RTD Can → Kapsel-Format (Nespresso-kompatibel)

---

## Strategischer Kontext

**Blueprint by Bryan Johnson** (blueprint.bryanjohnson.com) verkauft KEINEN Kaffee.
Sortiment: Longevity Mix Pulver, Ceremonial Matcha, Super Shrooms, Ashwagandha+Rhodiola,
NAC+Ginger+Curcumin, Essential Capsules, Creatine, Omega-3, Collagen.
→ **White Space: "The Longevity Coffee Blueprint doesn't make."**

Qualitätsniveau-Referenz Blueprint: "Science-backed, precision-dosed,
every ingredient fought for its life, no pixie-dusting, no BS."
Bryan Johnson hat Kaffee aus seinem Protokoll gestrichen.
Seine Community trinkt weiterhin Kaffee — und sucht ein Blueprint-kompatibles Produkt.

---

## Zielgruppe

1. **Athleten** (Hyrox, CrossFit, Triathlon) — Pre-Workout + Longevity-Stack
2. **Business / Executive** — Morning Deep Work, anhaltende Energie ohne Crash
3. **Biohacker / Blueprint-Follower** — wollen NMN, Urolithin A, Spermidine täglich

Gründer-Kontext: Oleg Kober, Berlin. Sales bei Doctolib GmbH.
Fitness: 188cm, 96.7kg, 20.3% KF, Hyrox aktiv. Aerobe Kapazität als Hauptlimiter.
Referenzrahmen: Bryan Johnson, Huberman Lab, Peter Attia.

---

## Bekannte Kritische Punkte

### Regulatorik
- NMN: EU Novel Food Status 2025/2026 unklar → VOR Stack-Entscheidung klären
- Urolithin A: Amazentis/Timeline Nutrition hat Patent (Mitopure) → Lizenz oder Alternative?
- Spermidine aus Weizenkeimen: Novel Food Status in DE prüfen
- NR (Nicotinamid Ribosid): Chromadex NIAGEN Patent → IP-Check
- Huperzin A: in DE als Lebensmittel verboten

### Zertifizierung (Priorität)
1. **Kölner Liste** — DACH-Standard, günstigste Option, sofort sinnvoll
2. **Informed Sport** — pan-europäisch, bei EU-Skalierung
3. **NSF Certified for Sport** — nur bei US-Expansion relevant

### Sensorik / Produktion
- NAC: Schwefelgeruch → Flavorist für Maskierung zwingend nötig
- Curcumin: hydrophob → liposomale oder mizellare Form für Löslichkeit
- NMN/NR: oxidationsempfindlich → Schutzgas-Versiegelung im Sachet
- Pilzextrakte: bitter → Röstgrad und Kaffee-Basis als natürliche Maskierung
- Light/Medium Roast bevorzugen: maximiert Chlorogensäure + Trigonellin

### Kaffee (Longevity-Joker)
- Trigonellin in Kaffee = natürliche NMN-Vorstufe (2024er Forschung)
- Chlorogensäure: AMPK-Aktivierung, Insulinsensitivität
- Light Roast maximiert beide Verbindungen
- Vietnamesischer Robusta: höchster Koffeingehalt, höchste Chlorogensäure

---

## Projekt-Status (Module)

| # | Modul | Status | Datei |
|---|-------|--------|-------|
| 0 | Longevity Science Grundlagen | ✅ abgeschlossen | research/01_longevity_science.md |
| 1 | Ingredienzen Datenbank | ⬜ leer | research/02_ingredienzen_db.md |
| 2 | Kaffee-Spezifikation | ⬜ leer | research/03_kaffee_specs.md |
| 3 | Marktanalyse + Wettbewerb | ⬜ leer | research/04_marktanalyse.md |
| 4 | Prototyp-Partner | ⬜ leer | research/05_prototyp_partner.md |
| 5 | Regulatorik + IP | ⬜ leer | research/06_regulatorik.md |
| 6 | Business Case + Unit Economics | ⬜ leer | research/07_business_case.md |
| 7 | Brand & Naming | ⬜ leer | brand/naming_brief.md |
| 8 | IP & Patent-Landschaft | ⬜ leer | legal/ip_landscape.md |
| 9 | Unit Economics Modell | ⬜ leer | models/unit_economics.py |

Status: ⬜ leer | 🔄 in Arbeit | ✅ abgeschlossen | ⚠️ Blocker

---

## Dateistruktur

```
performance-cafe/
├── CLAUDE.md                          ← du bist hier (Claude Code liest das)
├── .cursor/rules/
│   └── performance_cafe.mdc           ← Cursor liest das
├── research/
│   ├── 00_master_brief.md             ← vollständiger Master Prompt
│   ├── 01_longevity_science.md
│   ├── 02_ingredienzen_db.md
│   ├── 03_kaffee_specs.md
│   ├── 04_marktanalyse.md
│   ├── 05_prototyp_partner.md
│   ├── 06_regulatorik.md
│   └── 07_business_case.md
├── brand/
│   ├── naming_brief.md
│   └── positioning.md
├── legal/
│   ├── ip_landscape.md
│   └── entity_structure.md
├── models/
│   ├── unit_economics.py
│   └── ingredient_db.csv
└── ops/
    ├── supplier_list.md
    └── certification_roadmap.md
```

---

## Arbeitsweise

- **Sprache:** Immer auf Deutsch antworten
- **Format:** Markdown mit Frontmatter (`status`, `priority`, `date`, `modul`)
- **Qualität:** Konkrete Firmen, Dosierungen, Preise, Kontakte — keine Allgemeinheiten
- **Quellen:** Bei Recherche web_search nutzen, aktuelle Daten bevorzugen (2024/2025)
- **Dateien:** Output immer in die entsprechende Moduldatei schreiben, nicht nur in den Chat
- **Blocker:** Wenn ein Modul von einem anderen abhängt (z.B. Regulatorik vor Stack-Entscheidung), explizit markieren
- **Rückfragen:** Kurz klären wenn unklar, nicht stillschweigend optimieren

## Claude Code Befehle

```bash
# Modul starten
"Arbeite Modul 1 (Ingredienzen) aus. Schreibe Ergebnisse nach research/02_ingredienzen_db.md"

# Status prüfen
"Zeige mir den aktuellen Status aller Module aus CLAUDE.md"

# Modul verknüpfen
"Lies research/02_ingredienzen_db.md und aktualisiere research/06_regulatorik.md
 mit dem Novel Food Status aller Inhaltsstoffe"

# Finanzmodell
"Fülle models/unit_economics.py mit den Rohstoffpreisen aus research/02_ingredienzen_db.md"
```
