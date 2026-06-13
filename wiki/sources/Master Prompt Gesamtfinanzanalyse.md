---
title: Master Prompt Gesamtfinanzanalyse
type: source
tags: [finance, prompt, master, analyse, insolvenz, steuer, wagglz, ok-capital, cashflow, geschaeftsfuehrer-haftung]
sources: ["raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md"]
created: 2026-06-10
updated: 2026-06-10
summary: Master-Prompt für integrierte Finanzanalyse Privat + Wagglz GmbH + OK Capital UG — multi-perspektivisches Expertenteam (FD, ST, IA, US); fokussiert auf Insolvenzprüfung, Steuer, konsolidierte Vermögenslage und Exit-Strategien
---

# Master Prompt — Gesamtfinanzanalyse

## Overview

Dieses Dokument enthält den vollständigen Claude-Prompt für die integrierte Finanzanalyse der drei Entitäten von [[Oleg Personal Context|Oleg Kober]]:
- **Privat** (Oleg Kober persönlich)
- **[[Wagglz GmbH]]** (Gesellschafter/Geschäftsführer: Oleg)
- **[[OK Capital UG]]** (ebenfalls Oleg)

> Verwendung: Gesamten Prompt in ein **neues** Claude-Gespräch kopieren, dann Dokumente hochladen.

## Prompt-Architektur: Vier Perspektiven

Der Prompt definiert ein interdisziplinäres Expertenteam mit vier gleichwertigen Rollen:

| Kürzel | Rolle | Fokus |
|---|---|---|
| **[FD]** | Finance Director | Zahlen, Strukturen, Cashflow, konsolidierte Sicht |
| **[ST]** | Steuerberater | Steuerliche Risiken, Optimierung, Compliance |
| **[IA]** | Insolvenzanalyst | Überschuldung, Zahlungsunfähigkeit, Haftung, Risikobewertung |
| **[US]** | Unternehmensstratege | Entscheidungen, Prioritäten, Handlungsoptionen |

Jeder Befund wird mit dem Kürzel der ausgebenden Perspektive markiert. Widersprüche zwischen Perspektiven sind explizit erlaubt und gewünscht.

## Bekannter Kontext (im Prompt hardcodiert)

### Person
- **Name:** Oleg Kober, 32 J., Berlin
- **Angestellt bei:** [[DoktorLib|Doctolib GmbH]] (Sales)

### Privatfinanzen

| Posten | Wert |
|---|---|
| Fixgehalt netto | 3.638,82 €/Mo |
| Provision | ~4.611 € netto/Quartal (Jan/Apr/Jul/Okt) |
| Kontostand aktuell | −1.405 € (Dispo) |
| Ersparnisse | 1,10 € |
| Depot | keines |
| Strukturelles Jahresdefizit Privat | **−7.970 €/Jahr** |
| VW-Bank Kredit | 681,57 €/Mo bis 11/2028 |
| Kieferorthopädie-Rate | 176,53 €/Mo (Dr. Wiemann) |
| Firmenwagen geldwerter Vorteil | ~348 € brutto/Mo |

> ⚠️ **Kritisch:** Der VW-Bank-Kredit ist ein **persönlicher Kredit für ein Crypto-Investment** — der Erlös floss in die [[Wagglz GmbH]]. Dies schafft eine direkte persönliche Haftungsverbindung.

### Unternehmensbelastung

| Posten | Wert |
|---|---|
| Laufende Gesellschafterdarlehen Privat → Unternehmen | ~357 €/Mo |
| Jahresabschlüsse fällig (aktuell) | 5.000 € für beide |
| Jahresabschlüsse folgejahr | 2.500 € |
| Bekannte Rückflüsse aus Unternehmen | **keine erkennbaren** |
| Gesamtbelastung durch Unternehmen | **~8.000 €/Jahr** |

## Fünf Kritische Analysefragen

1. Sind [[Wagglz GmbH]] oder [[OK Capital UG]] aktuell **überschuldet** oder **zahlungsunfähig**?
2. Besteht eine **Insolvenzantragspflicht** als Geschäftsführer?
3. Wie hoch ist der **Gesamtschaden** aus den Unternehmensinvestitionen?
4. Gibt es **steuerliche Verluste**, die gegen Privateinkommen verrechnet werden können?
5. Was ist die beste **Exit-Strategie** für die Unternehmen?

## Dokumente-Checkliste

### Privat
- [ ] Kontoauszüge alle Jahre (CSV-Export Consorsbank Girokonto + Tagesgeld)
- [ ] Steuererklärungen ESt 2021–2024 inkl. Bescheide
- [ ] VW-Bank Kreditvertrag (Ursprungsbetrag, Zinssatz, Restschuld, Tilgungsplan)

### Wagglz GmbH
- [ ] BWA (Betriebswirtschaftliche Auswertung, aktuell)
- [ ] Jahresabschlüsse (Bilanz + GuV, alle Jahre)
- [ ] Kontoauszüge Geschäftskonto
- [ ] Steuerbescheide (KSt, GewSt, USt)

### OK Capital UG
- [ ] Jahresabschluss / BWA
- [ ] Kontoauszüge

### Verträge
- [ ] Gesellschaftsverträge
- [ ] Darlehensverträge / Rangrücktritte

## Analyse-Auftrag: Vier Schritte

### Schritt 1 — Insolvenzprüfung [IA] (Priorität 1)

Für jede Gesellschaft:
- **a) Zahlungsunfähigkeit (§ 17 InsO):** Kann die Gesellschaft fällige Verbindlichkeiten aus Liquidität bedienen?
- **b) Überschuldung (§ 19 InsO):** Ist das bilanzielle Eigenkapital negativ? Fortführungsprognose?
- **c) Antragspflicht:** Besteht aktuell Insolvenzantragspflicht (21-Tage-Frist)?
- **d) Geschäftsführer-Haftung:** Zahlungen nach Insolvenzreife → Anfechtungsrisiko?
- **Ergebnis:** GRÜN / GELB / ROT mit Begründung

### Schritt 2 — Steuerliche Lage [ST]

- Offene Steuerschulden Privat + je Gesellschaft
- Eingereichte vs. fehlende Steuererklärungen
- Verlustvorträge (§10d EStG privat; §8 KStG Kapitalgesellschaften)
- Gesellschafterdarlehen: Umqualifizierung als verdeckte Einlage?
- Optimierungspotenzial für 2024/2025

### Schritt 3 — Konsolidierte Vermögenslage [FD]

- AKTIVA: Forderungen, Anlagevermögen, Bankguthaben, sonstige Werte
- PASSIVA: VW-Bank, Lieferanten, Finanzamt, Gesellschafterdarlehen
- Konsolidiertes Nettovermögen: positiv oder negativ?
- Persönliche Haftungsexponierung total

### Schritt 4 — Unternehmens-Rentabilität [US]

Für jede Gesellschaft:
- Umsatzhistorie: je generiert? Wann, wie viel?
- Geschäftsmodell-Realismus
- Verhältnis Investition zu Ertrag
- Break-Even-Bedingungen
- Exit-Optionen: Liquidation / Verkauf / Dormancy / Insolvenz

## Expected Deliverables

| # | Deliverable | Federführung |
|---|---|---|
| 1 | **Ampel-Dashboard** (ROT/GELB/GRÜN je Entität + Insolvenzrisiko) | [IA] |
| 2 | **Konsolidierte Bilanz** (alle Aktiva/Passiva + Haftungsexponierung) | [FD] |
| 3 | **Steuerliche To-Do-Liste** mit Fristen + Konsequenzen | [ST] |
| 4 | **Sofortmaßnahmen 30-Tage-Plan** (rechtliche Dringlichkeit) | [IA] |
| 5 | **Strategische Optionen** je Gesellschaft (3 Szenarien) | [US] |
| 6 | **Gesamtstrategie + Zeitplan** | Alle |

## Kontext: Kritische Sachverhalte

### VW-Bank-Kredit → Crypto → Wagglz
Der persönliche Kredit bei der VW Bank (681,57 €/Mo bis 11/2028) wurde für ein Crypto-Investment aufgenommen; der Erlös floss in die [[Wagglz GmbH]]. Dies bedeutet:
- Oleg haftet **persönlich** für die Rückzahlung
- Die Investition in die GmbH generiert bislang **keine erkennbaren Rückflüsse**
- Dieser Sachverhalt ist zentral für die Frage der persönlichen Haftungsexponierung

### Strukturelles Privatdefizit
Mit −7.970 €/Jahr strukturellem Defizit und zusätzlichen ~8.000 €/Jahr Unternehmensbelastung ergibt sich eine Gesamtbelastung von ca. **−16.000 €/Jahr** — bevor etwaige Quartalsprovisionen eingerechnet werden.

### Gesellschafterdarlehen
Die monatlichen Überweisungen (~357 €/Mo) von Privat an die Unternehmen sind als Gesellschafterdarlehen bilanziert (oder sollten es sein). Die steuerliche Qualifikation (eigenkapitalersetzend, verdeckte Einlage?) ist eine offene kritische Frage.

## ⚠️ Neue Entitäten — Erfordern Wiki-Seiten

Dieser Prompt führt zwei bisher im Wiki nicht vorhandene Unternehmens-Entitäten ein:
- **[[Wagglz GmbH]]** — Gesellschaft von Oleg Kober
- **[[OK Capital UG]]** — zweite Gesellschaft von Oleg Kober

Siehe jeweilige Entitätsseiten für Details.

## Related Pages

- [[Oleg Personal Context]] — Subjekt der Analyse
- [[Wagglz GmbH]] — primäre operative Gesellschaft
- [[OK Capital UG]] — zweite Gesellschaft (UG)
- [[Oleg Business Entity Structure]] — Unternehmensstruktur-Übersicht
- [[Oleg Financial Situation]] — konsolidierte Finanzsituation
- [[Insolvenzprüfung]] — rechtliches Konzept (§17, §19 InsO)
- [[Gesellschafterdarlehen]] — steuerliches Konzept
- [[DoktorLib]] — Arbeitgeber
