# Performance Coffee — Prüfhinweise

Plausibilitätsflags aus Vault-Audit 2026-06-14. **Nicht stillschweigend korrigieren** — via Recherche oder Entscheidung des Nutzers auflösen.

---

## ✅ Bestätigt konsistent

| Thema | Quellen | Bewertung |
|-------|---------|-----------|
| Stack A Dosen | `Inhaltsstoffe — Datenbank.md`, `inhaltsstoffe_db.csv`, `02_Produkt_Rezeptur.md` | Abgestimmt: Koffein ~100 mg, L-Theanine 200 mg, L-Tyrosine 500 mg, B-Vitamine NRV |
| L-Theanine EU-Limit | Raw DB + `05_Recht_Regulatorik.md` | Max. 200 mg/Portion in Getränken — konsistent |
| Alpha-GPC EU-Limit | Raw DB + `inhaltsstoffe_db.csv` | Max. 400 mg/Tag — konsistent |
| Phase-1-Regulatorik | `00_Auftragsbrief.md` + `novel_food_longevity_wirkstoffe.md` | Stack A sauberster Launch; Longevity-Wirkstoffe erst Phase 3+ |
| Strategischer Pivot | `00_Auftragsbrief.md`, Pivot-Update raw, `CLAUDE.md` | 2026-06-14: Café-first → eCommerce-first — konsistent |

---

## ⚠️ Nutzerprüfung erforderlich

### 1. Ingested Café-Berlin-Quelle veraltet (ohne Pivot)

| Datei | Status |
|-------|--------|
| `raw/Business/Cafe/Café Berlin — Partnership Hai.md` | **INGESTED** — zeigt noch pre-Pivot Café-first-Modell |
| `raw/Business/Cafe/Café Berlin — Pivot Update 2026-06-14.md` | **NEU** — dokumentiert eCommerce-Pivot 2026-06-14 |

**Aktion:** Pivot-Update re-ingesten; `## Contradictions / Updates` in Wiki-Entity [[Café Berlin Partnership Hai]] ergänzen.

### 2. GmbH als „ruhend“ vs. „aktiv“ beschrieben

- Pivot-Update / Partnership-Notes: „GmbH (Oleg, ruhend)“
- Wiki [[Oleg Business Entity Structure]]: GmbH als **aktiv** (Wagglz GmbH)

**Vermutung:** Verschiedene Entities vermischt oder Status geändert. Klären, welche GmbH für Performance Coffee (Wagglz vs. neue GmbH).

### 3. NMN EFSA-Gutachten (Mai 2026) — extern verifizieren

`novel_food_longevity_wirkstoffe.md` zitiert positives EFSA-Gutachten EffePharm 11. Mai 2026. Plausibel zum Recherchedatum, aber **hochrelevante Regulatorik-Behauptung**. Vor CM-Briefing auf [EFSA OpenEFSA](https://open.efsa.europa.eu/) prüfen.

### 4. `inhaltsstoffe_db.csv` vs. Raw DB — kleine Lücken

| Item | CSV | Raw DB |
|------|-----|--------|
| Ashwagandha | gelistet (Phase 2+) | 🟡 situativ |
| Creatin | gelistet (Phase-2-Sport-SKU) | nicht in Vault-Stacks |
| NMN/Urolithin/Spermidin | nicht in CSV | nur in Longevity-Recht-Doc (korrekt von Phase 1 ausgeschlossen) |

Kein Widerspruch — CSV ist Phase 1 + Erweiterungen. Creatin nur explorativ.

### 5. Doppelte Supabase-Inbox-Quellen (beide ingested)

- `raw/inbox/Supabase Wagglz Tierapp Config.md` (Draft, ohne Projekt-Ref)
- `raw/inbox/Supabase Wagglz Tierapp Config 2026-06-14.md` (ersetzt)

Wiki hat beide Source-Pages. Ältere Quelle im Wiki als obsolet markieren — keine Dateilöschung (ingested).

### 6. `Intelligence Hub/Intelligence Hub/` verschachtelter Vault

Versehentlicher verschachtelter Obsidian-Vault (nur `.obsidian` + leerer `.trash`). Nested Folder löschen, wenn nicht beabsichtigt.

### 7. `raw/Finanzdaten/` Duplikat-Baum

52 MD5-identische Dateipaare vs. kanonisch `raw/Privat/Finanzen/` und `raw/Business/`. Archiviert mit README — nicht editieren.

---

## 📋 Empfohlene nächste Schritte

1. Ingest `raw/Business/Cafe/Café Berlin — Pivot Update 2026-06-14.md`
2. Ingest Performance Coffee Brand raw files aus `raw/Business/Cafe/Performance Coffee Brand/`
3. Module 01–07 füllen (aktuell Scaffold + TODOs)
4. NMN EFSA-Gutachten über offizielle Quelle verifizieren
5. Entity-Struktur entscheiden (Wagglz GmbH vs. neue GmbH mit Hai)
6. `raw/Finanzdaten/` löschen nach Bestätigung, dass kein Unique Content vorhanden
