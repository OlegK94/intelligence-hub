tags: [performance-cafe, audit, prüfhinweise, contradictions, regulatory, sourcing, plausibility-flags]
sources: ["raw/Business/Performance Coffee Brand/PRUEFHINWEISE.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Zentrale Audit-Flags aus Vault-Audit 2026-06-14 — dokumentiert konsistent verifizierten Content (Stack A, EU-Limits, Phase-1-Regulatorik, eCommerce-Pivot), identifiziert aber auch offene Widersprüche und erforderliche Nutzerprüfungen (Café Berlin Pivot Update, GmbH Status, NMN EFSA-Verifizierung, CMO-Kontakt-Priorisierung, inhaltsstoffe_db CSV-Lücken, Finanzdaten-Duplikate)
---

# Performance Coffee Brand — PRUEFHINWEISE Vault Audit 2026-06-14

## Übersicht

Dieses Quelldokument ist das **zentrale Audit-Flaggen-Dokument** aus dem regelmäßigen Vault-Audit (durchgeführt 2026-06-14). Es dokumentiert **konsistent verifizierten Content** mit ✅ sowie **offene Widersprüche und Nutzerprüfungen** mit ⚠️. Die Flags sind bewusst **nicht stillschweigend korrigiert** worden — sie erfordern eine Entscheidung des Nutzers oder zusätzliche Recherche.

---

## ✅ BESTÄTIGT KONSISTENT

### Stack A Dosierungen

| Zutat | Dosierung | Quellen | Status |
|---|---|---|---|
| Koffein | ~100 mg | Inhaltsstoffe Datenbank + inhaltsstoffe_db.csv + 02_Produkt_Rezeptur | ✅ Abgestimmt |
| L-Theanin | 200 mg | Raw DB + Recht & Regulatorik | ✅ Konsistent; Max. 200mg/Portion EU-Limit erfüllt |
| L-Tyrosin | 500 mg | Inhaltsstoffe Datenbank + Rezeptur | ✅ Abgestimmt |
| B-Vitamine | NRV | Datenbank + Quelldokumente | ✅ EU Health Claims-konform |

**Schlussfolgerung:** Stack A ist **intern konsistent** und regulatorisch korrekt. Keine Unstimmigkeiten zwischen Datenbank, CSV und technischen Dokumenten.

---

### EU-Limits (Konsistenzprüfung)

| Inhaltsstoff | Limit | Olegs Stack | Compliance |
|---|---|---|---|
| **L-Theanin** | Max. 200 mg/Portion in Getränken | 200 mg (Stack A) | ✅ Am Limit, konform |
| **Alpha-GPC** | Max. 400 mg/Tag | ~250 mg (Stack A) | ✅ Konform |

**Schlussfolgerung:** EU-regulatorische Limits sind in allen Stacks korrekt umgesetzt. Keine Überschreitungen erkannt.

---

### Phase-1-Regulatorik & Longevity-Wirkstoffe

| Element | Quelle | Befund |
|---|---|---|
| Stack A als Phase 1 (MVP) | 00_Auftragsbrief + novel_food_longevity_wirkstoffe.md | ✅ Sauberster Launch; keine Novel-Food-Blockierungen |
| Longevity-Wirkstoffe in Phase 3+ | novel_food_longevity_wirkstoffe.md | ✅ NMN, Urolithin A, Spermidin richtig ausgeschlossen Phase 1 |

**Schlussfolgerung:** Phase-1-Regulatorik ist **korrekt kalibriert**. Longevity-Wirkstoffe sind mit Absicht ausgeschlossen, um MVP-Timeline nicht zu gefährden.

---

### Strategischer Pivot (eCommerce-First, Juni 2026)

| Quelle | Befund |
|---|---|
| 00_Auftragsbrief (ursprünglich Café-first) | ✅ Dokumentiert |
| Pivot-Update raw (2026-06-14) | ✅ Dokumentiert: eCommerce-first neues Modell |
| Wiki [[Performance Coffee Brand]] / [[CLAUDE.md]] | ✅ Konsistent: eCommerce-first, Café als sekundär |

**Schlussfolgerung:** Der Strategische Pivot von Café-first zu **eCommerce-first ist durchgängig dokumentiert und konsistent** über alle Quellen.

---

## ⚠️ NUTZERPRÜFUNG ERFORDERLICH

### 1. Café Berlin Quelle veraltet ohne Pivot-Update

**Status:** Bereits ein neues **Pivot-Update 2026-06-14** vorhanden.

| Datei | Inhalt | Status |
|---|---|---|
| `raw/Business/Cafe/Café Berlin — Partnership Hai.md` | Pre-Pivot Café-first-Modell | ✅ Ingested, aber veraltet |
| `raw/Business/Cafe/Café Berlin — Pivot Update 2026-06-14.md` | **Neu:** eCommerce-Pivot dokumentiert | **⚠️ RE-INGEST ERFORDERLICH** |

**Handlung:** Das neue Pivot-Update muss im Wiki ingestiert werden. Die [[Café Berlin Partnership Hai]]-Entität sollte einen **`## Widersprüche / Updates`**-Abschnitt erhalten, der auf die neue Pivot-Realität verweist.

---

### 2. GmbH als „ruhend" vs. „aktiv" — Entity-Status unklar

**Beobachtung:**

| Quelle | GmbH-Status |
|---|---|
| Pivot-Update / Partnership-Notes | GmbH (Oleg, **ruhend**) |
| Wiki [[Oleg Business Entity Structure]] | Wagglz GmbH als **aktiv** |

**Vermutung:** Zwei verschiedene GmbHs werden vermischt, oder der Status wurde seit der Wiki-Entitäts-Erstellung geändert.

**Klärung erforderlich:**
- Gibt es zwei GmbHs (Wagglz vs. neue GmbH mit Hai)?
- Ist Wagglz tatsächlich noch aktiv oder inzwischen ruhend?
- Wird die neue GmbH für die Performance Coffee Brand gegründet?

**Handlung:** Nutzer muss das Dokument prüfen und [[Oleg Business Entity Structure]] aktualisieren.

---

### 3. NMN EFSA-Gutachten (Mai 2026) — extern verifizieren

**Behauptung:** 
- `novel_food_longevity_wirkstoffe.md` zitiert ein **positives EFSA-Gutachten** für NMN (EffePharm, 11. Mai 2026)
- Dies ist **hochrelevant** für die Phase-3-Planung (Longevity-Wirkstoffe ab Phase 3)

**Problem:** 
- Recherchedatum 2026-06-14 — das Gutachten liegt plausibel 1 Monat zurück
- **Aber:** Dies ist eine kritische regulatorische Aussage, die vor CM-Briefing verifiziert sein sollte

**Verifizierungsquelle:**
```
https://open.efsa.europa.eu/
```

**Handlung:** EFSA-Datenbank abfragen nach NMN + EffePharm + Mai 2026. Falls kein positives Gutachten vorliegt → Quelldokument korrigieren.

---

### 4. inhaltsstoffe_db.csv vs. Raw DB — kleine Lücken

**Beobachtung:**

| Zutat | CSV | Raw DB | Bewertung |
|---|---|---|---|
| Ashwagandha | ✅ Gelistet (Phase 2+) | 🟡 Situativ | Kein Widerspruch; CSV auf Phase 1 fokussiert |
| Creatin | ✅ Gelistet (Phase-2-Sport-SKU) | ❌ Nicht in Vault-Stacks | Explorativ, kein Widerspruch |
| NMN / Urolithin / Spermidin | ❌ Nicht in CSV | ✅ In Longevity-Recht-Doc | **Korrekt** von Phase 1 ausgeschlossen |

**Fazit:** Kein sachlicher Widerspruch. CSV ist Phase-1-fokussiert (richtig); Longevity-Wirkstoffe sind richtig ausgeschlossen Phase 1. Die Lücken sind **beabsichtigt**, nicht Fehler.

---

### 5. Doppelte Supabase-Inbox-Quellen (beide ingested)

**Beobachtung:**

| Datei | Datum | Status |
|---|---|---|
| `raw/inbox/Supabase Wagglz Tierapp Config.md` | Früher | Draft; ohne Projekt-Ref |
| `raw/inbox/Supabase Wagglz Tierapp Config 2026-06-14.md` | 2026-06-14 | Ersetzt die ältere Version |

**Wiki-Situation:** Beide Source-Pages wurden ingested. Die ältere Datei ist jetzt **veraltet**.

**Handlung:** Ältere Supabase-Quelldatei im Wiki als `STATUS: Obsolet — siehe 2026-06-14 Version` markieren. Keine Dateilöschung (ingested).

---

### 6. Verschachtelte Vault-Struktur: Intelligence Hub/Intelligence Hub/

**Beobachtung:**
Versehentliche Duplikation der Ordnerstruktur. Im Vault vorhanden:
```
Intelligence Hub/
  Intelligence Hub/
    .obsidian/
    .trash/
```

**Handlung:** Nested Folder löschen, wenn **nicht beabsichtigt**. Vermutlich ein Fehler beim Vault-Setup.

---

### 7. raw/Finanzdaten/ Duplikat-Baum

**Beobachtung:**
52 MD5-identische Dateipaare zwischen:
- `raw/Finanzdaten/` (Duplikat)
- `raw/Privat/Finanzen/` (Kanonisch) + `raw/Business/` (Kanonisch)

Beispiele:
- `raw/Finanzdaten/Obsidian_Vault/ALG I 2025.md` ≡ `raw/Privat/Finanzen/Einnahmen/ALG I 2025.md`
- `raw/Finanzdaten/Obsidian_Vault/Steuern/ALG I Progressionsvorbehalt.md` ≡ `raw/Privat/Finanzen/Steuern/ALG I Progressionsvorbehalt.md`

**Status:** Archiviert mit README. Nicht editieren.

**Handlung:** Nach Bestätigung, dass kein unique Content vorhanden ist → `raw/Finanzdaten/` löschen.

---

## 📋 EMPFOHLENE NÄCHSTE SCHRITTE (PRIORISIERT)

### Unmittelbar (Priorität 1)

1. **Café Berlin Pivot Update 2026-06-14 re-ingest**
   - Neue Datei: `raw/Business/Cafe/Café Berlin — Pivot Update 2026-06-14.md`
   - Aktualisiere [[Café Berlin Partnership Hai]] mit neuem Pivot-Kontext
   - Ergänze `## Widersprüche / Updates` Abschnitt

2. **GmbH-Status klären**
   - Wahglz GmbH noch aktiv oder ruhend?
   - Neue GmbH mit Hai gegründet?
   - [[Oleg Business Entity Structure]] aktualisieren

3. **Performance Coffee Brand raw files vollständig ingest**
   - `raw/Business/Cafe/Performance Coffee Brand/` → alle Module (01–07)
   - Derzeit: Scaffold + TODOs

### Mittelfristig (Priorität 2)

4. **NMN EFSA-Gutachten verifizieren**
   - Query: https://open.efsa.europa.eu/ für NMN + EffePharm + Mai 2026
   - Falls nicht gefunden → `novel_food_longevity_wirkstoffe.md` korrigieren

5. **Supabase-Duplikate markieren**
   - Ältere Quelle als obsolet kennzeichnen
   - Wiki-Verlinkungen auf neue Version korrigieren

### Nach Freigabe

6. **raw/Finanzdaten/ Duplikat-Baum löschen**
   - Nach Bestätigung: keine unique Daten
   - Löschen Sie den gesamten `raw/Finanzdaten/`-Ordner

---

## Quellenangaben

- Raw Audit-Datei: `raw/Business/Performance Coffee Brand/PRUEFHINWEISE.md` (2026-06-14)
- Referenzen: Stack-Datenbanken, Regulatorik-Dokumente, Pivot-Updates, Lieferanten-Listen

---

## Verwandte Seiten

- [[Performance Coffee Brand]] — Projekt-Entität
- [[Café Berlin Partnership Hai]] — benötigt Pivot-Update
- [[Novel Food Regulation]] — Kontext für NMN-Verifizierung
- [[Stack A Fokus]] — verifizierten Stack A
- [[Oleg Business Entity Structure]] — GmbH-Status-Entität
- [[Wagglz GmbH]] — zu klärende Entität
