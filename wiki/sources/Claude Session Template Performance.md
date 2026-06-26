---
title: "Claude Session Template Performance"
type: source
tags: [template, claude, performance, training, ernährung, longevity, hyrox, zone-2, oleg, body-composition, whrs, protein, kalorien]
sources: ["raw/Finanzdaten/ObsidianVault/Templates/Claude Session – Performance.md"]
created: 2026-06-13
updated: 2026-06-20
summary: Wiederverwendbare KI-Vorlage für Claude-Sessions zu Training, Ernährung, Körper und Longevity — enthält festen Kontext-Block mit Olegs aktuellen Körperdaten (Scan 29.05.2026, 96,7 kg, 20,3% KFA, WHR 0,92, Ziel <0,86, Protein ~220 g/Tag, 2.800 kcal) sowie fünf Session-Typen: Trainingsplan, Ernährungs-Tracking, Supplement-Check, Blutbild-Interpretation, Hyrox-spezifisch
---

# Claude Session Template — Performance

## Überblick

Dieses Quelldokument erfasst die wiederverwendbare KI-Vorlage (Claude-Session-Template) für alle Gespräche zu Training, Ernährung, Körper und Longevity im Vault von [[Oleg Personal Context|Oleg]]. Die Vorlage enthält einen **festen Kontext-Block**, der bei jeder neuen Session eingefügt wird, und fünf **Session-Typen** für strukturierte Anfragen.

Die Seite war im Wiki bereits als referenziertes Konzept bekannt (in [[3D Body Scan Scaneca Mai 2026]] und [[BMR and TDEE]] verlinkt). Diese Ingestion ergänzt die fehlende Source-Seite mit vollständigem Quelldokument-Inhalt.

---

## Kontext-Block (unveränderlich)

Der Kontext-Block enthält Olegs aktuelle Körperdaten und wird bei jeder Session eingefügt:

| Feld | Wert |
|---|---|
| **Person** | Oleg Kober, 32 J., Berlin |
| **Körpergröße** | 188 cm |
| **Gewicht** | 96,7 kg |
| **Scan-Datum** | 29.05.2026, Scaneca / Labor Berlin |
| **Körperfett** | 20,3% |
| **Lean Mass** | 77,1 kg |
| **Taille** | 97,2 cm |
| **Taille-Hüfte-Ratio (WHR)** | 0,92 |
| **WHR-Ziel** | <0,86 |
| **Grundumsatz (BMR)** | 2.113 kcal |
| **Zielkalorien** | ~2.800 kcal/Tag |
| **Protein-Ziel** | ~220 g/Tag |

### Strukturelle Befunde (Kontext-Block)

| Befund | Detail |
|---|---|
| **Kopfvorneigung** | ~30° (Forward Head Posture) |
| **Körperschwerpunkt** | rechts verschoben (bilaterale Asymmetrie) |
| **Fettverteilung** | viszeral (WHR 0,92) |

### Ziele und Referenzrahmen

- **Ziele:** Körperfett reduzieren, Oberkörper aufbauen, [[Hyrox Competition|Hyrox]]-Performance, [[Longevity]]
- **Hauptlimitor Hyrox:** Aerobe Kapazität
- **Referenzrahmen:** [[Andrew Huberman]], [[Peter Attia]], [[Bryan Johnson]]; evidenzbasiert
- **Ton:** Direkt, konkret, kein Wellness-Bullshit. Deutsch.

---

## Session-Typen

### 1 — Trainingsplan erstellen

```
[Kontext-Block oben]

Verfügbare Trainingstage: [X Tage/Woche]
Sedentäre Zeit: [Büro / Home-Office / gemischt]
Schlaf-Routine: [Einschlaf: XX:00 | Aufwach: XX:00]
Equipment: [Gym / Home / beides]

Erstelle wöchentliches Protokoll: Zone 2 + Kraft + Hyrox-Stationen + Haltung.
```

### 2 — Ernährungs-Tracking

```
[Kontext-Block oben]

Ich esse heute: [Mahlzeiten beschreiben]
Analysiere: Protein-Zielerreichung, Kalorienbalance, Timing-Optimierungen.
```

### 3 — Supplement-Check

```
[Kontext-Block oben]

Aktuelle Supplemente: [Liste]
Blutbild-Ergebnis: [Werte einfügen wenn vorhanden]
Frage: [Was fehlt / was ist überflüssig / Optimierungen?]
```

### 4 — Blutbild-Interpretation

```
[Kontext-Block oben]

Meine aktuellen Blutwerte (Abnahme: [Datum]):
[Werte einfügen]

Interpretiere gegen Longevity-Optimal-Bereiche (nicht nur Laborreferenzwerte).
Prioritäre Interventionen: was ändere ich zuerst?
```

### 5 — Hyrox-Spezifisch

```
[Kontext-Block oben]

Wettkampf: [Datum / Zieldatum]
Aktuelle Schwächen: [Stationen / aerobe Ausdauer / spezifisches]
Erstelle: Spezifischen Trainingsblock für [X Wochen] bis Wettkampf.
```

---

## Bestätigte Werte aus anderen Quellen

Dieses Template dient als **dritte unabhängige Bestätigung** der Körperdaten aus dem [[3D Body Scan Scaneca Mai 2026]]:

| Metrik | Wert in Template | Wert im Scan-Dokument | Übereinstimmung |
|---|---|---|---|
| Gewicht | 96,7 kg | 96,7 kg | ✅ |
| Körperfett | 20,3% | 20,3% | ✅ |
| Lean Mass | 77,1 kg | 77,1 kg | ✅ |
| Taille | 97,2 cm | 97,2 cm | ✅ |
| WHR | 0,92 | 0,92 | ✅ |
| BMR | 2.113 kcal | 2.113 kcal | ✅ |

### Geringfügige Abweichungen

| Metrik | Template | Scan-Dokument / Health Protocol | Anmerkung |
|---|---|---|---|
| **Protein-Ziel** | ~220 g/Tag | ~195–200 g/Tag (aus Magermasse) | Unterschied in der Berechnungsmethode (körpergewichtsbasiert vs. magermasse-basiert) — beide gültig |
| **WHR-Ziel** | <0,86 | <0,86 | ✅ übereinstimmend |

> ⚠️ **Diskrepanz beim Protein-Ziel:** Das Template verwendet ~220 g/Tag als operatives Ziel (körpergewichtsbasiert: ~2,3 g/kg × 96,7 kg). Das Scan-Dokument und [[Health Protocol Master]] verwenden 195–200 g/Tag (magermasse-basiert: ~2,6 g/kg × 77,1 kg). Das Template-Ziel von 220 g/Tag ist das täglich eingesetzte operative Ziel im KI-Tracking. Kein fundamentaler Widerspruch — unterschiedliche Berechnungsbasen.

---

## Verwendungskontext

Das Template fungiert als **Betriebsanleitung für KI-gestütztes Performance-Coaching**:

- Stellt sicher, dass bei jeder neuen Claude-Session keine erneute Kontextbereitstellung erforderlich ist
- Standardisiert den Ton (direkt, evidenzbasiert, kein Wellness-Bullshit)
- Referenzrahmen (Huberman, Attia, Bryan Johnson) verhindert generische Antworten
- Longevity-Optimal-Interpretation bei Blutbildwerten (nicht nur klinische Referenzbereiche — entspricht [[Biomarker Testing]])

---

## Verwandte Seiten

- [[Oleg Personal Context]] — Person, für die das Template gilt
- [[3D Body Scan Scaneca Mai 2026]] — Scan-Event, dessen Daten im Template stehen
- [[3D Body Scan Scaneca Mai 2026 Source Detail]] — primäres Scan-Quelldokument
- [[BMR and TDEE]] — metabolische Metriken aus dem Kontext-Block
- [[Health Protocol Master]] — übergeordnetes Protokoll
- [[Hyrox Competition]] — Wettkampfziel (Session-Typ 5)
- [[Zone 2 Training]] — Trainingsmodalität (Session-Typ 1)
- [[Forward Head Posture]] — struktureller Befund im Kontext-Block
- [[Biomarker Testing]] — Blutbild-Interpretation (Session-Typ 4)
- [[Supplement Stack]] — Supplement-Check (Session-Typ 3)
- [[Andrew Huberman]] — Referenzrahmen
- [[Peter Attia]] — Referenzrahmen (als „Attia" im Template)
- [[Bryan Johnson]] — Referenzrahmen
- [[MOC Performance und Leben]] — übergeordnete MOC
