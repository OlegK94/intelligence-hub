---
title: "Gesamtfinanzanalyse Methodik"
type: concept
tags: [finance, methodik, insolvenz, steuern, cashflow, exit-strategie, 4-rollen-framework, fd, st, ia, us, wagglz, ok-capital, privatfinanzen, analyse]
sources: ["raw/raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md"]
created: 2026-06-20
updated: 2026-06-20
summary: Konzeptseite zum interdisziplinären 4-Rollen-Framework [FD/ST/IA/US] für die integrierte Finanzanalyse von Privatfinanzen, Wagglz GmbH und OK Capital UG — beschreibt die Analyse-Reihenfolge (Insolvenz → Steuer → konsolidierte Bilanz → Rentabilität), die 6 Expected Outputs (Ampel-Dashboard, konsolidierte Bilanz, steuerliche To-Do-Liste, Sofortmaßnahmen, strategische Optionen, Gesamtstrategie) und die gesetzlichen Grundlagen der Insolvenzprüfung (§17/§19 InsO)
---

# Gesamtfinanzanalyse — Methodik

## Überblick

Die **Gesamtfinanzanalyse** ist ein interdisziplinärer Analyseansatz für die finanzielle Gesamtsituation von [[Oleg Personal Context|Oleg Kober]], die drei Entitäten umfasst:
1. **Privatfinanzen** (Oleg persönlich)
2. **[[Wagglz GmbH]]** (Gesellschafter + Geschäftsführer)
3. **[[OK Capital UG]]** (haftungsbeschränkt)

Das zugrundeliegende Prompt-Dokument ist unter [[Master Prompt Gesamtfinanzanalyse]] vollständig dokumentiert.

---

## Das 4-Rollen-Framework

Das Herzstück der Methodik ist die simultane Analyse durch vier gleichwertige Perspektiven:

| Kürzel | Rolle | Kernfrage |
|---|---|---|
| **[FD]** | Finance Director | Wie sehen die Zahlen wirklich aus? (konsolidiert, cashflow-basiert) |
| **[ST]** | Steuerberater | Welche steuerlichen Risiken und Chancen bestehen? |
| **[IA]** | Insolvenzanalyst | Besteht Insolvenzgefahr oder -pflicht? |
| **[US]** | Unternehmensstratege | Was ist die beste Handlungsoption? |

**Wichtiges Prinzip:** Ein [FD]-Befund kann eine andere Implikation haben als ein [IA]-Befund. Interne Widersprüche zwischen den Rollen sind nicht nur erlaubt, sondern erwünscht — sie spiegeln die tatsächliche Komplexität der Situation wider.

---

## Analyse-Reihenfolge und Begründung

Die Analyse wird in einer definierten Reihenfolge abgearbeitet, wobei die rechtliche Dringlichkeit die Priorität bestimmt:

```
Schritt 1: Insolvenzprüfung [IA]  →  Rechtliche Dringlichkeit (Haftungsrisiko)
Schritt 2: Steuerliche Lage [ST]  →  Compliance + Optimierungspotenzial
Schritt 3: Konsolidierte Bilanz [FD]  →  Gesamtbild der Vermögenslage
Schritt 4: Unternehmensrentabilität [US]  →  Strategische Entscheidungsgrundlage
```

### Begründung der Priorisierung

Die Insolvenzprüfung hat **Priorität 1**, weil:
- Eine Insolvenzantragspflicht zeitkritisch ist (21-Tage-Frist nach Erkennen)
- Unterlassene Antragstellung ist strafbar (§ 15a InsO)
- Zahlungen nach Insolvenzreife können zu persönlicher Haftung des GF führen
- Alle anderen Analysen (Steuer, Strategie) werden von der Insolvenzlage überlagert

---

## Gesetzliche Grundlagen (Insolvenzrecht)

### § 17 InsO — Zahlungsunfähigkeit
Eine Gesellschaft ist zahlungsunfähig, wenn sie nicht in der Lage ist, ihre fälligen Zahlungspflichten zu erfüllen. Zahlungsunfähigkeit liegt in der Regel vor, wenn die Zahlungslücke **10% der fälligen Verbindlichkeiten übersteigt** und nicht innerhalb von 3 Wochen geschlossen werden kann.

### § 19 InsO — Überschuldung
Eine Kapitalgesellschaft ist überschuldet, wenn ihr Vermögen die bestehenden Verbindlichkeiten nicht mehr deckt — also das **bilanzielle Eigenkapital negativ** ist — UND die **Fortführungsprognose negativ** ist.

> **Hinweis:** Seit der Insolvenzrechtsreform 2020 (COVID-Maßnahmen, später kodifiziert) gilt: Wenn die Fortführungsprognose positiv ist, begründet negatives Eigenkapital allein noch keine Überschuldung im Rechtssinne. Die Fortführungsprognose ist daher ein kritischer Analysegegenstand.

### § 15a InsO — Antragspflicht
Bei juristischen Personen (GmbH, UG) sind die **Mitglieder des Vertretungsorgans** (= Geschäftsführer) verpflichtet, ohne schuldhaftes Zögern, **spätestens drei Wochen** nach Eintreten der Zahlungsunfähigkeit oder Überschuldung Insolvenzantrag zu stellen.

**Persönliche Haftungskonsequenzen bei Verletzung:**
- Strafrechtliche Verfolgung (§ 15a Abs. 4 InsO)
- Zivilrechtliche Schadensersatzpflicht gegenüber Gläubigern
- Anfechtung von Zahlungen nach Insolvenzreife (§§ 129 ff. InsO)

---

## Konsolidierungsansatz [FD]

Die konsolidierte Vermögenslage umfasst alle drei Entitäten:

### Aktiva (konsolidiert)
- Gesellschafterdarlehen (Privat → Unternehmen) — als Forderung
- Anlagevermögen Wagglz GmbH + OK Capital UG
- Bankguthaben (alle Konten)
- Sonstige Werte

### Passiva (konsolidiert)
- VW-Bank Kredit (681,57 €/Mo bis 11/2028)
- Kieferorthopädie-Ratenzahlung (176,53 €/Mo)
- Verbindlichkeiten Wagglz GmbH (Lieferanten, Finanzamt)
- Verbindlichkeiten OK Capital UG
- Offene Jahresabschlüsse (5.000 €)

### Persönliche Haftungsexponierung
Trotz haftungsbeschränkter Gesellschaftsform (GmbH, UG) besteht persönliche Haftung in folgenden Fällen:
- Bürgschaften für Gesellschaftsschulden
- Zahlungen nach Insolvenzreife
- Gesellschafterdarlehen (Rückforderungsansprüche in der Insolvenz)
- Steuerliche Haftung (§ 69 AO — Haftung des GF für Steuerverbindlichkeiten der Gesellschaft)

---

## Steuerliche Analyse [ST]

### Verlustverrechnungsmöglichkeiten
- **Privat (§ 10d EStG):** Verluste aus Gewerbebetrieb, Kapitalanlagen
- **Wagglz GmbH (§ 8 KStG):** Körperschaftsteuerlicher Verlustvortrag
- **Gesellschafterdarlehen:** Können als verdeckte Einlage umqualifiziert werden → steuerliche Konsequenzen

### Gefährliche Konstruktion: VW-Bank-Kredit
- Privates Darlehen → Investition in GmbH
- Bei Verlust der GmbH-Investition: Kann der Kreditverlust steuerlich geltend gemacht werden?
- Hängt davon ab, ob Oleg das Darlehen als Gesellschafterdarlehen oder als Eigenkapitalzuführung klassifiziert hat

---

## Exit-Strategien [US]

| Option | Kosten | Zeitaufwand | Auswirkung auf Privatfinanzen |
|---|---|---|---|
| **Liquidation** | Liquidationskosten (Notar, Handelsregister) | 6–12 Monate | Verluste realisiert, aber sauber abgeschlossen |
| **Insolvenz** | Insolvenzverwalter-Kosten | 1–3 Jahre | Reputationsrisiko; mögliche Haftungsrisiken |
| **Dormancy** (ruhend stellen) | Laufende Grundkosten | Unbegrenzt | Kosten laufen weiter; Risiken bleiben |
| **Verkauf** | Transaktionskosten | Ungewiss | Nur bei positivem Unternehmenswert realistisch |

---

## Ampel-Dashboard (Konzept)

Die Analyse gibt für jede Entität ein GRÜN/GELB/ROT-Urteil aus:

| Farbe | Bedeutung |
|---|---|
| 🟢 **GRÜN** | Keine akute Insolvenzgefahr; Handlungsbedarf nicht dringend |
| 🟡 **GELB** | Erhöhtes Risiko; Handlungsbedarf innerhalb von Wochen |
| 🔴 **ROT** | Akute Insolvenzgefahr; Handlungsbedarf sofort (21-Tage-Frist beachten) |

Auf Basis der im [[Master Prompt Gesamtfinanzanalyse]] genannten Eckdaten (strukturelles Privatdefizit −7.970 €/Jahr, Unternehmensbelastung −8.000 €/Jahr, Kontostand −1.405 €, keine Rückflüsse) ist die Ausgangssituation ohne die hochgeladenen Dokumente als **GELB bis ROT** einzuschätzen.

---

## Verwandte Seiten

- [[Master Prompt Gesamtfinanzanalyse]] — vollständiges Quelldokument (Prompt-Text)
- [[Oleg Personal Context]] — analysierte Person
- [[Wagglz GmbH]] — primäres analysiertes Unternehmen
- [[OK Capital UG]] — zweites analysiertes Unternehmen
- [[Insolvenzprüfung GmbH]] — vertiefende Konzeptseite zur InsO-Prüfung
- [[MOC Finanzen]] — übergeordnete Finanz-MOC
- [[SP STB]] — Steuerberater im Kontext
- [[ESt 2025]] — laufende Steuererklärung
- [[ALG I Progressionsvorbehalt]] — steuerliche Komplexität 2025
