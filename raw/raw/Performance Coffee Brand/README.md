# Performance Coffee Brand — Projekt-Setup

**eCommerce/DTC-only** funktionale Kaffee-Marke. Masterbrief: `recherche/00_Auftragsbrief.md`.

**Kanonischer Projektroot:** `Performance Coffee Brand/` (Vault-Root)

**Scope:** Kein physisches Café. Historische Café-Notizen → `recherche/_archiv/cafe-berlin-historie.md`

---

## Quick Start

### Obsidian
Vault-Root `Intelligence Hub` öffnen → Ordner `Performance Coffee Brand/` ist der aktive Workspace.

### Cursor
`.cursor/rules/performance_coffee.mdc` lädt Projektkontext automatisch.

### Claude Code
```bash
cd "Performance Coffee Brand"
claude  # liest CLAUDE.md automatisch
```

---

## Recherche-Module

| Modul | Datei | Status | Fokus |
|-------|-------|--------|-------|
| 00 | `recherche/00_Auftragsbrief.md` | ✅ aktiv | Synthese + Roadmap |
| 01 | `recherche/01_Markt_Wettbewerb.md` | ✅ Recherche | Global + EU/DE Markt |
| 02 | `recherche/02_Produkt_Rezeptur.md` | ✅ Recherche | Stack A, Formate |
| 03 | `recherche/03_Lieferkette_Produktion.md` | Entwurf | CM, Lohnröster |
| 04 | `recherche/04_Marke_Positionierung.md` | ✅ Recherche | Positionierung, Ton |
| 05 | `recherche/05_Recht_Regulatorik.md` | Entwurf | EU-Compliance |
| 06 | `recherche/06_Kalkulation_Pricing.md` | Entwurf | COGS, RRP |
| 07 | `recherche/07_Vermarktung_Operations.md` | ✅ Recherche | Shopify DE, DTC |

**Priorität:** Modul 03 (CM-Anfrage) → 06 (COGS) → Shopify-Skeleton

**Plausibilitätsprüfung:** `PRUEFHINWEISE.md`

---

## Dateistruktur

```
Performance Coffee Brand/
├── CLAUDE.md
├── README.md
├── PRUEFHINWEISE.md
├── .cursor/rules/performance_coffee.mdc
├── recherche/                    ← Module 00–07
│   ├── 00_Auftragsbrief.md
│   ├── 01–07_*.md
│   └── _archiv/
│       └── cafe-berlin-historie.md
├── marke/
├── recht/
│   └── novel_food_longevity_wirkstoffe.md
├── betrieb/
└── modelle/
    ├── unit_economics.py
    └── inhaltsstoffe_db.csv
```

---

## Parent Vault — Rohquellen (read-only)

- `raw/Business/Performance Coffee Brand/` (5 Dateien)
- `raw/_archiv/cafe-berlin-deprecated/` (historische Café-Dokumente, ingested Partnership Hai)

---

## Archiviert (2026-06-14)

- `performance-coffee/` + `performance-cafe/` → merged in diesen Ordner
- `raw/Business/Cafe/` → aufgelöst; Brand-Docs nach `raw/Business/Performance Coffee Brand/`
- Physische Café-Planung → `raw/_archiv/cafe-berlin-deprecated/`
