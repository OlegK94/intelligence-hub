---
title: Performance Cafe Master Brief Quellendetail
type: source
tags: [performance-cafe, research, master-brief, longevity, functional-coffee, modul, strategy, regulatory, business-case, brand, IP, CMO, unit-economics]
sources: ["raw/Business/PerformanceCafe/research/00_master_brief.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Master-Forschungsprompt für Performance Coffee Brand — 9 Forschungsmodule (Modul 0–8) plus Python-Unit-Economics-Modell; definiert interdisziplinäre Teamrollen (LON/ING/COF/MKT/PRO/REG); ordnet jedem Modul eine Ausgabedatei zu; Stand 2026-06-14
---

# Performance Café — Master Research Brief (Quellendetail)

## Überblick

Dieses Quelldokument (`raw/Business/PerformanceCafe/research/00_master_brief.md`, Status: fertig, Priorität: Referenz, Datum: 2026-06-14, Typ: master-prompt) ist der **umfassende Forschungsrahmen** für [[Performance Coffee Brand]]. Es definiert den gesamten Arbeitsumfang über 9 Forschungsmodule plus ein Python-Modell, weist interdisziplinäre Teamrollen zu und ordnet jedem Modul seine Ausgabedatei zu.

> Zur Projektentitätsseite siehe [[Performance Coffee Brand]].
> Für die Naming-Ausgabe dieser Recherche siehe [[Performance Coffee Brand Naming]] und [[Aevum Brand]].
> Für die operative CMO-Ausgabe siehe [[CMO Sourcing Performance Coffee]].

---

## Teamrollen (ROLLE)

Das Dokument definiert ein **6-rollen-interdisziplinäres Forschungsteam** — jede Rolle mit einem Tag, der durchgängig in der Recherche verwendet wird:

| Tag | Rolle | Fachgebiet |
|---|---|---|
| **[LON]** | Longevity-Wissenschaftler | Aging-Biologie, Autophagie, Mitochondrien, Biomarker |
| **[ING]** | Lebensmittelwissenschaftler | Inhaltsstoffe, Wirkung, Dosen, Stabilität |
| **[COF]** | Kaffeespezialist / Q-Grader | Bohnen, Röstung, Extraktion, Synergien |
| **[MKT]** | Marktanalyst | Marktgröße, Wettbewerb, Lücken, Positionierung |
| **[PRO]** | Prototyp-Stratege | CMOs, Labore, Partner, Zeitplan |
| **[REG]** | Regulatory Affairs | EU Novel Food, EFSA, BfR, Health Claims |

Alle Antworten sollen auf **Deutsch** verfasst sein, direkt und konkret mit Quellenangaben.

---

## Modulstruktur

Der Brief ist in **9 Forschungsmodule** plus ein **Python-Modell** gegliedert:

| Modul   | Titel                  | Ausgabedatei                       |
| ------- | ---------------------- | ---------------------------------- |
| Modul 0 | Longevity-Wissenschaft | `research/01_longevity_science.md` |
| Modul 1 | Ingredienzen Datenbank | `research/02_ingredienzen_db.md`   |
| Modul 2 | Kaffee-Spezifikation   | `research/03_kaffee_specs.md`      |
| Modul 3 | Marktanalyse           | `research/04_marktanalyse.md`      |
| Modul 4 | Prototyp-Partner       | `research/05_prototyp_partner.md`  |
| Modul 5 | Regulatorik + IP       | `research/06_regulatorik.md`       |
| Modul 6 | Business Case          | `research/07_business_case.md`     |
| Modul 7 | Brand & Naming         | `brand/naming_brief.md`            |
| Modul 8 | IP & Legal Entity      | `legal/ip_landscape.md`            |
| —       | Unit Economics Modell  | `models/unit_economics.py`         |

---

## Modul 0 — Longevity-Wissenschaft

**Ausgabe:** `research/01_longevity_science.md`

### A) 12 Hallmarks of Aging (Lopez-Otin 2023)
Fokus auf Hallmarks, die durch Getränkeinhaltsstoffe adressierbar sind:
- Mitochondriale Dysfunktion
- Inflammaging
- Deregulierte Nährstoffsensorik (AMPK/mTOR/Sirtuine)
- Zelluläre Seneszenz
- Proteostaseverlust

### B) Kaffee als Longevity-Substanz
Wichtige Forschungsbereiche:
- **Chlorogensäure:** AMPK-Aktivierung, Insulinsensitivität
- **Trigonellin:** NMN-Vorstufe (NAD+-Booster) — aktuelle Forschung 2024
- **Cafestol/Kahweol:** LDL-Effekte vs. Leberschutz
- **Epidemiologie:** Kaffeekonsum vs. Mortalität (J-Kurve, optimale Tagesmenge)

### C) Biomarker-Profil
Vom Stack adressierte Marker: hs-CRP, HbA1c, ApoB, NAD+-Spiegel, IGF-1
DTC-Testverfügbarkeit, Kosten, Relevanz für Community-Strategie

---

## Modul 1 — Ingredienzen Datenbank

**Ausgabe:** `research/02_ingredienzen_db.md`

Format je Inhaltsstoff: Wirkung | Mechanismus | Dosis | Longevity-Pathway | Risiken | Kontraindikationen | EU-Status | EFSA Claim | Stabilität in Kaffee (90°C) | Blueprint-Status | Kosten/Dosis

### Kategorien

**Kategorie A — Stimulantien**
Koffein Anhydrous, Guarana-Extrakt, Teacrine (Theacrine), Dynamine (Methylliberine), Theobromin

**Kategorie B — Nootropika**
L-Theanin (Verhältnis zu Koffein), Alpha-GPC (50% vs. 99%), Citicoline, Lion's Mane (Doppelextrakt 8:1), Phosphatidylserine, Bacopa Monnieri

**Kategorie C — Adaptogene**
Ashwagandha KSM-66 vs. Sensoril, Rhodiola Rosea (3% Rosavine/1% Salidroside), Panax Ginseng, Eleuthero, Schisandra

**Kategorie D — Funktionspilze**
Lion's Mane, Cordyceps Militaris (VO2max), Reishi (Autophagie), Chaga (Antioxidantien), Turkey Tail

**Kategorie E — Aminosäuren**
L-Tyrosin vs. NALT, Taurin (Longevity-Daten 2023!), L-Citrullin, Beta-Alanin, Kreatin Monohydrat, Kollagenpeptide

**Kategorie F — Longevity Core ⚠️ KRITISCH**
> EU Novel Food Status 2025/2026 explizit angeben für jeden:
- NAC (Glutathion-Vorstufe)
- Curcumin (liposomal/mizellar)
- Quercetin (Senolytikum)
- [[Fisetin]] (potentestes natürliches Senolytikum)
- [[Urolithin A]] (Mitophagie ↑ — ⚠️ [[Amazentis]] Patent prüfen!)
- [[Spermidine]] (Autophagie-Induktion — ⚠️ EU Novel Food?)
- [[NMN]] (NAD+-Booster — ⚠️ EU-Zulassung 2025 Status!)
- NR / Nicotinamid Ribosid (NMN-Alternative — ⚠️ Chromadex Patent!)
- Resveratrol (Warum hat Blueprint es abgesetzt?)
- Astaxanthin (stärkstes Carotinoid-Antioxidans)
- CoQ10 Ubiquinol (Atmungskette)
- Trigonellin (im Kaffee enthalten → NMN-Vorstufe)

**Kategorie G — Vitamine & Mineralien**
B-Komplex, Magnesium (Glycinat vs. L-Threonat), Vitamin D3+K2, Omega-3, Zink+Selen

### Modul 1 Ausgaben
1. Master Stack Empfehlung (8–10 Stoffe, Performance + Longevity)
2. 3 SKU-Varianten: Morning Performance / Pre-Workout / Evening Recovery
3. „What would Blueprint do?" — Bryan Johnsons hypothetischer Longevity-Kaffee-Stack

---

## Modul 2 — Kaffee-Spezifikation

**Ausgabe:** `research/03_kaffee_specs.md`

### A) Robusta vs. Arabica
Koffein, Chlorogensäure, Trigonellin, Theobromin — je Sorte. Longevity-Relevanz.

### B) Vietnamesischer Robusta — Spezialanalyse
- Anbaugebiet: Buôn Ma Thuột (Dak Lak)
- Produzenten: Trung Nguyen, K'Ho Coffee
- Sourcing Europa (Importeure, MOQs, Preise)
- Koffeingehalt bis 2,7%

### C) Mischverhältnisse
5 Verhältnisse: 100/0, 80/20, 60/40, 40/60, 20/80 (Robusta/Arabica)
Je Verhältnis: Koffein gesamt, Chlorogensäure, Trigonellin, Geschmack, Stack-Kompatibilität

### D) Röstgrad (Longevity-optimiert)
Hell vs. Medium vs. Dunkel: Chlorogensäure- und Trigonellin-Erhalt
Welcher Röstgrad maximiert Longevity-Bioaktivität + Verbraucherakzeptanz?

### E) Extraktion
Cold Brew vs. Espresso vs. Instant (Freeze-Dried vs. Spray-Dried): Wirkstofferhalt
Optimale Kaffeebasis für das Instant-Sachet-Format

---

## Modul 3 — Marktanalyse

**Ausgabe:** `research/04_marktanalyse.md`

### A) Blueprint-Analyse als Referenz
- Stack, Preise ($39–49/Produkt)
- Transparenz-Strategie (COAs, Don't Die App)
- Community-Flywheel
- Protocol Marketplace Listungsmöglichkeit
- [[Bryan Johnson]] kein Kaffee → Chance oder Risiko?

### B) Direktwettbewerb
Four Sigmatic, RYZE, MUD\WTR, Clevr Blends, Kitu Super Coffee, Stanz Coffee (DE), Bulletproof
Je Wettbewerber: Stack-Tiefe, Longevity-Aspekt, Preisgestaltung, Schwächen

### C) Longevity-Supplement-Wettbewerb
Tru Niagen (NR), Timeline Mitopure ([[Urolithin A]]), Purovitalis (NMN/EU), DoNotAge (UK), Qualia Senolytic
**Kerninsight: Niemand hat Kaffee → das ist der White Space**

### D) Positionierungsmatrix
X-Achse: Performance-Intensität | Y-Achse: Longevity-Tiefe
Ziel: oben rechts, unbesetzt

### E) Marktgröße
Functional Beverage Market (global + DACH), Longevity Supplement Market, CAGR bis 2030

### F) Pricing-Benchmarks
- Blueprint Longevity Mix: ~1,63€/Portion
- Timeline Mitopure: ~3,30€/Portion
- Zielpreis Performance Café: noch festzulegen

---

## Modul 4 — Prototyp-Partner

**Ausgabe:** `research/05_prototyp_partner.md`

### A) Experten-Profile
Benötigte Rollen (wann, wo zu finden, Kosten):
- Lebensmitteltechnologe
- Flavorist (NAC-Maskierung)
- Longevity-Arzt
- Toxikologe
- Regulatory Affairs EU Novel Food
- Q-Grader
- Biomarker-Experte

### B) Contract Manufacturers DACH + EU
Erforderliche Spezialisierungen:
- Instant-Kaffeemischungen mit funktionellen Inhaltsstoffen
- Stick-Pack/Sachet-Fertigung
- Freeze-Drying Specialty Coffee
- Functional RTD

→ Aktuelle CMO-Kandidaten siehe [[CMO Sourcing Performance Coffee]].

### C) Technische Herausforderungen je Stoff

| Inhaltsstoff | Herausforderung | Lösungsansatz |
|---|---|---|
| NAC | Geruchs-/Geschmacksmaskierung (Schwefelgeruch) | Flavorist, Encapsulation |
| Curcumin | Löslichkeit in heißem Wasser | Liposomale/mizellare Formen |
| NMN/NR | Oxidationsschutz | Schutzgas-Verpackung |
| Spermidine | Hitzestabilität bei 90°C | Noch zu klären |
| CoQ10 | Emulgierung in Wasser | Noch zu klären |
| Pilzextrakte | Qualitätskontrolle (Heißwasser- vs. ethanolischer Extrakt) | Dual-Extrakt-Spezifikation |

### D) Analyse-Labore
Akkreditierte DACH-Labore für: Mikrobiologie, Schwermetalle, Inhaltsstoffgehalt, Haltbarkeit

### E) Entwicklungs-Zeitplan
Schritte 1–7 von Briefing bis Pilot-Batch — realistische Zeitfenster

---

## Modul 5 — Regulatorik + IP

**Ausgabe:** `research/06_regulatorik.md`

### A) EU Novel Food Status — Longevity-Stoffe ⚠️ KRITISCH
Expliziter Status 2025/2026 erforderlich für:
- [[NMN]] — EU-Zulassungsstatus 2025?
- [[Urolithin A]] — proprietäre Zulassung durch [[Amazentis]]
- [[Spermidine]] — EU Novel Food?
- [[Fisetin]] — Status?
- NR (Nicotinamid Ribosid) — [[Chromadex / Niagen Bioscience]] Patent

### B) IP & Patent-Landschaft
- **[[Amazentis]]/Timeline:** Urolithin-A-Patente — Umfang, Laufzeit (~2034–2036), Lizenzoptionen
- **[[Chromadex / Niagen Bioscience]]:** NIAGEN Patent (NR) — EU-Status?
- NMN-Patente: Wer hält was?
- Eigener IP-Schutz: Kombination patentierbar? Verfahren patentierbar?
- Trade Secret vs. Patent — Empfehlung

### C) Zertifizierungs-Roadmap
1. [[Kölner Liste]] — DACH, MVP
2. Informed Sport — EU-Skalierung
3. NSF Certified for Sport — US-Expansion
Je Zertifizierung: Prozess, Kosten, Timeline, CMO-Anforderungen

Bestehende Analyse siehe [[Certification Roadmap Performance Coffee Brand]].

### D) Health Claims Strategie
- Zugelassene EFSA-Claims (genaue Formulierung erforderlich)
- Anti-Aging Claims sind verboten
- Blueprint-Ansatz: Transparenz + Biomarker statt Claims

### E) Lebensmittel vs. NEM
Vor- und Nachteile, Empfehlung, kritischer Pfad

---

## Modul 6 — Business Case

**Ausgabe:** `research/07_business_case.md`

### A) Unit Economics
COGS je Portion: Rohstoffe + CMO-Marge + Verpackung + Fulfillment + Plattform
Deckungsbeitrag, Break-Even-Stückzahl, LTV:CAC-Zielkorridor

### B) Investoren & Finanzierung
Europäische Functional Food / Longevity Investoren:
- Angel-Netzwerke, Family Offices, Functional Food VCs
- Pre-Seed Ticket-Größen, KPIs, Bewertungsmaßstäbe

### C) Nachfragevalidierung
Landing Page + Warteliste + Hyrox-Popup als Validierungsplan
Budget, Timeline, Erfolgskriterien

### D) Go-to-Market Sequenz

| Phase | Kanal |
|---|---|
| Phase 1 (MVP) | DTC Online + Hyrox Events + CrossFit Boxes |
| Phase 2 | Amazon DE + B2B (Fitnessstudios, Coworking) |
| Phase 3 | Einzelhandel (dm, Rossmann, Metro) + EU-Expansion |
| Phase 4 | USA (NSF-Zertifizierung, Amazon US) |

### E) Blueprint Protocol Marketplace
Listungsbedingungen, Chancenbewertung — strategischer Partner oder Wettbewerber?

---

## Modul 7 — Brand & Naming

**Ausgabe:** `brand/naming_brief.md`

Naming-Kriterien: kurz, international, nicht generisch, .com verfügbar, EUIPO eintragbar
Positionierungsstatement: **„Perform now. Live longer."**

→ Abgeschlossene Ausgabe siehe [[Performance Coffee Brand Naming]] und [[Aevum Brand]].

---

## Modul 8 — IP & Legal Entity

**Ausgabe:** `legal/ip_landscape.md`

- [[Amazentis]] Urolithin-A-Patentrecherche
- [[Chromadex / Niagen Bioscience]] NR/NIAGEN Patent EU-Status
- NMN-Patentlandschaft
- Rechtsform: wann GmbH, IP-Eigentumsstruktur, EUIPO-Marke

→ Abgeschlossene Ausgabe (sofern eingelesen) siehe [[Performance Café IP Landscape Modul 8]].

---

## Unit Economics Modell

**Ausgabe:** `models/unit_economics.py`

Python-Modell zur COGS-Berechnung:
- Eingabe: Rohstoffpreise aus `research/02_ingredienzen_db.md`
- Ausgabe: Marge je Portion, Break-Even-Volumen, Preisszenarien

---

## Modulübergreifende Abhängigkeiten

```
Modul 0 (Wissenschaft) → Modul 1 (Inhaltsstoffe) → Modul 5 (Regulatorik)
                                                   → Modul 6 (Business Case)
                                                   → Unit Economics Modell
Modul 1 (Inhaltsstoffe) → Modul 2 (Kaffeespezifikationen) → Modul 4 (Prototyp)
Modul 3 (Markt) → Modul 6 (Business Case) → Modul 7 (Brand)
Modul 5 (Regulatorik/IP) → Modul 1 (Inhaltsstoff go/no-go)
                         → Modul 4 (CMO-Anforderungen)
                         → Modul 6 (Business Case Risiken)
```

---

## Wichtige Forschungshinweise (⚠️ Kritische Punkte)

| Punkt | Hinweis | Modul |
|---|---|---|
| [[NMN]] EU-Zulassung 2025 | Status explizit erforderlich | 5A |
| [[Urolithin A]] / [[Amazentis]] | Patentumfang + Lizenzkosten | 5B, 8 |
| [[Spermidine]] EU Novel Food | Expliziter Status erforderlich | 5A |
| [[Fisetin]] EU Novel Food | Expliziter Status erforderlich | 5A |
| NR / Chromadex Patent | EU-Geltungsbereich | 5B, 8 |
| NAC Geruchsmaskierung | Formulierungsblockade | 4C |
| Trigonellin als NMN-Vorstufe | Bereits im Kaffee → separate Dosierung? | 0B, 1F |
| Resveratrol Blueprint-Ausstieg | Warum entfernt? | 1F |
| CoQ10 Wasseremulgierung | Technische Herausforderung | 4C |
| Vietnam Robusta Sourcing | EU-Importeure, MOQs | 2B |

---

## Verwandte Seiten

- [[Performance Coffee Brand]] — Projektentität
- [[Performance Coffee Brand Naming]] — Modul-7-Ausgabe
- [[Aevum Brand]] — Top-Namenskandidat
- [[CMO Sourcing Performance Coffee]] — operative Modul-4-Ausgabe
- [[CMO Erstkontakt Email Template]] — CMO-Outreach-Quelle
- [[Amazentis]] — IP-Blocker (Urolithin A)
- [[Chromadex / Niagen Bioscience]] — IP-Blocker (NR/NIAGEN)
- [[NMN]] — kritischer Regulierungspunkt
- [[Urolithin A]] — kritischer IP-Punkt
- [[Spermidine]] — kritischer Regulierungspunkt
- [[Fisetin]] — Longevity Senolytikum
- [[Bryan Johnson]] — Marktreferenz und White-Space-Erzeuger
- [[EU Novel Food Regulation]] — regulatorischer Rahmen
- [[Longevity Stack Ingredients]] — Inhaltsstoff-Framework
- [[Certification Roadmap Performance Coffee Brand]] — Zertifizierungs-Roadmap
- [[Performance Café IP Landscape Modul 8]] — IP-Analyse-Ausgabe
- [[Kölner Liste]] — Phase-1-Zertifizierung
- [[Oleg Personal Context]] — Projektverantwortlicher