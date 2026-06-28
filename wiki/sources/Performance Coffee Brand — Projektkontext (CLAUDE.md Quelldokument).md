---
title: "Performance Coffee Brand — Projektkontext (CLAUDE.md Quelldokument)"
type: source
tags: [performance-coffee, dtc, kaffee, shopify, amazon, subscription, oleg, hai, wagglz, pivot, modul, rohquellen, orcheska, konventionen, quick-start]
sources: ["raw/Business/Performance Coffee Brand/CLAUDE.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Dedizierter Workspace für Performance Coffee Brand DTC/eCommerce — Scope: Shopify DE / Amazon DE / Subscription (kein Café); Co-Founder Oleg + Hai; Pivot 2026-06-14 physisches Café deprecated; Modular-Struktur (00–07); Phase 1 Stack: Koffein + L-Theanine 200mg + L-Tyrosine 500mg + B-Vitamine NRV; Longevity Phase 3+; Rohquellen unter raw/Business/Performance Coffee Brand/
---

# Performance Coffee Brand — Projektkontext (CLAUDE.md Quelldokument)

## Überblick

Dieses Quelldokument ist das zentrale Projektmanifest für die **Performance Coffee Brand** — eine dedizierte Workspace-Dokumentation, die Auftragsbrief, Ordnerstruktur, Konventionen, Stack-Definition und Quick-Start-Anleitung konsolidiert.

> Für die Entitätszusammenfassung und Strategieübersicht siehe [[Performance Coffee Brand]].

## Projektauftrag (Executive Summary)

**Performance Coffee Brand** ist eine **kapital-effiziente Kaffeemarke** für Sportler, Gründer und High Performer — "der verlässliche Partner für den Moment, wo man ihn braucht."

- **Geschäftsmodell:** DTC/eCommerce only (Shopify DE, Amazon DE, Subscription-Modell)
- **Nicht enthalten:** Physisches Café (Pivot 2026-06-14)
- **Co-Founder:** Oleg (Strategie, Finanzen, B2B) + Hai (Operations, Konzept, Produkt)
- **Parent-Entity:** [[Wagglz GmbH]]

## Ordnerstruktur

```
Performance Coffee Brand/
├── CLAUDE.md ← dieses Dokument
├── README.md
├── .cursor/rules/
├── recherche/             ← Module 00–07
│   ├── 00_Auftragsbrief.md
│   ├── 01_Markt_Wettbewerb.md
│   ├── 02_CMO_Sourcing.md
│   ├── 03_Content_Marketing.md
│   ├── 04_Produkt_Packaging.md
│   ├── 05_Ecommerce_Setup.md
│   ├── 06_Pricing_Unit_Economics.md
│   ├── 07_Branding_Naming.md
│   └── 08_IP_Landscape_Novel_Food.md
├── marke/
│   ├── naming_brief.md
│   ├── brand_identity.md
│   └── messaging.md
├── recht/
│   ├── novel_food_longevity_wirkstoffe.md
│   ├── health_claims.md
│   └── ip_landscape.md
├── betrieb/
│   ├── supplier_list.md
│   ├── cmo_evaluation_template.md
│   └── unit_economics.py
└── modelle/
    ├── unit_economics.py
    └── pricing_calculator.py
```

## Projektkonventionen

1. **Modul 00:** Auftragsbrief — bei wesentlichen Entscheidungen aktualisieren
2. **Module 01–07:** Deutsche Sprache, YAML-Frontmatter auf jeder Seite
3. **Querverweise:** Wiki-Links mit `[[Modul-Name]]` oder `[[Entität-Name]]`
4. **Rohquellen:** Unveränderlich unter `raw/Business/Performance Coffee Brand/`
   - **Nicht in die Wiki bearbeiten** — zitieren und verlinken statt editieren
5. **Café-Geschichte (deprecated):** `raw/_archiv/cafe-berlin-deprecated/`
6. **Wiki-Entity:** `wiki/entities/Performance Coffee Brand.md`
7. **Suche:** `python3 tools/search.py "Performance Coffee"` vom Vault-Root

## Stack A (Phase 1) — MVP-Formulierung

**Bereitgestellt:** Koffein (Blend) + Functional Additives

| Inhaltsstoff | Menge | Funktion |
|---|---|---|
| Koffein | Blend-Basis | Wachheit, mentale Klarheit |
| L-Theanine | 200 mg | Ruhiger, fokussierter Fokus (mit Koffein-Synergie) |
| L-Tyrosine | 500 mg | Dopamin-Unterstützung, kognitive Klarheit |
| B-Vitamine | NRV | Energiestoffwechsel, Müdigkeitsreduktion |
| Ashwagandha KSM-66 | 300 mg | Stressresilienz, Cortisolmodulation |

**Format:** Duo-Pack (Kaffeebohnen + Funktionales Sachet).

## Longevity-Wirkstoffe (Phase 3+)

**Geplant (abhängig von IP + Novel Food-Klärung):**
- Urolithin A ([[Amazentis]])
- NMN / NR (Niagen Bioscience)
- Weitere adaptogens

**Siehe:** `recht/novel_food_longevity_wirkstoffe.md` für IP- und Regulierungs-Blocker.

## Quick-Start-Pfad

1. **Starten mit:** `recherche/00_Auftragsbrief.md`
2. **Marktthese (Wettbewerb):** `recherche/01_Markt_Wettbewerb.md`
3. **Offenes Modul:** 03 (Content Marketing) oder 06 (Pricing)
4. **Unit Economics rechnen:** `python3 modelle/unit_economics.py` nach Kosten-Updates

## Assets & Finanzielle Basis

- **Shopify-Konto:** Unter Wagglz GmbH registriert
- **Geschäftskonto:** Wagglz Finom
- **Kapitalgrundlage:** ~€150k Verlustvortrag
- **IP-Erfahrung:** B2B-Sales-Background (Oleg)
- **Rohquellen:** 5 Raw-Recherche-Dateien unter `raw/Business/Performance Coffee Brand/`

## Pivot-Historie

- **2026-06-14:** Physisches Café Berlin deprecated
- **Begründung:** DTC-only-Fokus effizienter für MVP + Skalierung
- **Archiv:** `recherche/_archiv/cafe-berlin-historie.md`

## Verwandte Seiten

- [[Performance Coffee Brand]] — Entitätsseite
- [[Aevum]] — Markenname (Pivot nach Modul 07)
- [[CMO Sourcing Performance Coffee]] — Supplier-Evaluierung
- [[Performance Café IP Landscape]] — Patent- & Novel Food-Barrieren
- [[Wagglz GmbH]] — Parent-Entity
- [[Oleg Personal Context]] — Co-Founder
- [[Hai Personal Context]] — Co-Founder
