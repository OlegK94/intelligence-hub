---
status: fertig
priority: hoch
date: 2026-06-14
modul: 1
---

# Modul 1 — Ingredienzen-Datenbank

Strukturierte Daten in `models/ingredient_db.csv`. Hier: Bewertung, Stack-Logik, Preise ([A] = Annahme/Schätzung).

---

## Master Stack Empfehlung — MVP (regulatorik-konform, heute legal)

| # | Stoff | Dosis | Funktion | EU-Status | Kosten/Dosis [A] |
|---|---|---|---|---|---|
| Basis | Robusta Light 60-70% / Arabica Light 30-40% | 3-4g | Trigonellin + CGA + Koffein | natürlich | 0,08-0,12€ |
| 1 | L-Theanin | 200mg | Koffein-Synergie, Fokus | NF 2021 zugelassen | 0,02-0,04€ |
| 2 | Lion's Mane Dual Extract 8:1 | 500mg | NGF/BDNF, Neuroplastizität | zugelassen | 0,15-0,25€ |
| 3 | Cordyceps Militaris (Fruchtkörper) | 500mg | ATP, VO2max, Mitochondrien | zugelassen | 0,12-0,20€ |
| 4 | Ashwagandha KSM-66 | 300mg | Cortisol, HPA-Achse | zugelassen | 0,08-0,15€ |
| 5 | NAC | 600mg | Glutathion, Seneszenz | zugelassen (NEM) | 0,03-0,06€ |
| 6 | Spermidine (Weizenkeimextrakt) | 6mg | Autophagie | NF EU 2020/443 | 0,10-0,20€ |
| 7 | Taurin | 1000mg | Mitochondrien, Longevity | zugelassen | 0,02-0,04€ |
| 8 | Astaxanthin | 4mg | Antioxidans, Mitochondrien | zugelassen | 0,05-0,10€ |

**Rohstoffe gesamt: 0,65–1,16€/Portion** [A]

---

## Begründete Streichungen

- **NMN**: EU-illegal bis ~Q1 2027. → V2-Upgrade.
- **Urolithin A**: Amazentis-Patent (>100) + Nestlé-Lizenz. → gestrichen.
- **NR**: IP-Kurzcheck empfohlen. Machbar als NMN-Brücke in V1.5.
- **CoQ10 Ubiquinol**: Hydrophob, Emulgierung ungenöst. → RTD Phase 2.
- **Kreatin**: Hitzestabilität fraglich, Blueprint verkauft separat.
- **Fisetin/Quercetin**: EU-Status Grauzone. Niedrigdosiert tolerierbar, regulatorisch absichern.

---

## 3 SKU-Varianten

### SKU 1 — Morning Performance (Lead)
Vollständiger Stack. Light Roast, volles Koffein (~150-200mg). Positionierung: Deep Work, Energie ohne Crash.

### SKU 2 — Pre-Workout
Stack + L-Tyrosin 500mg + Koffein 200mg + Cordyceps 1000mg. Ohne Ashwagandha (Cortisol-Dämpfung kontraproduktiv). Positionierung: Hyrox/CrossFit, VO2max.

### SKU 3 — Evening Recovery
Decaf + L-Theanin 400mg + Mg-Glycinat 200mg + Spermidine 6mg + Glycin. Adressiert Bryan Johnsons Schlaf-Einwand.

---

## Vollständiges Stoff-Screening

### Kategorie A — Stimulantien
| Stoff | Urteil | Begründung |
|---|---|---|
| Koffein Anhydrous | ✅ | Hauptwirkstoff, EFSA-Claim |
| Guarana | ❌ | Redundant zu Koffein |
| Teacrine | ⚠️→❌ MVP | EU-Novel-Food-Grauzone, nicht autorisiert |
| Dynamine | ⚠️→❌ MVP | EU-Novel-Food-Status ungeklärt |
| Theobromin | 🔵 | Optional Evening-SKU, niedrige Priorität |

### Kategorie B — Nootropika
| Stoff | Urteil | Begründung |
|---|---|---|
| L-Theanin | ✅ | Kern. 1:2-Ratio mit Koffein, NF 2021 zugelassen |
| Alpha-GPC | 🔵 | Kandidat Pre-Workout-SKU |
| Citicoline | 🔵 | Alternative zu Alpha-GPC |
| Lion's Mane | ✅ | Dual Extract 8:1 zwingend |
| Phosphatidylserin | 🔵 | Eher Evening/Recovery |
| Bacopa Monnieri | ❌ MVP | Wirkt kumulativ, bitter, magenreizend |

### Kategorie C — Adaptogene
| Stoff | Urteil | Begründung |
|---|---|---|
| Ashwagandha KSM-66 | ✅ | MVP-Wahl. Sensoril nur für Evening-SKU |
| Rhodiola Rosea | 🔵 | Anti-Fatigue, Kandidat Pre-Workout |
| Panax Ginseng | 🔵 | Niedrige Priorität |
| Eleuthero | ❌ MVP | Schwächere Evidenz |
| Schisandra | ❌ MVP | Nische, Geschmack komplex |

### Kategorie D — Funktionspilze
| Stoff | Urteil | Begründung |
|---|---|---|
| Lion's Mane | ✅ | NGF/BDNF |
| Cordyceps Militaris | ✅ | ATP/VO2max, Fruchtkörper > Myzel |
| Reishi | 🔵 | Sedierend, Evening-SKU |
| Chaga | 🔵 | Antioxidans, Schwermetall-QC beachten |
| Turkey Tail | ❌ MVP | Immun/Darm, passt nicht zum Stack |

### Kategorie E — Aminosäuren
| Stoff | Urteil | Begründung |
|---|---|---|
| L-Tyrosin | 🔵 | Kandidat Pre-Workout |
| Taurin | ✅ | Longevity-Daten 2023 (Science), hitzestabil |
| L-Citrullin | 🔵 | Volumenproblem (3-6g) für Sachet |
| Beta-Alanin | ❌ MVP | Parästhesie, Dosis zu hoch für Sachet |
| Kreatin | ❌ MVP | Hitzestabilität fraglich, eigenes Produkt |
| Kollagen | ❌ | Nicht prioritär im Stack-Kontext |

### Kategorie F — Longevity Core
| Stoff | Urteil | Begründung |
|---|---|---|
| NAC | ✅ | Glutathion, Seneszenz. Schwefelgeruch = Flavorist |
| Curcumin | 🔵 | Hydrophob, mizellar für Instant. V1.5 |
| Quercetin | ⚠️ | EU-Status dosisabhängig. Reg.-Sign-off |
| Fisetin | ⚠️ | EU-Novel-Food-Grauzone. Niedrigdosiert |
| Urolithin A | ❌ | Amazentis-Patent + Nestlé-Lizenz |
| Spermidine | ✅ | Autophagie. Nur Weizenkeimextrakt (Reg. EU 2020/443), max 6mg |
| NMN | ❌ MVP → V2 | EU-illegal bis ~Q1 2027 |
| NR | ⚠️🔵 | IP-Check ChromaDex. NMN-Brücke möglich |
| Resveratrol | ❌ | Blueprint abgesetzt: schlechte Bioverfügbarkeit, pro-oxidativ |
| Astaxanthin | ✅ | Stärkstes Carotinoid-Antioxidans, opakes Sachet |
| CoQ10 Ubiquinol | ❌ MVP | Hydrophob, für Heißwasser ungeeignet |
| Trigonellin | ✅ (natürlich) | Im Kaffee enthalten (Nature Metab. 2024). Light Roast maximiert. Strategischer Joker |

### Kategorie G — Vitamine & Mineralien
| Stoff | Urteil | Begründung |
|---|---|---|
| B-Komplex | 🔵 | Energiemetabolismus, EFSA-Claims |
| Magnesium (Glycinat/L-Threonat) | 🔵 | Glycinat: Evening. L-Threonat: Kognition/teurer |
| Vitamin D3+K2 | 🔵 | Fettlöslich, Emulgierung prüfen |
| Omega-3 | ❌ MVP | Fischgeruch, oxidationsanfällig in Instant |
| Zink+Selen | 🔵 | Immun/antioxidativ, Synergie mit NAC |

### Synthese
**MVP-Stack (✅): 8 Stoffe** — Koffein, L-Theanin, Lion's Mane, Cordyceps, Ashwagandha, NAC, Spermidine, Taurin, Astaxanthin.
**SKU-Differenzierung (🔵):** Pre-Workout = +L-Tyrosin, Alpha-GPC, Rhodiola, mehr Cordyceps. Evening = +Reishi, Mg-Glycinat, kein Koffein.
**V1.5/V2 (🔵):** NR (Brücke), dann NMN (nach Zulassung), Curcumin (mizellar).
**Grauzone klären (⚠️):** Teacrine, Dynamine, Quercetin, Fisetin.
