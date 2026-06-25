---
title: Performance Coffee — Master-Auftragsbrief
module: "00"
status: aktiv
created: 2026-06-14
updated: 2026-06-14
sources:
  - raw/Business/Performance Coffee Brand/00 — Projektübersicht.md
  - raw/Business/Performance Coffee Brand/Kaffee mit Performance.md
  - raw/Business/Performance Coffee Brand/Inhaltsstoffe — Datenbank.md
  - raw/Business/Performance Coffee Brand/Kaffee — Rohstoffanalyse.md
  - raw/Business/Performance Coffee Brand/Prototyp — Hersteller & Prompt.md
  - Clippings/Best In Class Human Performance Products.md
  - Clippings/DRYLL Performance Hydration. High Salt. Zero Bullshit..md
summary: Synthese und Modul-Roadmap für Performance Coffee Brand — eCommerce/DTC only
---

# Performance Coffee — Master-Auftragsbrief

## Executive Summary

**Performance Coffee** ist eine **eCommerce-first / DTC** funktionale Kaffee-Marke für Sportler, Gründer und High Performer. Positionierung zwischen Specialty Coffee (Bonanza-Qualitätsniveau) und funktionalen Performance-Getränken (Momentous-Wissenschaft, DRYLL-no-BS-Ton).

**Scope (2026-06-14):** Ausschließlich **Online-Vertrieb** (Shopify DE, Amazon DE, Subscription). **Kein physisches Café**, kein Flagship, keine Partner-Cafés. Historische Café-Planung → `recherche/_archiv/cafe-berlin-historie.md`.

**Co-Founder-Modell:** 50/50 — Oleg (Sales/Strategie/Finanzen) + [[Hai]] (Operations/Konzept/Produkt) — **Brand-Partner**, nicht Café-Betreiber.

**Kanonischer Workspace:** `Performance Coffee Brand/` (Vault-Root)

---

## Strategischer Kontext

### Phasenmodell (DTC-only)

| Phase | Fokus | Trigger |
|-------|-------|---------|
| **1 — eCommerce** | Shopify DE, Content, Community, Subscription | SKU #1 live, Repeat-Purchase-Signal |
| **2 — Retail & Events** | Gym-Wholesale, Hyrox-Sampling, B2B (DRYLL-Modell) | CAC/LTV tragfähig, 500+ Kunden |
| **3 — Scale** | Amazon DE, EU-Expansion, RTD evaluieren | MOQ-Scale, Marke etabliert |

### Kernpositionierung

> *„Der verlässliche Partner für den Moment, wo man ihn braucht."*

Kaffee als **Performance-Tool** — präzise, verlässlich. Kein Energy Drink. Kein mindful Wellness. Kein physisches Café.

### Wettbewerbs-Referenzrahmen

| Vergleich | Übernehmen | Vermeiden |
|-----------|------------|-----------|
| **Momentous** | Science-backed, Experten-Credibility | Nur Supplements |
| **DRYLL** | Made in DE, lab-tested, Subscription, athletischer Ton | Nur Hydration |
| **Kimera/Bulletproof** | Nootropic-in-Coffee | US-Compliance-Risiko |
| **Bonanza** | Specialty-Qualitätsniveau | Pure Indulgence |
| **Four Sigmatic** | Subscription-Modell | Mushroom-Wellness-Ästhetik |

---

## Produktrichtung (Stack A — Phase 1)

| Inhaltsstoff | Dosis | Status |
|--------------|-------|--------|
| Koffein | ~140–220 mg (aus Blend) | ✅ |
| L-Theanine | 200 mg | ✅ EU Novel Food |
| L-Tyrosine | 500 mg | ✅ |
| B-Vitamine | NRV | ✅ Health Claims |

**Format:** Duo-Pack (250g Bohnen + 14–30 Sachets) — siehe [[02_Produkt_Rezeptur]]

**Longevity-Actives (NMN, Urolithin A):** Phase 3+ — siehe `recht/novel_food_longevity_wirkstoffe.md`

---

## Modul-Status

| Modul | Status | Inhalt |
|-------|--------|--------|
| [[01_Markt_Wettbewerb]] | ✅ Recherche | Global + EU/DE, Wettbewerbsmatrix, White Space |
| [[02_Produkt_Rezeptur]] | ✅ Recherche | Stack A, Format, globale Trends |
| [[03_Lieferkette_Produktion]] | Entwurf | CM-Shortlist, MOQ |
| [[04_Marke_Positionierung]] | ✅ Recherche | Positionierung, Persona, Ton |
| [[05_Recht_Regulatorik]] | Entwurf | EU-Compliance, Entity |
| [[06_Kalkulation_Pricing]] | Entwurf | COGS, RRP |
| [[07_Vermarktung_Operations]] | ✅ Recherche | Shopify DE, DTC-Playbook |

---

## Offene Entscheidungen

1. **SKU #1** — Power vs. Focus Blend + Duo-Pack final
2. **Rechtliche Entity** — Wagglz GmbH vs. neue GmbH mit Hai
3. **Markenname** — absichtlich leer
4. **CM-Outreach** — Pure Flavour / Wonnda
5. **Pricing** — RRP €49–59 Starter, Abo €39–49

---

## Entscheidungslog

| Datum | Entscheidung | Begründung |
|-------|--------------|------------|
| 2026-06-14 | Pivot eCommerce-first | Kapital-Effizienz |
| 2026-06-14 | Physisches Café deprecated | DTC-only Scope |
| 2026-06-14 | Stack A Phase 1 | Bestes Evidenz/Risiko-Verhältnis |
| 2026-06-14 | Workspace → `Performance Coffee Brand/` | Einheitliche Brand-Struktur |
| 2026-06-14 | raw/ → `Business/Performance Coffee Brand/` | Entkopplung von Café Berlin |

---

## Nächste Aktionen

1. Pure Flavour briefen (Stack A + Duo-Format)
2. Persona finalisieren → `marke/`
3. L-Theanine + L-Tyrosine Quotes → CSV
4. `python3 modelle/unit_economics.py` mit Platzhalter-Kosten
5. Shopify-Skeleton vorbereiten

---

*Wiki: [[Performance Coffee Brand]] | Partner: [[Hai]] | Entity: [[Wagglz GmbH]]*
