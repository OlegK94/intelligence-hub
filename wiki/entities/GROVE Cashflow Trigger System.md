---
title: GROVE Cashflow Trigger System
type: entity
tags: [cafe, grove, finanzen, cashflow, trigger, monitoring, kpi, liquiditaet, gehalt, risk-management]
sources: ["raw/Business/Cafe/cafe_masterplan_2026.md"]
created: 2026-06-16
updated: 2026-06-16
summary: Five-tier cash reserve monitoring system for GROVE café — automatic salary and operational actions triggered at predefined cash thresholds; monthly 30-minute monitoring ritual; 5 KPIs tracked; stress scenario shows insolvency risk at < 10k by Jan 2028 without countermeasures
---

# GROVE Cashflow Trigger System

## Overview

The **GROVE Cashflow Trigger System** is a mandatory monthly monitoring protocol and automatic action framework for [[GROVE Businessplan und Betriebshandbuch 2026|GROVE café]]. It converts cash reserve levels into predefined operational responses — removing emotional decision-making from financial management under stress.

---

## Five-Tier Trigger Matrix

| Kassenstand | Signal | Maßnahme |
|---|---|---|
| **> 45.000 €** | ✅ Grün | Normal — Gehaltsplan einhalten |
| **30.000–45.000 €** | 🟡 Gelb | Gehaltserhöhung einfrieren |
| **20.000–30.000 €** | 🟠 Orange | Beide auf 2.000 € brutto reduzieren |
| **< 20.000 €** | 🔴 Rot | Steuerberater einschalten, KfW informieren |
| **< 10.000 €** | ⛔ Kritisch | Externe Beratung oder geordneter Rückzug |

### Salary Impact at Each Level

| Trigger Level | Action | Monthly Cash Saving |
|---|---|---|
| Gelb (< 45k) | Phase 3 Gehaltserhöhung einfrieren | ~2.000 €/Monat |
| Orange (< 30k) | Beide auf 2.000 € reduzieren | ~6.000 €/Monat |
| Rot (< 20k) | Steuerberater + Nachfinanzierung | Variable |
| Kritisch (< 10k) | Geordneter Rückzug | — |

---

## Monthly Monitoring Ritual (30 Minuten, Pflicht)

Checklist ab Opening:
- [ ] Kassenstand aus Orderbird/Banking auslesen
- [ ] Gegen Trigger-Matrix prüfen
- [ ] Umsatz vs. Plan (Abweichung > 15% = Ursache identifizieren)
- [ ] Gehaltsentscheidung Folgemonat bestätigen

---

## 5 KPIs

| KPI | Ziel (Phase 3) | Warnsignal |
|---|---|---|
| Tagesumsatz Ø | > 600 € | < 450 € für 2+ Wochen |
| Food-Cost-% | < 30 % | > 35 % |
| Kassenstand Monatsende | > 35.000 € | < 25.000 € |
| Transaktionen/Tag | > 100 | < 70 für 2+ Wochen |
| Fr/Sa Abend-Umsatz | > 1.500 € | < 900 € |

---

## Stress Scenario Context

In the −25% revenue stress scenario, without countermeasures:
- **Januar 2028 (Month 11):** Kassenstand = **4.049 €** → Insolvenzgefahr

The trigger system is designed to intervene well before this point:
- Low-point in base scenario: **40.924 €** (Januar 2028) — well above Rot/Kritisch thresholds
- Stress scenario hits Gelb at Month 6, Orange at Month 8

---

## Related Pages

- [[GROVE Businessplan und Betriebshandbuch 2026]] — parent plan
- [[Wagglz GmbH]] — operating entity
- [[Oleg Personal Context]] — one of the two GF affected by salary triggers
- [[Hai]] — second GF affected
- [[KfW StartGeld ERP 067]] — informed at Rot level
