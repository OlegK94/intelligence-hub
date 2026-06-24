---
status: fertig
priority: referenz
date: 2026-06-14
typ: master-prompt
---

# Master Research Prompt — Performance Café

Vollständiger Forschungsauftrag. Module einzeln oder gesamt ausführen.
Claude Code: `"Arbeite [Modul X] aus und schreibe Ergebnis nach [Datei]"`

---

## ROLLE

Du bist ein interdisziplinäres Research-Team:

- **[LON]** Longevity-Wissenschaftler — Aging-Biologie, Autophagie, Mitochondrien, Biomarker
- **[ING]** Lebensmittelwissenschaftler — Inhaltsstoffe, Wirkung, Dosen, Stabilität
- **[COF]** Kaffeespezialist / Q-Grader — Bohnen, Röstung, Extraktion, Synergien
- **[MKT]** Market Analyst — Marktgröße, Wettbewerb, Gaps, Positioning
- **[PRO]** Prototyp-Stratege — CMOs, Labore, Partner, Zeitplan
- **[REG]** Regulatory Affairs — EU Novel Food, EFSA, BfR, Health Claims

Antworten auf Deutsch. Direkt, konkret, Quellenangaben.

---

## MODUL 0 — Longevity-Wissenschaft → `research/01_longevity_science.md`

**A) 12 Hallmarks of Aging (Lopez-Otin 2023)**
Welche Hallmarks sind durch Inhaltsstoffe in einem Getränk adressierbar?
Fokus: Mitochondriale Dysfunktion, Inflammaging, Deregulierte Nährstoffsensorik (AMPK/mTOR/Sirtuine), Zelluläre Seneszenz, Proteostaseverlust.

**B) Kaffee als Longevity-Substanz**
- Chlorogensäure: AMPK-Aktivierung, Insulinsensitivität
- Trigonellin: NMN-Vorstufe (NAD+-Booster) — aktuelle Forschung 2024
- Cafestol/Kahweol: LDL-Effekte vs. Leberschutz
- Epidemiologische Daten: Kaffeekonsum vs. Mortalität (J-Kurve)

**C) Biomarker-Profil**
Welche Biomarker bewegt unser Stack? hs-CRP, HbA1c, ApoB, NAD+ Level, IGF-1.

---

## MODUL 1 — Ingredienzen Datenbank → `research/02_ingredienzen_db.md`

Für jeden Stoff: Wirkung | Mechanismus | Dosis | Longevity-Pathway | Risiken | EU-Status | EFSA Claim | Stabilität 90°C | Kosten/Dosis

### Kategorie A — Stimulantien
Koffein Anhydrous, Guarana, Teacrine, Dynamine, Theobromin

### Kategorie B — Nootropika
L-Theanin, Alpha-GPC, Citicoline, Lion's Mane, Phosphatidylserine, Bacopa

### Kategorie C — Adaptogene
Ashwagandha KSM-66 vs. Sensoril, Rhodiola Rosea, Panax Ginseng, Eleuthero, Schisandra

### Kategorie D — Funktionspilze
Lion's Mane, Cordyceps Militaris, Reishi, Chaga, Turkey Tail

### Kategorie E — Aminosäuren
L-Tyrosin, Taurin, L-Citrullin, Beta-Alanin, Kreatin, Kollagenpeptide

### Kategorie F — Longevity Core
NAC, Curcumin, Quercetin, Fisetin, Urolithin A, Spermidine, NMN, NR, Resveratrol, Astaxanthin, CoQ10, Trigonellin

### Kategorie G — Vitamine & Mineralien
B-Komplex, Magnesium, Vitamin D3+K2, Omega-3, Zink+Selen

**Output:** Master Stack Empfehlung + 3 SKU-Varianten

---

## MODUL 2 — Kaffee-Spezifikation → `research/03_kaffee_specs.md`

Robusta vs. Arabica, Vietnam-Spezialanalyse, Mischverhältnisse, Röstgrad (Longevity-optimiert), Extraktion (Freeze-Dried vs. Spray-Dried).

---

## MODUL 3 — Marktanalyse → `research/04_marktanalyse.md`

Blueprint-Analyse, Direktwettbewerb, Positioning Matrix, Marktgröße, Pricing-Benchmarks.

---

## MODUL 4 — Prototyp-Partner → `research/05_prototyp_partner.md`

Experten-Profile, CMOs DACH+EU, Technische Herausforderungen, Analyse-Labore, Entwicklungs-Zeitplan.

---

## MODUL 5 — Regulatorik + IP → `research/06_regulatorik.md`

EU Novel Food Status je Longevity-Stoff, Patent-Landschaft, Zertifizierungs-Roadmap, Health Claims, Lebensmittel vs. NEM.

---

## MODUL 6 — Business Case → `research/07_business_case.md`

Unit Economics, Investoren & Funding, Demand Validation, GTM-Sequenz, Blueprint Protocol Marketplace.

---

## MODUL 7 — Brand & Naming → `brand/naming_brief.md`

Produktname, Positioning Statement: "Perform now. Live longer."

---

## MODUL 8 — IP & Legal Entity → `legal/ip_landscape.md`

Patent-Recherche Amazentis/Chromadex, Gesellschaftsstruktur, EUIPO Markenanmeldung.

---

## MODUL 9 — Unit Economics Modell → `models/unit_economics.py`

Python-Modell für COGS-Kalkulation. Input: Rohstoffpreise. Output: Marge, Break-Even, Preisszenarien.
