---
title: "Claude Session Template — Performance"
type: template
tags: [template, claude, performance, training, nutrition, supplement, longevity, blutbild, hyrox, protocol, deutsch]
sources: ["raw/Privat/Finanzen/Templates/Claude Session – Performance.md"]
created: 2026-06-13
updated: 2026-06-17
summary: Universelles Claude-Session-Template für Training, Ernährung, Körper und Longevity-Gespräche mit Oleg Kober (32J., Berlin, 96,7kg). Enthält standardisierter Kontext-Block (Scaneca-Baseline 29.05.2026, Ziele, Referenzen), 6 Session-Typen (Trainingsplan, Ernährungs-Tracking, Supplement-Check, Blutbild-Interpretation, Hyrox-spezifisch, Custom), ausführliche Parameter-Anforderungen und Ton-Richtlinien (direkt, evidenzbasiert, Deutsch). Zur Wiederverwendung bei neuen Performance-Gesprächen kopieren und Kontext-Block einfügen.
---

# Claude Session Template — Performance

> Für neue Gespräche zu Training, Ernährung, Körper, Longevity. Kontext einfügen, Frage stellen.

## Überblick

Dieses Template standardisiert Claude-Sessions zu Performance, Training, Ernährung und Longevity für [[Oleg Personal Context|Oleg Kober]]. Der Kontext-Block wird am Anfang jedes Gesprächs eingefügt — dadurch vermeidet man wiederholte Kontexterklärungen und dokumentiert die Baseline-Informationen konsistent.

**Zielgruppe:** Claude (in neuen Chats).  
**Sprache:** Deutsch (Fließtext, keine Wellness-Bullshit).  
**Referenzen:** Huberman, Attia, Bryan Johnson (evidenzbasiert).

---

## Standardisierter Kontext-Block

Diesen Block kopieren und am Anfang jedes neuen Gesprächs einfügen:

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

## Session-Typen

### 1. Trainingsplan erstellen

**Auftrag an Claude:**

```
[Kontext-Block oben einfügen]

Verfügbare Trainingstage: [X Tage/Woche]
Sedentäre Zeit: [Büro / Home-Office / gemischt]
Schlaf-Routine: [Einschlaf: XX:00 | Aufwach: XX:00]
Equipment: [Gym / Home / beides]

Erstelle wöchentliches Protokoll: Zone 2 + Kraft + Hyrox-Stationen + Haltung.
```

**Beispiel:**

```
Verfügbare Trainingstage: 6 Tage/Woche
Sedentäre Zeit: Büro (~7–8h/Tag)
Schlaf-Routine: Einschlaf: 22:30 | Aufwach: 06:30
Equipment: Gym (vollständig ausgestattet)

Erstelle wöchentliches Protokoll: Zone 2 + Kraft + Hyrox-Stationen + Haltung.
```

---

### 2. Ernährungs-Tracking

**Auftrag an Claude:**

```
[Kontext-Block oben einfügen]

Ich esse heute: [Mahlzeiten beschreiben]
Analysiere: Protein-Zielerreichung, Kalorienbalance, Timing-Optimierungen.
```

**Beispiel:**

```
Ich esse heute:
- 08:00 Uhr: 3 Eier, 100g Haferflocken, Berries
- 12:00 Uhr: 200g Hähnchenbrust, 200g Broccoli, 150g Jasminreis
- 16:00 Uhr: 50g Whey Protein, 1 Banane, 30g Erdnussbutter
- 19:30 Uhr: 250g Rinder-Steak, 300g Süßkartoffel, Spinat

Analysiere: Protein-Zielerreichung, Kalorienbalance, Timing-Optimierungen.
```

---

### 3. Supplement-Check

**Auftrag an Claude:**

```
[Kontext-Block oben einfügen]

Aktuelle Supplemente: [Liste]
Blutbild-Ergebnis: [Werte einfügen wenn vorhanden]
Frage: [Was fehlt / was ist überflüssig / Optimierungen?]
```

**Beispiel:**

```
Aktuelle Supplemente:
- Whey Protein (30g/Tag)
- Creatine Monohydrat (5g/Tag)
- Omega-3 (2g EPA+DHA/Tag)
- Vitamin D3 (4.000 IU/Tag)
- Magnesium Glycinat (400mg vor Schlaf)
- Koffein (200mg morgens)

Blutbild-Ergebnis:
- Vitamin D: 45 ng/mL (optimal)
- B12: 520 pg/mL (gut)
- Eisen (Ferritin): 88 ng/mL (gut)
- Magnesium: 2,1 mg/dL (am unteren Ende)

Frage: Sollte ich Magnesium erhöhen? Fehlt etwas für Longevity?
```

---

### 4. Blutbild-Interpretation

**Auftrag an Claude:**

```
[Kontext-Block oben einfügen]

Meine aktuellen Blutwerte (Abnahme: [Datum]):
[Werte einfügen]

Interpretiere gegen Longevity-Optimal-Bereiche (nicht nur Laborrefenzwerte).
Prioritäre Interventionen: was ändere ich zuerst?
```

**Beispiel:**

```
Meine aktuellen Blutwerte (Abnahme: 15.06.2026):
- Nüchtern-Glukose: 102 mg/dL
- HbA1c: 5,8 %
- Triglyzeride: 135 mg/dL
- LDL-C: 145 mg/dL
- HDL-C: 42 mg/dL
- hs-CRP: 1,8 mg/L
- Lipoprotein(a): 32 nmol/L
- Vitamin D: 38 ng/mL
- Ferritin: 92 ng/mL

Interpretiere gegen Longevity-Optimal-Bereiche (nicht nur Laborrefenzwerte).
Prioritäre Interventionen: was ändere ich zuerst?
```

---

### 5. Hyrox-spezifisch

**Auftrag an Claude:**

```
[Kontext-Block oben einfügen]

Wettkampf: [Datum / Zieldatum]
Aktuelle Schwächen: [Stationen / aerobe Ausdauer / spezifisches]
Erstelle: Spezifischen Trainingsblock für [X Wochen] bis Wettkampf.
```

**Beispiel:**

```
Wettkampf: 12.10.2026 (Berlin Hyrox)
Aktuelle Schwächen: 
- Aerobe Ausdauer (Hauptlimitor laut Scan)
- SkiErg (Oberkörper-Ausdauer)
- Wallball (explosive Kraft + Ausdauer-Kombination)

Erstelle: Spezifischen Trainingsblock für 12 Wochen bis Wettkampf.
```

---

### 6. Custom / Spezialfrage

**Auftrag an Claude:**

```
[Kontext-Block oben einfügen]

[Beliebige Frage zu Performance, Training, Nutrition, Longevity]
```

**Beispiele:**

- "Wie optimiere ich NSDR + Schlaf für WHR-Reduktion?"
- "Sollte ich auf Ketose wechseln vor Hyrox-Wettkampf?"
- "NMN + Urolithin A — brauche ich beide, oder reicht eins für Longevity?"
- "Trainiere ich genug Zone 2 für aerobe Kapazität-Anpassung?"

---

## Tone & Guidelines

| Richtlinie | Bedeutung |
|---|---|
| **Direkt** | Keine langen Vorrede; sofort zur Sache |
| **Konkret** | Zahlen, Protokolle, Mechanismen (nicht "alles ist möglich") |
| **Evidenzbasiert** | Huberman, Attia, Bryan Johnson, Peer-Review-Studien (nicht Instagram-Fitness) |
| **Deutsch** | Fließtext Deutsch; englische Fachbegriffe (Zone 2, NSDR, COGS) bleiben |
| **Kein Bullshit** | Keine Wellness-Phrasen; Bias-Disclosure bei Unsicherheit |

---

## Häufig benötigte Kontexte

### Ziele (aus 3D-Scan-Baseline)

| Ziel | Wert | Zieldatum |
|---|---|---|
| **Körperfett** | 15–17 % | ~Mitte September 2026 |
| **Taille** | <90 cm | ~Mitte September 2026 |
| **WHR** | <0,86 | ~Mitte September 2026 |
| **Lean Mass** | ≥77 kg (erhalten) | durchgehend |

### Hyrox-Vorbereitung

- **Zieldatum:** Okt/Nov 2026 (TBD)
- **Hauptlimitor:** Aerobe Kapazität
- **Fokus:** Zone 2 Training, technische Stationen (SkiErg, Wallball, Rope Climb)
- **Sekundär:** Kraft, Haltung (Forward Head 30°)

### Longevity-Stack

Aktuell unter Evaluation:
- **Phase 1:** Basicsupps (Protein, Omega-3, Vitamin D, Magnesium)
- **Phase 2:** Koffein + L-Theanin (Performance Coffee, geplant)
- **Phase 3:** NMN, Urolithin A, Spermidin (abhängig von [[Performance Coffee Brand]] Launch und Verfügbarkeit)

---

## Referenzmaterialien

- [[Health Protocol Master]] — Master-Protokoll mit Baseline
- [[3D Body Scan Scaneca Mai 2026]] — Baseline-Messwerte (29.05.2026)
- [[Zone 2 Training]] — aerobe Kapazität-Konzept
- [[Corrective Exercise]] — Forward Head Posture 30° Korrektur
- [[Performance Coffee Brand]] — Koffein-L-Theanin-Stack in Entwicklung
- [[ALG I Progressionsvorbehalt]] — ESt 2025 Kontext (falls relevant für Finanzplanung)

---

## Best Practices

1. **Kontext kopieren, nie umschreiben** — Die genaue Basis sichert Konsistenz
2. **Spezifische Daten eingeben** — "Ich esse viel" ist weniger wertvoll als genaue Mahlzeiten
3. **Ziel klar machen** — "Analysiere Protein-Zielerreichung" ist klarer als "Ist das gut?"
4. **Fehlendes flaggen** — "Ich habe kein Blutbild, aber [sichtbare Symptome]" ist besser als Umdeutung
5. **Feedback-Loop** — Wenn Claudios Antwort zu allgemein ist, spezifizieren: "Gib konkrete Makro-Aufteilung für die 2.800 kcal"

---

## Verwandte Seiten

- [[Health Protocol Master]] — Master-Protokoll
- [[3D Body Scan Scaneca Mai 2026]] — Baseline-Entität
- [[Zone 2 Training]] — Aerobe Kapazität
- [[Corrective Exercise]] — Haltungskorrektur
- [[Performance Coffee Brand]] — Koffein-Stack in Entwicklung
- [[Oleg Personal Context]] — Adressat dieses Templates
- [[Huberman Lab]], [[Attia (Peter)]], [[Bryan Johnson]] — Referenzen
