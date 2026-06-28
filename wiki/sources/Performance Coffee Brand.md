---
title: "Performance Coffee Brand"
type: source
tags: [performance-cafe, kaffee, dtc, ecommerce, longevity, funktionell, modul-00-07, recherche, marke, aevum, cmo, novel-food, stack-a-b-c, haiwagen]
sources: ["raw/raw/Performance Coffee Brand/README.md"]
created: 2026-06-20
updated: 2026-06-20
summary: Quelldokument für die Performance Coffee Brand — DTC/eCommerce-only funktionale Kaffee-Marke; kanonischer Projektroot `Performance Coffee Brand/`; Recherche-Module 00–07 (Markt, Produkt, Lieferkette, Kalkulation, Vermarktung); Priorität Modul 03 (CMO-Anfrage) → 06 (COGS) → Shopify-Grundgerüst
---

# Performance Coffee Brand — Quelldokument

## Überblick

Dies ist die primäre Quelldokumentseite für das **Performance Coffee Brand**-Projekt — eine eCommerce/DTC-only funktionale Kaffee-Marke mit kanonischem Projektroot `Performance Coffee Brand/` im Vault.

> Für die konzeptionelle Übersichtsseite siehe [[Performance Coffee Brand Entity]] — Synthese aller Quellen und Modul-Übersicht.

## Projektstruktur

### Recherche-Module (00–07)

Das Projekt folgt einem strukturierten 8-Modul-Ansatz:

| Modul | Datei | Status | Fokus |
|-------|-------|--------|-------|
| **00** | `recherche/00_Auftragsbrief.md` | ✅ aktiv | Synthese + Roadmap + Geschwindigkeit |
| **01** | `recherche/01_Markt_Wettbewerb.md` | ✅ Recherche | Global + EU/DE Markt; Wettbewerber (Blueprint, Function, Beantown, Happy Coffee, Dripkit) |
| **02** | `recherche/02_Produkt_Rezeptur.md` | ✅ Recherche | Stack A, B, C; Formate (Sachets, Pulver, Kapseln) |
| **03** | `recherche/03_Lieferkette_Produktion.md` | Entwurf | CMO-Sourcing (Prinova #1–5), Kaffee-Lieferanten, GMP-Anforderungen |
| **04** | `recherche/04_Marke_Positionierung.md` | ✅ Recherche | Namengebung ([[Aevum]]), Tonalität, Markendifferenzierung |
| **05** | `recherche/05_Recht_Regulatorik.md` | Entwurf | EU-Compliance, Novel Food ([[Amazentis]] Urolithin A), IP-Landscape ([[Chromadex]] NMN/NIAGEN) |
| **06** | `recherche/06_Kalkulation_Pricing.md` | Entwurf | COGS-Modell, RRP, Margin-Szenarien, CMO-Kosten-Integration |
| **07** | `recherche/07_Vermarktung_Operations.md` | ✅ Recherche | Shopify DE, DTC-Kanal-Mix, Branding, Launch-Roadmap |

### Prioritätsfolge (Handlung)

1. **→ Modul 03 (CMO-Anfrage):** Prinova, Lehvoss, Nutri-Epitech kontaktieren; Angebote sammeln
2. **→ Modul 06 (COGS):** CMO-Kostenmodell in Kalkulationssimulation integrieren
3. **→ Modul 07 (Shopify-Grundgerüst):** Shop-Struktur, Payment, Fulfillment

## Dateistruktur

```
Performance Coffee Brand/
├── CLAUDE.md                      ← Cursor/Claude Code Kontext-Datei
├── README.md                      ← Diese Datei (Projektstruktur)
├── PRUEFHINWEISE.md              ← Plausibilitätsprüfung für alle Module
├── .cursor/rules/
│   └── performance_coffee.mdc     ← Cursor-Regelwerk
├── recherche/                     ← Module 00–07
│   ├── 00_Auftragsbrief.md
│   ├── 01_Markt_Wettbewerb.md
│   ├── 02_Produkt_Rezeptur.md
│   ├── 03_Lieferkette_Produktion.md
│   ├── 04_Marke_Positionierung.md
│   ├── 05_Recht_Regulatorik.md
│   ├── 06_Kalkulation_Pricing.md
│   ├── 07_Vermarktung_Operations.md
│   └── _archiv/
│       └── cafe-berlin-historie.md  ← Archiviert (2026-06-14)
├── marke/
│   ├── naming_brief.md
│   ├── Aevum-Briefing/
│   └── positioning_guide.md
├── recht/
│   ├── novel_food_longevity_wirkstoffe.md
│   ├── ip_landscape.md
│   └── regulatory_checklist.md
├── betrieb/
│   ├── cmo_sourcing.md
│   ├── supplier_list.md
│   └── cmo-email-template.md
├── modelle/
│   ├── unit_economics.py
│   ├── inhaltsstoffe_db.csv
│   └── cogs_simulator.py
└── hai-onepager.md                ← Executive Summary (Wai-/Haiwagen-Format)
```

## Quick Start

### Obsidian
1. Vault-Root `Intelligence Hub` öffnen
2. Ordner `Performance Coffee Brand/` ist der aktive Workspace
3. Navigation über `README.md` → `recherche/00_Auftragsbrief.md`

### Cursor
Datei `.cursor/rules/performance_coffee.mdc` wird automatisch geladen und lädt den Projektkontext.

```bash
# Cursor-Fenster öffnen; das Projekt wird automatisch kontextualisiert
cursor "Performance Coffee Brand"
```

### Claude Code (lokal)
```bash
cd "Performance Coffee Brand"
claude  # liest CLAUDE.md automatisch
```

## Zeitliche Einordnung & Archivierung

**Status 2026-06-20:**
- Modul 00–02, 04, 07: ✅ Recherche weitgehend abgeschlossen
- Modul 03, 05, 06: ⏳ In Bearbeitung
- Physisches Café: **Archiviert** (2026-06-14) → `recherche/_archiv/cafe-berlin-historie.md`
- Alte Projekt-Ordner gemerged:
  - `performance-coffee/` + `performance-cafe/` → zentralisiert zu `Performance Coffee Brand/`
  - `raw/Business/Cafe/` → aufgelöst
  - Partner Hai-Dokumente → separat gelegen, Ingest ausstehend

## Verwandte Seiten

- [[Performance Coffee Brand Entity]] — Entitäts-Übersichtsseite mit Modul-Synthese
- [[Aevum — Performance Coffee Markenname]] — Namengebungs-Entität
- [[CMO Sourcing Performance Coffee]] — CMO-Priorisierungsliste (Modul 03)
- [[IP Risk Matrix Performance Coffee]] — Regulatorische + IP-Blocker (Modul 05)
- [[Amazentis]] — IP-Blocker Urolithin A
- [[Chromadex Niagen Bioscience]] — IP-Blocker NMN
- [[Novel Food Regulation]] — EU-Regulierung für neue Inhaltsstoffe
