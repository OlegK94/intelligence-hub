# Performance Coffee Brand — Projektkontext

Dedizierter Workspace für die **Performance Coffee** Brand: eCommerce/DTC funktionale Kaffee-Marke zwischen Specialty Coffee und Performance-Getränken.

## Projektauftrag

Kapital-effiziente Kaffeemarke für Sportler, Gründer und High Performer — „der verlässliche Partner für den Moment, wo man ihn braucht."

**Scope:** ausschließlich **DTC/eCommerce** (Shopify DE, Amazon DE, Subscription). **Kein physisches Café.**

**Co-Founder:** Oleg (Strategie, Finanzen, B2B) + Hai (Operations, Konzept, Produkt).

**Pivot 2026-06-14:** Physisches Café deprecated → DTC-only. Siehe `recherche/_archiv/cafe-berlin-historie.md`.

## Ordnerstruktur

```
Performance Coffee Brand/
├── CLAUDE.md
├── .cursor/rules/
├── recherche/             ← Module 00–07
├── marke/
├── recht/
├── betrieb/
└── modelle/
```

## Konventionen

- **00** Auftragsbrief — bei wesentlichen Entscheidungen aktualisieren
- **01–07** Deutsch, YAML-Frontmatter, Querverweise `[[NN_Modul]]`
- **raw/** im Parent-Vault **unveränderlich** — zitieren, nicht editieren
- Rohquellen: `raw/Business/Performance Coffee Brand/`
- Café-Historie: `raw/_archiv/cafe-berlin-deprecated/` (deprecated)
- Wiki-Entity: `wiki/entities/Performance Coffee Brand.md`
- Parent-Suche: `python3 tools/search.py "Performance Coffee"` vom Vault-Root

## Stack A (Phase 1)

Koffein (Blend) + L-Theanine 200 mg + L-Tyrosine 500 mg + B-Vitamine NRV. Format: Duo-Pack (Bohnen + Sachet).

Longevity-Actives (NMN etc.): Phase 3+ → `recht/novel_food_longevity_wirkstoffe.md`

## Quick Start

1. `recherche/00_Auftragsbrief.md`
2. `recherche/01_Markt_Wettbewerb.md` (Marktthese)
3. Offenes Modul 03 (CM) oder 06 (Pricing)
4. `python3 modelle/unit_economics.py` nach Kosten-Updates

## Assets

- Shopify (Wagglz GmbH)
- GmbH + ~€150k Verlustvortrag
- B2B-Sales-Erfahrung
- 5 Raw-Recherche-Dateien unter `raw/Business/Performance Coffee Brand/`
