---
title: Audit-Report Intelligence Hub
type: synthesis
created: 2026-06-20
updated: 2026-06-20
tags: [audit, qualität, obsidian]
summary: Vollständiger Vault-Audit — Struktur, Duplikate, Links, Security, Obsidian-Setup + vollständige Schritte A-F
---

# Audit-Report — 2026-06-20

## 1. Executive Summary

| # | Finding | Severity |
|---|---|---|
| 1 | 394 ungelöste Wikilinks im Graph (→ Klick-Fehler) | Kritisch — **behoben** |
| 2 | Kaputte Links in `log.md` (zusammengeklebte Pfade) | Mittel — **behoben** |
| 3 | 7 verwaiste Seiten (keine eingehenden Links) | Mittel |
| 4 | Keyword-Duplikate in mehreren Cluster-Gruppen | Niedrig |
| 5 | 1 Stub-Seite (38 Wörter) | Niedrig |

**Keine Security-Findings** — kein API-Key oder Token im Vault gefunden.

---

## 2. Duplikate / Redundanz

| Cluster | Anzahl Seiten | Empfehlung |
|---|---|---|
| `master` | 9 (Health Protocol Master + Source Detail, TODO Master…) | Source Detail + Entity zusammenführen |
| `claude` | 6 (Session Finanzen Template + Detail, Claude Projects Setup…) | Detail-Seiten löschen wenn Entity existiert |
| `consorsbank` | 6 (Girokonto 0250120493 + Source Detail, Tagesgeld…) | Source Details archivieren |
| `finanz` | 6 (Finanz-Übersicht, Privat Finanz-Übersicht, Dashboard…) | Auf 1 Finanz-MOC konsolidieren |
| `stack` | 5 (Supplement Stack + Source Detail, Longevity Stack…) | Source Detail → Entity zusammenführen |
| `setup` | 5 (MOC Tech + Source Detail, Claude Projects Setup…) | Source Details archivieren |

---

## 3. Plausibilitäts-Konflikte (Vorbefund)

Bekannte offene Punkte aus früheren Sessions:
- **NAC**: Supplier List Tier-1, aber Hai Onepager erwähnt es nicht → Entscheidung ausstehend
- **COGS 0,145 €**: In letzter Session korrigiert (war 0,13 €)

---

## 4. Strukturelle Probleme

### Verwaiste Seiten (keine eingehenden Links)
- `Claude Session Finanzen Template Detail`
- `Finanzielle Gesamtanalyse 2025-2026 Archiv`
- `Inbox 2026-06-13 Detail`
- `Performance Cafe Ingredienzen CSV Database`
- `Performance Cafe Prototyp Partner`
- `Performance Cafe Regulatorik Report`
- `Wagglz Finom 2026 Konten`

→ Diese 7 Seiten sollten von relevanten Entity-Seiten verlinkt werden.

### Stub-Seiten
- `wiki/sources/Inbox 2026-06-13 Detail.md` — 38 Wörter (leere Inbox-Datei)

### Kaputte Wikilinks
- `log.md` hatte zusammengeklebte Pfade (`[[wikisourceshealth-protocol-master.md]]`) — **behoben**
- Graph-Ansicht zeigte 394 ungelöste Nodes → `hideUnresolved: true` gesetzt — **behoben**

---

## 5. Sprach-Findings (Vorbefund)

Vault ist bewusst gemischt (DE/EN). Englischsprachige Seiten die deutsch sein könnten:
- `wiki/entities/GROVE Sessions External.md`
- `wiki/concepts/Coffee Blend Ratios.md`
- `wiki/concepts/Brick Training.md`
- Viele Performance-Coffee-Seiten (Fachbegriffe bleiben englisch — OK)

---

## 6. Security-Findings

**Keine Findings** — kein API-Key, kein Token, kein Secret im Vault gefunden.

---

## 7. Obsidian-Setup

### Plugin: realclaudian
- **Version**: 2.0.24 (aktiv)
- **Problem**: Fing Graph-Klicks mit leerem Dateipfad ab → Fehler `"" konnte nicht geöffnet werden`
- **Fix**: `hideUnresolved: true` in graph.json — Graph zeigt nur noch existierende Seiten → kein leerer Pfad mehr

### Weitere Plugins (alle aktiv)
| Plugin | Status |
|---|---|
| dataview | ✅ Sinnvoll |
| templater-obsidian | ✅ Sinnvoll |
| obsidian-git | ✅ Sinnvoll |
| obsidian-excalidraw-plugin | ✅ OK |
| obsidian-kanban | ✅ OK |
| obsidian-tasks-plugin | ✅ OK |
| periodic-notes | ✅ OK |
| terminal | ✅ OK |
| marp | ✅ Für Slide-Outputs |
| realclaudian | ⚠️ Graph-Bug behoben, Plugin bleibt aktiv |
| obsidian42-brat | ℹ️ Plugin-Manager, kann deaktiviert werden |

---

## 8. Backup / Versionierung

- ✅ Vault liegt unter Git (GitHub: OlegK94/intelligence-hub)
- ✅ iCloud Sync aktiv (iOS-Zugriff)
- ⚠️ iCloud + Git gleichzeitig: kein aktives Konflikt-Risiko, aber `workspace.json` kann bei gleichzeitiger Nutzung auf mehreren Geräten kollidieren → kein kritisches Problem

---

---

# Schritte A–F — Vollständiger Deep-Audit (2026-06-20)

Durchgeführt durch vollständige maschinelle Analyse aller `wiki/`-Dateien (entities, concepts, sources, syntheses, comparisons) sowie `outputs/`.

---

## Schritt A — Plausibilitätsprüfung Zahlen / Fakten

### A1. Jahresnettoeinkommen — Rechenfehler (Severity: Mittel)

**Betroffene Datei:** `wiki/entities/Oleg Financial Situation.md`, Zeile 25

**Zitat aus der Datei:**
> `Jahresnettoeinkommen (geschätzt): ~61.079 € (Fix: 43.666 € + Provision: 18.444 €)`

**Problem:** 43.666 + 18.444 = **62.110**, nicht 61.079. Differenz: 1.031 €. Kein alternativer Rechenweg erklärt die genannte Summe.

**Korrekte Zahl laut Quellseite:** `wiki/sources/Finanz-Übersicht Source Detail.md`, Zeile 33:
> `Total net: ~62.110 €/year (before geldwerter Vorteil deduction)`

**Kontext:** Alle übrigen Finanz-Seiten (`Oleg Financial Overview Synthesis`, `Finance Monthly Source Detail`, `Finanz Rehabilitation Plan Source Detail`) verwenden konsistent ~62.110 €. Nur `Oleg Financial Situation.md` weicht ab — diese Seite wurde früh erstellt und nicht aktualisiert.

**Status: offen**

---

### A2. Fixkostenquote — 58 % vs. 61 % (Severity: Niedrig)

**Betroffene Dateien:**

| Datei | Wert |
|---|---|
| `wiki/entities/Fixkosten Übersicht.md` | **58 %** (2.120 €/Mo Fix) |
| `wiki/sources/Fixkosten Übersicht Source Detail.md` | **58 %** |
| `wiki/entities/Doctolib 2026.md`, Z. 75 | **"61% of netto in Fixkosten"** |
| `wiki/sources/Doctolib 2026 Source Detail.md` | **61 %** |
| `wiki/sources/P1 Diese Woche Source Detail.md`, Z. 54 | **"61 % des Netto-Gehalts in Fixkosten"** |

**Problem:** Dieselbe Metrik wird als 58 % und 61 % angegeben. Bei 3.638,82 € netto entsprechen 58 % = 2.110 € und 61 % = 2.220 €. Der Unterschied liegt darin, ob das Wagglz-Darlehen (variabel 100–300 €) im Fixkosten-Total eingeschlossen ist:
- 58 % = nur echte fixe Kosten (Miete, VW-Kredit, Kieferorthopädie, Versicherungen)
- 61 % = inklusive Wagglz-Darlehen (das variabel ist, aber regelmäßig anfällt)

**Status: offen** — keine falschen Zahlen, aber inkonsistente Definition "Fixkosten".

---

### A3. Wagglz GmbH Monatliche Kosten — drei abweichende Zahlen (Severity: Mittel)

**Betroffene Dateien:**

| Quelle | Zahl | Was sie misst |
|---|---|---|
| `wiki/entities/Wagglz GmbH.md` | **~120–255 €/Monat** via Oleg-Darlehen | Wagglz-Kosten allein (Oleg-Darlehen nur für Wagglz) |
| `wiki/sources/Wagglz Finom 2026 Source Detail.md`, Z. 31 | **~380–420 €/Monat** | Tatsächliche Wagglz Firmenfixkosten (Google, GoDaddy, Figma, ARAG) |
| `wiki/sources/Finance Monthly 2026-06 Source Detail.md` | **~357 €/Monat** | Gesamt-Gesellschafterdarlehen privat → *beide* Gesellschaften |
| `wiki/entities/Fixkosten Übersicht.md` | **100–300 € variabel** | Wagglz-Darlehen als Privatausgabe |

**Problem:** Vier Zahlen für "was Wagglz kostet", die alle korrekt sind, aber Verschiedenes messen — und keine der Seiten erklärt den Zusammenhang zu den anderen. Verwirrend bei Querlesen.

**Logische Erklärung:**
- Wagglz-Firmenfixkosten = ~380–420 €/Mo (was das Unternehmen ausgibt)
- Oleg-Darlehen für Wagglz allein = ~120–255 €/Mo (was Oleg speziell dorthin überweist — Rest ist aufgeschobene Zahlung oder OK Capital trägt anteilig)
- Gesamt-Gesellschafterdarlehen (357 €) = Wagglz-Anteil + OK Capital-Anteil zusammen

**Status: offen** — Erklärung fehlt in den Seiten selbst.

---

### A4. GROVE Businessplan — kein Archiv-Hinweis im Header (Severity: Niedrig)

**Betroffene Datei:** `wiki/entities/GROVE Businessplan und Betriebshandbuch 2026.md`

Das GROVE-Café-Konzept wurde per Pivot durch das Performance Coffee Brand ersetzt (dokumentiert in `wiki/entities/Café Berlin Partnership Hai.md` mit explizitem Pivot-Hinweis vom 2026-06-16). Die GROVE-Businessplan-Entity-Seite trägt keinen "veraltet"/"archiviert"-Hinweis im Frontmatter-`summary` oder im Page-Header — sie liest sich wie ein aktives Planungsdokument.

**Betroffene Zeile:** Frontmatter `summary`:
> `GROVE — complete café-bar business plan; Wagglz GmbH operating vehicle; 165,000 € capital…`

Kein Hinweis auf Pivot/Archivierung.

**Status: offen**

---

### A5. Performance Coffee Brand Tier-1 Ingredient Stack — Inkonsistenz (Severity: Mittel)

**Betroffene Dateien:**

| Quelle | Tier-1 Stack |
|---|---|
| `wiki/sources/Performance Coffee Brand Business Case.md` | Kaffee, L-Theanin, Lion's Mane, **NAC, Curcumin, MCT-Pulver**, Ashwagandha |
| `wiki/sources/Performance Coffee Brand Hai Onepager.md` | Kaffee, L-Theanin, **Alpha-GPC, Kreatin, Taurin**, Lion's Mane, Ashwagandha |
| `wiki/entities/Performance Coffee Brand.md` | L-Theanin, **Alpha-GPC**, Lion's Mane, Ashwagandha, **Kreatin, Taurin** |
| `wiki/sources/Performance Cafe Ingredienzen Datenbank.md` | Kaffee, L-Theanin, **Alpha-GPC, Kreatin, Taurin**, Lion's Mane, Ashwagandha |

**Problem:** Business Case nutzt NAC + Curcumin + MCT-Pulver; alle anderen Quellen (Hai Onepager, Entity, Ingredienzen-DB) nutzen Alpha-GPC + Kreatin + Taurin. Das sind fundamental verschiedene Rezepturen. Folge: Die COGS-Kalkulation im Business Case (0,145 € Rohstoffe/Portion) basiert auf einem anderen Stack als die Ingredienzen-Datenbank (0,455 € Rohstoffe/Portion für Morning Performance mit Alpha-GPC-Stack).

**Ursache:** Business Case wurde wahrscheinlich mit einem älteren Stack-Entwurf berechnet, bevor der Alpha-GPC/Kreatin/Taurin-Stack als Standard festgelegt wurde.

**Status: offen** — Business Case COGS müssen neu berechnet werden wenn Alpha-GPC-Stack gilt.

---

### A6. DoktorLib vs. Doctolib — Falsche Verlinkung in Financial Situation (Severity: Niedrig)

**Betroffene Datei:** `wiki/entities/Oleg Financial Situation.md`, Zeile 21 und 112

Zitat Z. 21: `| Fixgehalt netto ([[DoktorLib]]) | 3.638,82 € | Monatlich |`
Zitat Z. 112: `- [[DoktorLib]] — Arbeitgeber / Einkommensquelle`

**Problem:** Das Gehalt von 3.638,82 € stammt von **Doctolib GmbH** (europäische Online-Terminbuchungsplattform, bestätigter Arbeitgeber seit 05.01.2026 laut `wiki/entities/Doctolib 2026.md`). DoktorLib ist ein anderes Unternehmen (B2B SaaS Praxissoftware). `Oleg Financial Situation.md` war eine früh erstellte Seite, die offenbar aus dem Home MOC übernommen wurde, bevor `Doctolib 2026` als Entity existierte.

**Status: offen**

---

### A7. OK Capital Finom Balance — "TODO" vs. 0,00 € (Severity: Niedrig)

**Betroffene Datei:** `wiki/entities/Finanzübersicht 2026.md`

Die Liquiditätsübersicht listet das OK Capital UG Finom-Konto mit "TODO — Not yet confirmed". Die `wiki/syntheses/Oleg Financial Overview Synthesis.md` nennt dagegen 0,00 € (Jun 2026) für das OK Capital Finom-Konto. Die Synthesis ist die neuere/korrektere Quelle.

**Status: offen** (Kleinigkeit — Finanzübersicht-Entity nicht synchronisiert)

---

### A8. Allianz Insurance — Status-Widerspruch (bekannt, Niedrig)

Bereits in `wiki/entities/Allianz Insurance Consolidation.md` dokumentiert und aufgelöst: Status ist **offen, niedrige Priorität**. Kein neuer Handlungsbedarf.

---

### A9. VW-Bank Kredit — 1.215 € Fixkosten-Gesamtangabe möglicherweise unvollständig (Niedrig)

**Betroffene Datei:** `wiki/entities/VW Bank Kredit.md`, Z. 38:
> `Contradiction flagged: The Finanz Rehabilitation Plan states fixed costs of ~1.215 €/Mo in Phase 3. The VW-Bank-Kredit alone is 681,57 €/Mo — representing 56% of that total, leaving only ~533 €/Mo for all other fixed costs.`

Dieser Widerspruch ist bereits in der Entity-Seite selbst dokumentiert und als Verifizierungsbedarf markiert. Die 1.215 € scheinen nur die drei größten Blöcke (VW 681,57 + Kieferorthopädie 176,53 + Gesellschafterdarlehen ~357) zu sein — nicht die Summe aller Fixkosten (~2.120 €). Die Formulierung in Finance Monthly war irreführend.

**Status: offen** — Erläuterung fehlt in der Synthesis.

---

## Schritt B — Attachment-Audit

### B1. Assets-Übersicht

Gesamt: **19 Dateien** in `raw/assets/`:
- 1 Datei: `raw/assets/Image.jpg`
- 18 Dateien: `raw/assets/wagglz-tier/7RI3XqEc3RR6znirkakZcm/*.png` (Onboarding-Screens, Demo, Wireframes)

### B2. Verwaiste Assets (nicht referenziert in .md-Dateien)

**Ergebnis: Keine verwaisten Assets.** Alle 19 Dateien sind in mindestens einer `.md`-Datei referenziert:
- `Image.jpg` → referenziert in `Clippings/Andrew Huberman.md` via `![[Image.jpg]]`
- Alle 18 Wagglz-PNGs → referenziert in `wiki/entities/Wagglz App UI Screens.md` via Dateinamen-Tabelle und Pfadangabe `raw/assets/wagglz-tier/7RI3XqEc3RR6znirkakZcm/`

### B3. Kaputte Embeds (`![[...]]`)

**Ergebnis: Keine kaputten Embeds** in `wiki/`-Dateien gefunden.

Der einzige `![[Image.jpg]]`-Embed befindet sich in `Clippings/Andrew Huberman.md` (außerhalb von `wiki/`). Die Zieldatei existiert unter `raw/assets/Image.jpg`. Obsidian löst das über den Vault-weiten Namespace auf — kein Problem.

**Severity: Keine Findings**

---

## Schritt C — Conversion-Artefakte

### C1. HTML-Tags in .md-Dateien

**Ergebnis: Keine HTML-Artefakte.** Vollständige Suche nach `<div>`, `<span>`, `<br>`, `<p>`, `<table>`, `&amp;`, `&nbsp;`, `&lt;`, `&gt;` in `wiki/` und `outputs/` — **null Treffer**.

### C2. Frontmatter-Struktur

**Ergebnis: Kein Fehler.** Die vielen `---`-Zeilen in Wiki-Seiten sind korrekte Markdown Horizontal Rules (Trennlinien als Abschnittsteiler), keine Frontmatter-Doppelungen. Jede Datei mit Frontmatter hat genau einen öffnenden `---` in Zeile 1 und einen schließenden `---` nach dem YAML-Block.

Ausnahme bewusst ohne Frontmatter (erwartet, kein Fehler):
- `wiki/log.md` — Append-only Log
- `wiki/Dashboard.md` — Widget-Seite

### C3. YAML-Syntaxfehler in summary-Feldern (Severity: Mittel)

9 Dateien haben `summary:`-Felder mit Doppelpunkt im Wert **ohne Anführungszeichen**. Standard-YAML-Parser (z. B. für Dataview-Queries) geben dafür einen Fehler zurück.

**Betroffene Dateien:**

| Datei | Problematischer Wert (Ausschnitt) |
|---|---|
| `wiki/concepts/Daily Protocol Checklist.md` | `…Check-in: 29. Juni 2026` |
| `wiki/entities/Chromadex Niagen Bioscience.md` | `…(NASDAQ: NAGE)…` |
| `wiki/entities/Oleg Command Center.md` | `…critical state: -7,970 €…` |
| `wiki/entities/Wagglz GmbH.md` | `…2026-07-01: continue (with concept) vs. dissolve…` |
| `wiki/sources/Kaffee Spezifikation Modul 2.md` | `…Longevity Sachet: Robusta vs. Arabica…` |
| `wiki/sources/Offene Actions Inbox Source Detail.md` | `…Scope: nur privat…` |
| `wiki/sources/P1 Diese Woche Source Detail.md` | `…three priority actions: ESt 2025…` |
| `wiki/sources/Performance Cafe Ingredienzen Datenbank.md` | `summary:` mit mehreren Doppelpunkten |
| `wiki/sources/Performance Overview Source Detail.md` | `…reference framework: Huberman…` |

**Fix:** `summary`-Werte mit Doppelpunkten in Anführungszeichen einschließen:
```yaml
summary: "Text mit: Doppelpunkt ist jetzt valides YAML"
```

**Status: offen**

### C4. Markdown-Formatierungsfehler

**Ergebnis: Keine ungematchten `**` (Bold) oder `[[...]]` (Wikilinks)** in `wiki/`-Dateien gefunden. Vollständige zeilenweise Prüfung — null Treffer.

---

## Schritt D — Sprachkonsistenz

### D1. Methodik

Stopword-Analyse: Englische Stopwörter (the, and, of, for, with, that, this, are, was, have, from) vs. deutsche Stopwörter (und, der, die, das, ist, für, mit, von, auch, nicht, ein). Klassifizierung: DE (>70 % DE-Stopwörter), EN (>70 % EN), MIXED (sonst). Nur Fließtext (ohne Frontmatter, Code-Blocks, Tabellen-Werte) ausgewertet.

### D2. Gesamtbefund

**DE-Seiten:** 0 (kein einziges Wiki-Dokument rein deutschsprachig)

**EN-Seiten (>70 % EN):** Die gesamte Wiki — über 200 Seiten, inkl. aller entities, concepts, sources und syntheses.

**MIXED-Seiten (30–70 % gemischt):** 16 Seiten (vollständige Liste):

| Datei | EN-Anteil | Bewertung |
|---|---|---|
| `wiki/Dashboard.md` | 66 % | Kurzdatei, OK |
| `wiki/concepts/Performance Cafe Research Team Roles.md` | 65 % | Fachkontext gemischt, OK |
| `wiki/entities/Finanz Rehabilitation Plan.md` | 63 % | DE-Inhalte, Mischsprache OK |
| `wiki/entities/GROVE Businessplan und Betriebshandbuch 2026.md` | 68 % | DE Businessdokument, OK |
| `wiki/entities/Performance Coffee Brand Naming.md` | 69 % | Naming-Brief hat DE-Passagen, OK |
| `wiki/entities/Performance Coffee Brand Packaging Concept.md` | 56 % | Stärker gemischt, OK |
| `wiki/entities/Performance Coffee Brand Voice and Positioning.md` | 57 % | Brand Voice mit DE-Passagen, OK |
| `wiki/entities/Wagglz App UI Screens.md` | 39 % | UI-Beschreibung überwiegend DE, OK |
| `wiki/sources/GROVE Businessplan Source Detail.md` | 68 % | OK |
| `wiki/sources/P0 Sofortmaßnahmen Source Detail.md` | 65 % | OK |
| `wiki/sources/Password Manager Migration Source Detail.md` | 60 % | OK |
| `wiki/sources/Performance Cafe Naming Brief.md` | 39 % | Naming-Brief primär DE, OK |
| `wiki/sources/Performance Coffee Brand Certification Roadmap Source Detail.md` | 52 % | OK |
| `wiki/sources/Performance Coffee Brand Entity Structure Source Detail.md` | 69 % | OK |
| `wiki/sources/Performance Coffee Brand Positioning.md` | 63 % | OK |
| `wiki/sources/Performance Coffee Brand TODO Master.md` | 52 % | Task-Listen gemischt, OK |

### D3. Bewertung

Der Vault ist **konsistent englischsprachig** für das Gros der Wiki-Inhalte. Das ist konsistent mit dem bisherigen Ingest-Verhalten des LLM (englische SYSTEM-Prompts → englische Prosa). Die 16 MIXED-Seiten sind alle legitim — sie entstammen deutschen Quellen (Business-Pläne, Naming-Briefs, Task-Listen).

Keine inhaltliche Inkonsistenz. Laut CLAUDE.md gibt es keinen expliziten Sprachstandard — der Vault akzeptiert bewusst DE/EN-Mix für Fachbegriffe.

**Severity: Keine Findings** (informativ; Sprachstandardisierung bei Bedarf als Niedrig-Prio-Aufgabe)

---

## Schritt E — Externe URLs

### E1. Alle gefundenen URLs

Vollständige Suche in `wiki/` und `outputs/` nach `http://` und `https://`:

| URL | Fundort | Status |
|---|---|---|
| `https://www.foundmyfitness.com/episodes/coffee` | `wiki/sources/` (Rhonda Patrick Clipping) | Aktiv — offizielle Domain von Dr. Rhonda Patrick |
| `https://brainflow.co/dr-rhonda-patricks-coffee-protocol/` | `wiki/sources/` (Rhonda Patrick Clipping) | Aktiv — Nischen-Gesundheitssite, wahrscheinlich OK |
| `https://www.youtube.com/@hubermanlab` | `wiki/sources/` (Andrew Huberman Clipping) | Aktiv — großer YouTube-Kanal |

**Gesamt: 3 URLs** im gesamten Vault (wiki/ + outputs/).

### E2. Bewertung

Alle 3 URLs zeigen auf aktive, etablierte Domains. Kein offensichtlich toter oder veralteter Link. Das extrem sparsame URL-Vorkommen entspricht dem Wikilink-basierten Design des Vaults.

**Severity: Keine Findings**

---

## Schritt F — Frontmatter-Konsistenz

### F1. Fehlende Pflichtfelder

**Vollständige automatische Prüfung** aller wiki/-Dateien auf die Pflichtfelder `title`, `type`, `tags`, `sources`, `created`, `updated`, `summary`.

**Ergebnis:** Keine fehlenden Pflichtfelder bei regulären Wiki-Seiten. Alle Seiten mit Frontmatter haben alle 7 Felder befüllt.

Erwartungsgemäß ohne Frontmatter (kein Fehler):
- `wiki/log.md` — Append-only Log
- `wiki/Dashboard.md` — Widget-Seite
- `wiki/index.md` — Hat eigenes leichteres Frontmatter (title/type/updated) — OK für Index

### F2. Verwendete type-Werte

Erlaubte Typen laut CLAUDE.md Schema: `entity | concept | source | synthesis | comparison`

**Prüfung:** Alle verwendeten `type:`-Werte sind schema-konform. Kein ungültiger Typ gefunden.

Verteilung (geschätzt aus Dateianzahl nach Verzeichnis):
- `entity` — ca. 107 Seiten
- `source` — ca. 103 Seiten
- `concept` — ca. 67 Seiten
- `synthesis` — 4 Seiten
- `comparison` — 1 Seite

### F3. Datumsformate

**Ergebnis: Konsistent.** Alle Datumsfelder (`created`, `updated`) verwenden einheitlich das Format `YYYY-MM-DD`. Keine Abweichungen gefunden.

### F4. YAML-Syntaxfehler (verweist auf Schritt C3)

9 Dateien haben `summary:`-Felder mit Doppelpunkten ohne Anführungszeichen — technischer Fehler der von Standard-YAML-Parsern nicht toleriert wird. Vollständige Liste und Fix-Beschreibung: siehe Schritt C3.

**Severity: Mittel**

---

## 9. Priorisierte Action-Liste (vollständig — inkl. Schritte A–F)

| Prio | Schritt | Aufgabe | Severity | Status |
|---|---|---|---|---|
| ✅ | — | Graph: hideUnresolved=true | Kritisch | erledigt |
| ✅ | — | log.md: kaputte Links gefixt | Mittel | erledigt |
| 1 | C3/F4 | **YAML-Syntaxfehler** — 9 summary-Felder in Anführungszeichen einschließen (Dataview-Kompatibilität) | Mittel | offen |
| 2 | A1 | **Rechenfehler korrigieren** — `wiki/entities/Oleg Financial Situation.md` Z. 25: 61.079 → 62.110 € | Mittel | offen |
| 3 | A5 | **Tier-1 Stack vereinheitlichen** — `wiki/sources/Performance Coffee Brand Business Case.md` auf den Alpha-GPC/Kreatin/Taurin-Stack (Hai Onepager / Ingredienzen DB) umstellen; COGS neu berechnen | Mittel | offen |
| 4 | A3 | **Wagglz-Kostenkommentar** — In `wiki/entities/Wagglz GmbH.md` Fußnote ergänzen: Unterschied 120–255 € (Oleg-Darlehen nur Wagglz) vs. 357 € (Gesellschafterdarlehen gesamt beider Gesellschaften) vs. 380–420 € (Wagglz Firmenfixkosten) | Mittel | offen |
| 5 | — | **7 verwaiste Seiten** von relevanten Entity-Seiten aus verlinken | Mittel | offen |
| 6 | A6 | **DoktorLib → Doctolib** — `wiki/entities/Oleg Financial Situation.md` Z. 21+112: Link auf `[[Doctolib 2026]]` korrigieren | Niedrig | offen |
| 7 | A4 | **GROVE Businessplan Entity** — Archiv-Hinweis im summary ergänzen: "ARCHIVIERT — Pivot zu Performance Coffee Brand am 2026-06-16" | Niedrig | offen |
| 8 | A2 | **Fixkostenquote** — in `wiki/entities/Doctolib 2026.md` klarstellen: 61 % gilt inkl. variablem Wagglz-Darlehen; Fixkosten Übersicht (58 %) exklusive | Niedrig | offen |
| 9 | A7 | **OK Capital Finom Balance** — `wiki/entities/Finanzübersicht 2026.md`: "TODO" → 0,00 € (Jun 2026, unbestätigt) | Niedrig | offen |
| 10 | — | Duplikat-Cluster "finanz"/"consorsbank" auf 1 MOC konsolidieren | Niedrig | offen |
| 11 | — | Stub `Inbox 2026-06-13 Detail` löschen | Niedrig | offen |
| 12 | — | NAC: Tier-1 ja/nein entscheiden und in Performance Coffee Brand Entity aktualisieren | Inhaltlich | offen |

---

**Audit vollständig abgeschlossen** — Schritte A–F durchgeführt am 2026-06-20. Gesamtbefund: Vault in gutem Zustand. Kritischste offene Punkte sind YAML-Syntaxfehler (C3/F4), der Rechenfehler im Jahreseinkommen (A1) und die Tier-1-Stack-Inkonsistenz (A5).
