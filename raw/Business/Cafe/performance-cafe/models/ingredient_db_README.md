# Wirkstoff-Datenbank — Lesehilfe

`ingredient_db.csv` — **127 Stoffe**, 20 Felder, Semikolon-getrennt. Vollständiges Kandidaten-Universum.
Quelle/Generator: `build_ingredient_db.py`.

In Excel/Numbers öffnen: Daten → Text in Spalten → Trennzeichen **Semikolon**.

## Kategorien (11)
Kaffee_intrinsisch (3) · A_Stimulans (12) · B_Nootropikum (15) · C_Adaptogen (11) · D_Pilz (7) · E_Aminosaeure (16) · F_Longevity (24) · G_Vitamin (9) · H_Mineral (9) · I_Botanik (10) · J_Hilfsstoff (11)

## Spalten
- **Schicht**: CORE · CORE_Option · CORE_gratis (im Kaffee) · OPTIONAL_Layer (Longevity-Premium) · PreWorkout_SKU · Evening_SKU · Sweetener/Emulgator/Creamer/Hilfsstoff · V1.5/V2 · separates_Produkt · Kandidat · "-" (verworfen)
- **Wirkung_spuerbar**: ja_stark/ja_mittel/ja_schwach/nein/indirekt — Schlüsselkriterium Performance-First
- **Evidenz**: hoch/mittel/niedrig/vorlaeufig
- **Form_empfohlen**: konkrete Stoffform/Salz/Standardisierung
- **EU_Status**: zugelassen / NF-pruefen / NF-Grauzone / illegal / Patent-blockiert / intrinsisch
- **Hitzestabil_90C** + **Wasserloeslich**: Format-Eignung Instant bei 90°C. `[A]` = vom Labor zu verifizieren
- **Geschmack_Geruch**: sensorisches Risiko (Flavorist-Input)
- **Keep_Cut**: KEEP · KEEP_Option · OPTIONAL · PRUEFEN · PREWORKOUT · EVENING · V1.5 · CUT_MVP · CUT
- **Begruendung**: warum die Einstufung

## Wichtige Hinweise
- **Longlist-/Screening-Werkzeug, kein Rezept.** Enthält bewusst auch CUT-Einträge (dokumentiert, dass sie geprüft wurden).
- **EU_Status ist Best-Knowledge, nicht rechtsverbindlich.** Verbindliche Klärung durch Reg.-Affairs-Berater (Roadmap Phase 1).
- **Stabilität/Löslichkeit sind Startpunkte** — echte Frage beantwortet nur das Labor (Phase 2).

## Workflow Phase 0 (Shortlist)
1. Filter `Schicht` = CORE → Performance-Kern-Kandidaten
2. Filter `Wirkung_spuerbar` = ja* → spürbarer Erstkauf-Nutzen
3. Eine-aus-Entscheidungen: Alpha-GPC vs. Citicoline; KSM-66 vs. Sensoril; L-Tyrosin vs. NALT
4. `OPTIONAL_Layer` separat → Longevity-Premium-Tier
5. `Sweetener`/`Creamer`/`Emulgator` (Kat J) → Formulierungsbausteine
6. Ergebnis: 8-10 Core-Stoffe + Dosen = Input für Reg.-Berater + Lebensmitteltechniker

## Erweitern
Neue Stoffe in `build_ingredient_db.py` → Liste ROWS ergänzen (20 Felder) → `python3 models/build_ingredient_db.py`.
