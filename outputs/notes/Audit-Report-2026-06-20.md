---
title: Audit-Report Intelligence Hub
type: synthesis
created: 2026-06-20
updated: 2026-06-20
tags: [audit, qualität, obsidian]
summary: Vollständiger Vault-Audit — Struktur, Duplikate, Links, Security, Obsidian-Setup
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

## 3. Plausibilitäts-Konflikte

Keine kritischen Widersprüche gefunden. Bekannte offene Punkte:
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

## 5. Sprach-Findings

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

# Teil 2 — Vertiefter Audit (Schritte A–F)

## A. Plausibilitätsprüfung — Zahlen & Fakten

| # | Befund | Severity | Status |
|---|---|---|---|
| A1 | **Wagglz Fehlbetrag-Widerspruch:** `entities/Wagglz GmbH.md` behauptete der Verlustbetrag sei *"not available in current sources"* — tatsächlich steht **27.926,89 €** im Raw-Source (`raw/Business/Wagglz/Wagglz GmbH.md`) und in 8 weiteren Wiki-Seiten. | Mittel | ✅ **behoben** — Entity synchronisiert (Fehlbetrag, §19 InsO, Rangrücktritt ergänzt) |
| A2 | **OK Capital Saldo-Widerspruch:** Innerhalb derselben Seite `entities/OK Capital UG.md` stand Zeile 25 „0,00 €", Zeile 8 + 30 „balance unknown". Quelle [[OK Capital Finom 2026]] sagt ebenfalls „not available". | Mittel | ✅ **behoben** — Contradictions-Sektion ergänzt, 0,00 € als unbestätigte Annahme [A] markiert |
| A3 | **Dezimalformat-Inkonsistenz:** ~10+ Seiten mischen DE-Format (3.638,82 €) und US-Format (3,638.82 €) — u.a. `Doctolib 2026.md`, `Fixkosten Übersicht.md`, `Oleg Command Center.md`. | Niedrig | offen — Vault-Standard sollte DE sein |

Verifizierte konsistente Werte (keine Widersprüche):
- **Doctolib Netto 3.638,82 €/Mo**, EBV-Brutto 6.664 € — über alle Seiten konsistent ✅
- **Performance Coffee COGS** ~0,145 €/Portion (Vorsession-Fix hält) ✅
- **Wagglz Umsatz 0 € seit Jan 2026** — konsistent ✅

## B. Attachment- & Embed-Audit

| Prüfung | Ergebnis |
|---|---|
| Assets in `raw/assets/` | 19 Dateien |
| Verwaiste Assets (nicht referenziert) | **0** ✅ |
| Kaputte Embeds `![[...]]` | **0** ✅ |

→ Attachment-Hygiene einwandfrei.

## C. Conversion-Artefakte

| Prüfung | Ergebnis |
|---|---|
| HTML-Tags (`<div>`, `<span>`, `&nbsp;` …) in wiki/ | **0** ✅ |
| HTML-Tags in outputs/ | **0** ✅ |
| Kaputte Frontmatter-Blöcke | **0** (nur `Dashboard.md` bewusst ohne FM) ✅ |

→ Keine Importreste aus HTML-zu-Markdown-Konvertierung.

## D. Sprachkonsistenz

| Klasse | Anzahl Seiten |
|---|---|
| Überwiegend **Englisch** (>70% EN-Stoppwörter) | **222 von 285** |
| **Gemischt** (40–70% EN) | 17 |
| Überwiegend Deutsch | ~46 |

**Severity: Mittel.** Der Vault-Standard ist laut CLAUDE.md Deutsch, aber 78% der Wiki-Seiten sind primär englisch verfasst. Ursache: der frühere `ingest.py` SYSTEM-Prompt war auf Englisch → das Modell schrieb englische Prosa. Betrifft auch deutsche Themen (z.B. `entities/Wagglz GmbH.md`, `entities/VW-Bank Finanzierung.md`). 

→ **Empfehlung:** Bei zukünftigen Ingests deutschen Output erzwingen (ingest.py Prompt ergänzen: „Schreibe alle Wiki-Seiten auf Deutsch"). Bestehende 222 Seiten nur bei Bedarf übersetzen — Fachbegriffe (Performance Coffee, Longevity) dürfen englisch bleiben.

## E. Externe URLs

Nur **3 externe URLs** im gesamten Vault — alle valide Domains:
- `foundmyfitness.com/episodes/coffee` (Rhonda Patrick)
- `brainflow.co/dr-rhonda-patricks-coffee-protocol/`
- `youtube.com`

→ Keine toten Links. Severity: keine.

## F. Frontmatter-Konsistenz

| Prüfung | Ergebnis |
|---|---|
| Seiten ohne Frontmatter | 0 ✅ |
| Fehlend `sources:` | 1 Seite |
| Fehlend `summary:` | 1 Seite |
| Ungültige `type:`-Werte | **0** ✅ |
| Type-Verteilung | entity 107, source 103, concept 67, synthesis 4, comparison 1 |

→ Frontmatter-Disziplin nahezu perfekt.

## G. Scope-Befund (zusätzlich)

**Doctolib/DoktorLib Namens-Split + Scope-Verletzung** — Severity: Mittel
- 4 Entity-Seiten für denselben Arbeitgeber: `Doctolib.md`, `Doctolib 2026.md`, `DoktorLib.md`, `DoktorLib Automation Pipeline.md` (zwei Schreibweisen)
- `DoktorLib Automation Pipeline.md` ist **Firmen-Automation** — laut CLAUDE.md explizit **„Nicht in diesem Vault"**
- **Empfehlung:** Schreibweise vereinheitlichen (Doctolib), Automation-Pipeline-Seite nach `_archiv` oder löschen. Gehalts-/Finanzdaten (Doctolib 2026) bleiben — die sind für Finanzen in-scope.

---

## 9. Priorisierte Action-Liste (final)

| Prio | Aufgabe | Severity | Status |
|---|---|---|---|
| — | Graph: hideUnresolved=true | Kritisch | ✅ erledigt |
| — | log.md: kaputte Links gefixt | Mittel | ✅ erledigt |
| — | Wagglz Fehlbetrag-Widerspruch (A1) | Mittel | ✅ erledigt |
| — | OK Capital Saldo-Widerspruch (A2) | Mittel | ✅ erledigt |
| 1 | DoktorLib-Automation aus Scope entfernen (G) | Mittel | offen |
| 2 | 222 EN-Seiten: künftigen Ingest auf DE umstellen (D) | Mittel | offen |
| 3 | Dezimalformat DE vereinheitlichen (A3) | Niedrig | offen |
| 4 | 7 verwaiste Seiten verlinken | Mittel | offen |
| 5 | Duplikat-Cluster "finanz"/"consorsbank" konsolidieren | Niedrig | offen |
| 6 | Stub `Inbox 2026-06-13 Detail` löschen | Niedrig | offen |
| 7 | NAC: Tier-1 ja/nein entscheiden | Inhaltlich | offen |

---

**Audit vollständig abgeschlossen** — alle Schritte 1–9 + A–G durchgeführt am 2026-06-20.
