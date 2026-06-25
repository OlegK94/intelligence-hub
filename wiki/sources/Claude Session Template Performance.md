---
title: Claude Session Template Performance
type: source
tags: [template, claude, performance, training, nutrition, hyrox, longevity, supplement, blutbild, oleg]
sources: ["raw/Privat/Finanzen/Templates/Claude Session – Performance.md"]
created: 2026-06-13
updated: 2026-06-13
summary: Wiederverwendbares Claude-Session-Template für Olegs Performance & Leben Domain — enthält einen persistenten Kontextblock mit Körperkennzahlen sowie fünf Session-Typ-Subtemplates für Trainingspläne, Ernährungs-Tracking, Supplement-Checks, Blutbild-Interpretation und Hyrox-spezifische Blöcke
---

# Claude Session Template — Performance

## Überblick

Dieses Quelldokument ist ein wiederverwendbares Prompt-Template für [[Oleg Personal Context|Olegs]] **Performance & Leben** Claude-Projekt (siehe [[Claude Projects Setup]]). Es ist so konzipiert, dass neue Sessions stets mit einem persistenten Kontextblock beginnen — wodurch das wiederholte Erklären von Basiskennzahlen entfällt — gefolgt von einem spezifischen Session-Typ-Template.

Das Template ist gespeichert unter `raw/Privat/Finanzen/Templates/Claude Session – Performance.md` (Hinweis: abgelegt unter Finanzen/Templates, obwohl der Inhalt zur Performance-Domain gehört).

> Zur übergeordneten Claude-Projects-Architektur siehe [[Claude Projects Setup]] und [[Claude Projects Setup Source Detail]].

---

## Persistenter Kontextblock

Der folgende Kontextblock ist dafür vorgesehen, am Anfang jeder neuen Konversation eingefügt zu werden:

```
KONTEXT — NICHT NEU ERKLÄREN

Person: Oleg Kober, 32 J., Berlin. 188 cm, 96,7 kg.
Scan: 29.05.2026, Scaneca/Labor Berlin.

Körperdaten:
- Körperfett: 20,3 % | Lean Mass: 77,1 kg
- Taille: 97,2 cm | Taille-Hüfte-Ratio: 0,92 (Ziel: <0,86)
- Grundumsatz: 2.113 kcal
- Zielkalorien: ~2.800 kcal/Tag | Protein: ~220 g/Tag

Strukturelle Befunde:
- Ausgeprägte Kopfvorneigung (~30°)
- Körperschwerpunkt rechts verschoben (bilaterale Asymmetrie)
- Viszeral-Fettverteilung (WHR 0,92)

Ziele: Körperfett reduzieren, Oberkörper aufbauen, Hyrox-Performance, Longevity.
Hauptlimitor Hyrox: Aerobe Kapazität.

Referenzrahmen: Huberman, Attia, Bryan Johnson. Evidenzbasiert.
Ton: Direkt, konkret, kein Wellness-Bullshit. Deutsch.
```

---

## Durch diese Quelle bestätigte Schlüsselkennzahlen

Dieses Template bestätigt unabhängig die folgenden Kennzahlen, konsistent mit [[3D Body Scan Scaneca Mai 2026]]:

| Kennzahl | Wert | Konsistent mit Scan? |
|---|---|---|
| Alter | 32 Jahre | ✅ |
| Standort | Berlin | ✅ |
| Größe | 188 cm | ✅ |
| Gewicht | 96,7 kg | ✅ |
| Körperfett | 20,3 % | ✅ |
| Lean Mass | 77,1 kg | ✅ |
| Taillenumfang | 97,2 cm | ✅ |
| Taille-Hüfte-Ratio | 0,92 | ✅ (konsistent mit Taille 97,2 / Hüfte 105,5 = 0,922) |
| Grundumsatz | 2.113 kcal | ✅ |
| Tägliches Kalorienziel | ~2.800 kcal | ✅ |
| Kopfvorneigung | ~30° | ✅ |
| Scan-Datum | 29.05.2026 | ✅ |

### ⚠️ Kleinere Abweichung: Protein-Zielwert

Dieses Template gibt **~220 g/Tag** als Proteinziel an. Die Entitätsseite [[3D Body Scan Scaneca Mai 2026]] nennt **195–200 g/Tag**, und [[BMR and TDEE]] verwendet denselben aus dem Scan-Dokument abgeleiteten Wert von 195–200 g.

> ⚠️ **Widerspruch festgestellt:** Abweichung beim Proteinziel — Scan- und Protokollseiten nennen 195–200 g/Tag; dieses Template gibt ~220 g/Tag an. Das Template repräsentiert möglicherweise ein aktualisiertes oder aufgerundetes Ziel (eventuell nach dem Scan festgelegt) oder eine andere Berechnungsmethode (z. B. 2,3 g pro kg Körpergewicht × 96,7 kg ≈ 222 g gegenüber der Lean-Mass-basierten Berechnung von ~2,6 g/kg Lean Mass × 77,1 kg ≈ 200 g). Der 220-g-Wert basiert auf dem Körpergewicht; 195–200 g basieren auf der Lean Mass. **Beide Ansätze sind valide.** Der 220-g-Wert des Templates sollte als operativ genutztes Ziel in Claude-Sessions vermerkt werden.

### ⚠️ Neue Datenpunkte: WHR-Ziel und bilaterale Asymmetrie

Dieses Template ergänzt zwei Datenpunkte, die **bisher nicht im Wiki erfasst** waren:

1. **WHR-Ziel: <0,86** — Die Scan-Seiten dokumentieren WHR = 0,92, nennen aber keinen Ziel-WHR. Dieses Template fügt das Ziel hinzu: **<0,86**.
2. **Bilaterale Asymmetrie / Körperschwerpunkt nach rechts verschoben** — Dieser strukturelle Befund ist weder auf der Seite [[3D Body Scan Scaneca Mai 2026]] noch auf [[3D Body Scan]] enthalten. Er sollte dort ergänzt werden.
3. **Viszeral-Fettverteilung explizit benannt** (nicht nur aus dem WHR abgeleitet) — ergänzt die klinische Einordnung.
4. **Hauptlimitor Hyrox: Aerobe Kapazität** — benennt die aerobe Kapazität explizit als primären limitierenden Faktor für [[Hyrox Competition]], konsistent mit [[Hyrox 10-Week Training]], aber bisher nicht so explizit im Wiki formuliert.
5. **Peter Attia als Referenz ergänzt** — Das Template listet Huberman, Attia, Bryan Johnson. [[Peter Attia]] taucht im Wiki als Referenzperson auf, doch dieses Template bestätigt seine explizite Aufnahme in Olegs Performance-Referenzrahmen neben [[Andrew Huberman]] und [[Bryan Johnson]].

---

## Fünf Session-Typ-Templates

### 1. Trainingsplan erstellen

**Erforderliche Variablen:**
- Verfügbare Trainingstage (Trainingstage pro Woche)
- Sedentäre Zeit (Arbeitskontext: Büro / Homeoffice / gemischt)
- Schlaf-Routine (Schlafplan: Einschlaf- und Aufwachzeit)
- Equipment (Fitnessstudio / zu Hause / beides)

**Angeforderter Output:** Wochenprotokoll mit Zone 2, Kraft, Hyrox-Stationen und Haltungskorrektur.

Dies entspricht der Trainingsstruktur aus [[Health Protocol Master]]: Die vier Komponenten (Zone 2, Kraft, Hyrox-spezifische Stationen, Haltungskorrektur) sind genau die Bausteine von Olegs aktuellem Trainings-Split.

### 2. Ernährungs-Tracking

**Erforderliche Variablen:**
- Beschreibung der an diesem Tag gegessenen Mahlzeiten

**Angeforderter Output:** Analyse der Proteinzielerreichung, Kalorienbilanz, Timing-Optimierungen.

Dies unterstützt die tägliche Ausführungsebene des [[BMR and TDEE]]-Frameworks (2.800-kcal-Ziel, ~220 g Protein).

### 3. Supplement-Check

**Erforderliche Variablen:**
- Aktuelle Supplement-Liste
- Blutbefunde (falls vorhanden)

**Angeforderter Output:** Lücken, Redundanzen und Optimierungsmöglichkeiten identifizieren.

Dieses Template unterstützt direkt [[Supplement Stack]]-Review-Sessions und blutbildgestützte Protokollanpassungen.

### 4. Blutbild-Interpretation

**Erforderliche Variablen:**
- Datum der Blutabnahme
- Laborwerte

**Angeforderter Output:** Interpretation anhand **Longevity-optimaler Referenzbereiche** (nicht nur anhand der Standardlabor-Referenzbereiche); priorisierte Interventionsliste.

> **Wesentliche Unterscheidung:** Das Template fordert explizit eine Interpretation anhand Longevity-optimaler Benchmarks, nicht anhand klinischer Standardbereiche. Dies ist konsistent mit dem Referenzrahmen aus [[Oleg Personal Context]] (Attia, Huberman, Johnson), bei dem sich Longevity-optimale Bereiche häufig erheblich von klinischen Referenzbereichen unterscheiden (z. B. ApoB <60 mg/dL für Longevity gegenüber <130 mg/dL als klinischer Normwert).

### 5. Hyrox-Spezifisch

**Erforderliche Variablen:**
- Wettkampfdatum / Zieldatum
- Aktuelle Schwachstellen (Stationen / aerobe Ausdauer / spezifisch)

**Angeforderter Output:** Spezifischer Trainingsblock für X Wochen bis zum Wettkampf.

Dieses Template unterstützt die Planung von [[Hyrox 10-Week Training]] sowie zukünftige wettkampfspezifische Blöcke.

---

## Integration in die Claude-Projects-Architektur

Dieses Template ist für die Verwendung im kontextgesteuerten Projekt **Performance & Leben** konzipiert (siehe [[Claude Projects Setup]]):

| Template-Element | Ausrichtung auf Claude Projects |
|---|---|
| Persistenter Kontextblock | Ergänzung des kontextgesteuerten Projektgedächtnisses |
| Direkter Ton, kein Wellness-Bullshit | Globale Präferenz: direkt, präzise |
| Deutschsprachiger Output | Globale Präferenz: immer Deutsch |
| Evidenzbasiertes Framework | Projektrolle: Elite Performance Coach |
| Sofort umsetzbare Ergebnisse | Globale Präferenz: sofort verwendbar |

Der Kontextblock fungiert als **manueller Kontext-Inject** — er kompensiert die Einschränkungen beim sitzungsübergreifenden Gedächtnis, indem er sicherstellt, dass die KI stets mit genauen Basisdaten startet.

---

## Verwandte Seiten

- [[Claude Projects Setup]] — übergeordnete KI-Projektarchitektur
- [[Claude Projects Setup Source Detail]] — vollständige Claude-Projektkonfiguration
- [[3D Body Scan Scaneca Mai 2026]] — Quelle aller Körperkennzahlen im Kontextblock
- [[3D Body Scan Scaneca Mai 2026 Source Detail]] — Rohdaten des Scans
- [[Health Protocol Master]] — Protokoll, das durch diese Session-Templates unterstützt wird
- [[Supplement Stack]] — Ziel des Supplement-Check-Templates
- [[BMR and TDEE]] — metabolische Baseline, auf die im Ernährungs-Template verwiesen wird
- [[Hyrox 10-Week Training]] — Anwendung des Hyrox-spezifischen Templates
- [[Hyrox Competition]] — Wettkampfziel
- [[Andrew Huberman]] — Referenzrahmen
- [[Bryan Johnson]] — Referenzrahmen
- [[Peter Attia]] — Referenzrahmen (durch diese Quelle ergänzt)
- [[Forward Head Posture]] — struktureller Befund, auf den im Kontextblock verwiesen wird
- [[Oleg Personal Context]] — Subjekt aller Templates
- [[MOC Performance und Leben]] — übergeordnete MOC