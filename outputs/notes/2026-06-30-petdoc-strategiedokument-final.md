---
title: "PetDoc — Marktanalyse & Strategiedokument (kanonisch, faktenkorrigiert)"
type: synthesis
tags: [wagglz, petdoc, markt, wettbewerb, b2b-saas, b2c, ki-telefonie, ki-doku, telemedizin, moat, gtm, tam, doctolib-modell, kanonisch]
created: 2026-06-30
updated: 2026-06-30
supersedes: outputs/notes/2026-06-30-doctolib-fuer-tieraerzte-marktanalyse.md
summary: Konsolidierte, red-team-geprüfte Marktanalyse für PetDoc (All-in-One PMS+KI+B2C, DE). 34,3M Heimtiere / €7Mrd Heimtiermarkt vs. nur ~€31M Vet-Software-TAM. GOT +20-60%. 5-Gruppen-Wettbewerb; PetsXL korrekt VetZ zugeordnet; KI-Punktlösungen als eigene Gruppe; IDEXX/Nordhealth als 12-18-Monats-Bedrohung. Moat = System-of-Record + 2-seitiger Netzwerkeffekt + Ausführungstempo. Gating: Wagglz GmbH §19 InsO, KI-Telefonie (Beachhead) noch nicht gebaut.
---

# PetDoc — Marktanalyse & Strategiedokument (DE)

> **Analyst-Disclaimer (ungeschönt):** Die Marktchance ist strukturell attraktiv und der White Space real. Zwei Realitäten gehören in jedes IC-Memo und stehen daher vorne: (1) Der adressierbare **Software-TAM in DE ist klein (~€31 Mio./Jahr)** — die €7-Mrd.-Zahl ist Futter/Zubehör, nicht Software. (2) Die ausführende **Wagglz GmbH ist §19-InsO-überschuldet (€0 Umsatz)**, und der KI-Telefonie-Beachhead — auf dem die gesamte GTM ruht — **ist noch nicht gebaut.** Diese Analyse beschreibt das Spielfeld; die Spielfähigkeit ist separat zu klären.

---

## 1. Marktübersicht & Makro-Trends (DE)

### 1.1 Marktvolumen — die zwei Geldtöpfe sauber getrennt

| Kennzahl | Wert | Einordnung |
|----------|------|-----------|
| Heimtiere DE | **34,3 Mio.** (15,7M Katzen, 10,5M Hunde) | B2C-Reichweite |
| Haushalte mit Heimtier | **43 %** | App-Adressmarkt |
| Heimtiermarkt-Umsatz | **~€7 Mrd.** | ⚠️ **Futter/Zubehör — NICHT Software** |
| Tierarztpraxen DE | **10.428** | B2B-Adressmarkt |
| Niedergelassene (rückläufig) | **11.216** | Konsolidierung (CVS, IVC) |
| Kleintier-Spezialisierung | **51,8 %** | Kern-SAM |
| **Vet-Software-TAM (DE, PMS)** | **~€31 Mio./Jahr** | das real monetarisierbare Volumen |
| EU-Vet-Software-Markt | **$483M → $987M (2030)** | **CAGR 12,7 %**, PMS = 66,7 % |

**Die zentrale Spannung:** Großer Haustiermarkt, **kleiner Softwaremarkt**. Der Hebel liegt nicht im €31M-Software-Topf allein, sondern darin, sich als Infrastruktur *zwischen* die Ströme von Behandlung, Diagnostik, Apotheke, Telemedizin und Versicherung zu setzen.

### 1.2 GOT-Novelle 2022 — der wirtschaftliche Katalysator

- **+20–30 % Ø**, **+60 %** bei Standard-Posten (Allgemeinuntersuchung, Injektion, Narkose) — fällt bei *jedem* Besuch an
- **80 %** der Tierschutzvereine melden mehr Halter mit Finanzierungsbedarf
- **B2C-Effekt:** Ruf nach Preis-Transparenz, digitalen Belegen, Versicherung
- **B2B-Effekt:** Druck auf lückenlose, GOT-konforme Abrechnung (keine Umsatzleckage)

*(Hinweis: kursierende „+50–100 %" sind überzeichnet; belegt sind +20–30 % Ø / +60 % Standard.)*

### 1.3 Pet Parenting
Tier = Familienmitglied; Erwartung = Human-Healthcare-Komfort (Doctolib-/N26-Niveau). Die Lücke zwischen Erwartung (digital, sofort, transparent) und Realität (Telefon, Papier-Impfpass, Wartezimmer) **ist** die Marktöffnung.

### 1.4 Kollaps des Ist-Systems
- **TFA-Fachkräftemangel:** hohe Fluktuation, niedriges Gehalt, Feminisierung + Wunsch nach geregelten Zeiten → Personalnot
- **Telefon-Flaschenhals:** bis zu **50 % verpasste Anrufe** zu Stoßzeiten = verlorener GOT-Umsatz + frustrierter Halter
- **Admin-Last:** Tierarzt dokumentiert „nach Feierabend" statt zu behandeln
- **Digitalisierungsstau:** Marktführer = 20–30 Jahre alter Kern, Cloud nur nachgerüstet, geschlossene Schnittstellen

---

## 2. Wettbewerbsanalyse — 5 strategische Gruppen

| Gruppe | Vertreter | Fokus | KI-Telefonie | KI-Doku | Telemed | B2C | Gravierende Schwäche |
|--------|-----------|-------|:---:|:---:|:---:|:---:|----------------------|
| **1 · Dinosaurier** | easyVET (VetZ), Vetera, Vetinf | B2B-PMS (Cloud auf Legacy-Kern) | ✕ | ✕ | ✕ | ~ (PetsXL/Portal) | Tiefe Funktion, aber überladene UX, **keine native KI**, Schnittstellen-Mauer |
| **2 · Cloud-Herausforderer** | inBehandlung, Provet, IDEXX Animana, debevet | B2B-PMS (SaaS) | ✕ | ~ (Provet ✓) | ✕ | ✕ | Moderne UI, aber **rein defensiv, keine KI-Automation, kein B2C-Netzwerk** |
| **3 · B2C-Marktplätze/Add-ons** | Petleo | B2C→B2B-Bridge | ✕ | ✕ | ~ | ✓ | **Schnittstellen-abhängig** vom Fremd-PMS; keine B2B-Datenhoheit |
| **4 · D2C-Spezialisten** | vetevo, PetsXL* | B2C-Gesundheit | ✕ | ✕ | ~ | ✓ | Besitzen den Halter, **keinen Fuß in der Praxis**; monetarisieren Labor/Produkte |
| **5 · KI-Punktlösungen** | Voisa, Manta, VetFox | KI-Telefonie/Scribe | ✓ | ~ | ✕ | ✕ | **Haben die KI — aber kein System-of-Record**, Bolt-on, kein Lock-in |
| **★ PetDoc** | — | **All-in-One** | **✓ nativ** | **✓ nativ** | **✓** | **✓ gekoppelt** | Hoher Initial-Bauaufwand (PMS-Kern: GoBD/Apotheke) |

> **\*Faktenkorrektur:** PetsXL ist **kein** unabhängiger Brückenbauer — es ist die **hauseigene B2C-App von VetZ** (`com.vetz.petsxl.app`), also dem easyVET-Hersteller. Heißt: Die Dinosaurier haben B2C *bereits angebaut*. Der White Space ist daher **nicht** „PMS ohne B2C", sondern präzise: **niemand koppelt PMS + native KI-Automation + B2C in einem Stack.**

**Die drei Strukturbefunde:**
1. **Horizontal geschichtet, nicht vertikal integriert.** Jede Gruppe besitzt *eine* Schicht. Die Integration besitzt niemand.
2. **KI existiert bereits — aber als Insel** (Gruppe 5 + Provets Doku). PetDocs Vorsprung ist **nicht „erste KI", sondern „native KI im eigenen System-of-Record"** → eliminiert das Schnittstellen-Problem.
3. **Die realen Bedrohungen sitzen in Gruppe 2:** **Nordhealth** (Vetera+Provet+Vetstoria) und **IDEXX** (Animana + Diagnostik-/Labor-Imperium + B2C-Kanal) — die Einzigen, die Kapital, PMS *und* B2C/Diagnostik vereinen und den White Space in **12–18 Monaten zusammenbauen könnten.**

**All-in-One-Vorteil:** Wer das PMS besitzt, hat **kein Schnittstellen-Problem.** Bolt-on-KI (Gruppe 5) muss über fragile APIs der Legacy-Systeme andocken — hakt die Sync, drohen Doppelbuchungen (Tierarzt-Albtraum). Native KI liest die echte Akte für Triage und schreibt Termin/SOAP-Note direkt in dasselbe System → **10x statt Flickwerk.**

---

## 3. B2B Pain-Points & ROI-Hebel

### 3.1 Daily Grind
Telefon (bis 50 % verpasst) = größte Zeitsenke · Tierarzt 1–2h „nach Feierabend" für Befunde/Berichte · GOT-Leckage durch vergessene Posten.

### 3.2 KI-Hebel quantifiziert (Einzelpraxis, realistisch)

| Modul | Mechanik | Einsparung/Tag | €-Wert/Monat |
|-------|----------|----------------|--------------|
| **KI-Telefonie** | 60 Anrufe/Tag, KI nimmt 50 % Routine (à 3 Min) ab | **~90 Min TFA** | **~€700** (à €22 AG-Brutto) + recovered Termine |
| **+ Recovered Notfall** | verpasster Notdienst (GOT €350–450) wird angenommen | — | 1 Fall/Quartal deckt KI-Jahreskosten |
| **KI-Doku (Scribe)** | Live-Diktat → SOAP, 2 Min/Patient × 25 | **~50 Min Arzt** | **2–3 Zusatzbehandlungen/Tag** → direkter Umsatz |

→ **Kombiniert €15.000–30.000/Jahr** an Zeit + Kapazität vs. **KI-Kosten ~€1.200–4.800/Jahr** = **ROI 5–10x.**

### 3.3 Switching Costs durchbrechen
Praxen wechseln PMS ungern (Migrationsangst) — das schützt die Platzhirsche. **Hebel:** nicht „besseres PMS" verkaufen, sondern die **KI-Telefonie als autarken Türöffner** — messbarer ROI ab Tag 1, läuft *parallel* zum Altsystem (kein Rip-and-Replace) → erlebter Wert → **Land-and-Expand ins PMS** bei Auslaufen des Altsystem-Wartungsvertrags. Wechselangst wird durch erlebten ROI neutralisiert, nicht frontal angegriffen.

### 3.4 Compliance — Mindestanforderung ab Tag 1 (nicht verhandelbar)

| Pflicht | Konkret | Bei Fehlen |
|---------|---------|-----------|
| **GoBD** | Unveränderbare Rechnungen, lückenlose Storno-/Korrektur-Protokollierung | Steuerprüfung scheitert |
| **Dispensierrecht** | Hausapotheke: Chargen, Verfall, Mindestbestand, AuA-Belege (TÄHAV) | Medikamentenabgabe rechtswidrig |
| **DSGVO Art. 9** | Halter- *und* Patientendaten, EU-Hosting (Frankfurt), AVV, Verschlüsselung | Bußgeld, kein Praxis-Vertrauen |
| **Aufbewahrung** | Med. Akten 10 J. (§12 TÄHAV), Rechnungen 10 J. (§147 AO) | Rechtswidrig |
| **KI-Haftung** | Human-in-the-Loop: keine autonome Diagnose, Arzt-Freigabe vor Speicherung | Berufsrechtliches Risiko |

> Wagglz erfüllt diese Punkte **architektonisch bereits** (GOT, Soft-Delete, RLS, Frankfurt, Human-in-Loop) — seltener Startvorteil gegenüber Greenfield.

---

## 4. B2C Zielgruppen-Analyse

### 4.1 Erwartung vs. Realität

| Pet Parent erwartet | Bekommt heute |
|---------------------|---------------|
| 24/7-Buchung (wie Booking.com) | Telefon 08–11 Uhr, 15× wählen |
| Echtzeit-Befunde/Laborwerte (post-GOT: „wofür €300?") | Papier oder gar nichts |
| Preis-Transparenz | Überraschungsrechnung |
| Sofort-Hilfe bei Akutfall | Notdienst-Odyssee |

### 4.2 Retention ehrlich
Tierarztbesuch = 1–2×/Jahr → **keine DAU-Logik.** Ziel = vertrauenswürdige Utility (wie Doctolib), nicht Daily Active. Durabel bindende Trigger:
- **Digitale Akte als „Scheckheft":** Befunde/Röntgen/Medikation kommen *automatisch vom Arzt* — **nur möglich durch B2B+B2C-Kopplung** (vetevo kann das nicht, weil ohne PMS). Der eigentliche Sticky-Faktor.
- **Smarte Prophylaxe-Reminder:** Zecke/Floh (saisonal), Impfung, Folgetermine chronisch Kranker.
- **Telemedizin als First-Line:** Sonntag, Hund erbricht → Videosprechstunde €39 statt teurer Notfallklinik. Stärkster „Open-the-app"-Trigger zwischen Besuchen.
- **Versicherungs-Integration:** Schadensmeldung direkt aus der Akte (post-GOT hochrelevant).

---

## 5. Monetarisierung

### 5.1 B2B — der Umsatzmotor

| Komponente | Modell | Zielpreis |
|------------|--------|-----------|
| PMS-Base-Fee | Flat/Praxis, skaliert nach Ärzten | **€149–249/Mo** (Kalender, Akte, GOT-Abrechnung, Apotheke) |
| KI-Telefonie | Flat **oder** pro Minute | €99/Mo **oder** €0,15/Min |
| KI-Doku | Flat pro behandelndem Arzt | €49/Mo |

→ Die KI-Module sind der **margentragende Preis-Expander** über das nackte PMS hinaus.

### 5.2 B2C — Moat + Akquise, nicht Primärumsatz
- **Freemium:** Suchen + Standard-Buchung gratis (Einstiegshürde null)
- **Premium „Pet Health Club" €4,99/Mo:** Langzeit-Laboranalysen, automatische Versicherungs-Weiterleitung/Direktabrechnung
- **Telemedizin-Provision:** 15–20 % Marktplatz-Gebühr pro Videosprechstunde

> **Ungeschönt:** B2C finanziert die Firma **nicht** allein (vetevo lebt von Labor/Produkten, nicht der App). **B2B-SaaS ist die Engine, B2C der Burggraben + billige Akquise.** Wer es umkehrt, verbrennt Marketing-Geld.

---

## 6. Strategische Roadmap & Unfair Advantage

### 6.1 Henne-Ei lösen — B2B-First / Trojanisches Pferd (Doctolib-Playbook)
1. **Verkaufe dem Arzt die KI-Telefonie + KI-Doku** — nicht „neue Kunden", sondern **Entlastung der bestehenden Vorzimmer-Last.** Autarker ROI ab Tag 1.
2. **Praxis schickt ihre *bestehenden* Halter** in die B2C-App (per SMS/beim Checkout) für Buchung + Akte.
3. **Die Ärzte holen die B2C-Nutzer kostenlos auf die Plattform.** Bei kritischer Praxisdichte je Stadt füllt sich der Marktplatz regional von selbst → **€0 B2C-Cold-Marketing.**

### 6.2 Der Burggraben (Moat)
```
Bolt-on-KI (Voisa/Manta) → 1 Feature  → kein Lock-in
Reines PMS (easyVET)     → die Praxis → aber Legacy, KI/B2C nur angebaut
Reine B2C-App (vetevo)   → den Halter → aber keine Praxisdaten (Sackgasse)
─────────────────────────────────────────────────────────────────────
PetDoc (PMS + native KI + gekoppelte B2C-App) → das SYSTEM OF RECORD
```
1. **System-of-Record-Lock-in:** gesamte Praxissteuerung (Finanzen, Apotheke, Akten, Telefonie) in *einer* Cloud → strukturell niedriger Churn (~5–10 %/J., nicht „0 %"); Wechsel = Datenverlust.
2. **Zwei-seitiger Netzwerkeffekt auf EINEM Daten-Graphen:** Praxen + Halter auf derselben Akte. Mehr Praxen → mehr Halter-Wert → mehr Halter → vollere Kalender. Reine B2C-App fehlt der Praxis-Graph; reines PMS fehlt der Halter-Graph. **Nur die Kopplung erzeugt den Effekt.**
3. **Native KI als 10x-Keil:** lernt die Behandlungsmuster des Arztes → bessere Doku → noch höherer Wechselaufwand für die Konkurrenz.

### 6.3 Ehrlicher Realitäts-Check (Analyst-Pflicht)

| Stärke | Brutale Gegenseite |
|--------|---------------------|
| Echter White Space (Integration unbesetzt) | **3-Fronten-Krieg**; jede Schicht hat etablierte Gegner |
| ROI 5–10x, sauber gerechnet | Vertrieb schlägt Produkt (easyVET: 31 J. Trust, 24/7-Support) |
| Moat real **wenn** Beachhead fällt | PMS-Beachhead ist der schwerste Schritt; €0 Traction + null Trust fatal |
| Wagglz hat ~70 % gebaut + Compliance | **KI-Telefonie (der Beachhead!) fehlt** + GmbH §19 InsO |
| Markt +12,7 % CAGR | DE-TAM nur ~€31M; **Nordhealth/IDEXX können den Stack in 12–18 Mon. nachbauen** |

→ **Der Moat ist nicht eine dauerhaft leere Nische, sondern Ausführungsgeschwindigkeit + System-of-Record-Lock-in, bevor die Kapitalstarken aufschließen.**

### 6.4 Synthese & nächster Schritt
Die Architektur-These ist **strategisch korrekt** und Wagglz hat **~70 % gebaut** (PMS, Wartezimmer, Scribe, Discharge, Portal, Compliance). Die richtige Reihenfolge ist nicht „mehr bauen", sondern:

1. **Beachhead validieren:** 5 Praxen fragen, ob der native KI-Telefonie→Kalender-Vorteil sie zum Pilotieren bewegt (Telefonie ist ROI-stärkster Einstieg, aber via Voisa/Manta/VetFox bereits umkämpft).
2. **Insolvenzfrage klären:** Rangrücktritt §15a InsO *oder* bewusste Liquidation — vor weiterem Kapital.
3. **Erst bei Go:** KI-Telefonie nativ ins Wagglz-PMS bauen (der fehlende 30 %-Baustein = zugleich der Beachhead).

→ **Nächster Schritt = 5 Praxis-Gespräche, kein Code.** Testet die teuerste Annahme (kauft der Arzt wegen des KI-ROI?) für €0.

---

## Quellen
ZZF/IVH Heimtiermarkt 2025 · BTK Statistik 2025 · GOT 2022 (gesetze-im-internet.de, BTK, Tierschutzbund) · Grand View / Wissen Research (EU Vet Software, CAGR 12,7 %) · vetz.de (easyVET; PetsXL = `com.vetz.petsxl.app`) · vetera.net / nordhealth.com · inbehandlung.de · provet.com (Pricing + 113 Screenshots raw/Archiv) · vetpraxis.de · vetevo.de · vet.petleo.net · voisa.ai / manta.vet / vetfox.ai · vetsoftwarehub.com (AI-Scribe-Pricing 2026) · digirift.com · Vault: [[Wagglz Wettbewerber]], [[Wagglz GmbH — Insolvenzstatus Juni 2026]], Diligence v1.
