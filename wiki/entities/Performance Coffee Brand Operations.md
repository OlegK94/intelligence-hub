tags: [performance-cafe, betrieb, operations, cmo, sourcing, lieferanten, shopify, launch, supplier-list, fulfillment, kpi]
sources: ["raw/Business/PerformanceCafe/betrieb/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Operations workspace für Performance Coffee Brand — CMO Sourcing (5 Kandidaten), Lieferantenkontakte, Shopify-Setup, Launch-Runbook, Fulfillment-SOP, KPI-Tracking; Querverweis zu Recherche (Markt, Produkt, Lieferkette), Kalkulation, Vermarktung; CMO-Outreach und Launch-Checkliste ausstehend
---

# Performance Coffee Brand Operations (betrieb/)

## Überblick

**Performance Coffee Brand Operations** ist der operative Workspace (`betrieb/`) für die [[Performance Coffee Brand]]. Er konsolidiert die tägliche Ausführung von Supply-Chain-Management, Lieferantenkommunikation, eCommerce-Setup und Launch-Aktivitäten.

---

## Zweck

**Operative Ausführung tracken:**
- Lieferantenkontakte, Angebote, Kommunikation
- Contract Manufacturer (CMO) Sourcing und Evaluierung
- Shopify-Setup und App-Stack
- Fulfillment-Operationen (Pick, Pack, Ship, Returns)
- Launch-Runbook (Soft Launch → Public Launch)
- KPI-Tracking und Spreadsheet-Verknüpfungen

---

## Was hier hinein (In-Scope)

| Kategorie | Details |
|---|---|
| **CMO-Sourcing** | Lieferantenlisten, Angebote, RFQ-Vorlagen, Evaluierungsmatrix |
| **Lohnröster** | Kontakte, Samples, Röstprofile, Preisvergleiche |
| **Shopify-Setup** | Checkliste, App-Stack-Dokumentation, Domain-Konfiguration |
| **Fulfillment-SOP** | Pick → Pack → Ship → Returns-Prozess |
| **Launch-Runbook** | Soft Launch Timeline, Public Launch Checklist, Go-Live-Koordination |
| **KPI-Tracking** | Spreadsheet-Links, Dashboard-Verweise |
| **Korrespondenz-Summaries** | Zusammenfassungen von Lieferantendiskussionen (z.B. Wonnda, Pure Flavour) |

---

## Was NICHT hier (Out-of-Scope)

| Kategorie | Verweis |
|---|---|
| **Strategische Marktanalyse** | [[Performance Cafe Markt Wettbewerb]] (recherche/) |
| **Produkt-Formulierungsentscheidungen** | [[Performance Cafe Produkt Rezeptur]] (recherche/) |
| **Lieferketten-Strategie** | [[Performance Cafe Lieferkette Produktion]] (recherche/) |
| **Signierte Verträge** | Sichere Ablage + Summary in `recht/` |

---

## Verknüpfte Recherche-Module

| Modul | Relevanz |
|---|---|
| **07 Vermarktung & Operations (GTM)** | Primäres GTM-Modul; Launch-Roadmap |
| **03 Lieferkette & Produktion** | CMO und Verpackungs-Strategie |
| **06 Kalkulation & Pricing** | Pricing-Ziele und Margenziele |

---

## Lieferanten-Shortlist (aus Quelldokument)

### CMO-Kandidaten (nach Priorität)

| Priorität | Anbieter | Land | Fokus | Status |
|---|---|---|---|---|
| **#1** | [[Prinova Europe]] | Düsseldorf, DE | Inhaltsstoffe + funktionale Getränke | `recherche_noetig` |
| **#2** | [[Lehvoss Nutrition]] | Hamburg, DE | Custom Formulation | `recherche_noetig` |
| **#3** | [[Nutri-Epitech]] | Italien | Longevity-Stack-Erfahrung | `recherche_noetig` |
| **#4** | [[Aidea]] | Mailand, IT | Functional Drinks + Sachets | `recherche_noetig` |
| **#5** | [[Herbafit]] | Deutschland | Pulver-Sachets, IFS Food | `recherche_noetig` |

### Inhaltsstoffe & Rohstoffe

| Anbieter | Rolle | Status |
|---|---|---|
| [[Prinova Europe]] | Ingredienser-Lieferant | `recherche_noetig` |
| [[Pure Flavour GmbH]] | CM — funktionale Produkte | `recherche_noetig` |
| [[Wonnda.com]] | CM-Discovery-Plattform | `recherche_noetig` → **3 Kandidaten shortlisten** |
| [[Döhler GmbH]] | Scale-CM (Backup) | `zurückgestellt` |

### Kaffeeröstung

| Anbieter | Rolle | Status |
|---|---|---|
| **Lohnröster (TBD)** | Kaffeeröstung; Röstprofile | `recherche_noetig` |

---

## Vorhandene Assets

| Asset | Status | Entscheidung |
|---|---|---|
| **Shopify-Account** (Wagglz GmbH) | Vorhanden | Reuse-Entscheidung **offen** |
| **GmbH-Struktur** | Verfügbar | Ggf. für eCommerce-Operations nutzen |
| **Versicherungen** (Wagglz) | Laufend | [[ARAG Wagglz Versicherung]] (Kündigung bis 2026-06-30) |

---

## Nächste Schritte (Priorisiert)

### Phase 1 — CMO-Sourcing (diese Woche)

- [ ] **Prinova (Priority #1) Erstkontakt** — Email mit [[CMO Erstkontakt Email Template]]
- [ ] **Wonnda.com Market Scan** → 3 CMO-Kandidaten shortlisten
- [ ] **Pure Flavour Email** — Stack-A-Briefing versenden

### Phase 2 — eCommerce Setup (nächste Woche)

- [ ] Shopify-Skeleton-Store (bei Wagglz-Account oder neu)
- [ ] Domain-Registrierung (aevum.de, aevum.com) — abhängig von [[Aevum — Performance Coffee Markenname|Markenentscheidung]]
- [ ] Payment-Processor-Integration (Stripe oder ähnlich)

### Phase 3 — Product Launch (4–6 Wochen)

- [ ] CMO-Pilot-Batch (1.000–2.000 Sachets) in Auftrag geben
- [ ] Geschmackstest + Konsumentenfeedback-Runde
- [ ] Shopify-Produktlisting mit Bildern / Beschreibungen
- [ ] Soft-Launch-Koordination (Beta-Community / Newsletter)

---

## KPI-Tracking

| KPI | Quelle | Frequenz |
|---|---|---|
| **CMO-Angebote eingegangen** | Supplier-Log | Laufend |
| **Sample-Status** | Korrespondenz | Wöchentlich |
| **Shopify-Setup-Fortschritt** | Checkliste | Wöchentlich |
| **Launch-Readiness** | Runbook | Täglich vor Launch |

---

## Dokumentenstruktur (Raw)

```
raw/Business/PerformanceCafe/betrieb/
├── README.md (diese Seite — Quelldokument)
├── supplier_list.md (CMO + Inhaltsstoffe Shortlist)
├── cmo-email-template.md (Erstkontakt-Vorlage)
├── shopify-setup-checklist.md (Setup-Schritte)
├── fulfillment-sop.md (Pick/Pack/Ship/Returns)
├── launch-runbook.md (Soft Launch → Public Launch)
├── kpi-tracking.md (Spreadsheet-Verweise)
└── correspondence/
    ├── wonnda-notes.md
    ├── pure-flavour-notes.md
    └── ...
```

---

## Status

⚠️ **Leer — Initialphase**

- CMO-Outreach: **Nicht begonnen** → Priority #1 (Prinova) diese Woche starten
- Lohnröster-Anfragen: **Ausstehend**
- Shopify-Skeleton: **Ausstehend**
- Launch-Checkliste: **Vorlage vorhanden, Details abhängig von CMO-Auswahl**

---

## Verwandte Seiten

- [[Performance Coffee Brand]] — übergeordnetes Projekt
- [[CMO Sourcing Strategy Performance Coffee]] — Evaluierungsrahmen + IP-Analyse
- [[Performance Cafe Vermarktung Operations (Modul 07)]] — GTM-Roadmap
- [[Performance Cafe Lieferkette Produktion (Modul 03)]] — Supply-Chain-Strategie
- [[Performance Cafe Kalkulation Pricing (Modul 06)]] — COGS und Pricing
- [[Aevum — Performance Coffee Markenname]] — Markenentscheidung für Shop-Setup
- [[Prinova Europe]] — Priority #1 CMO-Kandidat
- [[Wonnda.com]] — CM-Discovery-Plattform
- [[Pure Flavour GmbH]] — Funktionale-Produkte-CMO
- [[Lehvoss Nutrition]] — Priority #2 CMO-Kandidat
- [[Aidea]] — Priority #4 CMO-Kandidat
- [[Shopify eCommerce Setup]] — (noch nicht erstellt)
- [[Oleg Personal Context]] — Projektverantwortlicher
