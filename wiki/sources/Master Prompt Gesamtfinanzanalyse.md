---
title: "Master Prompt — Gesamtfinanzanalyse"
type: source
tags: [finance, prompt, master, analyse, wagglz, ok-capital, insolvenz, steuern, privatfinanzen, cashflow, exit-strategie, claude, oleg]
sources: ["raw/raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md"]
created: 2026-06-10
updated: 2026-06-20
summary: Vollständiger Claude-Analyse-Prompt für die integrierte Finanzanalyse Privat + Wagglz GmbH + OK Capital UG — 4-Rollen-Framework [FD/ST/IA/US]; priorisierte Analyse-Schritte (Insolvenzprüfung → Steuerlage → konsolidierte Bilanz → Rentabilität); 6 Expected Outputs; umfangreicher Dokumenten-Upload-Katalog; offene Kritische Fragen zu Insolvenzpflicht und Exit-Strategie
---

# Master Prompt — Gesamtfinanzanalyse

## Übersicht

Dieses Dokument ist ein **vollständiger Analyse-Prompt** für ein neues Claude-Gespräch, das die integrierte Finanzlage von [[Oleg Personal Context|Oleg Kober]] und seinen beiden Unternehmen ([[Wagglz GmbH]] und [[OK Capital UG]]) untersucht. Es handelt sich um ein strukturiertes Planungs- und Analyse-Tool, das für interne Entscheidungsfindung erstellt wurde.

> **Verwendung:** Gesamten Prompt kopieren → neues Claude-Gespräch starten → Prompt einfügen → Dokumente hochladen.

---

## Bekannter Kontext (aus Prompt)

### Person
- **Oleg Kober**, 32 J., Berlin
- Angestellt bei Doctolib GmbH (Sales)

### Privatfinanzen

| Posten | Wert |
|---|---|
| Fixgehalt netto | 3.638,82 €/Mo |
| Provision netto | ~4.611 €/Quartal (Jan/Apr/Jul/Okt) |
| Kontostand aktuell | −1.405 € (Dispo) |
| Ersparnisse | 1,10 € |
| Depot | keines |
| Strukturelles Jahresdefizit Privat | **−7.970 €/Jahr** |
| VW-Bank Kredit | 681,57 €/Mo bis 11/2028 |
| Kieferorthopädie (Dr. Wiemann) | 176,53 €/Mo |
| Firmenwagen Doctolib | ~348 € geldwerter Vorteil brutto/Mo |

> **Wichtige Anmerkung:** Der VW-Bank-Kredit ist ein **persönlicher Kredit für ein Crypto-Investment** — der Erlös floss in die [[Wagglz GmbH]]. Dies ist eine besonders risikoreiche Konstruktion: privates Schuldverhältnis für unternehmerische Investition.

### Unternehmen

| Entität | Rolle Oleg | Status |
|---|---|---|
| [[Wagglz GmbH]] | Gesellschafter + Geschäftsführer | Jahresabschlüsse fällig (5.000 €) |
| [[OK Capital UG]] | Inhaber (haftungsbeschränkt) | Jahresabschlüsse fällig (5.000 €, zusammen) |

**Laufende Belastungen durch Unternehmen:**
- Gesellschafterdarlehen Privat → Unternehmen: ~357 €/Mo
- Jahresabschlüsse (aktuell): 5.000 € für beide Gesellschaften
- Jahresabschlüsse (nächstes Jahr): 2.500 €
- Gesamtbelastung durch Unternehmen: **~8.000 €/Jahr**
- Bekannte Rückflüsse aus Unternehmen: **keine erkennbaren**

---

## Offene Kritische Fragen

Die Analyse soll folgende Fragen beantworten:

| # | Frage | Dringlichkeit |
|---|---|---|
| 1 | Sind Wagglz GmbH oder OK Capital UG aktuell überschuldet oder zahlungsunfähig? | 🔴 Kritisch |
| 2 | Besteht eine Insolvenzantragspflicht als Geschäftsführer? | 🔴 Kritisch |
| 3 | Wie hoch ist der Gesamtschaden aus den Unternehmensinvestitionen? | 🟡 Hoch |
| 4 | Gibt es steuerliche Verluste, die gegen Privateinkommen verrechnet werden können? | 🟡 Hoch |
| 5 | Was ist die beste Exit-Strategie für die Unternehmen? | 🟡 Hoch |

---

## 4-Rollen-Framework

| Kürzel | Rolle | Fokus |
|---|---|---|
| **[FD]** | Finance Director | Zahlen, Strukturen, Cashflow, konsolidierte Sicht |
| **[ST]** | Steuerberater | Steuerliche Risiken, Optimierung, Compliance |
| **[IA]** | Insolvenzanalyst | Überschuldung, Zahlungsunfähigkeit, Haftung, Risikobewertung |
| **[US]** | Unternehmensstratege | Entscheidungen, Prioritäten, Handlungsoptionen |

Befunde werden mit dem jeweiligen Kürzel gekennzeichnet. Interne Widersprüche zwischen Rollen sind ausdrücklich gewünscht — ein [FD]-Befund kann andere Implikationen haben als ein [IA]-Befund.

---

## Analyse-Reihenfolge

### Schritt 1 — Insolvenzprüfung [IA] (PRIORITÄT 1)
Für jede Gesellschaft:
- **a) Zahlungsunfähigkeit** (§ 17 InsO): Kann die Gesellschaft fällige Verbindlichkeiten bedienen?
- **b) Überschuldung** (§ 19 InsO): Ist das bilanzielle Eigenkapital negativ?
- **c) Antragspflicht:** Besteht die 21-Tage-Frist?
- **d) Geschäftsführer-Haftung:** Zahlungen nach Insolvenzreife? (Anfechtungsrisiko)
- **Ergebnis:** GRÜN / GELB / ROT mit Begründung

### Schritt 2 — Steuerliche Lage [ST]
- Offene Steuerschulden (Privat + je Gesellschaft)
- Fehlende Steuererklärungen
- Verlustvorträge (§10d EStG privat, §8 KStG Kapitalgesellschaften)
- Gesellschafterdarlehen: Droht Umqualifizierung als verdeckte Einlage?
- Optimierungspotenzial 2024/2025

### Schritt 3 — Konsolidierte Vermögenslage [FD]
- Aktiva: Forderungen, Anlagevermögen, Bankguthaben
- Passiva: VW-Bank, Lieferanten, Finanzamt, externe Darlehen
- Konsolidiertes Nettovermögen
- Persönliche Haftungsexponierung total

### Schritt 4 — Unternehmens-Rentabilität [US]
- Hat das Unternehmen je Umsatz generiert?
- Geschäftsmodell realistisch profitabel?
- Break-Even: wann und unter welchen Bedingungen?
- Exit-Optionen: Liquidation / Verkauf / Dormancy / Insolvenz

---

## Expected Outputs (6 Deliverables)

| # | Deliverable | Federführung |
|---|---|---|
| 1 | **Ampel-Dashboard** — ROT/GELB/GRÜN je Entität (Privat / Wagglz / OK Capital) | [IA] |
| 2 | **Konsolidierte Bilanz** — alle Aktiva und Passiva + persönliche Haftungsexponierung | [FD] |
| 3 | **Steuerliche To-Do-Liste** mit Fristen + Konsequenzen bei Nicht-Einhaltung | [ST] |
| 4 | **Sofortmaßnahmen** — 30-Tage-Plan, priorisiert nach rechtlicher Dringlichkeit | [IA] |
| 5 | **Strategische Optionen** — 3 Szenarien je Gesellschaft (Kosten, Zeitaufwand, Auswirkung auf Privatfinanzen) | [US] |
| 6 | **Gesamtstrategie** — Reihenfolge + Zeitplan zum realistischen Weg in die finanzielle Stabilität | Alle |

---

## Dokumenten-Checkliste

### Privat
- [ ] Kontoauszüge alle Jahre (CSV-Export Consorsbank Girokonto + Tagesgeld)
- [ ] Steuererklärungen ESt 2021–2024 inkl. Bescheide
- [ ] VW-Bank Kreditvertrag (Ursprungsbetrag, Zinssatz, Restschuld, Tilgungsplan)

### Wagglz GmbH
- [ ] BWA (aktuell, vom Steuerberater)
- [ ] Jahresabschlüsse (Bilanz + GuV, alle Jahre)
- [ ] Kontoauszüge Geschäftskonto
- [ ] Steuerbescheide (KSt, GewSt, USt)

### OK Capital UG
- [ ] Jahresabschluss / BWA (alles Vorhandene)
- [ ] Kontoauszüge

### Verträge
- [ ] Gesellschaftsverträge
- [ ] Darlehensverträge / Rangrücktritte

---

## Dokument-Extraktion nach Typ (aus Prompt)

| Dokumenttyp | Extraktionsziele |
|---|---|
| **Kontoauszüge** | Kategorisierung Ein-/Ausgänge; Cashflow-Monatstabelle; Intercompany-Flows Privat ↔ Wagglz ↔ OK Capital |
| **BWA** | Umsatz, EBITDA, operative Profitabilität; Trend; Liquidität BWA vs. Kontostand |
| **Jahresabschlüsse** | Eigenkapital (positiv/negativ?); Verbindlichkeiten; Gesellschafterdarlehen (eigenkapitalersetzend?); latente Steuern |
| **Steuererklärungen** | Offene Schulden; fehlende Jahre; Verlustvorträge; verdeckte Gewinnausschüttung? |
| **Sonstige Verträge** | Rangrücktritte; Besicherungen; Fälligkeitsklauseln |

---

## Kontext zur Finanzlage

Die im Prompt genannten Eckdaten lassen eine **prekäre Finanzlage** erkennen:

1. **Strukturelles Privatdefizit:** −7.970 €/Jahr bei gleichzeitig laufenden Unternehmensbelastungen von −8.000 €/Jahr → Gesamtdefizit ~16.000 €/Jahr
2. **Kontostand negativ:** −1.405 € (Dispo), Ersparnisse 1,10 €, kein Depot
3. **VW-Bank-Kredit für Crypto/GmbH-Investment:** Persönliche Haftung für unternehmerische Risiken
4. **Jahresabschlüsse offen:** 5.000 € fällig — ein weiterer sofortiger Liquiditätsdruck
5. **Keine erkennbaren Rückflüsse** aus den Unternehmen

Diese Kombination ist das Kernthema der Analyse und begründet die Priorisierung der Insolvenzprüfung als **Schritt 1**.

---

## Verwandte Seiten

- [[Oleg Personal Context]] — Person, deren Finanzen analysiert werden
- [[Wagglz GmbH]] — Primäres Unternehmen in der Analyse
- [[OK Capital UG]] — Zweites Unternehmen in der Analyse
- [[Gesamtfinanzanalyse Methodik]] — Konzeptseite zum 4-Rollen-Framework
- [[Insolvenzprüfung GmbH]] — Konzept: §17/§19 InsO für GmbH-Geschäftsführer
- [[MOC Finanzen]] — übergeordnete Finanz-MOC
- [[SP STB]] — Steuerberater im Kontext der steuerlichen Analyse
- [[ESt 2025]] — Laufende Steuererklärung mit ALG-I-Komplexität
