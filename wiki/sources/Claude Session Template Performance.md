---
title: Claude Session Template Performance
type: source
tags: [template, claude, performance, training, nutrition, hyrox, longevity, supplement, blutbild, oleg]
sources: ["raw/Privat/Finanzen/Templates/Claude Session – Performance.md"]
created: 2026-06-13
updated: 2026-06-13
summary: Reusable Claude session template for Oleg's Performance & Leben domain — includes persistent context block with body metrics, and five session-type sub-templates covering training plans, nutrition tracking, supplement checks, bloodwork interpretation, and Hyrox-specific blocks
---

# Claude Session Template — Performance

## Overview

This source document is a reusable prompt template for [[Oleg Personal Context|Oleg]]'s **Performance & Leben** Claude project (see [[Claude Projects Setup]]). It is designed so that new sessions always start with a persistent context block — eliminating repeated re-explanation of baseline metrics — followed by a specific session-type template.

The template is stored at `raw/Privat/Finanzen/Templates/Claude Session – Performance.md` (note: filed under Finanzen/Templates, though content is performance-domain).

> For the broader Claude Projects architecture, see [[Claude Projects Setup]] and [[Claude Projects Setup Source Detail]].

---

## Persistent Context Block

The following context block is designed to be pasted at the top of every new conversation:

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

## Key Data Points Confirmed by This Source

This template independently confirms the following metrics, consistent with [[3D Body Scan Scaneca Mai 2026]]:

| Metric | Value | Consistent with Scan? |
|---|---|---|
| Age | 32 years | ✅ |
| Location | Berlin | ✅ |
| Height | 188 cm | ✅ |
| Weight | 96.7 kg | ✅ |
| Body fat | 20.3% | ✅ |
| Lean mass | 77.1 kg | ✅ |
| Waist | 97.2 cm | ✅ |
| Waist-hip ratio | 0.92 | ✅ (consistent with waist 97.2 / hip 105.5 = 0.922) |
| BMR | 2,113 kcal | ✅ |
| Daily calorie target | ~2,800 kcal | ✅ |
| Forward head posture | ~30° | ✅ |
| Scan date | 29.05.2026 | ✅ |

### ⚠️ Minor Data Point: Protein Target

This template states **~220 g/day** protein target. The [[3D Body Scan Scaneca Mai 2026]] entity page states **195–200g/day**, and [[BMR and TDEE]] uses the same 195–200g figure derived from the scan document.

> ⚠️ **Contradiction noted:** Protein target discrepancy — scan/protocol pages state 195–200 g/day; this template states ~220 g/day. The template may represent an updated or rounded-up target (possibly set after the scan), or a different calculation method (e.g., 2.3g per kg body weight × 96.7 kg ≈ 222 g vs. lean-mass-based calculation of ~2.6g/kg lean mass × 77.1 kg ≈ 200 g). The 220g figure is body-weight-based; 195–200g is lean-mass-based. **Both are valid approaches.** The template's 220g figure should be noted as the operationally used target in Claude sessions.

### ⚠️ New Data Point: WHR Target and Bilateral Asymmetry

This template adds two data points **not previously captured** in the wiki:

1. **WHR target: <0.86** — The scan pages record WHR = 0.92 but do not specify a target WHR. This template adds the target: **<0.86**.
2. **Bilateral asymmetry / body center of gravity shifted right** — This structural finding is not in the [[3D Body Scan Scaneca Mai 2026]] or [[3D Body Scan]] pages. It should be added to those pages.
3. **Visceral fat distribution explicitly named** (not just inferred from WHR) — adds clinical framing.
4. **Hauptlimitor Hyrox: Aerobe Kapazität** — explicitly names aerobic capacity as the primary limiting factor for [[Hyrox Competition]], consistent with [[Hyrox 10-Week Training]] but not previously stated as explicitly in the wiki.
5. **Peter Attia added as reference** — The template lists Huberman, Attia, Bryan Johnson. [[Peter Attia]] appears in the wiki as a reference figure but this template confirms his explicit inclusion in Oleg's performance reference framework alongside [[Andrew Huberman]] and [[Bryan Johnson]].

---

## Five Session-Type Templates

### 1. Trainingsplan erstellen (Training Plan Creation)

**Variables required:**
- Verfügbare Trainingstage (training days/week)
- Sedentäre Zeit (sedentary context: office / home office / mixed)
- Schlaf-Routine (sleep schedule: bedtime + wake time)
- Equipment (gym / home / both)

**Output requested:** Weekly protocol covering Zone 2 + strength + Hyrox stations + posture.

This maps to [[Health Protocol Master]]'s training structure: the four components (Zone 2, strength, Hyrox-specific stations, posture correction) are exactly the building blocks of Oleg's current training split.

### 2. Ernährungs-Tracking (Nutrition Tracking)

**Variables required:**
- Description of meals eaten that day

**Output requested:** Analysis of protein target achievement, caloric balance, timing optimizations.

This supports the daily execution layer of the [[BMR and TDEE]] framework (2,800 kcal target, ~220g protein).

### 3. Supplement-Check

**Variables required:**
- Current supplement list
- Bloodwork results (if available)

**Output requested:** Identify gaps, redundancies, and optimization opportunities.

This template directly supports [[Supplement Stack]] review sessions and bloodwork-driven protocol adjustments.

### 4. Blutbild-Interpretation (Bloodwork Interpretation)

**Variables required:**
- Blood draw date
- Lab values

**Output requested:** Interpretation against **longevity-optimal ranges** (not just standard lab reference ranges); prioritized intervention list.

> **Key distinction:** The template explicitly requests interpretation against longevity-optimal benchmarks, not standard lab ranges. This is consistent with the [[Oleg Personal Context]] reference framework (Attia, Huberman, Johnson) where longevity-optimal ranges often differ substantially from clinical reference ranges (e.g., ApoB <60 mg/dL for longevity vs. <130 mg/dL clinical normal).

### 5. Hyrox-Spezifisch (Hyrox-Specific Block)

**Variables required:**
- Competition date / target date
- Current weaknesses (stations / aerobic endurance / specific)

**Output requested:** Specific training block for X weeks leading up to competition.

This template supports [[Hyrox 10-Week Training]] planning and any future race-specific blocks.

---

## Integration with Claude Projects Architecture

This template is designed for use within the **Performance & Leben** context-driven project (see [[Claude Projects Setup]]):

| Template Element | Claude Projects Alignment |
|---|---|
| Persistent context block | Context-driven project memory supplement |
| Direct tone, no wellness BS | Global preference: direkt, präzise |
| German language output | Global preference: Deutsch always |
| Evidenzbasiert framework | Project role: Elite Performance Coach |
| Immediately actionable outputs | Global preference: sofort verwendbar |

The context block functions as a **manual context inject** — compensating for limitations in cross-session memory by ensuring the AI always starts with accurate baseline data.

---

## Related Pages

- [[Claude Projects Setup]] — parent AI project architecture
- [[Claude Projects Setup Source Detail]] — full Claude project config
- [[3D Body Scan Scaneca Mai 2026]] — source of all body metric data in context block
- [[3D Body Scan Scaneca Mai 2026 Source Detail]] — raw scan data
- [[Health Protocol Master]] — protocol supported by these session templates
- [[Supplement Stack]] — target of supplement-check template
- [[BMR and TDEE]] — metabolic baseline referenced in nutrition template
- [[Hyrox 10-Week Training]] — Hyrox-specific template application
- [[Hyrox Competition]] — competition goal
- [[Andrew Huberman]] — reference framework
- [[Bryan Johnson]] — reference framework
- [[Peter Attia]] — reference framework (added by this source)
- [[Forward Head Posture]] — structural finding referenced in context block
- [[Oleg Personal Context]] — subject of all templates
- [[MOC Performance und Leben]] — parent MOC
