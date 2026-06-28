---
title: "02 Ingredienzen Datenbank — Performance Coffee Quelldokument"
type: source
tags: [performance-cafe, modul-01, ingredienzen, datenbank, recherche, in-progress, placeholder, claude-code]
sources: ["raw/Business/PerformanceCafe/recherche/_archiv/02_ingredienzen_db.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Quelldokument Modul 01 — Ingredienzen Datenbank für Performance Coffee Brand; aktueller Status leer/placeholder; Claude Code Auftrag zur Ausfüllung mit Web-Recherche nach aktuellen Daten (2024/2025); Sourcing-Kosten, Verfügbarkeit und Novel Food-Konformität für Stack A (L-Theanin, L-Tyrosine, Alpha-GPC, Koffein, B-Vitamine, Ashwagandha); abhängig von Modul 00 Auftragsbrief
---

# 02 Ingredienzen Datenbank — Performance Coffee (Quelldokument)

## Überblick

Dieses Quelldokument (`raw/Business/PerformanceCafe/recherche/_archiv/02_ingredienzen_db.md`) ist das **Modul 01-Placeholder** der strukturierten [[Performance Coffee Brand]]-Recherche. Der Status ist explizit **leer/noch nicht bearbeitet** — es handelt sich um einen verwalteten Platzhalter mit folgendem Auftrag:

> **Claude Code Befehl:**  
> Arbeite Modul 1 (Ingredienzen Datenbank) aus. Lies recherche/00_Auftragsbrief.md für den vollständigen Auftrag. Schreibe alle Ergebnisse nach recherche/_archiv/02_ingredienzen_db.md. Nutze web_search für aktuelle Daten (2024/2025). Quellenangaben am Ende jedes Abschnitts.

## Status & Metadaten

| | |
|---|---|
| **Status** | leer — noch nicht bearbeitet |
| **Modul** | 1 (Ingredienzen Datenbank) |
| **Priorität** | hoch |
| **Datum Quelldokument** | 2026-06-14 |
| **Abhängigkeit** | recherche/00_Auftragsbrief.md (Modul 00) |

## Erwartete Inhalte (aus der Struktur)

Das Dokument ist als Platzhalter mit folgender Struktur konzipiert:

1. **Ingredient Stack A (Tier 1) — Sourcing-Kosten**
   - L-Theanin 200 mg/Portion
   - L-Tyrosine 500 mg/Portion
   - Alpha-GPC (eingeschränktes Novel Food)
   - Koffein (je nach Format 70–200 mg)
   - B-Vitamin-Premix (B6, B12, B5 → NRV)
   - Ashwagandha KSM-66 300–600 mg

2. **Novel Food-Konformität pro Zutat**
   - Status (genehmigt / eingeschränkt / blockiert)
   - EU-Limits (falls zutreffend)
   - Dokumentations-Anforderungen

3. **Supplier-Datenbank**
   - ≥5 Quotes pro Inhaltsstoff
   - Verfügbarkeit
   - MOQ (Minimum Order Quantity)
   - Lieferzeit

4. **Quellenangaben** — Web-Recherche-Belege für alle Kostendaten (ECHA, EFSA, Supplierlisten)

## Claude Code — Auftragsdetails

Der Auftrag richtet sich explizit an Claude Code:

```
Arbeite Modul 1 (Ingredienzen Datenbank) aus.
Lies recherche/00_Auftragsbrief.md für den vollständigen Auftrag.
Schreibe alle Ergebnisse nach recherche/_archiv/02_ingredienzen_db.md.
Nutze web_search für aktuelle Daten (2024/2025).
Quellenangaben am Ende jedes Abschnitts.
```

**Interpretation:** Dieses Quelldokument ist ein verwalteter Arbeitsplatz für eine **Claude Code-Ausführung** — nicht für manuelles Eintippen konzipiert. Es beschreibt, welche Auftragsstruktur Claude Code folgen soll, um die Datenbank auszufüllen.

## Blockierende Abhängigkeiten

Dieses Modul ist abhängig von:

1. **[[00 Auftragsbrief Performance Coffee]]** (Modul 00)
   - Stack A Final-Spezifikation
   - Zielkosten-Grenzen
   - Compliance-Anforderungen

2. **Web-Recherche-Verfügbarkeit**
   - Aktuelle Supplier-Preislisten (2024/2025)
   - Novel Food-Database (EFSA)
   - EU-Regulatorische Updates

## Verknüpfung im Projekt-Workflow

| Modul | Abhängigkeit | Status |
|---|---|---|
| **00 Auftragsbrief** | Primär | ✅ Existiert |
| **01 Ingredienzen DB** | Diese (Placeholder) | ⏳ Ausstehend (Modul 00 → Ausführung) |
| **02 Produkt & Rezeptur** | Abhängig von 01 | ⏳ Blockiert bis 01 fertig |
| **03 Lieferkette & Produktion** | Abhängig von 01 + 02 | ⏳ Blockiert |
| **05 Recht & Regulatorik** | Abhängig von 01 | ⏳ Blockiert (aktuelle Compliance-Angaben) |
| **06 Kalkulation & Pricing** | Abhängig von 01 | ⏳ Blockiert (Kostendata) |

## Nächste Schritte

1. **Claude Code Ausführung:**
   - `python tools/ingest.py --claude-code 02_ingredienzen_db`
   - oder manuelle Weiterleitung an Claude mit Auftrag + recherche/00_Auftragsbrief.md

2. **Validierung:**
   - Überprüfung der Web-Recherche-Quellen
   - Novel Food-Status gegen EFSA-Database kreuzen
   - Supplierlisten verifizieren

3. **Integration:**
   - Ergebnisse nach modelle/inhaltsstoffe_db.csv exportieren (für unit_economics.py)
   - COGS-Modell (Modul 06) kann dann finalisiert werden

## Verwandte Seiten

- [[00 Auftragsbrief Performance Coffee]] — Parent-Modul mit Kontext
- [[Performance Coffee Brand]] — Projekt-Entität
- [[02 Produkt & Rezeptur Performance Coffee]] — Abhängiges Modul
- [[05 Recht & Regulatorik (EU Lebensmittel/Supplements)]] — Regulatory Context
- [[06 Kalkulation & Pricing Performance Coffee]] — Kostenmodell abhängig von dieser DB
- [[EU Novel Food Regulation]] — Regulatory Framework
- [[COGS]] — Kostenberechnungskontext
- [[L-Theanin]], [[L-Tyrosine]], [[Alpha-GPC]], [[Koffein]], [[B-Vitamine B6/B12/B5]], [[Ashwagandha KSM-66]] — Einzelne Zutatenseiten
