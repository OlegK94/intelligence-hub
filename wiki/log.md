# Wiki Log

Append-only timeline of ingests, queries, and lint passes.

## [2026-06-25 12:00] ingest | Bulk Raw Files — Café Berlin, OK Capital, Privat, Clippings, Wagglz Design

### Quellen geprüft (alle Batches)

**BATCH 1 — Café Berlin:**
- `raw/Business/Cafe/Café Berlin — Partnership Hai.md` — bereits vollständig abgedeckt durch [[Café Berlin Partnership Hai]] entity + [[Café Berlin Partnership Hai Raw Source]] source
- `raw/Business/Cafe/cafe_masterplan_2026.md` — bereits vollständig abgedeckt durch [[GROVE Businessplan Source Detail]] und alle GROVE-Entity-Seiten
- `raw/raw/Business/Cafe/` — Duplikate von raw/Business/Cafe/, kein neuer Inhalt

**BATCH 2 — OK Capital:**
- `raw/Business/OK-Capital/OK Capital UG.md` — bereits abgedeckt durch [[OK Capital UG Source Detail]], [[OK Capital UG]], [[OK Capital Finom 2026]]
- `raw/Business/OK-Capital/OK Capital UG — Finance Vault.md` — bereits abgedeckt durch [[OK Capital UG Finance Vault Source Detail]]
- `raw/Business/OK-Capital/Finanzen/Konten/OK Capital Finom 2026.md` — bereits abgedeckt durch [[OK Capital Finom 2026]] (source)
- `raw/Business/OK-Capital/Rangrücktritt §15a InsO.md` — bereits abgedeckt durch [[Rangrücktritt §15a InsO Source Detail]]

**BATCH 3 — Wagglz Design:**
- `raw/raw/Business/Wagglz/Design/figma-index.md` — NEU → [[Wagglz Figma Design Index Source Detail]] erstellt
- `raw/raw/Business/Wagglz/Wagglz Wettbewerber.md` — bereits abgedeckt durch [[Wagglz Wettbewerber Source Detail]] (updated 2026-06-25)
- `raw/raw/Business/Wagglz/Performance Coffee Brand/00 — Projektübersicht.md` — NEU → [[Performance Coffee Brand Projektübersicht Source Detail]] erstellt

**BATCH 4 — Privat/Finanzen & Auswandern:**
- `raw/Privat/Finanzen/00 Finanz-Übersicht.md` — bereits abgedeckt durch [[Finanz-Übersicht Source Detail]], [[MOC Finanzen Source Detail]], [[Finanzübersicht 2026]]
- `raw/Privat/Finanzen/00 MOC Finanzen.md` — bereits abgedeckt durch [[MOC Finanzen Source Detail]]
- `raw/Privat/Auswandern/Cyprus Relocation.md` — bereits abgedeckt durch [[Cyprus Relocation Detail]], [[Cyprus Relocation Source Detail]]
- `raw/Privat/Auswandern/Cyprus Relocation Tracker.md` — bereits abgedeckt durch [[Cyprus Relocation Tracker Source Detail]], [[Cyprus Relocation Tracker Privat Source Detail]]

**BATCH 5 — Clippings:**
- Andrew Huberman, Rhonda Patrick, Jeff Cavaliere — bereits ingested (log 2026-06-13)
- 13 Claude Code Tutorial Clippings (DE/EN) — NEU → [[Claude Code Tutorials DE Clippings]] erstellt (konsolidierte Quellseite)

### Neu erstellt
- [[Wagglz Figma Design Index Source Detail]] — Master-Katalog aller 10 Figma-Dateien Wagglz/Wufflz
- [[Performance Coffee Brand Projektübersicht Source Detail]] — Pivot-Moment 14.06.2026, frühe Konzeptübersicht
- [[Claude Code Tutorials DE Clippings]] — 13 YouTube-Clippings Claude Code (DE/EN), konsolidiert

### index.md aktualisiert
- 3 neue Quelldokument-Einträge eingefügt (alphabetisch korrekt)
- updated: 2026-06-25

## [2026-06-21] query | Vetera + DACH Veterinär-Software-Markt

- Kernfakt: Vetera (1989, Eltville am Rhein) = DACH-Marktführer mit 18.000+ Nutzern
- Nordhealth kaufte Vetera Juni 2022 für €8,36M → gleicher Eigentümer wie Provet Cloud
- DACH-Rangfolge: Vetera ~55%, easyVET ~20%, IDEXX Animana ~12%, Provet ~8%
- Vetera-Stärken: GOT-Abrechnung nativ, alle Schnittstellen kostenlos, lebenslanger Support, Schulung vor Ort
- Vetera-Schwächen: kein Cloud-native (VeteraSky in Entwicklung), veraltete UX, kein Tierhalter-Portal
- Wagglz kritische Pflicht erkannt: Vetera-Datenmigration/-Import muss angeboten werden
- Go-To-Market-Empfehlung: Neugründungen + junge Tierärzte, dann Bestandsmigration
- Entität erstellt: [[Vetera]]
- Output: `outputs/notes/2026-06-21-vetera-dach-analysis.html`
- IMGs 3342-3344 = LinkedIn-Screenshots (nicht Provet-UI): #3342 = VetSoftwareHub Top-10 (Provet #1), #3343+3344 = Longevity-Peptide-Post

## [2026-06-21] query | Provet Cloud Deep Research

- Quellen: 5 Web-Suchen, provet.com (geblockt), Review-Aggregatoren, LinkedIn-Screenshot IMG_3342.PNG
- Kernfakten: #1 VetSoftwareHub, 3.000+ Kliniken, 45+ Länder, 55.000+ Vets, ~$60M Umsatz (Nordhealth)
- Gegründet: 2001 Nordhealth Helsinki; Provet erworben ~2005; 90% FI-Marktanteil 2014
- Preise: ab €25/User/Monat (Optimise/Elevate/Enterprise)
- AI Suite lanciert Aug 2025: AI Scribe + Patient History Summary + AI Discharge Instructions
- Stärken: GDPR-EU, Open REST API, 150+ Integrationen, Multi-Site
- Schwächen: UX (viele Klicks), Support-Backline, Datenmigration, kein GOT
- Wagglz-Chancen: GOT-Pflicht DE/AT (kein Konkurrent hat das), UX-Vorteil, Tierhalter-Portal, transparentes Pricing
- Entität erstellt: [[Provet-Cloud]]
- Output: `outputs/notes/2026-06-21-provet-cloud-analysis.html`

## [2026-06-21] ingest | Index + Log update — Provet-Cloud & Vetera entities

- Wiki-Index aktualisiert: [[Provet Cloud]], [[Vetera]], [[Nordhealth]] eingetragen (updated 2026-06-21)
- Supplement Stack raw/inbox Update 2026-06-20 bestätigt als bereits abgedeckt (wiki-Eintrag existiert, updated 2026-06-20)
- Alle raw/inbox-Dateien geprüft: keine neuen Duplikate; alle relevanten Inhalte bereits in wiki/ representiert
- Keine unverarbeiteten Dateien im raw/ gefunden (Archiv.zip noch nicht auf Server; Intelligence-Hub-Unterordner existiert nicht auf Server)

## [2026-06-21] query | Wagglz Asset- & Wettbewerbs-Analyse

- Analysiert: 19 Screenshots aus `raw/assets/wagglz-tier/7RI3XqEc3RR6znirkakZcm/`, 6 WhatsApp App-Fotos (ZIP), SVG-Logomark
- Brand-Erkenntnisse: Farben #2E54CB (Blue), #CCFFB0 (Lime), #A6A6FF (Lavender); Font Poppins; alter Produktname war "Wufflz"
- Onboarding-Wireframes: 6-Schritt-Wizard vollständig analysiert (Business Info → Kontakt → Veterinär → Betrieb → Technik → Mitarbeiter)
- 14 Fachbereiche für Department-Multiselect extrahiert (a4-1.png)
- Wettbewerber identifiziert: Rex (Direktkonkurrenz), Doctolib (Referenz), Rover, PetLEO, Hundeo, Dogorama, Tractive GPS, PetBacker, Dog Walk, Walkies, Dog Assistant
- Design-Inspiration: Fantastical-App (Kalender), Defcon Systems (Wochenraster)
- ZIP-Inhalt: vollständiges Brand-Kit + Pitch Deck + Investoren-Präsentation + Design Concept PDF (6.3 MB, noch nicht gelesen)
- Output: `outputs/notes/2026-06-21-wagglz-competitive-analysis.html`
- TODO: Design_Concept.pdf analysieren · Investoren-Präsentation lesen · Poppins + Brand-Farben in App einbinden

## [2026-06-13] setup | LLM Wiki initialized

- Created Karpathy-style schema (CLAUDE.md), tools, and directory structure.
- Ready to ingest first source from `raw/inbox/` or any path under `raw/`.

## [2026-06-13 09:45 UTC] ingest | raw/Privat/Performance/Health Protocol — Master.md
- Pages: [[Health Protocol Master]], [[Andrew Huberman]], [[Rhonda Patrick]], [[Bryan Johnson]], [[Hiit Training]], [[Zone 2 Cardio]], [[Nsdr]], [[3d Body Scan]], [[Sauna]], [[Supplement Stack]], [[Alpha Gpc]], [[L Tyrosine]], [[index.md]]
- Ingested comprehensive health optimization protocol with baseline 3D body scan metrics, 6-day training split, nutrition plan, and daily structure. Created source page plus 10 entity/concept pages covering key experts (Huberman, Patrick, Johnson), training methods (HIIT, Zone 2), recovery protocols (NSDR, Sauna), supplements (Alpha-GPC, L-Tyrosine), and assessment methods (3D body scanning). All pages extensively cross-linked with Obsidian wikilinks.

## [2026-06-13 09:48 UTC] ingest | Clippings/Andrew Huberman.md
- Pages: [[Andrew Huberman]]
- Updated Andrew Huberman from entity to source page based on the clipping source. Enhanced with comprehensive information about his podcast, scientific approach, and integration with existing health protocols. Index updated to reflect the source classification.

## [2026-06-13 09:49 UTC] ingest | Clippings/The Best Vitality & Health Protocols  Dr. Rhonda Patrick.md
- Pages: [[The Best Vitality & Health Protocols Dr. Rhonda Patrick]]
- Ingested comprehensive 3-hour Huberman-Patrick discussion covering exercise protocols, nutrition strategies, supplementation, and health mechanisms. Added detailed coverage of metabolic flexibility, visceral fat risks, LPS-inflammation pathways, and evidence-based supplement protocols including creatine dosing for cognitive enhancement.

## [2026-06-13 09:52 UTC] ingest | Clippings/Build Muscle, Great Posture & Resilience to Injury  Jeff Cavaliere.md
- Pages: [[Build Muscle, Great Posture & Resilience to Injury Jeff Cavaliere]], [[Jeff Cavaliere]], [[Glute Medius]], [[Corrective Exercise]], [[Neck Training]]
- Added comprehensive content from Jeff Cavaliere/Huberman Lab discussion. Created 5 new articles covering training principles, injury prevention, corrective exercise protocols, and practical implementation strategies. Key additions: glute medius training for back pain, neck training protocols, grip corrections for elbow pain, and comprehensive approach to sustainable training for longevity.

## [2026-06-13 09:53 UTC] ingest | raw/Privat/Performance/Hyrox — 10-Week Training.md
- Pages: [[Hyrox 10-Week Training]], [[Hyrox Competition]], [[Brick Training]]
- Ingested Hyrox training protocol: Created 3 new pages covering the 10-week training plan, Hyrox competition format, and brick training methodology. Added to health/performance section of knowledge base with focus on hybrid fitness training and competition preparation.

## [2026-06-13 09:54 UTC] lint
- Found 1 orphan page (Dashboard), identified 6 missing supplement entities from Patrick content, and noted cross-reference opportunities between training methodologies

## [2026-06-13 10:03 UTC] ingest | raw/00-MOC/🏠 Home.md
- Pages: [[Oleg Home MOC]], [[Oleg Personal Context]], [[DoktorLib]], [[DoktorLib Automation Pipeline]], [[Café Berlin Partnership Hai]], [[Cyprus Relocation]], [[Password Manager Migration]], [[Allianz Insurance Consolidation]], [[Financial Independence]]
- Ingested raw/00-MOC/🏠 Home.md (Oleg's personal vault home page, dated 2026-06-13). Created 8 new pages: (1) Oleg Home MOC [source] — mirrors the home page structure with wikilinks; (2) Oleg Personal Context [entity] — consolidated identity/context profile; (3) DoktorLib [entity] — employer profile; (4) DoktorLib Automation Pipeline [entity] — Priority 2 work project; (5) Café Berlin Partnership Hai [entity] — Priority 1 business venture; (6) Cyprus Relocation [entity] — Priority 3 relocation goal (blocked); (7) Password Manager Migration [entity] — Priority 5 tech project; (8) Allianz Insurance Consolidation [entity] — Priority 6 finance project; (9) Financial Independence [concept] — core strategic life goal. Added strategic tension note in Cyprus Relocation: potential conflict between Berlin café venture (P1) and Cyprus move (P3). Updated index.md with new Entities (People, Companies & Projects), Concepts (Strategy & Life), and Sources (Personal Vault) sections, plus MOC stub section. No contradictions found with existing wiki content — this source introduces new personal/strategic context not previously covered.

## [2026-06-13 10:06 UTC] ingest | raw/00-MOC/MOC Performance & Leben.md
- Pages: [[MOC Performance and Leben]], [[3D Body Scan Scaneca Mai 2026]], [[Tagesstruktur and Schedule]], [[TEMPUR Matratzenkauf]]
- Ingested raw/00-MOC/MOC Performance & Leben.md. Created 4 new pages: (1) MOC Performance and Leben — source/navigation page mapping the domain MOC with all linked protocols, baseline, and research items; (2) 3D Body Scan Scaneca Mai 2026 — entity page for the specific May 2026 scan event (distinct from the existing general '3D Body Scan' concept page, which was preserved); (3) Tagesstruktur and Schedule — entity page for Oleg's active daily schedule protocol, consolidating data already in Health Protocol Master with dedicated navigation entry as warranted by MOC listing; (4) TEMPUR Matratzenkauf — stub entity page for mattress purchase research project with contextual links to sleep optimization. Updated index.md to include all four new pages in appropriate categories, plus reorganized the full index for completeness with all existing wiki pages. No contradictions found with existing wiki content — MOC data is consistent with Health Protocol Master and Oleg Home MOC entries already in wiki.

## [2026-06-13 10:07 UTC] ingest | raw/00-MOC/MOC Strategie & Business.md
- Pages: [[MOC Strategie und Business]], [[Allianz Insurance Consolidation]], [[Café Berlin Solo Analyse]], [[Hai]], [[Oleg Business Entity Structure]]
- Ingested raw/00-MOC/MOC Strategie & Business.md. Created 4 new articles: (1) MOC Strategie und Business — source summary page with active projects, archive, and entity context; (2) Café Berlin Solo Analyse — new entity for the rejected solo café analysis (first mention in vault); (3) Hai — new entity page for Oleg's café co-founder (extracted from existing references but lacked a dedicated page); (4) Oleg Business Entity Structure — synthesis page covering GmbH/UG/Fashion Brand structure and Cyprus relocation implications. Updated existing Allianz Insurance Consolidation entity to document a status contradiction: Home MOC lists it as open (Priority 6), but MOC Strategie & Business places it in the Abgeschlossen/Archiv section. New entity 'Fashion Brand (discontinued)' noted in synthesis — only mention in entire vault. Index updated with all new entries; Contradictions table added with C-001 for the Allianz status discrepancy.

## [2026-06-13 10:09 UTC] ingest | raw/00-MOC/MOC Tech & Setup.md
- Pages: [[MOC Tech und Setup]], [[Privacy and Tech Stack]], [[Claude Projects Setup]]
- Ingested raw/00-MOC/MOC Tech & Setup.md. Created 3 new pages: (1) MOC Tech und Setup — source page documenting Oleg's tech domain navigation hub, infrastructure stack (Proton Mail/VPN/Pass, Brave, Safari, iPhone/iPad Air 2025/Mac, ok-holding.com domain via GoDaddy DNS), and active projects; (2) Privacy and Tech Stack — entity page for Oleg's privacy-first tool philosophy and current stack details; (3) Claude Projects Setup — entity page for Oleg's use of Claude AI Projects feature. Updated index.md with all three new entries under appropriate categories. Added a new 'Known Contradictions' section to the index capturing the existing Allianz contradiction and a newly identified minor contradiction: the Home MOC lists Password Manager Migration without specifying the current tool, while the Tech MOC clarifies Proton Pass is current and Apple Passwords is the migration target. Wikilinks added throughout to connect new pages to existing wiki (Oleg Personal Context, Password Manager Migration, Oleg Home MOC, Oleg Business Entity Structure, etc.).

## [2026-06-13 10:10 UTC] ingest | raw/01-Strategie-Business/Allianz Insurance Consolidation.md
- Pages: [[Allianz Insurance Consolidation Detail]], [[Allianz Insurance Consolidation]], [[Risikolebensversicherung]]
- Ingested raw/01-Strategie-Business/Allianz Insurance Consolidation.md. Changes: (1) Created new source page 'Allianz Insurance Consolidation Detail' capturing the full policy table, the 5-policy/20%-discount strategy, the term life exclusion rationale, and open next-steps checklist. (2) Updated entity page 'Allianz Insurance Consolidation' to incorporate the new detail — added policy breakdown, term life rationale, Check24 benchmark note, and updated the status contradiction section with a third source now confirming 'open' status, providing a clearer resolution. (3) Created new concept page 'Risikolebensversicherung' explaining German term life insurance mechanics (entry-age locking, Gesundheitsprüfung risk) as a reusable concept. (4) Updated index.md with Risikolebensversicherung under Concepts > Finance & Insurance, and Allianz Insurance Consolidation Detail under Sources > Raw Source Summaries.

## [2026-06-13 10:13 UTC] ingest | raw/01-Strategie-Business/Café Berlin — Partnership Hai.md
- Pages: [[Café Berlin Partnership Hai — Planning Detail]], [[Café Berlin Partnership Hai]], [[Hai]], [[KfW ERP-Gründerkredit]], [[Friedrichshain]], [[Prenzlauer Berg]], [[Oleg Business Entity Structure]]
- Ingested raw/01-Strategie-Business/Café Berlin — Partnership Hai.md. Changes made:

1. CREATED new source page: 'Café Berlin Partnership Hai — Planning Detail' — full extraction of the planning document including decision history, 5-agenda-item kickoff structure, role split, location economics (Friedrichshain/Prenzlauer Berg, 25-40€/m², 80-120m²), profitability model (break-even <18 months, APC formula), legal prerequisites, and open questions. Contradiction flagged: source refers to 'GmbH (Oleg, ruhend)' but other sources consistently show GmbH as active — resolved as informal usage.

2. UPDATED entity page: 'Café Berlin Partnership Hai' — now substantially richer with origin story (solo model rejection rationale: Einkommensdeckel), role split table, location targets, financial structure details, legal entity options, legal prerequisites, and strategic tension with Cyprus Relocation. Sources list updated to include new planning document.

3. UPDATED entity page: 'Hai' — added proposed responsibility breakdown from planning doc (Operatives, Konzept, Küchenlogik, Lieferanten) and contextual note on why his skills make the partnership viable where solo model was not.

4. UPDATED synthesis page: 'Oleg Business Entity Structure' — added new contradiction section documenting GmbH 'ruhend' discrepancy, added café entity options discussion (GmbH activation vs. new GbR vs. new GmbH), updated sources list.

5. CREATED new concept page: 'KfW ERP-Gründerkredit' — new concept introduced in source; covers program overview, relevance to Café Berlin financing, typical loan parameters, and application process.

6. CREATED new entity pages: 'Friedrichshain' and 'Prenzlauer Berg' — two Berlin neighborhoods identified as target locations for the café venture.

7. UPDATED index.md — added Friedrichshain, Prenzlauer Berg (Entities); KfW ERP-Gründerkredit (Concepts); Café Berlin Partnership Hai — Planning Detail (Sources); updated summary for Café Berlin Partnership Hai entity to reflect richer content.

## [2026-06-13 10:16 UTC] ingest | raw/01-Strategie-Business/Cyprus Relocation.md
- Pages: [[Cyprus Relocation Detail]], [[Cyprus Tax Regime]], [[Cyprus Relocation]], [[Employer of Record]], [[Portugal IFICI]]
- Ingested raw/01-Strategie-Business/Cyprus Relocation.md. Created: (1) Cyprus Relocation Detail [source] — full analysis of country comparison, cost structure, gate items, lifestyle fit, 2027 timeline; (2) Cyprus Tax Regime [concept] — 50% exemption, Non-Dom status, 60-day rule, DE-CY treaty, comparison table; (3) Employer of Record [concept] — EOR mechanics, Deel/Remote.com, cost considerations, risk factors; (4) Portugal IFICI [concept] — NHR successor, reason for rejection (sales exclusion). Updated Cyprus Relocation [entity] — added detailed gate items, financial case, assumption [A] on 60-day presence, 2027 timeline, country decision rationale from source. Index updated with all new pages under correct categories. Key relationships established: Cyprus Relocation ↔ Café Berlin Partnership Hai (strategic tension), Cyprus Tax Regime ↔ EOR (employment requirement for exemption), Portugal IFICI ↔ Cyprus Tax Regime (comparison). No contradictions with existing wiki found beyond those already documented; source confirms 2027 timeline and both-partners EOR requirement not previously detailed in entity page.

## [2026-06-13 10:21 UTC] ingest | raw/01-Strategie-Business/DoktorLib Automation Pipeline.md
- Pages: [[DoktorLib Automation Pipeline Source Detail]], [[DoktorLib Automation Pipeline]], [[Tally]], [[Make]], [[Salesforce]], [[Dust Agent]], [[Notion]], [[Kundenerfassungsbogen]]
- INGESTED: raw/01-Strategie-Business/DoktorLib Automation Pipeline.md

CHANGES MADE:

1. NEW SOURCE PAGE: 'DoktorLib Automation Pipeline Source Detail' — Full architecture documentation with Ziel-Architektur flow diagram, 4 build phases, stack table, decisions made, and next step rationale. Reveals that Tally and Dust are NOT alternative choices (as existing entity implied) but complementary tools in phases 1 and 3 respectively. Make and Salesforce were also entirely absent from the existing entity page.

2. UPDATED ENTITY: 'DoktorLib Automation Pipeline' — Significantly expanded from original stub (which only mentioned 'Tally or Dust Agent as options'). Now includes: correct 5-tool stack (Tally + Make + Salesforce + Notion + Dust), full target flow diagram, all 4 build phases, key decisions, and a correction notice flagging the earlier misrepresentation of Tally/Dust as alternatives.

3. NEW CONCEPT PAGES (5): Tally, Make, Salesforce, Dust Agent, Notion — each documenting the tool's role in the DoktorLib pipeline, integration points, build status, and open items.

4. NEW CONCEPT PAGE: 'Kundenerfassungsbogen (KEB)' — The central artifact being automated; current state (manual Excel), target state (Dust Agent output via Notion link), field structure status (not yet defined), and why it drives the entire pipeline design.

5. CONTRADICTION NOTED: Existing DoktorLib Automation Pipeline entity described Tally and Dust as 'technology options under consideration' implying a binary choice. Source document shows both are used in a single multi-phase pipeline. Flagged and corrected in both entity and source pages.

6. INDEX UPDATED: Added 7 new entries across Entities (DoktorLib Automation Pipeline updated), Concepts (Dust Agent, Kundenerfassungsbogen, Make, Notion, Salesforce, Tally), and Sources (DoktorLib Automation Pipeline Source Detail). Reorganized Concepts section with new Technology & Automation subsection for clarity.

## [2026-06-13 10:23 UTC] ingest | raw/Privat/Performance/3D Body Scan — Scaneca Mai 2026.md
- Pages: [[3D Body Scan Scaneca Mai 2026 Source Detail]], [[3D Body Scan Scaneca Mai 2026]], [[3D Body Scan]], [[FFMI]], [[Forward Head Posture]], [[BMR and TDEE]]
- Ingested raw/Privat/Performance/3D Body Scan — Scaneca Mai 2026.md. Changes made:

1. CREATED wiki/sources/3D Body Scan Scaneca Mai 2026 Source Detail.md — new source page for the raw scan document with full German measurement table, interpretation, targets, and follow-up timeline. Flagged contradiction: source specifies 15–17% KFA target range vs. Health Protocol Master's 15% single value.

2. UPDATED wiki/entities/3D Body Scan Scaneca Mai 2026.md — added source reference to the new raw source file, corrected KFA target from '15%' to '15–17%' (per raw source), added waist target <90 cm, added 12-week follow-up timeline, added links to new concept pages (Forward Head Posture, FFMI, BMR and TDEE, 3D Body Scan Scaneca Mai 2026 Source Detail).

3. UPDATED wiki/concepts/3D Body Scan.md — added sources field entry for raw source, added target values section, added 12-week follow-up note, added links to new source page.

4. CREATED wiki/concepts/FFMI.md — new concept page for Fat-Free Mass Index with reference ranges, Oleg's baseline (21.3), formula, and protocol context.

5. CREATED wiki/concepts/Forward Head Posture.md — new concept page for FHP, Oleg's 30° finding, consequences, corrective protocol from Health Protocol Master, and Cavaliere neck training methodology.

6. CREATED wiki/concepts/BMR and TDEE.md — new concept page for metabolic rate metrics, Oleg's baseline values, implied activity multiplier (~1.72), caloric strategy (2,800 kcal, 845 kcal deficit), and protein rationale.

7. UPDATED index.md — added new concept entries (FFMI, Forward Head Posture, BMR and TDEE) and new source entry (3D Body Scan Scaneca Mai 2026 Source Detail) in appropriate categories.

Contradiction noted: Health Protocol Master source states 15% body fat goal; raw scan source specifies 15–17% range. Documented in source detail page and entity page; raw scan document treated as authoritative for the target range.

## [2026-06-13 10:27 UTC] ingest | raw/Privat/Performance/Supplement Stack.md
- Pages: [[Supplement Stack Source Detail]], [[Supplement Stack]], [[Momentous]], [[Creatine]], [[Sulforaphane]], [[Sunday Natural]], [[Rhonda Patrick]], [[L-Tyrosine]], [[Magnesium L-Threonate]], [[Apigenin]], [[L-Theanin]]
- Ingested raw/Privat/Performance/Supplement Stack.md. Created: (1) Supplement Stack Source Detail [source] — full document with Momentous-exclusivity principle, all 6 active supplements with dosing/timing, explicit exclusions table, situational pre-workout stack, and Vitamin D3 duplication flag; (2) Supplement Stack [entity] — updated from stub (previously referenced only in Health Protocol Master) to full entity with complete stack table, pre-workout stack, exclusion list, and framework references; (3) Momentous [entity] — new page for the primary supplement brand and Huberman Lab partner; (4) Creatine [concept] — new page covering 5g/day protocol and 'consistency > timing' principle; (5) Sulforaphane [concept] — new page covering NRF2 pathway, Rhonda Patrick protocol, Sunday Natural brand; (6) Sunday Natural [entity] — new page for the German supplement brand used as sole exception; (7) Rhonda Patrick [entity] — new page (previously referenced but no dedicated page) covering her research areas and direct influence on sulforaphane choice; (8) L-Tyrosine [entity] — expanded from implicit mention in Alpha-GPC page to full entity with mechanisms and Alpha-GPC synergy; (9) Magnesium L-Threonate [concept] — new page for brain-bioavailable magnesium in sleep stack; (10) Apigenin [concept] — new page for chamomile flavonoid in sleep stack; (11) L-Theanin [concept] — new page for the relaxation amino acid in sleep stack. Contradictions flagged: (a) Vitamin D3 potential double-dosing (Momentous Expert Stack + 20,000 IU × 2/week stock); (b) L-Tyrosine brand unspecified — may be a minor inconsistency with Momentous-exclusivity principle. Updated index.md with all new pages under appropriate categories and added supplement-related concepts to health section.

## [2026-06-13 10:29 UTC] ingest | raw/Privat/Tech/Claude Projects Setup.md
- Pages: [[Claude Projects Setup Source Detail]], [[Claude Projects Setup]]
- Ingested raw/Privat/Tech/Claude Projects Setup.md. Created two new pages: (1) 'Claude Projects Setup Source Detail' (source type) — full ingestion of the raw document capturing all 7 projects, context-driven vs task-driven distinction, 6-part instruction schema, global preferences, and tech stack; (2) Updated 'Claude Projects Setup' (entity type) — previously a stub with unknown details, now fully populated with project count (7), roles per project, design rationale, and cross-references. Key enrichments: the source resolves all three 'Unknown Details' flagged in the prior entity stub (number of projects, use cases, specific configurations). Cross-links added to Café Berlin Partnership Hai, Health Protocol Master, DoktorLib Automation Pipeline, Make, Tally, Notion, Salesforce, and Dust Agent. No contradictions detected with existing wiki content. Index updated with new source page entry and enriched Claude Projects Setup entity summary.

## [2026-06-13 10:30 UTC] ingest | raw/Privat/Tech/Password Manager Migration.md
- Pages: [[Password Manager Migration Source Detail]], [[Password Manager Migration]], [[Proton Pass]], [[Apple Passwords]], [[Privacy and Tech Stack]]
- Ingested raw/Privat/Tech/Password Manager Migration.md. Created 5 new pages: (1) Password Manager Migration Source Detail [source] — full technical detail, field incompatibility table, decision framework, CSV fix; (2) Password Manager Migration [entity] — decision status, framework, strategic context, required audit action; (3) Proton Pass [entity] — current password manager, feature set, privacy profile; (4) Apple Passwords [entity] — migration target, limitations, advantages; (5) Privacy and Tech Stack [concept stub] — referenced in source as linked context, placeholder for future full ingestion. Updated index.md with all new pages categorized under Entities (Tools & Products: Apple Passwords, Proton Pass; Businesses & Projects: Password Manager Migration) and Sources (Tech & Setup: Password Manager Migration Source Detail). Privacy and Tech Stack added under Concepts > Tech & Tools. No contradictions found with existing wiki content. Tags from source (entscheidung-offen) preserved throughout.

## [2026-06-13 10:32 UTC] ingest | raw/Privat/Tech/Privacy & Tech Stack.md
- Pages: [[Privacy and Tech Stack]], [[Privacy and Tech Stack Source Detail]], [[Proton Mail]], [[Proton VPN]], [[Proton Pass]]
- Ingested raw/Privat/Tech/Privacy & Tech Stack.md. Created: (1) Privacy and Tech Stack [entity] — full summary of devices, browser strategy, Proton ecosystem, domain/DNS, security measures, and open migration; (2) Privacy and Tech Stack Source Detail [source] — faithful German-language source capture with annotations; (3) Proton Mail [concept] — new stub concept page; (4) Proton VPN [concept] — new stub concept page; (5) Proton Pass [concept] — new concept page integrating existing Password Manager Migration knowledge. Updated index.md with all new pages categorized. Key wikilinks: Privacy and Tech Stack ↔ Password Manager Migration ↔ Apple Passwords ↔ Proton Pass ↔ MOC Tech und Setup. No contradictions with existing wiki found — the source references [[Password Manager Migration]] explicitly, consistent with existing Apple Passwords and Password Manager Migration entity pages. The domain ok-holding.com is consistent with Oleg Business Entity Structure. VPN Kill Switch and Proton Sentinel detail is new information not previously captured.

## [2026-06-13 10:34 UTC] ingest | raw/Privat/Recherchen/TEMPUR Matratzenkauf.md
- Pages: [[TEMPUR Matratzenkauf Source Detail]], [[TEMPUR Matratzenkauf]], [[Sleep Optimization]]
- Ingested raw/Privat/Recherchen/TEMPUR Matratzenkauf.md. Created 3 new pages: (1) TEMPUR Matratzenkauf Source Detail (source) — full product comparison tables, firmness rationale, pillow config, deal research; (2) TEMPUR Matratzenkauf (entity) — purchase decision summary with wikilinks; (3) Sleep Optimization (concept) — new concept page synthesizing TEMPUR hardware decision with existing supplement stack (Apigenin, Magnesium L-Threonate, L-Theanin) and Forward Head Posture / Health Protocol Master context. Added cross-link note: Oleg's L-size pillow selection at 188 cm is consistent with his 30° Forward Head Posture correction protocol. Updated index.md with TEMPUR Matratzenkauf entity, TEMPUR Matratzenkauf Source Detail source, and Sleep Optimization concept entries.

## [2026-06-13 10:36 UTC] ingest | raw/inbox/_merged/📥 Offene Actions.md
- Pages: [[Offene Actions Inbox]], [[Password Manager Migration]], [[Hyrox 10-Week Training]]
- Ingested raw/inbox/_merged/📥 Offene Actions.md. Created 3 new pages: (1) Offene Actions Inbox [source] — full action list with context, cross-references to all linked projects, contradiction note on Cyprus status; (2) Password Manager Migration [entity] — consolidated entity page (was only referenced, never had its own page); (3) Hyrox 10-Week Training [entity] — consolidated entity page with training plan overview and registration status. Updated index.md with all pages including new entries; added Comparisons section; added Password Manager Migration and Hyrox 10-Week Training to Entities; added Offene Actions Inbox to Sources. Tracked new contradiction: Cyprus listed as 'Someday/Maybe' in inbox but 'Priority 3 Blocked' in strategic MOC — resolved in favor of MOC with inbox context explanation. Confirmed existing wiki pages for Café Berlin Partnership Hai, Allianz Insurance Consolidation, 3D Body Scan, and Password Manager/Apple Passwords tools are all consistent with inbox actions. Minor date note flagged: inbox has Scaneca follow-up as 2026-09-01 vs 'mid-September' in scan documents (minor, consistent).

## [2026-06-13 10:49 UTC] ingest | raw/Finanzdaten/ObsidianVault/Finance/00 Finanz-Übersicht.md
- Pages: [[Finanz-Übersicht Source Detail]], [[Oleg Financial Situation]], [[Wagglz GmbH]], [[OK Capital UG]], [[Rehabilitation Plan]]
- Ingested raw/Finanzdaten/ObsidianVault/Finance/00 Finanz-Übersicht.md. Created 5 new pages: (1) Finanz-Übersicht Source Detail [source] — full source document for Oleg's financial overview including income tables, fixed expenses, asset status, company burden, and critical risks; (2) Oleg Financial Situation [entity] — synthesized financial picture with structural deficit of −7,970 €/year, Dispo overdraft, zero savings, two capital-consuming companies, and insolvency/GF-liability risk flags; (3) Wagglz GmbH [entity] — first explicit naming of Oleg's GmbH (funded via VW-Bank-Kredit → Crypto), consuming capital without returns; (4) OK Capital UG [entity] — first explicit naming of Oleg's UG, with contradiction note (other wiki pages call it dormant but this source lists it as capital-consuming with accounts due); (5) Rehabilitation Plan [entity] — three-phase plan with July provision allocation priority order. Key contradictions flagged: (a) OK Capital UG described as 'dormant' in existing wiki pages but this source lists it with annual accounts due and ~8,000 €/year combined company burden — resolution: likely dormant but still incurring compliance costs; (b) Cyprus Relocation plan assumes 30,000–35,000 € startup capital while current financial position shows near-zero assets — significant gap not addressed in Cyprus source documents; (c) Oleg Business Entity Structure and Café Berlin Planning Detail reference GmbH as 'active/Betriebsgesellschaft' without naming it — now identified as Wagglz GmbH. Updated index.md with new entities (OK Capital UG, Wagglz GmbH, Oleg Financial Situation, Rehabilitation Plan) and new source (Finanz-Übersicht Source Detail) plus Master Prompt – Gesamtanalyse added to stub pages.

## [2026-06-13 10:53 UTC] ingest | raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md
- Pages: [[Master Prompt Gesamtfinanzanalyse]], [[Wagglz GmbH]], [[OK Capital UG]], [[Oleg Financial Situation]], [[Insolvenzprüfung]], [[Gesellschafterdarlehen]], [[Oleg Business Entity Structure]]
- Ingested raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md. Created 6 new pages: (1) Master Prompt Gesamtfinanzanalyse [source] — full prompt documentation with four-perspective expert team (FD/ST/IA/US), hardcoded personal/company context, five critical analysis questions, document checklist, and six deliverables. (2) Wagglz GmbH [entity] — Oleg's active GmbH, crypto-financed via VW-Bank personal credit, no recognizable returns, open insolvency risk. (3) OK Capital UG [entity] — Oleg's dormant/low-activity UG (haftungsbeschränkt), subject to same insolvency assessment. (4) Oleg Financial Situation [entity] — consolidated private financials: −7.970 €/year structural deficit, −1.405 € Dispo, 1.10 € savings, total annual pressure ~−16k before provisions; VW-Bank credit (681,57 €/Mo to 11/2028) tied to Wagglz investment. (5) Insolvenzprüfung [concept] — §17 InsO (Zahlungsunfähigkeit) and §19 InsO (Überschuldung) explained with thresholds, Rangrücktritt relevance, GF Antragspflicht (21-day rule), and Anfechtungsrisiko. (6) Gesellschafterdarlehen [concept] — shareholder loan mechanics, automatic insolvency subordination (§39 InsO), 10-year claw-back risk (§135 InsO), Rangrücktritt for Überschuldung relief, verdeckte Einlage risk. Updated Oleg Business Entity Structure entity page (previously stub-level) with consolidated entity table, financial flows, strategic options, and contradiction resolution for the GmbH 'ruhend' discrepancy. The VW-Bank → Crypto → Wagglz GmbH capital flow is flagged throughout as a critical personal liability link. All pages include wikilinks to Oleg Personal Context, DoktorLib, Cyprus Relocation, Café Berlin Partnership Hai. Index updated with new Finance Concepts (Gesellschafterdarlehen, Insolvenzprüfung), Finance Entities (Wagglz GmbH, OK Capital UG, Oleg Financial Situation, Oleg Business Entity Structure updated), and Finance Sources (Master Prompt Gesamtfinanzanalyse).

## [2026-06-13 10:55 UTC] ingest | raw/Finanzdaten/ObsidianVault/Finance/OK Capital UG.md
- Pages: [[OK Capital UG]], [[OK Capital UG Source Detail]], [[Wagglz GmbH]], [[Master Prompt Gesamtanalyse]], [[Oleg Business Entity Structure]]
- Ingested raw/Finanzdaten/ObsidianVault/Finance/OK Capital UG.md. Created 5 new pages: (1) OK Capital UG [entity] — full entity page for the UG including financial position, insolvency questions, strategic options, and contradiction note vs existing 'dormant UG' references; (2) OK Capital UG Source Detail [source] — raw source summary page; (3) Wagglz GmbH [entity stub] — created from cross-reference in source, no dedicated source doc yet ingested; (4) Master Prompt Gesamtanalyse [entity stub] — created from wikilink in source, underlying doc not yet ingested; (5) Oleg Business Entity Structure [entity] — synthesized from OK Capital UG source + prior wiki references in Café Berlin and Cyprus pages; resolves the 'dormant UG' contradiction (operationally inactive but legally active with filing obligations). Key contradiction flagged: prior wiki pages describe UG as 'dormant' but OK Capital UG source shows ongoing Jahresabschluss costs, indicating legal activity. Strategic downstream links established to Café Berlin Partnership Hai (GmbH activation question), Cyprus Relocation (Wegzugsteuer risk), and Financial Independence (8,000 €/Jahr drag). Index updated with new Finance section entries under Entities, Sources, and Concepts.

## [2026-06-13 16:46 UTC] ingest | raw/Business/OK-Capital/Finanzen/Konten/OK Capital Finom 2026.md
- Pages: [[OK Capital Finom 2026]], [[OK Capital UG]]
- Ingested raw/Business/OK-Capital/Finanzen/Konten/OK Capital Finom 2026.md. Created 2 new pages: (1) sources/OK Capital Finom 2026 — source summary page with full account detail, recurring costs (WestX 23,50 €/Mo + Google 8,10 €/Mo), and Oleg Darlehen 100 € (01.03.2026); (2) entities/OK Capital UG — new entity page for the UG business entity, cross-referencing existing Oleg Business Entity Structure wiki knowledge. Flagged potential contradiction: source references GmbH as 'ruhend' in Café Berlin Planning Detail context, but the UG (not GmbH) is the formally dormant entity per existing wiki — added ⚠️ Assumption [A] callout on OK Capital UG page. Also flagged that zero saldo + active 31,60 €/Mo costs suggests entity is operationally minimal but not fully dormant. Updated index.md with both new pages in their respective sections.

## [2026-06-15 12:00] write | raw/Business/PerformanceCafe/research/01_longevity_science.md
- Created/updated: [[Longevity Science Grundlagen]]
- Notes: Modul 0 vollständig ausgearbeitet (280+ Zeilen). Abgedeckt: 12 Hallmarks of Aging (López-Otín 2023) mit Adressierbarkeits-Matrix, Kaffee als Longevity-Substanz (Chlorogensäure AMPK-Mechanismus, Trigonellin als NAD+-Vorstufe nach Nature Metabolism 2024, Cafestol/Kahweol LDL-Kontraindikation, Epidemiologie J-Kurve mit BMJ 2017 Metaanalyse n=3,8 Mio.), Biomarker-Profil (hs-CRP, HbA1c, ApoB, NAD+, IGF-1) mit DTC-Anbietern in DACH (Cerascreen, Lykon, Sanitas Health). Status in CLAUDE.md auf ✅ abgeschlossen gesetzt.

## [2026-06-15 12:00] ingest | raw/Business/Wagglz/Wagglz GmbH.md + Wagglz GmbH — Finance Vault.md
- Created/updated: [[Wagglz]]
- Notes: Neue Entity-Seite wiki/entities/Wagglz.md erstellt. Abdeckt: Stammdaten (100% OK Capital UG, GF Oleg Kober), Kapitalstruktur (VW-Bank-Kredit → Crypto → GmbH), Finanzlage (0 € Umsatz 2026, 27.926,89 € Fehlbetrag, §19 InsO Überschuldung, Rangrücktritt noch nicht unterschrieben), laufende Kosten, monatliche Gesellschafterdarlehen 2026 (~2.170 €), strategische Optionen (Weiterführung / Auflösung §17 EStG / Dormancy), offene kritische Punkte. Wikilinks zu [[OK Capital UG]], [[Insolvenzprüfung]], [[Gesellschafterdarlehen]], [[Oleg Business Entity Structure]].

## [2026-06-15 12:00] edit | raw/Business/PerformanceCafe/CLAUDE.md
- Notes: Umbenennung "Performance Café" → "Performance Coffee Brand" (Aufgabe 3). Produktname-Feld aktualisiert auf "Performance Coffee Brand (Arbeitstitel)". Datum auf 2026-06-15 aktualisiert. Modul-0-Status auf ✅ abgeschlossen gesetzt.

## [2026-06-15 17:10 UTC] ingest | raw/Business/OK-Capital/OK Capital UG.md
- Pages: [[OK Capital UG]], [[OK Capital UG Source Detail]], [[Wagglz GmbH]], [[Oleg Business Entity Structure]]
- Ingested raw/Business/OK-Capital/OK Capital UG.md. Created 4 new pages: (1) OK Capital UG [entity] — holding company detail, 31.60 €/Mo costs, 0.00 € balance, 100 € shareholder loan, two-tier structure diagram; (2) OK Capital UG Source Detail [source] — raw source summary; (3) Wagglz GmbH [entity] — new entity page for the operational subsidiary (previously only implied in wiki); (4) Updated Oleg Business Entity Structure [entity] — reconciled the previously ambiguous 'active GmbH + dormant UG' description with the now-confirmed structure (OK Capital UG = holding, Wagglz GmbH = operativ subsidiary of UG). Key contradiction resolved: earlier wiki pages described a 'dormant UG' but OK Capital UG is actively incurring costs as a holding — 'dormant' referred to absence of trading activity, not legal dormancy. Flagged ongoing tension with Café Berlin Planning Detail reference to 'GmbH (Oleg, ruhend)' — best interpretation is Wagglz GmbH not yet deployed for café, not formally dormant. Index updated with OK Capital UG, Wagglz GmbH, and Oleg Business Entity Structure entries; source entry added for OK Capital UG Source Detail.

## [2026-06-15 17:42 UTC] ingest | raw/Business/OK-Capital/Rangrücktritt §15a InsO.md
- Pages: [[Rangrücktritt §15a InsO Source Detail]], [[Rangrücktritt §15a InsO]], [[Wagglz GmbH]]
- Ingested raw/Business/OK-Capital/Rangrücktritt §15a InsO.md. Created 3 new wiki pages: (1) 'Rangrücktritt §15a InsO Source Detail' (source) — full legal mechanism documentation for the P0 subordination declaration, including §15a/§19 InsO chain, Überschuldung of 27,926.89 €, criminal liability risk, and 2026-06-15 signature deadline; (2) 'Rangrücktritt §15a InsO' (entity) — summary entity page with legal chain diagram and urgency note; (3) 'Wagglz GmbH' (entity) — new company entity under OK-Capital umbrella, flagging assumption that it is distinct from Oleg's primary GmbH in Oleg Business Entity Structure. Added cross-links throughout to Oleg Personal Context, Oleg Business Entity Structure, and P0 Sofort. Updated index.md: added Wagglz GmbH under Entities/Companies, Rangrücktritt §15a InsO under Entities/Projects, and Rangrücktritt §15a InsO Source Detail under Sources/Business & Strategy. No contradictions with existing wiki detected — this is entirely new territory (OK-Capital / Wagglz domain not previously documented).

## [2026-06-15 17:48 UTC] ingest | raw/Business/PerformanceCafe/CLAUDE.md
- Pages: [[Performance Coffee Brand CLAUDE Project Context]], [[Performance Coffee Brand]], [[NMN]], [[Urolithin A]], [[Trigonellin]], [[Chlorogenic Acid]], [[Longevity Stack Ingredients]], [[Kölner Liste]], [[Oleg Personal Context]], [[Bryan Johnson]]
- Ingested raw/Business/PerformanceCafe/CLAUDE.md. Created 8 new articles: (1) source page 'Performance Coffee Brand CLAUDE Project Context' capturing the full CLAUDE.md; (2) entity page 'Performance Coffee Brand' summarizing the startup concept, white space, segments, stack, and regulatory blockers; (3) concept page 'NMN' covering NAD+ pathway, trigonellin connection, and EU Novel Food blocker; (4) concept page 'Urolithin A' covering mitophagy mechanism and Amazentis/Mitopure patent barrier; (5) concept page 'Trigonellin' covering the 2024 NMN-precursor discovery and roast optimization; (6) concept page 'Chlorogenic Acid' covering AMPK activation and Vietnamese Robusta optimization; (7) concept page 'Longevity Stack Ingredients' mapping all proposed ingredients with regulatory/IP status; (8) concept page 'Kölner Liste' covering DACH anti-doping certification relevance. Updated 'Bryan Johnson' entity to add coffee-removal white space detail and Performance Coffee Brand connection. Updated 'Oleg Personal Context' entity to add Performance Coffee Brand as a business venture and incorporate the Doctolib/Hyrox athlete/biohacker framing from the CLAUDE.md. Updated index.md with new entries under Entities (Performance Coffee Brand), Concepts (Trigonellin, Chlorogenic Acid, Longevity Stack Ingredients, Kölner Liste, NMN, Urolithin A), and Sources (Performance Coffee Brand CLAUDE Project Context). No contradictions with existing wiki content found — the Performance Coffee Brand is a new project not previously represented. Note: Daily Protocol Checklist already contained a [[Performance Coffee]] wikilink confirming this project was anticipated in prior wiki content.

## [2026-06-15 19:17 UTC] ingest | raw/Business/PerformanceCafe/README.md
- Pages: [[Performance Cafe README Project Setup]], [[Performance Coffee Brand]], [[EU Novel Food Regulation]], [[Amazentis]], [[Chromadex Niagen Bioscience]], [[Kölner Liste]], [[NAC]], [[Spermidine]]
- Ingested raw/Business/PerformanceCafe/README.md. Created 7 new articles: (1) Performance Cafe README Project Setup [source] — project setup, toolchain, module priority order, critical blockers; (2) Performance Coffee Brand [entity] — updated/created full entity page for the longevity coffee brand concept, consolidating README + CLAUDE.md context (CLAUDE.md was already referenced in existing Bryan Johnson and Chlorogenic Acid pages, confirming this brand concept existed partially in wiki); (3) EU Novel Food Regulation [concept] — EU 2015/2283 framework; blocks NMN, Urolithin A, Spermidine; (4) Amazentis [entity] — Swiss biotech holding Urolithin A patents (MITOPURE) and Novel Food authorization; IP blocker; (5) Chromadex [entity] — US biotech holding NR/NMN-adjacent patents (Tru Niagen); parallel IP blocker; (6) Kölner Liste [concept] — German anti-doping certification roadmap for Performance Café CMO selection; (7) NAC [concept] — N-Acetyl Cysteine; glutathione precursor; sulfurous odor formulation challenge; (8) Spermidine [concept] — polyamine autophagy inducer; EU Novel Food status unclear. Updated index.md with all new entries under appropriate categories. Existing Bryan Johnson page already referenced Performance Coffee Brand and CLAUDE.md — no contradictions found. Existing Chlorogenic Acid page already referenced Performance Coffee Brand CLAUDE Project Context. The Performance Coffee Brand entity page was newly created as a proper full entity page (prior wiki only had concept-level references scattered in Bryan Johnson and Chlorogenic Acid pages). NMN and Urolithin A pages are referenced but not yet in wiki — flagged for future creation via wikilinks.

## [2026-06-15 19:24 UTC] ingest | raw/Business/PerformanceCafe/TODO.md
- Pages: [[Performance Coffee Brand TODO Master]], [[Performance Coffee Brand]], [[Wagglz GmbH]], [[Hai]], [[NMN]], [[Urolithin A]], [[Trigonellin]], [[Longevity Stack Ingredients]], [[EUIPO Trademark Registration]], [[Kölner Liste]]
- Ingested raw/Business/PerformanceCafe/TODO.md. Created 8 new articles:

1. **Performance Coffee Brand TODO Master** (source) — Full task list source document for all phases (0–4+) with budget breakdown, regulatory blockers, brand naming candidates (AEVUM/KOLVR/ORVYN), CMO tasks, and go-to-market strategy.

2. **Performance Coffee Brand** (entity) — Updated/created comprehensive entity page integrating TODO.md data with existing CLAUDE.md/README.md knowledge; covers product concept, Tier-1/Tier-2 stacks, regulatory blockers, go-to-market, pricing, certifications roadmap, and phase timeline. Flagged new risk: Hai's dual-venture bandwidth (Café Berlin + Performance Coffee simultaneously).

3. **Wagglz GmbH** (entity) — New entity page for the operating vehicle; documents reactivation requirements, ownership structure, and open question about relationship to Oleg's personal GmbH/UG structure.

4. **Hai** (entity) — Expanded from existing partial references; now documents dual-venture role (Café Berlin + Performance Coffee Brand), 50% Gesellschafter status in Wagglz GmbH, and flagged bandwidth risk.

5. **NMN** (concept) — New dedicated concept page covering NAD+ mechanism, EU Novel Food blocker status, Chromadex IP overlap, decision tree with Trigonellin fallback, and stack tier placement.

6. **Urolithin A** (concept) — New dedicated concept page covering mitophagy mechanism, Amazentis dual barrier (patent + Novel Food), decision options, and Tier-2 deferral rationale.

7. **Trigonellin** (concept) — New concept page covering NAD+ precursor pathway, roast sensitivity, and strategic role as natural NMN fallback if EU approval is denied.

8. **Longevity Stack Ingredients** (concept) — Comprehensive Tier-1 / Tier-2 ingredient framework with regulatory status, NAD+ pathway strategy, and formulation challenges (NAC odor, Curcumin solubility).

9. **EUIPO Trademark Registration** (concept) — New concept covering EU trademark process, Nice Classes 30+5, cost (~1.000€), and pre-launch timing requirement.

10. **Kölner Liste** (concept) — New concept covering German anti-doping certification; MVP standard for DACH market; progression to Informed Sport and NSF.

Index updated with all new entries properly categorized. No contradictions found with existing wiki content — the TODO.md is consistent with the CLAUDE.md and README.md already ingested (Amazentis, Chromadex, Bryan Johnson entries remain valid). New risk flagged: Hai simultaneously co-founding Café Berlin (Priority 1) and Performance Coffee Brand — bandwidth not addressed in any source document.

## [2026-06-15 19:32 UTC] ingest | raw/Business/PerformanceCafe/brand/positioning.md
- Pages: [[Performance Coffee Brand Positioning]], [[Performance Coffee Brand]], [[Rhonda Patrick]], [[Peter Attia]], [[Competitive Landscape Performance Coffee]]
- Ingested raw/Business/PerformanceCafe/brand/positioning.md (status: fertig, date: 2026-06-15).

New pages created:
1. **Performance Coffee Brand Positioning** (source) — Full brand positioning document: tagline 'Perform now. Live longer.', 3 segments (Athlete/Executive/Biohacker), brand voice rules, 5-competitor differentiation matrix, pricing story at 3.49€/sachet, visual identity (matte off-white + amber, 30×110mm stick-pack), 3-phase launch messaging sequence. Includes regulatory notes on EFSA 'Anti-Aging' prohibition and pharmaceutical law claim restrictions.
2. **Performance Coffee Brand** (entity) — Updated/created comprehensive entity page consolidating all known information about the startup concept; added brand positioning section, competitive matrix, document status tracker, founder-market fit section. Previously existed as entity in sources (README/CLAUDE) but now has its own dedicated entity page with full positioning context.
3. **Rhonda Patrick** (entity) — New entity page; referenced in positioning document as Segment 3 biohacker influencer; connected to Huberman Lab episode already in wiki and to Oleg's sulforaphane use in Daily Protocol Checklist.
4. **Peter Attia** (entity) — New entity page; referenced as Segment 3 biohacker influencer; connected to NMN and longevity ingredient discussions.
5. **Competitive Landscape Performance Coffee** (comparison) — New comparison page; structured competitor profiles for Blueprint, Four Sigmatic, RYZE, MUD\WTR, Timeline Mitopure; positioning matrix visualization; pricing comparison table; strategic conclusion with risk factors.

Index updated with all new pages in appropriate categories. Existing entity [[Bryan Johnson]] already had the blueprint/coffee white-space context from prior ingestion — no contradiction.

Notable cross-links: Amazentis appears as BOTH competitor (Timeline Mitopure) AND IP blocker — flagged in Competitive Landscape page. The positioning doc references internal files (naming_brief, marktanalyse, business_case) not yet ingested — noted in source page.

No contradictions found with existing wiki content.

## [2026-06-15 19:34 UTC] ingest | raw/Business/PerformanceCafe/hai-fragen.md
- Pages: [[Fragen an Hai Performance Coffee Brand]], [[Hai]], [[Performance Coffee Brand]]
- Ingested raw/Business/PerformanceCafe/hai-fragen.md. Created 3 new pages: (1) source page 'Fragen an Hai Performance Coffee Brand' — full structured analysis of the due-diligence questionnaire with significance notes per section; (2) entity page 'Hai' — consolidated from all sources (café partnership + coffee brand), now includes all open questions from the questionnaire and dual-venture involvement note; (3) updated entity page 'Performance Coffee Brand' — added candidate brand names (AEVUM, KOLVR, ORVYN), Phase 0-1 budget (5-8k EUR 50/50), vesting structure (4yr/1yr cliff), Blueprint transparency strategy, updated co-founder section. Two contradictions flagged: (a) questionnaire references both 'UG-Gründungskosten' (new UG) and 'Wagglz GmbH als operative Einheit' (existing GmbH) as legal entity options — both remain open, no decision made; (b) Hai's role spans both café and coffee brand simultaneously — capacity risk noted. Index updated with new source entry and Hai entity entry; Performance Coffee Brand updated with brand name candidates.

## [2026-06-15 19:39 UTC] ingest | raw/Business/PerformanceCafe/hai-onepager.md
- Pages: [[Performance Coffee Brand Hai Onepager]], [[Performance Coffee Brand]], [[Hai]], [[Wagglz GmbH]], [[OK Capital Holding]], [[Taurin]], [[Lion's Mane]], [[Ashwagandha KSM-66]]
- Ingested raw/Business/PerformanceCafe/hai-onepager.md. Created 6 new pages: (1) Performance Coffee Brand Hai Onepager [source] — full source detail with Tier-1 stack, market numbers, GTM, budget, and legal structure; (2) Performance Coffee Brand [entity] — updated/created master entity page consolidating all three Performance Cafe sources; (3) Hai [entity] — person page for co-founder appearing in both café and coffee ventures; (4) Wagglz GmbH [entity] — operating vehicle for Performance Coffee; (5) OK Capital Holding [entity] — IP holding entity; (6) Taurin [concept] — Tier-1 ingredient with Science 2023 longevity reference. Also created Lion's Mane [concept] and Ashwagandha KSM-66 [concept] as new ingredient pages introduced by this source. Updated index.md with all new pages categorized. Key new information: brand name candidates AEVUM/KOLVR/ORVYN (first appearance in wiki); 77% contribution margin at Tier-1; 130 boxes/month break-even; Hyrox GTM channel with 8,500 participants/event figure; explicit Tier-1 vs Tier-2 stack split logic (Tier-1 = no Novel Food/IP issues, Tier-2 = deferred). One potential contradiction flagged: Wagglz GmbH identity relative to Oleg's existing GmbH in Oleg Business Entity Structure is ambiguous.

## [2026-06-15 19:42 UTC] ingest | raw/Business/PerformanceCafe/legal/entity_structure.md
- Pages: [[Performance Coffee Brand Entity Structure Source Detail]], [[OK Capital]], [[Performance Coffee Brand Legal and Entity Structure]], [[Hai]], [[Performance Coffee Brand AEVUM Naming]], [[Wagglz]]
- Ingested raw/Business/PerformanceCafe/legal/entity_structure.md. Created 5 new wiki pages:

1. **Performance Coffee Brand Entity Structure Source Detail** (source) — Full source document ingestion: UG→GmbH roadmap, 50/50 Oleg+Hai structure under OK Capital, 4-year vesting with 1-year cliff, deadlock clauses, IP separation at holding level (4–6% license fees), EUIPO trademark plan for Classes 30+5, AEVUM as top name candidate.

2. **OK Capital** (entity) — New entity page for Oleg's existing holding company; documents portfolio (Wagglz + planned Performance Coffee Brand), Phase 2 IP structure with 95% tax-free inter-company dividends (§ 8b KStG), and cross-references to Cyprus Relocation complexity. Flagged contradiction with Café Berlin source that refers to 'GmbH (Oleg, ruhend)' — best interpretation documented.

3. **Performance Coffee Brand Legal and Entity Structure** (entity) — Structured summary of all legal/corporate decisions: phase roadmap, partnership terms, role split table, EUIPO strategy.

4. **Hai** (entity) — Consolidated Hai's role across BOTH ventures (Performance Coffee Brand 50/50 + Café Berlin partnership). Previously Hai appeared as a reference in other pages but had no dedicated entity page. Now documents confirmed contributions, role splits in both ventures, vesting terms, and flags the concentration risk of two simultaneous ventures with the same partner.

5. **Performance Coffee Brand AEVUM Naming** (entity) — Dedicated page for brand name candidates; AEVUM etymology and trademark fit analysis, Kolvr/Orvyn alternatives, EUIPO research status.

6. **Wagglz** (entity) — Stub entity page for existing OK Capital subsidiary mentioned in corporate structure; documents the gap in available information.

Key contradiction noted: The Café Berlin Planning Detail references 'GmbH (Oleg, ruhend)' as potential café operator, but the Performance Coffee Brand entity structure shows OK Capital as the active holding with Wagglz and Performance Coffee Brand beneath it. The Oleg Business Entity Structure page identifies GmbH=active, UG=dormant. This three-way inconsistency is documented in both OK Capital and Performance Coffee Brand Entity Structure Source Detail pages.

Index updated with all new pages plus reorganized for completeness; Hai moved from implicit reference to explicit entity listing.

## [2026-06-15 19:51 UTC] ingest | raw/Business/PerformanceCafe/ops/certification_roadmap.md
- Pages: [[Performance Coffee Brand Certification Roadmap Source Detail]], [[Kölner Liste]], [[Informed Sport]], [[NSF Certified for Sport]], [[NEM Konformität]], [[EFSA Health Claims]], [[Certification Roadmap Performance Coffee Brand]]
- Ingested raw/Business/PerformanceCafe/ops/certification_roadmap.md. Created 6 new pages: (1) Performance Coffee Brand Certification Roadmap Source Detail [source] — full ops document mapping 3-tier certification strategy with costs, timelines, and processes; (2) Kölner Liste [entity] — German athlete supplement certification, DACH MVP tier for Performance Coffee Brand; (3) Informed Sport [entity] — LGC Group pan-European per-batch certification, scale tier; (4) NSF Certified for Sport [entity] — US gold standard certification, US expansion tier; (5) NEM Konformität [concept] — mandatory EU/DACH food law compliance framework covering LMIV labeling, Novel Food checks (NMN, Urolithin A), and EFSA health claims; (6) EFSA Health Claims [concept] — EU health claims regulation, what is permitted vs. forbidden, Blueprint transparency strategy as compliant alternative. Also created (7) Certification Roadmap Performance Coffee Brand [synthesis] — maps all three tiers plus mandatory compliance to business phases, costs, and dependencies. Key cross-links added to existing entities: Performance Coffee Brand, Amazentis (Urolithin A Novel Food), Chromadex (NMN IP), NMN, Urolithin A, Bryan Johnson (Blueprint strategy), EU Novel Food Regulation. Important finding documented in NEM Konformität: both NMN and Urolithin A face regulatory/IP blockers (Novel Food + patent) that could prevent their use in the stack — this is the core launch risk beyond certifications. Updated index.md with new Certifications section under Entities, and NEM Konformität + EFSA Health Claims added to Concepts. LGC Group added as company entity stub.

## [2026-06-15 19:53 UTC] ingest | raw/Business/PerformanceCafe/ops/cmo-email-template.md
- Pages: [[CMO Erstkontakt Email Template]], [[CMO Sourcing Performance Coffee]], [[Performance Coffee Brand]]
- Ingested raw/Business/PerformanceCafe/ops/cmo-email-template.md. Created: (1) CMO Erstkontakt Email Template [source] — full template detail, 5 candidate profiles, technical specs, NAC odor masking challenge; (2) CMO Sourcing Performance Coffee [entity] — new entity consolidating CMO search workstream with selection criteria and certification dependency mapping; (3) Updated Performance Coffee Brand [entity] — added CMO sourcing status, NAC contradiction note, and links to new pages. Key findings: (a) NAC appears in CMO email as technical challenge but is absent from official Tier-1 stack in other sources — contradiction flagged on both CMO pages and Performance Coffee Brand entity; (b) Herbafit has IFS Food (not GMP/Kölner Liste) — noted in ranking rationale; (c) Sender email accounts@ok-holding.com confirms OK-Holding connection to Performance Coffee Brand; (d) Pilot batch target (1,000–2,000 sachets) and scale target (10,000–50,000/month) are now formally documented. Index updated with all new/updated pages.

## [2026-06-15 20:55 UTC] ingest | raw/Business/Wagglz/Finanzen/Einnahmen/Wagglz GF-Gehalt 2025.md
- Pages: [[Wagglz GF-Gehalt 2025 Source Detail]], [[Wagglz GmbH]], [[ESt 2025]], [[SP STB]], [[ALG I 2025]]
- Ingested raw/Business/Wagglz/Finanzen/Einnahmen/Wagglz GF-Gehalt 2025.md. Created 5 new pages: (1) Wagglz GF-Gehalt 2025 Source Detail [source] — primary source document summary with tax classification detail and action item; (2) Wagglz GmbH [entity] — new business entity stub, flagged as missing from Oleg Business Entity Structure (contradiction/gap noted); (3) ESt 2025 [entity] — 2025 income tax return entity, notes Progressionsvorbehalt implication of ALG I + GF salary combination; (4) SP STB [entity] — Steuerberater stub; (5) ALG I 2025 [entity] — unemployment benefit stub with Progressionsvorbehalt explanation. Key observations: (a) Wagglz GmbH was not previously documented in the wiki — it appears to be a third distinct entity alongside the GmbH and UG referenced in Oleg Business Entity Structure; contradiction flagged on Wagglz GmbH page. (b) Co-occurrence of ALG I and GF salary in same tax year triggers Progressionsvorbehalt — this is a non-obvious tax implication worth surfacing. (c) All wikilinks from the original source ([[ESt 2025]], [[Wagglz GmbH]], [[ALG I 2025]]) now resolve to real pages. Index updated with Finance & Tax section under Entities and Sources.

## [2026-06-15 20:59 UTC] ingest | raw/Business/Wagglz/Wagglz GmbH — Finance Vault.md
- Pages: [[Wagglz GmbH Finance Vault]], [[Wagglz GmbH]], [[OK Capital UG]]
- Ingested raw/Business/Wagglz/Wagglz GmbH — Finance Vault.md. Created 3 new articles: (1) Wagglz GmbH Finance Vault [source] — full detail on capital chain, insolvency questions, document checklist, strategic options; (2) Wagglz GmbH [entity] — consolidated entity page noting the capital chain risk, insolvency legal exposure, and connection to OK Capital UG; (3) OK Capital UG [entity] — stub entity created from single reference in Finance Vault, flagged as assumption-heavy pending additional sources. The Wagglz GmbH entity page previously existed only as a cross-reference target in ALG I 2025 and Wagglz GF-Gehalt 2025 Source Detail — this ingestion gives it a proper entity page. No contradictions found with existing wiki content; the existing ALG I 2025 and Wagglz GF-Gehalt 2025 Source Detail pages are consistent with this new source. Index updated with all three new pages under appropriate categories.

## [2026-06-15 21:02 UTC] ingest | raw/Business/Wagglz/Wagglz GmbH.md
- Pages: [[Wagglz GmbH Source Detail]], [[Wagglz GmbH]], [[Rangrücktritt §15a InsO]], [[OK Capital UG]]
- Ingested raw/Business/Wagglz/Wagglz GmbH.md. Created 4 new pages: (1) 'Wagglz GmbH Source Detail' (source) — full company data, insolvency figures, loan schedule, costs, strategic options; (2) 'Wagglz GmbH' (entity) — master entity page for the company with insolvency analysis, §19/§15a InsO legal context, option to continue vs. dissolve; (3) 'Rangrücktritt §15a InsO' (concept) — legal instrument concept page covering the subordination mechanism, Wagglz application, drafting requirements, and Oleg's personal liability risk; (4) 'OK Capital UG' (entity) — holding UG that owns 100% of Wagglz GmbH, with corporate structure diagram and contradiction note on Gesellschafter identity in loan documents. All pages cross-link to existing wiki entities: Oleg Personal Context, SP STB, ALG I 2025, ESt 2025, Oleg Business Entity Structure, P0 Sofort, P1 Diese Woche. Wagglz GmbH entity page updated to include both source files in frontmatter (existing GF-Gehalt source + new Wagglz GmbH source). Index updated with new entries in Entities (OK Capital UG, Wagglz GmbH under Companies), Concepts (Rangrücktritt §15a InsO under Legal & Business), and Sources (Wagglz GmbH Source Detail). No contradictions found with existing wiki content — ALG I 2025 already references Wagglz GmbH as GF-salary payer, consistent with new data.

## [2026-06-15 21:03 UTC] ingest | raw/Privat/Auswandern/Cyprus Relocation Tracker.md
- Pages: [[Cyprus Relocation Tracker Source Detail]], [[Cyprus Relocation]]
- Ingested raw/Privat/Auswandern/Cyprus Relocation Tracker.md. Created new source page 'Cyprus Relocation Tracker Source Detail' in wiki/sources/ capturing the paused private tracker. Updated the existing 'Cyprus Relocation' entity page to: (1) add the private tracker as a third source, (2) note the paused/someday status from the private file, (3) add the reactivation checklist, and (4) confirm financial benchmarks (4,100 €/month, 30,000–35,000 € startup capital) are consistent across both source documents — no contradictions found. Updated index.md to include the new source page entry and reorganized the existing truncated index into a clean full index covering all currently visible wiki pages. The private tracker's data is fully consistent with the existing Cyprus Relocation entity page content.

## [2026-06-15 21:07 UTC] ingest | raw/Privat/Finanzen/00 MOC Finanzen.md
- Pages: [[MOC Finanzen Source Detail]], [[MOC Finanzen]], [[Doctolib 2026]], [[VW Konsumkredit]], [[Consorsbank Girokonto 0250120493]], [[OK Capital UG]], [[Fixkosten Übersicht]], [[ESt 2025]], [[ALG I Progressionsvorbehalt]], [[Rangrücktritt §15a InsO]], [[Wagglz Finom 2026]], [[OK Capital Finom 2026]]
- Ingested raw/Privat/Finanzen/00 MOC Finanzen.md. Created: (1) MOC Finanzen Source Detail [source], (2) MOC Finanzen [entity — finance dashboard hub], (3) Doctolib 2026 [entity — 3,638.82 €/month + 8,249.96 € bonus], (4) VW Konsumkredit [entity — 18,858 € Restschuld until Nov 2028], (5) Consorsbank Girokonto 0250120493 [entity — +971.67 € saldo], (6) OK Capital UG [entity — updated/created with finance MOC context], (7) Fixkosten Übersicht [entity — ~2,200 €/month placeholder], (8) ESt 2025 [entity — complex 2025 filing with Wagglz + ALG I + Doctolib], (9) ALG I Progressionsvorbehalt [concept — §32b EStG mechanism], (10) Rangrücktritt §15a InsO [concept — subordination agreement], (11) Wagglz Finom 2026 [entity — Wagglz business banking], (12) OK Capital Finom 2026 [entity — OK Capital business banking]. Updated index.md with new Finance section entries, added MOC Finanzen to MOCs section, added new contradiction (Doctolib vs DoktorLib employer name). Note: ALG I 2025 entity already existed in wiki — not duplicated but cross-referenced. Several stub pages (P0 Sofort, P1 Diese Woche, P2 Diesen Monat, Wagglz GF-Gehalt 2025, SP STB, Wagglz GmbH) referenced but not created as they either already exist or await their own source ingestion.

## [2026-06-15 21:08 UTC] ingest | raw/Privat/Finanzen/Archiv/GESAMTANALYSE Archiv.md
- Pages: [[GESAMTANALYSE Archiv Source Detail]], [[MOC Finanzen]]
- Ingested raw/Privat/Finanzen/Archiv/GESAMTANALYSE Archiv.md. Created one new source page (GESAMTANALYSE Archiv Source Detail) documenting the archive pointer, its two referenced external files (GESAMTANALYSE_Oleg_Kober_2025-2026.md and Finanzdashboard_Oleg_Kober_2026.html), and the period covered (Jan 2025–Jun 2026). Created/updated MOC Finanzen entity page to reference the archive and establish it as the current financial navigation hub superseding the archive. Both pages include full wikilinks to existing financial entities (ESt 2025, ALG I 2025, Wagglz GF-Gehalt 2025, Doctolib 2026, Fixkosten Übersicht, Consorsbank, etc.) and flag that the actual analysis content has not been ingested. No contradictions found with existing wiki content — the source is purely a pointer/archive document with no substantive data to conflict. Index updated with new MOC Finanzen entity and GESAMTANALYSE Archiv Source Detail source entries.

## [2026-06-15 21:15 UTC] ingest | raw/Privat/Finanzen/Aufgaben/P0 Sofort.md
- Pages: [[P0 Sofortmaßnahmen Source Detail]], [[P0 Sofortmaßnahmen]], [[Rangrücktritt §15a InsO]], [[VW Kredit]], [[Consorsbank Girokonto 260809254]]
- Ingested raw/Privat/Finanzen/Aufgaben/P0 Sofort.md. Created 5 new pages: (1) P0 Sofortmaßnahmen Source Detail — source page for the raw file; (2) P0 Sofortmaßnahmen — entity page summarizing open critical tasks (Rangrücktritt Wagglz by 2026-06-15 with §15a InsO criminal liability risk, Vollständigkeitserklärung SP STB by 2026-06-20 blocking Jahresabschluss) and completed items; (3) Rangrücktritt §15a InsO — new concept page explaining the legal mechanism, GF criminal liability under Insolvenzverschleppung, and the Wagglz-specific situation with 27,926.89 € Fehlbetrag; (4) VW Kredit — new entity page for the confirmed vehicle loan (18,858 € Restschuld, runs until Nov 2028); (5) Consorsbank Girokonto 260809254 — new entity page for the now-closed second Consorsbank account (distinct from the existing 0250120493 main account). Updated index.md to include all new pages under Entities (Accounts & Finance), Concepts (Finance & Law), and Sources (Finance) sections. No contradictions found with existing wiki content — the Consorsbank 260809254 account is confirmed distinct from the existing 0250120493 entity page.

## [2026-06-15 21:18 UTC] ingest | raw/Privat/Finanzen/Aufgaben/P1 Diese Woche.md
- Pages: [[P1 Diese Woche Source Detail]], [[ESt 2025]], [[Wagglz GmbH]], [[Fixkosten Übersicht]], [[Oleg-Darlehen]], [[HEK]], [[Barmenia]], [[SP STB]]
- Ingested raw/Privat/Finanzen/Aufgaben/P1 Diese Woche.md. Created 8 new pages: (1) P1 Diese Woche Source Detail [source] — full task list with extracted data points; (2) ESt 2025 [entity] — tax filing with document checklist, Progressionsvorbehalt note, Lohnsteuerbescheinigung blocker; (3) Wagglz GmbH [entity] — zero revenue since Jan 2026, §17 EStG dissolution option, Oleg-Darlehen financing; (4) Fixkosten Übersicht [entity] — 61% fixkostenquote, three optimization targets; (5) Oleg-Darlehen [entity] — shareholder loan to Wagglz, §17 EStG loss implications; (6) SP STB [entity] — Steuerberater handling ESt 2025 and Wagglz; (7) HEK [entity] — KV provider for ESt 2025; (8) Barmenia [entity] — second KV provider for ESt 2025, possible Tierversicherung comparison candidate. All pages cross-linked to existing wiki pages (ALG I 2025, ALG I Progressionsvorbehalt, Allianz Insurance Consolidation, Consorsbank Girokonto 0250120493, Oleg Business Entity Structure, MOC Finanzen, Oleg Personal Context, Wagglz GF-Gehalt 2025 Source Detail). Updated index.md with all new entries categorized. No contradictions found with existing wiki content; one new potential contradiction flagged in Wagglz GmbH page (Lohnsteuerbescheinigung not yet available vs. assumed availability in ESt 2025 workflow).

## [2026-06-15 21:21 UTC] ingest | raw/Privat/Finanzen/Aufgaben/P2 Diesen Monat.md
- Pages: [[P2 Diesen Monat Source Detail]], [[Doctolib PKW-Sachbezug]], [[Notfallfonds]], [[DZR GmbH]], [[VW Konsumkredit]], [[P2 Diesen Monat]], [[ARAG Wagglz Versicherung]]
- Ingested raw/Privat/Finanzen/Aufgaben/P2 Diesen Monat.md. Created: (1) P2 Diesen Monat Source Detail (source page — full task breakdown with financial context), (2) P2 Diesen Monat (entity page — task summary with wikilinks), (3) Doctolib PKW-Sachbezug (concept page — 1%-Regel vs Fahrtenbuch analysis), (4) Notfallfonds (concept page — emergency fund goal, Q2 bonus allocation conflict with VW Sondertilgung), (5) DZR GmbH (entity page — creditor, payment history, closure pending), (6) VW Konsumkredit (entity page — loan details, Sondertilgung evaluation framework), (7) ARAG Wagglz Versicherung (entity page — insurance cancellation task). Added wikilinks throughout to existing wiki pages: Wagglz GmbH, SP STB, Doctolib 2026, Consorsbank Girokonto 0250120493, Fixkosten Übersicht, MOC Finanzen, P0 Sofortmaßnahmen, Wagglz Finom 2026, Financial Independence. Noted one new contradiction: Notfallfonds task confirms Consorsbank Tagesgeld exists but is currently unfunded (0 €) — the MOC Finanzen Source Detail references this account but did not specify its funded status. Updated index.md with all new pages in appropriate categories.

## [2026-06-15 21:25 UTC] ingest | raw/Privat/Finanzen/Ausgaben/Fixkosten Übersicht.md
- Pages: [[Fixkosten Übersicht Source Detail]], [[Fixkosten Übersicht]], [[VW Konsumkredit]], [[Uelzener Tierversicherung]], [[GSW Immobilien]], [[Barmenia]]
- Ingested raw/Privat/Finanzen/Ausgaben/Fixkosten Übersicht.md. Created 6 new pages: (1) Fixkosten Übersicht Source Detail [source] — full cost table with all line items, income comparison, and closed positions; (2) Fixkosten Übersicht [entity] — analysis, breakdown by category, optimization targets, risk flags, and temporal outlook; (3) VW Konsumkredit [entity] — 681.57 €/Mo loan, Restschuld 18,858 €, ends Nov 2028, financial impact analysis; (4) Uelzener Tierversicherung [entity] — 132.48 €/Mo dog insurance, optimization target with comparison providers; (5) GSW Immobilien [entity] — Oleg's landlord Auerstr. 29 Berlin, 991.09 €/Mo, §536 BGB Vorbehalt explained; (6) Updated Barmenia [entity] — added 33 €/Mo KV-Zusatz from Fixkosten Übersicht, updated sources/tags, added insurance stack context and Uelzener comparison angle. Cross-links added throughout: Consorsbank Girokonto 260809254 (existing entity, closure confirmed by this source), ARAG Wagglz Versicherung (existing entity, future saving noted), Allianz Insurance Consolidation (existing entity, RLV 31.55 €/Mo confirmed), Wagglz GmbH (existing entity, variable darlehen). No contradictions found with existing wiki content. Index updated with new Finance entities section and new source entry.

## [2026-06-15 21:26 UTC] ingest | raw/Privat/Finanzen/Ausgaben/VW Konsumkredit.md
- Pages: [[VW Konsumkredit]], [[VW Konsumkredit Source Detail]]
- Ingested raw/Privat/Finanzen/Ausgaben/VW Konsumkredit.md. Created two new pages: (1) wiki/entities/VW Konsumkredit.md — entity page with full loan details, restlaufzeit calculation, Sondertilgung decision analysis, and integration into Oleg's broader financial picture; (2) wiki/sources/VW Konsumkredit Source Detail.md — faithful source summary preserving original data and open task. Added wikilinks to MOC Finanzen, Fixkosten Übersicht, Q-Bonus Doctolib, Consorsbank Girokonto 0250120493, Schulden Übersicht, and Oleg Personal Context. Index updated with VW Konsumkredit in Entities section and VW Konsumkredit Source Detail in Sources section. No contradictions with existing wiki content found. Note: Q-Bonus Doctolib and Schulden Übersicht are forward-referenced — those pages may need creation when relevant sources are ingested.

## [2026-06-15 21:28 UTC] ingest | raw/Privat/Finanzen/Einnahmen/ALG I 2025.md
- Pages: [[ALG I 2025]], [[ALG I 2025 Source Detail]], [[ALG I Progressionsvorbehalt]]
- Ingested raw/Privat/Finanzen/Einnahmen/ALG I 2025.md. Key changes:

1. UPDATED wiki/entities/ALG I 2025.md — Added two previously unknown facts now confirmed by the new source: (a) duration 'bis ca. Juni 2025', (b) amount '~8.400 € gesamt'. Removed the [A] assumption flags for these fields. Added §46 EStG Pflichtveranlagung note (explicitly stated in source). Added reference to new source detail page. Updated sources frontmatter to include the new raw file.

2. CREATED wiki/sources/ALG I 2025 Source Detail.md — New source summary page capturing the raw document's facts, statutory references (§32b EStG, §46 EStG), required Bescheinigung, and explicit note on what this source resolves vs. the prior entity stub.

3. UPDATED wiki/concepts/ALG I Progressionsvorbehalt.md — Added §46 EStG Pflichtveranlagung note (newly confirmed from source), updated the 'Magnitude for Oleg' section to reference the now-known ~8,400 € figure instead of the prior 'not yet known' placeholder. Updated sources frontmatter. Updated practical example to use 8,400 € as the ALG I amount. Added reference to ALG I 2025 Source Detail.

4. No contradictions found with existing wiki content. The new source confirms and resolves open questions from the entity page seeded from the Wagglz GF-Gehalt source — fully consistent.

5. Updated index.md — Added ALG I 2025 Source Detail to Sources section; updated ALG I 2025 entity summary to include the now-known amount and period; updated ALG I Progressionsvorbehalt concept summary to note the ~8,400 € figure.

## [2026-06-15 21:29 UTC] ingest | raw/Privat/Finanzen/Einnahmen/Doctolib 2026.md
- Pages: [[Doctolib 2026 Source Detail]], [[Doctolib 2026]]
- Ingested raw/Privat/Finanzen/Einnahmen/Doctolib 2026.md. Created two new pages: (1) 'Doctolib 2026' entity page — employer entity for Oleg from Jan 2026, documenting salary structure (6,300 € brutto + 364 € PKW-Sachbezug, 3,638.82 € netto, Steuerklasse 1, HEK), Q1 bonus (8,533 € brutto, April 2026), Jan–Mai payroll totals (41,040 € brutto / 22,327 € netto), and full-year projection (~105,568 € brutto / ~66,416 € netto); (2) 'Doctolib 2026 Source Detail' source page — raw source transcription with detailed notes on PKW-Sachbezug tax logic, cross-references to Fixkosten Übersicht (61% netto in fixed costs), ESt 2025, Consorsbank Girokonto 0250120493, and P2 Diesen Monat. Added wikilinks to: HEK (already in wiki as entity), Fixkosten Übersicht, Consorsbank Girokonto 0250120493, ESt 2025, P2 Diesen Monat, MOC Finanzen, Oleg Personal Context, Wagglz GmbH. Updated index.md with Doctolib 2026 under Entities and Doctolib 2026 Source Detail under Sources. No contradictions found with existing wiki content — HEK is confirmed as Oleg's KV for 2026 (consistent with Doctolib employer record), and Consorsbank Girokonto 0250120493 is listed in source as salary-deposit account (consistent with existing entity page which notes this account is likely the salary-receipt account). The 61% Fixkosten ratio aligns with the Fixkosten Übersicht entity already in the wiki.

## [2026-06-15 21:32 UTC] ingest | raw/Privat/Finanzen/Konten/Consorsbank Girokonto 0250120493.md
- Pages: [[Consorsbank Girokonto 0250120493 Source Detail]], [[Consorsbank Girokonto 0250120493]], [[VW-Bank Finanzierung]], [[GSW Miete]], [[Consorsbank Tagesgeld 253403894]], [[Consorsbank Depot 1117241081]]
- Ingested raw/Privat/Finanzen/Konten/Consorsbank Girokonto 0250120493.md. Changes:

1. CREATED wiki/sources/Consorsbank Girokonto 0250120493 Source Detail.md — full source summary with IBAN (DE23760300800250120493), BIC (CSDBDE71XXX), Dispo (5.000 €), complete 2026 balance history (Jan–Mai), all regular income items (Doctolib 3.638,82 €/month, Q1 bonus 8.249,96 €, Spesenerstattungen 731,50 €), all 10 fixed outgoing line items (~2.053,29 €/month total), and 3 linked accounts (Tagesgeld 253403894, closed Girokonto 260809254, Depot 1117241081).

2. UPDATED wiki/entities/Consorsbank Girokonto 0250120493.md — significantly expanded from sparse MOC-seeded stub to full entity page with IBAN/BIC/Dispo, income table, outgoings table with 10 line items, 2026 balance history, linked accounts, and liquidity assessment. Added source to frontmatter.

3. CREATED wiki/entities/VW-Bank Finanzierung.md — new entity for the 681,57 €/month VW Bank financing debit (second-largest fixed cost); inferred ~32.700 € financed vehicle over 48 months; 8.178,84 €/year.

4. CREATED wiki/entities/GSW Miete.md — new entity for 991,09 €/month rent to GSW (state-owned Berlin housing); below-market regulated contract; strategic tension with Cyprus Relocation noted.

5. CREATED wiki/entities/Consorsbank Tagesgeld 253403894.md — new entity for linked savings account; 1,00% p.a. from 16.06.2026; below-market rate noted.

6. CREATED wiki/entities/Consorsbank Depot 1117241081.md — new entity for linked investment depot; no holdings data available.

7. No contradictions with existing wiki content found. All figures (Barmenia 33 €, Uelzener 132,48 €, Allianz PKV 22,62 €, Consorsbank 260809254 closure) are consistent with existing entity pages.

8. New data point: Doctolib net monthly salary confirmed as 3.638,82 € (previously unspecified in wiki). Q1 bonus of 8.249,96 € confirmed as net (received directly in Girokonto).

9. Updated index.md with new entries under Finance — Accounts (Tagesgeld, Depot), Finance — Costs (GSW Miete, VW-Bank), and Sources (Consorsbank Girokonto Source Detail).

## [2026-06-15 21:35 UTC] ingest | raw/Privat/Finanzen/Rehabilitation Plan.md
- Pages: [[Finanz Rehabilitation Plan]], [[Finanz Rehabilitation Plan Source Detail]], [[OK Capital UG]], [[VW Bank Kredit]]
- Ingested raw/Privat/Finanzen/Rehabilitation Plan.md. Created 4 new wiki pages:

1. **wiki/entities/Finanz Rehabilitation Plan.md** — Entity page summarizing the 3-phase plan, structural deficit mechanics, phase details, and key pending decisions. Links to Wagglz GmbH, OK Capital UG, Fixkosten Übersicht, SP STB, ESt 2025.

2. **wiki/sources/Finanz Rehabilitation Plan Source Detail.md** — Source page with all quantitative data from the document. Flags two key contradictions/gaps: (a) VW-Bank-Kredit 681,57 €/Mo not previously recorded in wiki — potential discrepancy with stated ~1.215 €/Mo fixed cost figure in Phase 3; (b) Gesellschafterdarlehen 357 €/Mo is a new specific figure.

3. **wiki/entities/OK Capital UG.md** — New entity page for OK Capital UG, previously only mentioned as a wikilink in Wagglz-related pages. Documents its role as structural cost block, pending decision (liquidation/dormancy/continuation), and known gaps.

4. **wiki/entities/VW Bank Kredit.md** — New entity page for the VW-Bank loan (681,57 €/Mo until 11/2028), previously unrecorded in wiki. Flags potential contradiction with the ~1.215 €/Mo fixed cost total stated in the rehabilitation plan (the VW loan alone is 56% of that figure).

Index updated with new Finance section entries (Finanz Rehabilitation Plan, OK Capital UG, VW Bank Kredit) and a new 'Financial Rehabilitation' cross-domain theme cluster. The source document introduces two previously unrecorded financial obligations (VW-Bank-Kredit and Gesellschafterdarlehen 357 €/Mo) that should be reconciled with the Fixkosten Übersicht pages.

## [2026-06-15 21:36 UTC] ingest | raw/Privat/Finanzen/Steuern/ALG I Progressionsvorbehalt.md
- Pages: [[ALG I Progressionsvorbehalt Source Detail]], [[ALG I Progressionsvorbehalt]]
- Ingested raw/Privat/Finanzen/Steuern/ALG I Progressionsvorbehalt.md. Created new source page 'ALG I Progressionsvorbehalt Source Detail' capturing the §32b EStG mechanics and the worked 2025 example (30,000 € taxable income + 8,400 € ALG I → ~25% rate → ~7,500 € tax vs ~5,500 € without → ~2,000 € Mehrbelastung). Updated the existing 'ALG I Progressionsvorbehalt' concept page to: (1) add the new source to its sources array, (2) incorporate a second worked example table (Example B) from the new source alongside the existing Example A, (3) add a note that SP STB is responsible for exact calculation (directly from source), (4) add wikilink to the new source detail page. No contradictions found — the new source's ~2,000 € Mehrbelastung estimate aligns with the concept page's existing illustrative example despite using a different income base (30k vs 50k). Updated index.md to add the new source page entry under Sources.

## [2026-06-15 21:38 UTC] ingest | raw/Privat/Finanzen/Steuern/ESt 2025.md
- Pages: [[ESt 2025 Source Detail]], [[ESt 2025]]
- Ingested raw/Privat/Finanzen/Steuern/ESt 2025.md. Created two new pages: (1) ESt 2025 Source Detail (source type) capturing all content from the raw file, and (2) ESt 2025 (entity type) as the canonical entity page for Oleg's 2025 income tax filing. The source was fully consistent with existing wiki pages — ALG I ~8,400 €, period until June 2025, §32b/§46 EStG mechanics, and KV providers (HEK + Barmenia) all confirm existing data without contradiction. Notable new information: Doctolib explicitly confirmed at 0 € for 2025 (starts Jan 2026); Vollständigkeitserklärung for SP STB has an earlier deadline (2026-06-20) vs other docs (2026-06-30); estimated zvE 30,000–35,000 €. Updated index.md to add ESt 2025 entity and ESt 2025 Source Detail entries under appropriate categories.

## [2026-06-15 21:45 UTC] ingest | raw/Privat/Finanzen/Templates/Claude Session – Performance.md
- Pages: [[Claude Session Template Performance]], [[Oleg Personal Context]], [[3D Body Scan Scaneca Mai 2026]], [[BMR and TDEE]]
- Ingested raw/Privat/Finanzen/Templates/Claude Session – Performance.md. Created new source page 'Claude Session Template Performance' capturing the full template structure, context block, and 5 session types. Updated 'Oleg Personal Context' entity with new data points: WHR target <0.86 (previously missing from wiki), bilateral asymmetry / rightward CoG shift (not previously captured), protein target discrepancy resolved (195-200g scan-based vs 220g operational/body-weight-based), Peter Attia explicitly added to reference framework, Hyrox primary limiter named as aerobic capacity. Updated '3D Body Scan Scaneca Mai 2026' entity to include WHR target <0.86 and bilateral asymmetry structural finding. Updated 'BMR and TDEE' concept to document the protein target discrepancy and add 220g as the operational figure. Noted one contradiction: protein target 220g (template) vs 195-200g (scan document) — both documented with methodology explanation. No existing pages deleted or contradicted beyond the protein figure clarification. Index updated with new source entry.

## [2026-06-15 21:48 UTC] ingest | raw/Privat/MOC/Finanz-Home.md
- Pages: [[Finanz-Home Dashboard Source Detail]], [[Oleg Command Center]], [[Rehabilitation Plan]], [[Oleg Personal Context]]
- Ingested raw/Privat/MOC/Finanz-Home.md (Oleg's Command Center dashboard). Created 3 new pages: (1) Finanz-Home Dashboard Source Detail — source summary with full metric analysis and cross-reference validation; (2) Oleg Command Center — entity page for the dashboard with financial severity assessment and navigation map; (3) Rehabilitation Plan — stub entity page for the 3-phase financial recovery framework (full content pending ingestion of source doc). Updated Oleg Personal Context entity to add financial metrics (net salary 3,638.82 €, structural deficit -7,970 €, overdraft -1,405 €, savings 1.10 €, April commission ~4,611 €) alongside existing body composition data — all metrics consistent with existing wiki (no contradictions found). Body composition figures (20.3% KFA, WHR 0.92, target <0.86) confirmed consistent with 3D Body Scan Scaneca Mai 2026 entries. Flagged 4 stub pages newly identified: Finanz-Übersicht, Blutbild Panel 24 Marker, Master Prompt Gesamtanalyse, and Rehabilitation Plan detail content. Updated index.md with new entries categorized under Entities (Oleg Command Center, Rehabilitation Plan, Finanz-Übersicht stub), Sources (Finanz-Home Dashboard Source Detail), and Stub Pages section.

## [2026-06-15 21:51 UTC] ingest | raw/Privat/Performance/_vault/00 Performance-Übersicht.md
- Pages: [[Performance Overview Source Detail]], [[Performance Overview]], [[Peter Attia]], [[Zone 2 Cardio]], [[Blutbild Panel]]
- Ingested raw/Privat/Performance/_vault/00 Performance-Übersicht.md. Created 5 new pages: (1) Performance Overview Source Detail [source] — full content capture including body baseline, nutrition, limitators, protocol notes, and contradiction flags on KFA target range (14–16% vs 15–17% vs 15%); (2) Performance Overview [entity] — master performance entity consolidating goals, baseline, nutrition, limitators, Zone 2+Posture unified protocol, and protocol rules; (3) Peter Attia [entity] — new stub-to-full entity for the third named reference authority (alongside Huberman and Bryan Johnson), covering ApoB, Zone 2, metabolic health, longevity medicine; (4) Zone 2 Cardio [concept] — new concept page covering physiology, Zone 2+Posture unified protocol framing, Hyrox application, Attia longevity connection, intensity guidelines; (5) Blutbild Panel [entity] — stub entity for 24-marker blood panel, noting ApoB must be separately requested. Key additions to existing wiki: ApoB note (first explicit mention), Zone 2 as unified protocol with posture correction (new synthesis), Peter Attia as named authority (first appearance), explicit weight target ~88-90 kg (new metric), KFA target discrepancy flagged (14-16% in this source vs 15-17% in scan source vs 15% in Health Protocol Master). No existing pages required modification as new pages capture all new knowledge. Index updated with all new pages.

## [2026-06-15 21:54 UTC] ingest | raw/Privat/Performance/_vault/Blutbild Panel.md
- Pages: [[Blutbild Panel]], [[Blutbild Panel Source Detail]], [[Biomarker Testing]]
- Ingested raw/Privat/Performance/_vault/Blutbild Panel.md. Key changes: (1) Upgraded Blutbild Panel entity page from stub to full entity — populated all 24 markers with longevity-optimized target ranges, quarterly schedule, Priority 1/2 split, ApoB instruction, and base supplementation protocol. (2) Created new Blutbild Panel Source Detail source page capturing the raw document content. (3) Upgraded Biomarker Testing concept page from a stub reference to a full concept page covering longevity-optimized vs standard reference ranges, marker categories, and integration with Oleg's 3-pillar tracking system. (4) Updated index.md with Blutbild Panel (entity), Biomarker Testing (concept), and Blutbild Panel Source Detail (source) entries. No contradictions found — supplement dosages are consistent with existing Supplement Stack entries; ApoB emphasis aligns with existing Peter Attia references; Vitamin D target (50–80 ng/mL) is consistent with protocol context. Minor marker count discrepancy noted (14 Priority 2 rows vs stated 13) — flagged in entity and source pages.

## [2026-06-15 21:56 UTC] ingest | raw/Privat/Performance/_vault/Hyrox Prep.md
- Pages: [[Hyrox Prep Source Detail]], [[Hyrox Competition]], [[Zone 2 Training]], [[Performance Overview]]
- Ingested raw/Privat/Performance/_vault/Hyrox Prep.md. Created 4 new pages: (1) Hyrox Prep Source Detail [source] — full protocol documentation including Zone 2 structure, 12-week milestones, structural blockers, and pending weekly protocol items; (2) Hyrox Competition [entity] — upgraded from implicit references to a full entity page consolidating competition format, Oleg's current status, preparation strategy, and structural blockers; (3) Zone 2 Training [concept] — new concept page covering Zone 2 physiology, Oleg's specific protocol parameters, sequencing rules, and relationship to Hyrox; (4) Performance Overview [entity] — created stub entity for the parent 00 Performance-Übersicht vault document referenced internally by Hyrox Prep and Blutbild Panel sources. Flagged one contradiction: Hyrox Prep source describes a 12-week plan while an existing wiki reference is to Hyrox 10-Week Training — both noted as potentially valid for different competition timelines, with 12-week plan being the more recently created document. All wikilinks cross-referenced to existing pages (3D Body Scan Scaneca Mai 2026, Forward Head Posture, Blutbild Panel, Health Protocol Master, Cold Exposure Protocols, Brick Training, Corrective Exercise, etc.). Updated index.md with new entries in Entities, Concepts, and Sources sections.

## [2026-06-15 21:59 UTC] ingest | raw/Privat/Performance/_vault/Körper & Scan.md
- Pages: [[Körper und Body Composition Scan Source Detail]], [[3D Body Scan Scaneca Mai 2026]], [[Zone 2 Training]], [[Forward Head Posture]]
- Ingested raw/Privat/Performance/_vault/Körper & Scan.md. Created: (1) 'Körper und Body Composition Scan Source Detail' source page capturing new detail from this vault document. (2) Updated '3D Body Scan Scaneca Mai 2026' entity page to incorporate new data: structural findings with Hyrox injury risk context, 14–16% KFA alternate target, explicit weight goal ~88–90 kg, Zone 2 as visceral fat priority action, forward head → breathing mechanism, same-conditions repeat scan protocol. (3) Created 'Zone 2 Training' concept page (new page, referenced in source but not previously in wiki). (4) Created/updated 'Forward Head Posture' concept page to add the breathing mechanism detail (diaphragm compression) sourced from this vault document — significant new content not in the prior stub. Key contradiction flagged: this vault note specifies KFA target 14–16% vs. 15–17% in the original scan source — both recorded with explanation. Index updated with new entries across Entities, Concepts, and Sources.

## [2026-06-15 22:00 UTC] ingest | raw/README.md
- Pages: [[Raw Vault Structure README]], [[Vault Architecture]]
- Ingested raw/README.md — a structural/meta source describing the vault's directory layout and inbox→ingest→wiki workflow. Created two new pages: (1) 'Raw Vault Structure README' (type: source) — summarizes the raw/ folder structure, maps sub-areas to their wiki equivalents, and documents the _archiv/ exclusion rule; (2) 'Vault Architecture' (type: concept) — generalizes the two-layer immutable-raw / living-wiki design pattern, documents page type hierarchy, YAML frontmatter standard, and naming conventions. Both pages are wikilinked to all relevant entities already in the wiki (Wagglz GmbH, Café Berlin Partnership Hai, Performance Coffee Brand, Cyprus Relocation, ESt 2025, Hyrox Competition, Supplement Stack, Apple Passwords, Proton Pass, and all MOC pages). Index updated with both new pages; existing entries preserved unchanged. No contradictions identified — the README is a pure structural document with no data conflicts.

## [2026-06-15 22:02 UTC] ingest | raw/data/README.md
- Pages: [[Structured Data Directory README]]
- Ingested raw/data/README.md — a minimal 3-line README for the vault's structured data directory. Created one new source page: 'Structured Data Directory README' (wiki/sources/). The README contains no substantive content beyond labeling the directory's purpose (CSV exports for Dataview/CLI: cashflow, health metrics, training logs) and a no-secrets rule. No entity or concept pages required. No contradictions with existing wiki content. Updated index.md to add the new source entry under Sources. The index was also lightly reorganized to ensure all previously existing pages visible in the wiki dump are represented — no existing entries were removed.

## [2026-06-15 22:04 UTC] ingest | raw/inbox/00-Master-Context.md
- Pages: [[Master Context Oleg Kober]], [[Oleg Personal Context]], [[OK Capital UG]], [[Cyprus Relocation]]
- Ingested raw/inbox/00-Master-Context.md. Created 4 new pages: (1) Master Context Oleg Kober [source] — full detail of the central truth document; (2) Oleg Personal Context [entity] — upgraded/replaced stub with comprehensive profile including named OK Capital UG, confirmed income figures, Cyprus downgrade, and all active priorities; (3) OK Capital UG [entity] — new entity page naming the dormant UG for the first time (previously wiki referred to it only as 'the dormant UG'); (4) Cyprus Relocation [entity] — new entity page resolving the previously flagged strategic tension with Café Berlin; explicitly downgraded to Someday/Maybe per 2026-06-13 update. Key wiki-wide updates: Cyprus/Relocation tension with Café Berlin is now resolved (café wins, relocation has no active timeline); OK Capital UG named; Doctolib income figures confirmed (3,638.82 €/month + ~4,611 €/quarter provision); Scaneca follow-up target date confirmed as 2026-09-01; no contradictions with existing wiki found except one flagged — Master Context lists OK Capital UG as dormant while earlier Café planning docs used 'GmbH (ruhend)' loosely, now clarified. Index updated with all existing and new pages, organized by Entities/Concepts/Sources/Syntheses/Comparisons.

## [2026-06-15 22:07 UTC] ingest | raw/inbox/2026-06 Finance Monthly.md
- Pages: [[Finance Monthly 2026-06 Source Detail]], [[Finanzübersicht 2026]], [[Doctolib]], [[Consorsbank]], [[OK Capital UG]]
- Ingested raw/inbox/2026-06 Finance Monthly.md. Created 5 new pages: (1) Finance Monthly 2026-06 Source Detail — full source summary with cashflow table, account snapshot, tax obligations, company obligations, and risk register; (2) Finanzübersicht 2026 — new entity page synthesizing Oleg's overall 2026 financial picture including structural deficit ~−7,970 €/year, near-zero savings (1.10 €), Consorsbank in Dispo (−1,405 €), and 10,000 € combined Jahresabschluss costs due; (3) Doctolib — new entity page for Oleg's primary employer (3,638.82 €/month netto); (4) Consorsbank — new entity page for primary private account currently in overdraft; (5) OK Capital UG — new entity page for the dormant UG with 5,000 € Jahresabschluss due and insolvency risk flagged. Key new information added to wiki: (a) structural annual deficit figure ~−7,970 € (first time quantified); (b) ALG-I-Bescheinigung deadline 2026-06-30 (additive to existing ALG I 2025 page); (c) Wagglz and OK Capital each have 5,000 € Jahresabschluss costs currently due; (d) zero savings liquidity crisis; (e) § 15a InsO GF-Haftung risk flagged. No direct contradictions with existing wiki found — source data is additive. Updated index.md with all new pages categorized under Entities (Finance), Sources (Finance), and existing structure preserved.

## [2026-06-15 22:09 UTC] ingest | raw/inbox/Cyprus Relocation Tracker.md
- Pages: [[Cyprus Relocation]], [[Cyprus Relocation Tracker Source Detail]]
- Ingested raw/inbox/Cyprus Relocation Tracker.md. Created two new pages: (1) entities/Cyprus Relocation — entity page for the paused relocation plan with full context, budget parameters, strategic tensions, and wikilinks; (2) sources/Cyprus Relocation Tracker Source Detail — source summary page. Key integrations: linked to Café Berlin Partnership Hai (pre-existing strategic tension confirmed and cross-linked), Financial Independence, Oleg Personal Context, MOC Strategie und Business, MOC Finanzen. No contradictions found with existing wiki content — the paused status is consistent with Cyprus not appearing in any existing active priority lists. Updated index.md with Cyprus Relocation entry under Entities > Business & Projects and Cyprus Relocation Tracker Source Detail under Sources > Business.

## [2026-06-15 22:18 UTC] ingest | raw/Business/PerformanceCafe/brand/naming_brief.md
- Pages: [[Performance Cafe Naming Brief]], [[Performance Coffee Brand Naming]], [[Aevum Brand]], [[Performance Coffee Brand Voice and Positioning]], [[Performance Coffee Brand Packaging Concept]]
- Ingested raw/Business/PerformanceCafe/brand/naming_brief.md. Created 5 new pages: (1) 'Performance Cafe Naming Brief' [source] — full source summary of the completed Modul 7 naming brief with all 15 candidates, domain/EUIPO analysis, positioning, and packaging specs; (2) 'Performance Coffee Brand Naming' [entity] — entity page for the naming decision process with top recommendation AEVUM and full candidate matrix; (3) 'Aevum Brand' [entity] — dedicated entity for the top-recommended brand name, etymology, IP assessment, and design implications; (4) 'Performance Coffee Brand Voice and Positioning' [concept] — brand voice framework, taglines, target audience messaging, and competitor matrix; (5) 'Performance Coffee Brand Packaging Concept' [concept] — packaging design spec, materials, color system, sachet dimensions, MOQ, and sachet manufacturer options. Updated index.md with all new pages in correct categories plus reorganized existing entries for clarity. Cross-linked to existing wiki entities: Bryan Johnson, Andrew Huberman, AG1, Alpha-GPC, L-Theanin, Ashwagandha KSM-66, Taurin, Kölner Liste, Informed Sport, NEM Konformität, CMO Sourcing Performance Coffee, Certification Roadmap Performance Coffee Brand, Amazentis, Longevity Stack Ingredients, Oleg Personal Context. No contradictions with existing wiki found — this is new brand/naming content not previously covered.

## [2026-06-16 10:30] ingest | gap-fill — alle fehlenden raw/ Quelldateien
- Erstellt: 26 neue wiki/sources/ Seiten für alle raw/.md-Dateien ohne entsprechende source page
- Neue Seiten:
  - [[GROVE Businessplan und Betriebshandbuch 2026]] — Vollständiger Businessplan (34 Sektionen)
  - [[Café Berlin Partnership Hai Raw Source]] — Ursprüngliche Kickoff-Agenda
  - [[OK Capital UG Finance Vault Source Detail]] — Holding-Stammblatt
  - [[Performance Coffee Brand Master Research Brief]] — 9-Modul Forschungsauftrag
  - [[Performance Coffee Brand Longevity Science Source Detail]] — Modul 0
  - [[Performance Coffee Brand Ingredienzen Datenbank]] — Modul 1
  - [[Performance Coffee Brand Kaffee-Spezifikation]] — Modul 2
  - [[Performance Coffee Brand Marktanalyse]] — Modul 3
  - [[Performance Coffee Brand Prototyp Partner Source Detail]] — Modul 4
  - [[Performance Coffee Brand Regulatorik Report]] — Modul 5
  - [[Performance Coffee Brand Business Case]] — Modul 6
  - [[Performance Coffee Brand IP und Patent-Landschaft]] — Modul 8
  - [[Performance Coffee Brand Supplier List]] — Ops Lieferantenliste
  - [[Wagglz Finom 2026 Source Detail]] — Wagglz Finom-Konto 2026
  - [[Cyprus Relocation Source Detail]] — Zypern Strategie-Dokument
  - [[Cyprus Relocation Tracker Privat Source Detail]] — Kurznotiz pausiert
  - [[Privat Finanz-Übersicht Source Detail]] — Überblick Privatfinanzen
  - [[Finanzielle Gesamtanalyse Oleg Kober 2025-2026]] — Vollständige Analyse Juni 2026
  - [[Master Prompt Gesamtfinanzanalyse Source Detail]] — Analyse-Prompt-Template
  - [[Claude Session Finanzen Template]] — Kurzformat Finance-Session-Template
  - [[MOC Performance und Leben Source Detail]] — Navigation Performance-Bereich
  - [[MOC Tech und Setup Source Detail]] — Navigation Tech-Bereich
  - [[Health Protocol Master Source Detail]] — 6-Tage-Split, 2.800 kcal, Tagesstruktur
  - [[Allianz Versicherungskonsolidierung Privat Source Detail]] — Privates Versicherungsdokument
  - [[Offene Actions Inbox Source Detail]] — Privater Action-Tracker (inbox)
  - [[Inbox 2026-06-13 Source Detail]] — Leere Inbox-Placeholder-Datei
- Aktualisiert: wiki/index.md (Sections erweitert: Health, Finance, Business, Relocation, Inbox)
- Notizen: Einige Seiten decken Dateien ab die unter neuem Vault-Pfad leben, während ältere wiki sources noch auf alte Pfade verweisen (01-Strategie-Business/ etc.)

## [2026-06-16 12:20] update | GROVE → Performance Coffee Brand pivot dokumentiert
- Updated: [[Café Berlin Partnership Hai]] — Status-Update: physisches Café-Konzept GROVE ersetzt durch Performance Coffee Brand
- Updated: [[Performance Coffee Brand]] — GROVE-Pivot-Kontext ergänzt
- Notes: GROVE-Businessplan (cafe_masterplan_2026.md) bleibt als Referenz erhalten, ist aber archiviert

## [2026-06-19 19:37 UTC] ingest | raw/Business/Cafe/cafe_masterplan_2026.md
- Pages: [[GROVE Businessplan Source Detail]], [[GROVE Businessplan und Betriebshandbuch 2026]], [[Vietnamese Coffee GROVE]], [[ROYCE Nama Schokolade]], [[GROVE Cashflow Trigger System]], [[GROVE Revenue Streams]], [[GROVE Sessions External]]
- Ingested GROVE Businessplan 2026 (cafe_masterplan_2026.md) — created source summary, updated GROVE Businessplan entity, created new entities for Wagglz GmbH context, GROVE Revenue Streams, Vietnamese Coffee concept, ROYCE Nama Schokolade, Espresso Club Radio reference, and Cashflow Trigger System; updated index.

## [2026-06-19 19:43 UTC] ingest | raw/Business/PerformanceCafe/legal/ip_landscape.md
- Pages: [[Performance Café IP Landscape Modul 8]], [[Amazentis]], [[Timeline Nutrition]], [[Chromadex Niagen Bioscience]], [[NMN EU Status 2026]], [[Urolithin A]]
- Ingested Performance Café IP & Patent Landscape (Modul 8) — created source summary page, updated Amazentis entity with full patent detail, created new entities for Chromadex/Niagen Bioscience and NMN EU Status, created concept pages for EU Novel Food Regulation, EUIPO Trademark Strategy, Trade Secret Strategy, GmbH IP Structure, and IP Risk Matrix; updated index with all new pages.

## [2026-06-19 19:48 UTC] ingest | raw/Business/PerformanceCafe/ops/supplier_list.md
- Pages: [[Performance Cafe Supplier List]], [[Ingredient Suppliers Performance Coffee]], [[Prinova]], [[Lehvoss Nutrition]], [[Nutri-Epitech]], [[Aidea]], [[Herbafit]], [[Queisser Pharma]], [[ESB Naturkost]], [[Constantia Flexibles]], [[Flavorist Services Performance Coffee]], [[Schutzgas-Versiegelung]]
- Ingested Performance Coffee Brand supplier list (raw/Business/PerformanceCafe/ops/supplier_list.md) — created source summary page and updated/created entity/concept pages for CMO suppliers, ingredient suppliers, analysis labs, and flavorists; linked to existing Performance Coffee Brand wiki pages.

## [2026-06-19 19:53 UTC] ingest | raw/Business/PerformanceCafe/research/00_master_brief.md
- Pages: [[Performance Cafe Master Brief Source Detail]], [[Performance Coffee Brand]], [[Performance Cafe Research Team Roles]], [[Longevity Stack Ingredients]]
- Ingested Performance Café Master Research Brief (00_master_brief.md) — created source summary page and updated Performance Coffee Brand entity with full 9-module research structure, team roles, and module-to-file mapping.

## [2026-06-19 19:58 UTC] ingest | raw/Business/PerformanceCafe/research/01_longevity_science.md
- Pages: [[Longevity Science Research Modul 0]], [[Hallmarks of Aging]], [[Chlorogenic Acid]], [[Trigonellin]]
- Ingested raw/Business/PerformanceCafe/research/01_longevity_science.md — created source summary page, plus entity/concept pages for Longevity Hallmarks of Aging, Chlorogensäure, Trigonellin, Cafestol/Kahweol, DTC Biomarker Tests DACH, and Longevity Science Kaffee Stack; updated index.

## [2026-06-19 20:03 UTC] ingest | raw/Business/PerformanceCafe/research/02_ingredienzen_db.md
- Pages: [[Performance Cafe Ingredienzen Datenbank]]
- Ingested Performance Café Ingredienzen-Datenbank (Modul 1) — created source summary + 15 new entity/concept pages covering all major ingredient categories, SKU formulations, regulatory blockers (NMN, Urolithin A), and the Blueprint Coffee hypothetical stack; updated Bryan Johnson entity with 2026 stack details; flagged multiple regulatory status items as wiki-searchable concepts.

## [2026-06-19 20:08 UTC] ingest | raw/Business/PerformanceCafe/research/03_kaffee_specs.md
- Pages: [[Kaffee Spezifikation Modul 2]], [[Chlorogenic Acid]], [[Trigonellin NAD Precursor]], [[Coffee Roast Profile Longevity]], [[Coffee Extraction Methods Instant]], [[Coffee Blend Ratios]]
- Ingested Performance Café Modul 2 (Kaffee-Spezifikation): created source summary + 8 new entity/concept pages covering Robusta vs. Arabica, Vietnamese Robusta sourcing, chlorogenic acid, trigonellin, roasting profiles, and instant extraction methods; updated index.

## [2026-06-19 20:13 UTC] ingest | raw/Business/PerformanceCafe/research/04_marktanalyse.md
- Pages: [[Performance Cafe Marktanalyse Source Detail]], [[Blueprint by Bryan Johnson]], [[Bryan Johnson]], [[Four Sigmatic]], [[RYZE Mushroom Coffee]], [[MUDWTR]], [[Bulletproof Coffee]], [[Clevr Blends]]
- Ingested Performance Café market analysis (04_marktanalyse.md) — created source summary, updated Bryan Johnson entity, created new entities for Blueprint, Four Sigmatic, RYZE, MUD\WTR, Timeline Nutrition (update), key market concept pages, and pricing analysis; updated index.

## [2026-06-20 12:00] ingest | raw/inbox/supplement-stack-update-2026-06-20.md
- Updated: [[Supplement Stack]]
- Notes: Stack-Update per Nutzerangabe — Momentous: Protein Isolat, Kreatin, Magnesium, Collagen, Omega-3; Thorne: Vitamin D3 Drops, Zinc Picolinat 30mg. Collagen war zuvor explizit ausgeschlossen → Contradictions-Sektion hinzugefügt. Thorne Zinc Picolinat 30mg neu. D3 von Eigenvorrat auf Thorne D3 Drops gewechselt. Status von Sulforaphane, Alpha-GPC, L-Tyrosine unbestätigt.

## [2026-06-20 12:30] ingest | Momentous Scientific Advisors (Screenshot)
- Erstellt: [[Andy Galpin]], [[Kelly Starrett]], [[Stacy Sims]], [[Dan Garner]]
- Aktualisiert: [[Supplement Stack]] — Wissenschaftliche Referenzen-Tabelle erweitert
- Notes: Momentous Scientific Advisory Board dokumentiert — 6 Experten (Huberman, Galpin, Starrett, Sims, Garner, McDaniel) als Referenzen für Olegs Stack; Brandon McDaniel (MLB VP Player Performance) fehlt noch als eigene Entity

## [2026-06-20 20:00] query | "32 Tricks Claude Code — was fehlt noch?"
- Quelle: Clippings/32 Tricks to Level Up Claude Code in 16 Mins.md (YouTube, Nate Herk)
- Output: outputs/notes/2026-06-20-claude-code-32-tricks-audit.html (Apple-Stil)
- Befund: 21 umgesetzt/verfügbar, 3 echte Lücken (Custom Skills, CLAUDE.md schlanker+routen, Permissions Allow/Deny), 5 optional (Coding), 3 nicht relevant
- Supplement Stack: deutsche Übersetzung mit 2026-06-20-Update + Scientific-References-Tabelle (Galpin/Starrett/Sims/Garner/McDaniel) re-integriert nach Rebase-Verlust
## [2026-06-21] todo | Wagglz Setup
- TODO: Supabase Projekt in Frankfurt (eu-west-1) erstellen + .env.local befüllen → App lokal testen

## [2026-06-25 21:45] ingest | raw/raw/Business/Wagglz/ + raw/Business/Wagglz/ + Clippings/
- Neue raw-Dateien von lokalem Mac gepusht (nach längerem git-Merge-Prozess)
- Created: [[Wagglz Wettbewerber Source Detail]], [[Voisa AI]]
- Updated: [[wiki/index.md]]
- Neue Quellen vorhanden aber noch nicht vollständig ingested (API-Key fehlt in dieser Umgebung):
  - raw/raw/Business/Wagglz/Design/ (Figma-Manifeste)
  - raw/raw/Business/PerformanceCafe/ (vollständige Recherche)
  - Clippings/ (17 Claude Code Tutorial-Videos)
  - raw/Archiv/ + raw/Archiv Kopie/ (Screenshots)
  - raw/Wagglz/ (Logomark, Presentation Templates)
- Notes: raw/raw/ = alter Vault-Inhalt vor Reorganisation; vollständig verfügbar

## [2026-06-25 20:36 UTC] ingest | raw/inbox/supplement-stack-update-2026-06-20.md
- Pages: [[Supplement Stack Update 2026-06-20]], [[Supplement Stack]], [[Momentous]], [[Thorne]], [[Zinc Picolinate]], [[Collagen]], [[Vitamin D3]], [[Whey Protein Isolate]], [[Creatine Monohydrate]], [[Magnesium]]
- Supplement Stack Update 2026-06-20 ingested: Oleg's current stack updated to Momentous (Protein Isolate, Creatine, Magnesium, Collagen, Omega-3) + Thorne (Vitamin D3 Drops, Zinc Picolinate 30mg); Collagen contradiction flagged (previously "not currently needed"); Alpha-GPC, L-Tyrosine, Sulforaphane, Apigenin, L-Theanin status now unclear; new entity pages for Momentous, Thorne, Zinc Picolinate created; Supplement Stack entity and source page updated.

## [2026-06-25 20:38 UTC] ingest | raw/raw/Business/Cafe/Café Berlin — Partnership Hai.md
- Pages: [[Café Berlin Co-Founder Venture]], [[Hai]], [[Co-Founder Café Modell]], [[Gaststättenrecht Berlin]], [[Café Berlin Partnership Hai Source Detail]]
- Neue Quelle "Café Berlin — Partnership mit Hai" ingested: Entitätsseite für das Café-Berlin-Co-Founder-Venture (Oleg + Hai) erstellt, Quelldokument-Seite angelegt, Konzeptseite für Co-Founder-Café-Venture erstellt, Index aktualisiert.

## [2026-06-25 20:43 UTC] ingest | raw/raw/Business/Cafe/cafe_masterplan_2026.md
- Pages: [[GROVE Businessplan 2026 Source Detail]], [[GROVE Café]], [[GROVE TagNacht-Konzept]], [[KfW StartGeld ERP 067]], [[Vietnamese Coffee Phin-Filter]], [[Wagglz GmbH]]
- GROVE Café Businessplan (Wagglz GmbH, Juni 2026) vollständig ingested: Source-Seite, Entity-Seiten für GROVE, Wagglz GmbH, Oleg Kober, Hai Tran sowie Konzept-Seiten für Café Tag/Nacht-Konzept und KfW StartGeld erstellt; Index erweitert.

## [2026-06-25 20:46 UTC] ingest | raw/raw/Business/Fashion-Brand/Fashion Brand Suppliers.md
- Pages: [[Fashion Brand Suppliers Source Detail]], [[Fashion Brand Lieferanten]], [[Mended]], [[AS Colour]], [[Stanley Stella]], [[Arsonists]], [[Mr. Socks]]
- Neue Quelldatei "Fashion Brand Suppliers" ingested: Quelldokument-Seite erstellt, Entitätsseiten für Mended, AS Colour, Stanley/Stella, Arsonists und Mr. Socks erstellt, Konzeptseite "Fashion Brand Lieferanten" erstellt, Index aktualisiert.

## [2026-06-25 20:47 UTC] ingest | raw/raw/Business/Fashion-Brand/README.md
- Pages: [[Fashion Brand README Source Detail]], [[Fashion Brand]]
- Neue Fashion-Brand-README-Quelldatei ingested: Source-Summary-Seite erstellt; Fashion Brand-Entität und Index aktualisiert. Keine Widersprüche mit bestehenden Wiki-Inhalten gefunden.

## [2026-06-25 20:50 UTC] ingest | raw/raw/Business/MOC/MOC Strategie & Business.md
- Pages: [[MOC Strategie und Business Source]], [[MOC Strategie und Business]], [[Café Berlin Partnership Hai]], [[Café Berlin Solo Analyse]], [[Cyprus Relocation]], [[DoktorLib Automation Pipeline]]
- Ingested MOC Strategie & Business: created source summary page, entity pages for MOC Strategie und Business, Café Berlin Partnership Hai, Cyprus Relocation, DoktorLib Automation Pipeline; updated Fashion Brand entities to reflect discontinued status; confirmed Allianz Insurance Consolidation archival contradiction; updated index.

## [2026-06-25 20:51 UTC] ingest | raw/raw/Business/OK-Capital/Finanzen/Konten/OK Capital Finom 2026.md
- Pages: [[OK Capital Finom 2026 Source Detail]], [[OK Capital Finom 2026]], [[OK Capital UG]]
- Neue Quelldatei OK Capital Finom 2026 eingelesen: Quell-Zusammenfassungsseite erstellt, Entitätsseite für OK Capital Finom 2026 Konto erstellt, OK Capital UG-Seite als Stub aktualisiert, Index erweitert.

## [2026-06-25 20:53 UTC] ingest | raw/raw/Business/OK-Capital/OK Capital UG — Finance Vault.md
- Pages: [[OK Capital UG Finance Vault]], [[OK Capital UG]]
- OK Capital UG (haftungsbeschränkt) ingested: Quell-Zusammenfassungsseite erstellt, Entitätsseite erstellt, bestehende Wagglz-Entität verlinkt, Index aktualisiert.

## [2026-06-25 20:55 UTC] ingest | raw/raw/Business/OK-Capital/OK Capital UG.md
- Pages: [[OK Capital UG]], [[OK Capital UG Source Detail]]
- Neue Quelldatei OK Capital UG.md eingelesen — Entitätsseite für OK Capital UG erstellt, Entitätsseite für Oleg Personal Context als Holding-Kontext verknüpft, Index aktualisiert.

## [2026-06-25 20:57 UTC] ingest | raw/raw/Business/OK-Capital/Rangrücktritt §15a InsO.md
- Pages: [[Rangrücktritt §15a InsO Source Detail]], [[Rangrücktritt Insolvenzrecht]], [[Rangrücktritt §15a InsO Wagglz]]
- Neue Seiten erstellt: Rangrücktritt §15a InsO (source + entity + concept) für Wagglz GmbH — Insolvenzrecht, Überschuldungsprüfung §19 InsO, Insolvenzantragspflicht §15a InsO, persönliche Strafbarkeit Oleg als GF; Verlinkung mit bestehenden Wagglz-Entitäten.

## [2026-06-25 21:01 UTC] ingest | raw/raw/Business/PerformanceCafe/CLAUDE.md
- Pages: [[Performance Coffee Brand CLAUDE Source Detail]], [[Performance Coffee Brand]], [[Oleg Personal Context]]
- Neue Quelldatei `raw/Business/PerformanceCafe/CLAUDE.md` ingested: Performance Coffee Brand Projektkontext-Seite erstellt, Oleg Personal Context aktualisiert, Index erweitert.

## [2026-06-25 21:03 UTC] ingest | raw/raw/Business/PerformanceCafe/README.md
- Pages: [[Performance Cafe README Source Detail]], [[Performance Coffee Brand]]
- Performance Café README.md ingested: Created source summary page and updated/created entity pages for Performance Coffee Brand (project setup), with critical blocker table, file structure, and workflow details linked to existing wiki entities.

## [2026-06-25 21:07 UTC] ingest | raw/raw/Business/PerformanceCafe/TODO.md
- Pages: [[Performance Coffee Brand TODO Source Detail]], [[Performance Coffee Brand]], [[Wagglz GmbH]], [[Performance Coffee Brand Roadmap]], [[NMN EU Novel Food Status]]
- Performance Coffee Brand TODO.md ingested: Neue Source-Seite erstellt, Wagglz GmbH Entity aktualisiert, Performance Coffee Brand Entity aktualisiert, Budget-Übersicht und Phasen-Roadmap dokumentiert, Index erweitert.

## [2026-06-25 21:12 UTC] ingest | raw/raw/Business/PerformanceCafe/brand/naming_brief.md
- Pages: [[Performance Cafe Naming Brief]], [[Performance Coffee Naming Candidates]], [[Performance Coffee Brand Voice]], [[Performance Coffee Taglines]], [[Performance Coffee Packaging]]
- Ingested Performance Café Naming Brief (Modul 7, 2026-06-14): created source page, updated Aevum Brand entity with packaging/positioning details, created new concept pages for Performance Coffee Brand Voice, Performance Coffee Taglines, and Performance Coffee Packaging; updated index.

## [2026-06-25 21:16 UTC] ingest | raw/raw/Business/PerformanceCafe/brand/positioning.md
- Pages: [[Performance Cafe Brand Positioning Source Detail]], [[Performance Coffee Brand Positioning]], [[Performance Coffee Brand Voice]], [[Performance Coffee Brand Zielgruppen]], [[Performance Coffee Brand Pricing]], [[Performance Coffee Brand Wettbewerbsmatrix]]
- Brand Positioning für Performance Coffee Brand (positioning.md) eingelesen — neue Source-Seite erstellt, Performance Coffee Brand Entity aktualisiert, neue Konzeptseiten für Brand Voice, Zielgruppen-Segmente und Pricing-Story angelegt; index.md erweitert.

## [2026-06-25 21:18 UTC] ingest | raw/raw/Business/PerformanceCafe/hai-fragen.md
- Pages: [[Hai Fragen Performance Coffee Source Detail]], [[Hai (Co-Founder Kandidat)]]
- Neue Quelldatei `raw/Business/PerformanceCafe/hai-fragen.md` ingested: Due-Diligence-Fragenkatalog für den potenziellen Co-Founder „Hai" der Performance Coffee Brand — deckt Produkt-Know-how, Netzwerk, operative Rolle, Kapital, Gesellschaftsstruktur und Produkt-Vision ab. Neue Quelldokument-Seite erstellt, Hai-Entitätsseite erstellt, Performance Coffee Brand-Entität aktualisiert, Index ergänzt.

## [2026-06-25 21:20 UTC] ingest | raw/raw/Business/PerformanceCafe/hai-onepager.md
- Pages: [[Hai Onepager Performance Coffee Brand Source Detail]], [[Performance Coffee Brand]]
- Neue Quelldatei `raw/Business/PerformanceCafe/hai-onepager.md` ingested: Quelldokument-Seite erstellt, Performance Coffee Brand Entität aktualisiert (Budget, Gesellschaft, GTM, Namenskandidaten, Zielpreis, Contribution Margin, Break-Even), neue Konzeptseiten für Wagglz GmbH als Vehikel und Hyrox als GTM-Kanal verlinkt, Index erweitert.

## [2026-06-25 21:23 UTC] ingest | raw/raw/Business/PerformanceCafe/legal/entity_structure.md
- Pages: [[Performance Coffee Brand Gesellschaftsstruktur Source Detail]], [[Performance Coffee Brand Gesellschaftsstruktur]], [[OK Capital]], [[Hai]]
- Neue Quelle `raw/Business/PerformanceCafe/legal/entity_structure.md` eingelesen: Gesellschaftsstruktur der Performance Coffee Brand (UG→GmbH-Pfad, 50/50 Oleg/Hai, Vesting, IP-Struktur via OK Capital, EUIPO-Anmeldung, AEVUM als Top-Namenskandidat) — neue Source-Seite, neue Entity-Seiten für OK Capital, Hai und Performance Coffee Brand Gesellschaftsstruktur erstellt; Index aktualisiert.

## [2026-06-25 21:28 UTC] ingest | raw/raw/Business/PerformanceCafe/legal/ip_landscape.md
- Pages: [[Performance Café IP Landscape Modul 8 Source]], [[Niagen Bioscience]], [[Performance Café EUIPO Markenschutz]], [[NMN EU-Status]]
- IP-Landschaft Modul 8 für Performance Café ingested: neue Quellseite erstellt, bestehende Amazentis-Entität aktualisiert, neue Entitäten für Niagen Bioscience, EUIPO-Markenanmeldung, NMN EU-Status, IP-Risikoübersicht erstellt; Index aktualisiert.

## [2026-06-25 21:32 UTC] ingest | raw/raw/Business/PerformanceCafe/ops/certification_roadmap.md
- Pages: [[Zertifizierungs-Roadmap Performance Coffee]], [[Kölner Liste]], [[Informed Sport]], [[NSF Certified for Sport]], [[NEM-Konformität Performance Coffee]], [[EFSA Health Claims]]
- Neue Quelle `certification_roadmap.md` eingelesen: Zertifizierungs-Roadmap für Performance Coffee Brand (Kölner Liste, Informed Sport, NSF Certified for Sport) sowie NEM-Konformität und EFSA-Werberichtlinien — neue Seiten für Quelldokument, Kölner Liste, Informed Sport, NSF Certified for Sport und NEM-Konformität erstellt; Performance Coffee Brand-Entität um Zertifizierungskontext erweitert.

## [2026-06-26 07:11 UTC] ingest | raw/raw/Business/PerformanceCafe/ops/cmo-email-template.md
- Pages: [[CMO Erstkontakt Email Template]], [[Prinova]], [[Lehvoss Nutrition]], [[Nutri-Epitech]], [[Herbafit]], [[Aidea]], [[NAC]], [[CMO Kandidaten Vergleich]]
- Neue Quelldatei `cmo-email-template.md` eingelesen: E-Mail-Vorlage für CMO-Erstkontakt mit Priorisierungsliste (Prinova, Lehvoss, Nutri-Epitech, Aidea, Herbafit) — NAC-Stack-Hinweis neu, bestehende Aidea-Seite aktualisiert, neue Seiten für Prinova, Lehvoss Nutrition, Nutri-Epitech und Herbafit erstellt, CMO Erstkontakt Email Template als Source-Seite angelegt.

## [2026-06-26 07:15 UTC] ingest | raw/raw/Business/PerformanceCafe/ops/supplier_list.md
- Pages: [[Performance Cafe Supplier List Source Detail]], [[NAC Geruchsmaskierung]], [[Queisser Pharma]], [[Herbafit]], [[Prinova]], [[Lehvoss Nutrition]], [[Nutri-Epitech]], [[ESB Naturkost]], [[Neumann Kaffee Gruppe]], [[Sievert Storey]], [[Coffee Circle B2B]], [[Trung Nguyen Export]]
- Neue Quelldatei `raw/Business/PerformanceCafe/ops/supplier_list.md` ingested: Lieferantenliste Performance Coffee Brand mit CMOs (DACH+EU), Rohstoff-Lieferanten (Kaffee-Basis + funktionelle Inhaltsstoffe + Packaging), Analyse-Labore und Flavoristen. Neue Entitäts-Seiten für alle noch nicht im Wiki erfassten Lieferanten erstellt; bestehende Seiten (Aidea) aktualisiert; Konzeptseite für NAC-Maskierung und Überblicksseite für die Supplier List als Source-Seite angelegt.

## [2026-06-26 07:18 UTC] ingest | raw/raw/Business/PerformanceCafe/research/00_master_brief.md
- Pages: [[Performance Coffee Master Research Brief Source]], [[Performance Coffee Master Research Brief]], [[Performance Coffee Brand]]
- Master Research Prompt für Performance Café (00_master_brief.md) eingelesen — neue Source-Seite erstellt; Performance Coffee Brand Entity und relevante Konzept-Seiten aktualisiert/erstellt; Index erweitert.

## [2026-06-26 07:23 UTC] ingest | raw/raw/Business/PerformanceCafe/research/01_longevity_science.md
- Pages: [[Longevity Science Source Detail]], [[Longevity Science Grundlagen]], [[Hallmarks of Aging]], [[Chlorogensäure]], [[Trigonellin]]
- Neue Quelle `raw/Business/PerformanceCafe/research/01_longevity_science.md` aufgenommen: Longevity Science Grundlagen für die Performance Coffee Brand — 12 Hallmarks of Aging, Chlorogensäure, Trigonellin/NAD+-Pathway, Cafestol/Kahweol, Epidemiologie Kaffee/Mortalität, Biomarker-Profil und DACH-DTC-Testanbieter. Neue Seiten: Source-Zusammenfassung, Konzeptseiten für Hallmarks of Aging, Chlorogensäure, Trigonellin, Cafestol/Kahweol, Inflammaging; Entitätsseiten für Cerascreen und Longevity Science Grundlagen; Index aktualisiert.

## [2026-06-26 07:28 UTC] ingest | raw/raw/Business/PerformanceCafe/research/02_ingredienzen_db.md
- Pages: [[Performance Café Ingredienzen Datenbank Source Detail]]
- Ingredienzen-Datenbank für Performance Café (Modul 1) ingested: 40+ Inhaltsstoffe mit EU-Status, Hitzestabilität, COGS und Blueprint-Status; 3 SKU-Varianten dokumentiert; neue Entity-Seiten für Kerninhaltsstoffe (Taurin, L-Theanin, Kreatin, Spermidine, Lion's Mane, Cordyceps, Reishi, NMN, Urolithin A, Quercetin, Fisetin, Curcumin, NAC, Trigonellin) sowie Konzeptseiten für Koffein-Theanin-Ratio, Ashwagandha KSM-66 vs. Sensoril Vergleich, Hitzestabilität-Klassifikation; Master Stack Top 10 und SKU-Übersicht als Synthese; Index erweitert.

## [2026-06-26 07:33 UTC] ingest | raw/raw/Business/PerformanceCafe/research/03_kaffee_specs.md
- Pages: [[Performance Cafe Kaffee Spezifikation Source Detail]], [[Chlorogensäure]], [[Trigonellin]]
- Neue Quelldatei 03_kaffee_specs.md für Performance Coffee Brand ingested: Kaffee-Spezifikationsseite erstellt (Robusta vs. Arabica, Vietnamesischer Robusta S18, Röstgrade, Instant-Extraktionsverfahren, Blend-Empfehlung 60/40, Sourcing-Kontakte DACH/EU), plus neue Entitäten für Chlorogensäure, Trigonellin, Vietnamesischer Robusta S18, Freeze-Dried Instant Coffee, und ergänzende Sourcing-Entitäten (Vietnam Rohkaffee Berlin, Bernhard Rothfos, Sucafina, Kaffeekraftwerk Berlin, The Barn Coffee Roasters).

## [2026-06-26 07:38 UTC] ingest | raw/raw/Business/PerformanceCafe/research/04_marktanalyse.md
- Pages: [[Performance Cafe Marktanalyse Source Detail]], [[Blueprint by Bryan Johnson]], [[Four Sigmatic]], [[RYZE Mushroom Coffee]], [[MUDWTR]], [[Clevr Blends]], [[Bulletproof Coffee]]
- Marktanalyse Performance Café (Modul 3) vollständig integriert: Neue Source-Seite erstellt, Blueprint-Entität aktualisiert, neue Entitäten für Wettbewerber (Four Sigmatic, RYZE, MUD\WTR, Clevr Blends, Bulletproof, Timeline Nutrition, Tru Niagen, Purovitalis, DoNotAge, Qualia Senolytic) angelegt, neue Konzeptseiten für Functional Coffee White Space, Pricing Strategy und Marktgröße erstellt, Index erweitert.

## [2026-06-26 07:43 UTC] ingest | raw/raw/Business/PerformanceCafe/research/05_prototyp_partner.md
- Pages: [[Performance Café Prototyp Partner Source Detail]], [[OH!S]], [[Goerlich Pharma GmbH]], [[sanotact GmbH]], [[SternMaid GmbH]], [[Döhler GmbH]], [[Hawlik BioImport GmbH]]
- Neue Quelle "Prototyp-Partner Performance Café" (Modul 4) eingelesen: CMO-Strategie (OH!S, Goerlich Pharma, sanotact, SternMaid, Döhler), Analytik-Labore (Eurofins, SGS Fresenius, CePreDo/Kölner Liste), Pilzextrakt-Lieferanten (Hawlik BioImport, Functional Mushrooms EU, MUSHEEZ) und 4 Formulierungsherausforderungen (NAC-Geruch, Curcumin-Löslichkeit, NMN/NR-Oxidation, Pilzextrakt-Qualität) mit konkreten Lösungen und Partnern (IFF/NovaSOL, Indena/Meriva, MoleQlar, Symrise) erfasst; 12 neue Wiki-Seiten erstellt/erweitert.

## [2026-06-26 07:48 UTC] ingest | raw/raw/Business/PerformanceCafe/research/06_regulatorik.md
- Pages: [[Performance Cafe Regulatorik Source Detail]], [[Performance Cafe Regulatorischer Pfad]], [[Novel Food Status Vergleich Performance Cafe]]
- Regulatorik-Report für Performance Café (Modul 5, 2026-06-14) eingespeist: Novel Food Status (NMN, Urolithin A, Spermidine, NR, Fisetin, Huperzin A), Patent-Landschaft (Amazentis, ChromaDex/Niagen Bioscience, NMN), Zertifizierungs-Roadmap (Kölner Liste, Informed Sport), EFSA Health Claims und kritischer regulatorischer Pfad für EU/DACH-Launch.

## [2026-06-26 07:53 UTC] ingest | raw/raw/Business/PerformanceCafe/research/07_business_case.md
- Pages: [[Performance Coffee Business Case Source Detail]], [[Hai Partner Performance Café]], [[Performance Coffee Business Case]], [[COGS Performance Café]]
- Business Case Performance Café (Modul 6) ingested: Neue Source-Seite, neue/aktualisierte Entity-Seiten für Performance Coffee Business Case, Hai (Partner), Funding DACH, Gesellschaftsstruktur; Index erweitert.

## [2026-06-26 07:54 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-25-b2b-software.md
- Pages: [[25 B2B Software Figma Manifest]]
- Neue Quellseite erstellt: Figma-Manifest 25 B2B Software (Wagglz/Wufflz Design-Datei, Figma-Key NO7zf85jnhjIcJ13QGyESY, Status: Fehler/ausstehend, keine Frames exportiert); Index aktualisiert unter Wagglz/Design-Bereich.

## [2026-06-26 07:56 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-25-wufflz-wireframes.md
- Pages: [[25 Wufflz Wireframes Figma Manifest]]
- Neue Quellseite "25 Wufflz Wireframes Figma Manifest" erstellt; bestehende Wagglz/Wufflz-Entitäten verlinkt; Index aktualisiert.

## [2026-06-26 07:57 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-pitch-deck-investoren-v1.md
- Pages: [[Pitch Deck Investoren v1 Figma Manifest]]
- Neue Quelldatei "Pitch Deck Investoren v1" (Figma, File Key 5Fp2RQjupexSkR1eFe638X) ingested: Source-Seite erstellt, Wagglz-Entität und Index aktualisiert.

## [2026-06-26 07:58 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-pitch-deck-investoren-v2.md
- Pages: [[Pitch Deck Investoren v2 Figma Manifest]]
- Neue Quellseite "Pitch Deck Investoren v2 Figma Manifest" erstellt und Index aktualisiert — Figma-Datei FnhmUL3cHzDIM2HOFF2306, Kategorie pitch, API-Fehler 403, keine Frames exportiert.

## [2026-06-26 07:59 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-pitch-deck-investoren-v3.md
- Pages: [[Pitch Deck Investoren v3 Figma Manifest]]
- Neue Quelldatei "Pitch Deck Investoren v3 Figma Manifest" für Wagglz/Wufflz ingested — Quellseite erstellt und Index aktualisiert; keine Widersprüche zu bestehenden Seiten.

## [2026-06-26 08:01 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-pitch-deck-wufflz-gmbh-editor-banken.md
- Pages: [[Pitch Deck Wufflz GmbH Editor Banken Figma Manifest]]
- Neue Quellseite für Pitch Deck Wufflz GmbH Editor Banken (Figma File Key X9DzUUoJwilVPOlkqLiI2b) angelegt — API-Fehler 403, keine Frames exportiert, canonical in 10-Dateien-Migrationsliste; Index aktualisiert.

## [2026-06-26 08:02 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-proto-txernzeob.md
- Pages: [[Proto TXErnZeob Figma Manifest]]
- Neue Quellseite für Proto TXErnZeob Figma Manifest erstellt; Index um Wagglz-Design-Eintrag ergänzt.

## [2026-06-26 08:03 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-wufflz-cvs.md
- Pages: [[Wufflz CVs Figma Manifest]]
- Neue Quellseite für Wufflz CVs Figma Manifest (NmlKQIeKhRJiPzIMTDmCN3) erstellt; Index um Eintrag unter Sources/Wagglz-Design erweitert.

## [2026-06-26 08:04 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-wufflz-pitchdeck-template.md
- Pages: [[Wufflz PitchDeck Template Figma Manifest]]
- Neue Quellseite für Wufflz PitchDeck Template Figma-Manifest erstellt; Index aktualisiert.

## [2026-06-26 08:06 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-wufflz-website-design-copy.md
- Pages: [[Wufflz Website Design Copy Figma Manifest]]
- Neue Quellseite für Wufflz Website Design (Copy) Figma-Duplikat erstellt; Index aktualisiert mit neuem Eintrag unter Sources/Wagglz-Design.

## [2026-06-26 08:08 UTC] ingest | raw/raw/Business/Wagglz/Design/Figma-Manifest-wufflz-website-design-dogwalking.md
- Pages: [[Wufflz Website Design Dogwalking Figma Manifest]]
- Neue Quelldatei "Wufflz Website Design Dogwalking Figma Manifest" (File Key r8locNzgmU9mw67i5xBiRT) ingested — Quelldokumentseite erstellt; Index aktualisiert; verknüpft mit Wagglz GmbH, Wufflz und bestehenden Figma-Manifestseiten.

## [2026-06-26 08:10 UTC] ingest | raw/raw/Business/Wagglz/Design/README.md
- Pages: [[Wagglz Wufflz Design README]], [[Wufflz Website Design]], [[Wufflz Pitch Deck Banken]], [[Wufflz Pitch Investoren]], [[25 Wufflz Wireframes Figma Manifest]]
- Wagglz/Wufflz Design README ingested: Neue Source-Seite erstellt; Wufflz Website Design, Pitch Deck Banken und Pitch Investoren v1–v3 als Entitäten angelegt; bestehende 25 Wufflz Wireframes-Seite um README-Kontext ergänzt; Index aktualisiert.

## [2026-06-26 08:13 UTC] ingest | raw/raw/Business/Wagglz/Design/figma-index.md
- Pages: [[Figma Index Wagglz Source]], [[Figma Migration Wagglz]]
- Wagglz/Wufflz Figma Master Index ingested — neue Source-Seite erstellt, bestehende Manifest-Seiten verlinkt, Figma-Katalog-Übersicht als Konzeptseite hinzugefügt, Index aktualisiert.

## [2026-06-26 08:14 UTC] ingest | raw/raw/Business/Wagglz/Design/kits/Figma-Manifest-ant-design-system-for-figma-preview.md
- Pages: [[Ant Design System for Figma Preview]]
- Neue Quellseite für Ant Design System for Figma (Preview) erstellt — Drittanbieter-UI-Kit im Wagglz/Wufflz-Design-Kontext, File Key faSohMPNaRaWIimPAQAlCA, kein vollständiger Export erforderlich, Status ausstehend; Index aktualisiert.

## [2026-06-26 08:15 UTC] ingest | raw/raw/Business/Wagglz/Design/kits/Figma-Manifest-nucleus-plus.md
- Pages: [[Nucleus Plus Figma Manifest]]
- Neue Quellseite für „Nucleus Plus — Figma Export 2026-06-13" erstellt (Drittanbieter-UI-Kit, File Key wzKhS5oRrI1FgK3cIRfCiP, kits/-Ordner, niedrige Priorität, Status ausstehend); Index um Eintrag ergänzt.

## [2026-06-26 08:17 UTC] ingest | raw/raw/Business/Wagglz/Design/kits/Figma-Manifest-theprojekts-design-system-v2.md
- Pages: [[theProjekts Design System V2 Figma Manifest]]
- Neue Quellseite für theProjekts Design System V2 (Figma UI-Kit, File Key YCUvHIoaxSoQSPveySgTLP) erstellt; Index um Wagglz-Design-Quelleintrag ergänzt.

## [2026-06-26 08:18 UTC] ingest | raw/raw/Business/Wagglz/Design/kits/README.md
- Pages: [[Wagglz UI-Kits README]], [[Ant Design System for Figma Preview]], [[Nucleus Plus Figma Kit]], [[theProjekts Design System V2]]
- Neue Quellseite "Wagglz UI-Kits README" erstellt; bestehende Seiten "Ant Design System for Figma Preview" und "Figma Index Wagglz" aktualisiert um Nucleus Plus und theProjekts Design System V2; Index erweitert.

## [2026-06-26 08:20 UTC] ingest | raw/raw/Business/Wagglz/Design/legacy-wagglz/Figma-Manifest-my-rex-copy.md
- Pages: [[My Rex Copy Figma Manifest]]
- Neue Quellseite für das Figma-Manifest „My Rex (Copy)" (File Key 7yBGOpEg0ETNXR3cQ4bOl4) erstellt; Index um den Eintrag erweitert; Figma Index Wagglz als verwandte Seite referenziert.

## [2026-06-26 08:21 UTC] ingest | raw/raw/Business/Wagglz/Design/legacy-wagglz/Figma-Manifest-wagglz-app-dogwalking.md
- Pages: [[Wagglz App Dogwalking Figma Manifest]]
- Neue Quellseite erstellt: Wagglz App Dogwalking Figma Manifest (File Key MUvsIoZBIT0kOdIQjdn0s9) — Dogwalking-Design-Datei im wagglz/-Ordner; Status ausstehend, keine Frames exportiert; index.md aktualisiert.

## [2026-06-26 08:22 UTC] ingest | raw/raw/Business/Wagglz/Design/legacy-wagglz/Figma-Manifest-wagglz-dogwalking.md
- Pages: [[Wagglz Dogwalking Figma Manifest]]
- Neue Quellseite für Wagglz Dogwalking Figma Manifest (legacy, File Key JjJ4CgJCqURgjohhbvcOrZ) erstellt; in Index eingetragen; liegt im wagglz/-Ordner (nicht wufflz/); Status ausstehend; noch keine Frames exportiert.

## [2026-06-26 08:24 UTC] ingest | raw/raw/Business/Wagglz/Design/legacy-wagglz/Figma-Manifest-wagglz-research-dogwalking.md
- Pages: [[Wagglz Research Dogwalking Figma Manifest]]
- Neue Quellseite für Wagglz Research Dogwalking Figma Manifest (File Key 23wUJ3p6E7Y6Om6qo5GF5w) erstellt — Design/Research-Datei im legacy-wagglz/-Ordner; Status ausstehend; keine Frames exportiert; in Figma-Index-Kontext eingeordnet.

## [2026-06-26 08:25 UTC] ingest | raw/raw/Business/Wagglz/Design/legacy-wagglz/Figma-Manifest-wufflz-app-market-research.md
- Pages: [[Wufflz App Market Research Figma Manifest]]
- Neue Quellseite "Wufflz App Market Research Figma Manifest" erstellt — FigJam-Board (File Key IXxrNkPjBIPGi8QbNgpdea) im legacy-Ordner wagglz/; API-Fehler 403 beim Abruf; keine Frames exportiert; Status error; in 10-Dateien-Migrationsliste; Index aktualisiert.

## [2026-06-26 08:27 UTC] ingest | raw/raw/Business/Wagglz/Design/legacy-wagglz/README.md
- Pages: [[Wagglz Legacy Design README]], [[Figma Manifest Wagglz Dogwalking]], [[Figma Manifest Wagglz App Dogwalking]], [[Figma Manifest Wagglz Research Dogwalking]], [[Figma Manifest My Rex Copy]]
- Added Wagglz Legacy Design README source page documenting 4 Figma files (Wagglz Dogwalking, Wagglz App Dogwalking, Wagglz Research, My Rex Copy) with their file keys; created stub entity pages for each; updated index.md.

## [2026-06-26 08:28 UTC] ingest | raw/raw/Business/Wagglz/Design/product/Figma-Manifest-25-b2b-software.md
- Pages: [[25 B2B Software Figma Manifest]]
- Aktualisiert: Wiki-Quellseite "25 B2B Software Figma Manifest" mit neuem Pfad (`product/` statt `wufflz/`), aktualisiertem Migration-Status (`ausstehend` statt `error`) und neuem Export-Befehl aus der Raw-Quelle.

## [2026-06-26 08:30 UTC] ingest | raw/raw/Business/Wagglz/Design/workshop/Figma-Manifest-co-founders-workshop.md
- Pages: [[Co-Founders Workshop Figma Manifest]]
- Neue Quellseite für das Co-Founders Workshop Figma-Manifest (FigJam, File Key VmWAOTBCe1hSspmmQY6S14) erstellt; in Index eingetragen; bestehende Vergleichstabelle auf Wagglz-Figma-Entitätsseiten verlinkt.

## [2026-06-26 08:31 UTC] ingest | raw/raw/Business/Wagglz/Design/workshop/README.md
- Pages: [[Co-Founders Workshop FigJam]]
- Neue Quellseite für das Co-Founders Workshop FigJam-Board (Key VmWAOTBCe1hSspmmQY6S14) erstellt; Index um den Eintrag erweitert.

## [2026-06-26 08:33 UTC] ingest | raw/raw/Business/Wagglz/Finanzen/Einnahmen/Wagglz GF-Gehalt 2025.md
- Pages: [[Wagglz GF-Gehalt 2025 Source Detail]], [[Wagglz GF-Gehalt 2025]]
- Neue Quelldatei `Wagglz GF-Gehalt 2025` ingested: Source-Seite erstellt, bestehende Entity-Seite `ALG I 2025` aktualisiert (Wagglz-GF-Gehalt-Quelle war bereits referenziert), neue Entity-Seite `Wagglz GF-Gehalt 2025` erstellt.

## [2026-06-26 08:34 UTC] ingest | raw/raw/Business/Wagglz/Finanzen/Konten/Wagglz Finom 2026.md
- Pages: [[Wagglz Finom 2026 Source Detail]], [[Wagglz Finom 2026]]
- Neue Quelldatei Wagglz Finom 2026 ingested: Quelldokument erstellt, Entitätsseite Wagglz Finom 2026 erstellt (IBAN DE36100180000083465573, Saldo Jan 0 €, wesentliche Buchungen 2026 inkl. USt-Nachzahlung, ARAG, Claude.ai, GoDaddy, Figma), Index aktualisiert.

## [2026-06-26 08:37 UTC] ingest | raw/raw/Business/Wagglz/Performance Coffee Brand/00 — Projektübersicht.md
- Pages: [[Performance Coffee Brand Projektübersicht]], [[Café Berlin Partnership Hai]], [[Performance Coffee Brand]]
- Neue Quelldatei "Performance Coffee Brand — Projektübersicht" ingested: Projektübersicht-Seite für die Performance Coffee Brand erstellt, Entität "Café Berlin Partnership Hai" als pivotiertes Vorgängerprojekt angelegt, und Index aktualisiert.

## [2026-06-26 08:42 UTC] ingest | raw/raw/Business/Wagglz/Performance Coffee Brand/Cafe/cafe_masterplan_2026.md
- Pages: [[GROVE Café Masterplan 2026 Source]], [[GROVE Café]], [[Oleg Kober]], [[Hai Tran]], [[GROVE Brand]], [[GROVE Finanzplan]]
- GROVE Café Masterplan 2026/2027 (Wagglz GmbH) vollständig aufgenommen: 1 Source-Seite + 7 Entity/Concept-Seiten erstellt (GROVE Café, Oleg Kober, Hai Tran, GROVE Brand, KfW StartGeld, GROVE Finanzplan, GROVE Betriebskonzept) + Index aktualisiert.

## [2026-06-26 08:46 UTC] ingest | raw/raw/Business/Wagglz/Performance Coffee Brand/Inhaltsstoffe — Datenbank.md
- Pages: [[Inhaltsstoffe Datenbank Performance Coffee]], [[Koffein Performance Coffee]], [[L-Theanin Performance Coffee]], [[L-Tyrosin Performance Coffee]], [[Rhodiola Rosea Performance Coffee]], [[Lion's Mane Performance Coffee]], [[B-Vitamine Performance Coffee]]
- Neue Quelldatei "Inhaltsstoffe — Datenbank" (Performance Coffee Brand) ingested: Quelldokument-Seite erstellt, bestehende Alpha-GPC-Entität aktualisiert, neue Konzept-Seiten für L-Theanin, L-Tyrosin, Rhodiola Rosea, Lion's Mane, B-Vitamine Performance und Supplement Stacks Performance Coffee erstellt; Index um alle neuen Seiten erweitert.

## [2026-06-26 08:49 UTC] ingest | raw/raw/Business/Wagglz/Performance Coffee Brand/Kaffee mit Performance.md
- Pages: [[Kaffee mit Performance Source Detail]], [[Performance Coffee Brand Phasenmodell]], [[Performance Coffee Brand]]
- Neue Quellseite für Performance Coffee Brand eCommerce-Pivot-Entscheidung (14.06.2026) erstellt; Konzeptseite Performance Coffee Brand Phasenmodell angelegt; bestehende Performance Coffee Brand Entity-Seite aktualisiert mit Pivot-Details, Verlustvortrag und offenen Fragen; Index erweitert.

## [2026-06-26 08:53 UTC] ingest | raw/raw/Business/Wagglz/Performance Coffee Brand/Kaffee — Rohstoffanalyse.md
- Pages: [[Kaffee Rohstoffanalyse Source]], [[Robusta vs Arabica Vergleich]], [[Robusta Kaffee]], [[Arabica Kaffee]], [[Vietnamesischer Kaffee]], [[Kaffee Röstgrade]], [[Zusatzstoffe Kombinierbarkeit Kaffee]]
- Neue Quelle ingested: Kaffee Rohstoffanalyse für Performance Coffee Brand — Robusta vs. Arabica Vergleich, Vietnam-Fokus, 3 Blend-Optionen, Röstgrade, Zusatzstoff-Kombinierbarkeit und EU-Rösterei-Beschaffung; neue Seiten erstellt für Quelle, Konzepte (Robusta, Arabica, Vietnamesischer Kaffee, Röstgrade, Beschaffung) und Entitäten (drei Blend-Optionen); Index erweitert.

## [2026-06-26 08:56 UTC] ingest | raw/raw/Business/Wagglz/Performance Coffee Brand/Prototyp — Hersteller & Prompt.md
- Pages: [[Prototyp Hersteller Research Performance Coffee]], [[Lohnhersteller Performance Coffee]], [[Pure Flavour GmbH]], [[Döhler GmbH]], [[Wonnda]], [[Prinova Europe]]
- Neue Seiten erstellt: Prototyp Hersteller Research (Source), Lohnhersteller Performance Coffee (Concept), Pure Flavour GmbH (Entity), Döhler GmbH (Entity), Wonnda (Entity), Prinova Europe (Entity); Index aktualisiert.

## [2026-06-26 08:58 UTC] ingest | raw/raw/Business/Wagglz/Wagglz GmbH — Finance Vault.md
- Pages: [[Wagglz GmbH Finance Vault]], [[Wagglz GmbH]]
- Neue Quelldatei "Wagglz GmbH — Finance Vault" ingested: Wagglz GmbH Finance-Seite erstellt/aktualisiert mit Insolvenzprüfung, Kapitaltransfer-Historie, Stammdaten und strategischen Optionen; Index aktualisiert.

## [2026-06-26 09:01 UTC] ingest | raw/raw/Business/Wagglz/Wagglz GmbH.md
- Pages: [[Wagglz GmbH Source Detail]], [[Wagglz GmbH]]
- Neue Quelldatei "Wagglz GmbH.md" ingested: Entitätsseite für Wagglz GmbH aktualisiert (Stammdaten, Insolvenzstatus §19 InsO, Gesellschafterdarlehen, Fixkosten, strategische Optionen); neue Quellseite erstellt; Index ergänzt.

## [2026-06-26 09:04 UTC] ingest | raw/raw/Business/Wagglz/Wagglz Wettbewerber.md
- Pages: [[Wagglz Wettbewerber Source]], [[Wagglz Wettbewerber]], [[VetPraxis]], [[Vetera]], [[easyVET Vetz]], [[Nordhealth]], [[Provet]], [[Vetnio]], [[Manta Vet]], [[Voisa AI]], [[VetPal]], [[PetsXL]], [[Tierärzteatlas]], [[Petleo]], [[Vetstoria]]
- Neue Quelldatei "Wagglz Wettbewerber" ingested: Quelldokument erstellt, Entitätsseiten für Wagglz GmbH und Wufflz verlinkt, 13 Wettbewerber-Entitäten als Kurzstubs angelegt, Index aktualisiert.

## [2026-06-26 09:09 UTC] ingest | raw/raw/Finanzdaten/GESAMTANALYSE_Oleg_Kober_2025-2026.md
- Pages: [[GESAMTANALYSE Oleg Kober 2025–2026]], [[Doctolib GmbH]], [[OK Capital UG]], [[Oleg Kober Vermögensübersicht]], [[ESt 2025]], [[ESt 2024]], [[ESt 2026]]
- Neue Gesamtfinanzanalyse Oleg Kober 2025–2026 ingested: Doctolib-Gehalt, Wagglz-Überschuldung, OK Capital UG Holding-Struktur, private Fixkosten, Consorsbank-Konten, ESt-2025-Schätzung und offene Maßnahmen (Rangrücktritt, ESt-Beauftragung) vollständig erfasst; neue Seiten für Doctolib GmbH, OK Capital UG, Oleg Kober Vermögensübersicht, ESt 2025 (aktualisiert), ALG I 2025 (aktualisiert), Wagglz GmbH (aktualisiert), Oleg Personal Context (aktualisiert), Consorsbank-Konten, VW Kredit, Rangrücktritt-Konzept und Gesamtanalyse-Source erstellt.

## [2026-06-26 09:11 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Finance/00 Finanz-Übersicht.md
- Pages: [[Finanz-Übersicht Source]], [[OK Capital UG]], [[Finanzielle Rehabilitation]]
- Neue Quellseite "Finanz-Übersicht" erstellt; Entitäten Wagglz GmbH und OK Capital UG ergänzt/verlinkt; Oleg Personal Context Finanzlage dokumentiert; MOC Finanzen und Rehabilitation Plan als Konzeptseiten verlinkt; Index aktualisiert.

## [2026-06-26 09:14 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md
- Pages: [[Master Prompt Gesamtfinanzanalyse]], [[Gesamtfinanzanalyse Methodik]], [[Insolvenzprüfung GmbH]]
- Neue Quellseite `Master Prompt Gesamtfinanzanalyse` erstellt; Entitätsseite `Oleg Personal Context` aktualisiert (Kontext zur Gesamtfinanzanalyse ergänzt); Konzeptseite `Gesamtfinanzanalyse Methodik` neu erstellt; Index erweitert.

## [2026-06-26 09:16 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Finance/OK Capital UG.md
- Pages: [[OK Capital UG Source Detail]], [[OK Capital UG]]
- Neue Quellseite für OK Capital UG erstellt; Entitätsseite erstellt; Wagglz GmbH Entität verlinkt; Index aktualisiert.

## [2026-06-26 09:18 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Finance/Rehabilitation Plan.md
- Pages: [[Finanz-Rehabilitation Plan Source]], [[Finanz-Rehabilitation Plan]], [[Strukturelles Defizit]]
- Neue Quellseite „Finanz-Rehabilitation Plan" erstellt; Entitätsseiten für Wagglz GmbH und OK Capital UG mit Rehabilitationsplan-Kontext verlinkt/aktualisiert; Konzeptseite „Strukturelles Defizit" erstellt; Index aktualisiert.

## [2026-06-26 09:20 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Finance/Wagglz GmbH.md
- Pages: [[Wagglz GmbH Finance Source Detail]], [[Wagglz GmbH]]
- Neue Quellseite `Wagglz GmbH Finance Source Detail` erstellt; Entitätsseite `Wagglz GmbH` erstellt mit vollständiger Dokumentation der Kapitaltransferhistorie, Insolvenzprüfung und strategischen Optionen; Index um beide Einträge erweitert.

## [2026-06-26 09:22 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Home.md
- Pages: [[Oleg Command Center Home]], [[Oleg Personal Context]]
- Neue Quelldatei `raw/raw/Finanzdaten/ObsidianVault/Home.md` (Oleg Kober Command Center Dashboard) ingested: Quelldokument-Seite erstellt, Entität `Oleg Personal Context` mit kritischen Finanzkennzahlen aktualisiert, Index erweitert.

## [2026-06-26 09:24 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Performance/00 Performance-Übersicht.md
- Pages: [[Performance Übersicht Source Detail]], [[Performance Übersicht]]
- Neue Seite "Performance Übersicht" (Quelle + Entitätsaktualisierungen) erstellt; Verlinkungen zu bestehenden Seiten (3D Body Scan, Hyrox, Zone 2, Biomarker Testing) hergestellt; Index um Performance-Einträge ergänzt.

## [2026-06-26 09:26 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Performance/Blutbild Panel.md
- Pages: [[Blutbild Panel Source Detail]], [[Blutbild Panel]], [[Supplement Stack Basisprotokoll]]
- Neues Blutbild Panel (24 Marker, Longevity-Zielbereiche, quartalsweise) als Source- und Konzeptseiten angelegt; Biomarker-Testing-Konzeptseite aktualisiert; index.md ergänzt.

## [2026-06-26 09:29 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Performance/Hyrox Prep.md
- Pages: [[Hyrox Vorbereitung Source]], [[Hyrox Competition]], [[Zone 2 Training]]
- Neue Seiten erstellt: Hyrox Vorbereitung (Source), Hyrox Competition (Entity), Zone 2 Training (Concept); bestehende Seiten [[3D Body Scan Scaneca Mai 2026]] und [[Biomarker Testing]] bereits verlinkt; Index aktualisiert.

## [2026-06-26 09:31 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Performance/Körper & Scan.md
- Pages: [[Körper und Body Composition Vault Finanzdaten Source]], [[3D Body Scan Scaneca Mai 2026]]
- Neue Source-Seite für `raw/Finanzdaten/ObsidianVault/Performance/Körper & Scan.md` erstellt — identifiziert als die bereits in [[3D Body Scan Scaneca Mai 2026]] referenzierte „Vault-Planungsnotiz" (KFA-Ziel 14–16%, WHR-Ziel <0,86, Gewichtsziel 88–90 kg); Entity-Seite mit korrekter Quellenverknüpfung aktualisiert; keine neuen Widersprüche — bestätigt bestehende Diskrepanz 15–17% vs. 14–16% KFA.

## [2026-06-26 09:34 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Templates/Claude Session – Finanzen.md
- Pages: [[Claude Session – Finanzen Template]], [[Oleg Personal Context]], [[MOC Finanzen]]
- Neue Quellseite `Claude Session – Finanzen Template` erstellt; Entitätsseite `Oleg Personal Context` aktualisiert (Finanzdaten ergänzt); `MOC Finanzen` aktualisiert; Index erweitert.

## [2026-06-26 09:35 UTC] ingest | raw/raw/Finanzdaten/ObsidianVault/Templates/Claude Session – Performance.md
- Pages: [[Claude Session Template Performance]]
- New source page created for Claude Session Performance Template; entity page for Claude Session Template Performance updated with new source path; BMR and TDEE concept page updated to reflect confirmed 220g protein target; index updated.

## [2026-06-26 09:38 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/00 MOC Finanzen.md
- Pages: [[MOC Finanzen Source Detail]], [[MOC Finanzen]]
- Neue Quelldatei "00 MOC Finanzen.md" (Finanz-Dashboard Oleg Kober, Stand Juni 2026) ingested — MOC Finanzen Source Detail erstellt; MOC Finanzen Entität aktualisiert; Index erweitert.

## [2026-06-26 09:40 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Archiv/GESAMTANALYSE Archiv.md
- Pages: [[GESAMTANALYSE Archiv Source]]
- Archiv-Quelldokument GESAMTANALYSE Archiv ingested — minimale Quelldaten (nur Metaverweise auf externe Dateien); Source-Seite erstellt und Index aktualisiert.

## [2026-06-26 09:42 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Aufgaben/P0 Sofort.md
- Pages: [[P0 Sofortmaßnahmen Source]], [[Rangrücktritt §15a InsO]]
- Neue Source-Seite `P0 Sofortmaßnahmen` erstellt; Entities `Wagglz GmbH` und `Rangrücktritt §15a InsO` als Wikilinks referenziert; `Consorsbank 260809254` als erledigtes Item dokumentiert; Index aktualisiert.

## [2026-06-26 09:45 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Aufgaben/P1 Diese Woche.md
- Pages: [[P1 Diese Woche Source Detail]], [[ESt 2025]], [[Wagglz GmbH]], [[Fixkosten Übersicht]]
- Neue Quellseite „P1 Diese Woche Source Detail" angelegt; Entitätsseiten für ESt 2025, Wagglz GmbH und Fixkosten Übersicht aktualisiert/erstellt; Index erweitert.

## [2026-06-26 09:48 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Aufgaben/P2 Diesen Monat.md
- Pages: [[P2 Diesen Monat Source Detail]], [[Doctolib PKW-Sachbezug]], [[Notfallfonds Aufbau]], [[DZR GmbH]], [[ARAG Wagglz Versicherung]], [[Steamone Transaktion]], [[VW Konsumkredit]]
- P2-Aufgabenliste (Diesen Monat) ingested: Source-Seite erstellt; Entitäten für Doctolib PKW-Sachbezug, Notfallfonds, DZR GmbH, VW Konsumkredit aktualisiert/erstellt; ARAG Wagglz Versicherung-Entität aktualisiert; Steamone-Transaktion als neue Entität erfasst; Index erweitert.

## [2026-06-26 09:50 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Ausgaben/Fixkosten Übersicht.md
- Pages: [[Fixkosten Übersicht Source Detail]], [[Fixkosten Übersicht]]
- Neue Seite "Fixkosten Übersicht" erstellt (source + entity): monatliche Fixkosten ~2.120–2.420 €, Doctolib-Netto 3.638,82 €, VW-Kredit, Versicherungen, Streaming-Abos; Verbindungen zu Wagglz GmbH, VW Konsumkredit, Uelzener Tierversicherung, Allianz, Barmenia, Oleg Personal Context.

## [2026-06-26 09:51 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Ausgaben/VW Konsumkredit.md
- Pages: [[VW Konsumkredit]], [[VW Konsumkredit Source]]
- Neue Seite erstellt: VW Konsumkredit (Entität + Source) — 18.858 € Restschuld, 681,57 €/Monat, Laufzeit bis November 2028; Sondertilgungsoption mit Q-Bonus verknüpft; Index aktualisiert.

## [2026-06-26 09:53 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Einnahmen/ALG I 2025.md
- Pages: [[ALG I 2025 Source Detail]]
- Neue Quelldatei `raw/Finanzdaten/Obsidian_Vault/Einnahmen/ALG I 2025.md` ingested — bestätigt alle Eckdaten der bestehenden Wiki-Seiten (Betrag ~8.400 €, Zeitraum bis ca. Juni 2025, §32b/§46 EStG, Pflichtveranlagung, Bescheinigung für ESt 2025); keine Widersprüche; `ALG I 2025 Source Detail` wird um zweite Quell-Pfad-Referenz erweitert.

## [2026-06-26 09:55 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Einnahmen/Doctolib 2026.md
- Pages: [[Doctolib Gehalt 2026 Source]], [[Doctolib GmbH]], [[PKW-Sachbezug 1%-Regel]]
- Neue Quelle "Doctolib 2026.md" integriert: Source-Seite erstellt, Entity-Seite für Doctolib GmbH erstellt/aktualisiert, Concept-Seite für PKW-Sachbezug 1%-Regel erstellt, Index um alle neuen Einträge erweitert.

## [2026-06-26 09:56 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Einnahmen/Wagglz GF-Gehalt 2025.md
- Pages: [[Wagglz GF-Gehalt 2025 Source Detail]]
- Neue Quellseite `Wagglz GF-Gehalt 2025 Source Detail` erstellt; bestehende Entität `Wagglz GF-Gehalt 2025` aktualisiert (zweiter Vault-Pfad `raw/Finanzdaten/Obsidian_Vault/Einnahmen/` ergänzt); Index um neuen Eintrag erweitert.

## [2026-06-26 09:57 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Konten/Consorsbank Girokonto 0250120493.md
- Pages: [[Consorsbank Girokonto 0250120493 Source]], [[Consorsbank Girokonto 0250120493]]
- Neue Seite erstellt: Consorsbank Girokonto 0250120493 (Source + Entity); Index aktualisiert mit Finanzkonto-Eintrag.

## [2026-06-26 09:59 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Konten/OK Capital Finom 2026.md
- Pages: [[OK Capital Finom 2026 Source]], [[OK Capital UG]]
- Neue Quelldatei "OK Capital Finom 2026" ingested: Konto-Entity für OK Capital UG (Finom-Konto), Saldo 0 €, laufende Kosten 31,60 €/Mo (WestX + Google), Oleg-Darlehen 100 € (März 2026); Source-Seite und Entity-Seite erstellt; Index aktualisiert.

## [2026-06-26 10:01 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Konten/Wagglz Finom 2026.md
- Pages: [[Wagglz Finom 2026 Source]], [[Wagglz Finom 2026]]
- Neue Quelldatei "Wagglz Finom 2026" ingested: Kontoseite für Wagglz GmbH Finom-Konto (IBAN DE36100180000083465573) — Saldo Jun 2026 = 0 €, wesentliche Buchungen 2026 dokumentiert; Entitätsseite erstellt und Index aktualisiert.

## [2026-06-26 10:03 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Steuern/ALG I Progressionsvorbehalt.md
- Pages: [[ALG I Progressionsvorbehalt Source Detail]], [[ALG I Progressionsvorbehalt]]
- Neue Quellseite `ALG I Progressionsvorbehalt Source Detail` aus `raw/Finanzdaten/Obsidian_Vault/Steuern/ALG I Progressionsvorbehalt.md` ingested — bestätigt bestehendes Quelldokument vollständig; zweiter Vault-Pfad hinzugefügt; keine Widersprüche; bestehende Konzept- und Quellseiten aktualisiert.

## [2026-06-26 10:05 UTC] ingest | raw/raw/Finanzdaten/Obsidian_Vault/Steuern/ESt 2025.md
- Pages: [[ESt 2025 Source Detail]], [[ESt 2025]]
- Neue Source-Seite `ESt 2025 Source Detail` erstellt; Entity-Seite `ESt 2025` erstellt (Steuererklärung 2025 mit Wagglz-Gehalt, ALG I, Pflichtveranlagung, Checkliste und erwartetem Ergebnis); Index um ESt-2025-Einträge erweitert.
