---
title: "Doctolib 2026 Gehalt (Quelldokument)"
type: source
tags: [einnahmen, doctolib, gehalt, 2026, employment, brutto, netto, sachbezug, bonus, est-2026, finanzen]
sources: ["raw/Privat/Finanzen/Einnahmen/Doctolib 2026.md"]
created: 2026-06-12
updated: 2026-06-17
summary: Quelldokument für Olegs Doctolib-Anstellung ab 2026-01-05; Gehalt 6.300 € brutto/Monat + 364 € PKW-Sachbezug (1%-Regel, Listenpreis ~36.400 €); Netto 3.638,82 €/Monat; Q1-Bonus 8.533 € brutto (April 2026); Jahresprognose 2026 ~105.568 € brutto / ~66.416 € netto (3 Quartals-Boni angenommen); Steuerklasse 1, KV HEK; Internetzuschuss 50 €/Monat steuerfrei
---

# Doctolib 2026 Gehalt — Quelldokument

## Überblick

Dieses Quelldokument (`raw/Privat/Finanzen/Einnahmen/Doctolib 2026.md`) erfasst die Anstellungsdaten und Gehaltsabrechnung von [[Oleg Personal Context|Oleg]] bei [[Doctolib GmbH]] ab dem **05.01.2026**. Es ist die primäre Quelle für die [[Doctolib GmbH – Gehalt 2026]]-Entität und eine kritische Komponente der Einnahmenseite für [[ESt 2026]] (Steuererklärung 2026).

## Stammdaten & Metadaten

| Feld | Wert |
|---|---|
| **Arbeitgeber** | Doctolib GmbH |
| **Eintrittsdatum** | 05.01.2026 |
| **Quelldatum** | 2026-06-12 (letzter Update) |
| **Steuerklasse** | 1 |
| **Krankenversicherung** | HEK (Hanse Ersatzkasse) |
| **Quelldatei** | raw/Privat/Finanzen/Einnahmen/Doctolib 2026.md |

---

## Monatliche Gehaltsstuktur

### Brutto-Komponenten

| Position | Betrag | Rhythmus |
|---|---|---|
| **Gehalt** | 6.300 € | monatlich (Basis) |
| **PKW-Sachbezug** | 364 € | monatlich (1%-Regel) |
| **EBV-Brutto (= Geldwert für Lohnsteuer)** | 6.664 € | monatlich |
| **Internetzuschuss** | 50 € | monatlich (§40 Abs. 2 EStG pauschal, steuerfrei) |

### Netto nach Abzügen

| | |
|---|---|
| **Netto/Monat** | 3.638,82 € |
| **Berechnung** | EBV 6.664 € − Lohnsteuer, Sozialversicherung, KV-Beitrag |

---

## PKW-Sachbezug (1%-Regelung)

| | |
|---|---|
| **Listenpreis Fahrzeug** | ~36.400 € |
| **1%-Monatsbetrag** | 364 € geldwerter Vorteil |
| **Behandlung** | Voll versteuert; auf Lohnsteuer angerechnet |
| **Audit-Hinweis** | Fahrtenbuch vs. 1%-Regel sollte überprüft werden; Dokumentation im [[P2 Diesen Monat]]-Backlog vermerkt |

---

## Monatliche Abrechnungen (Jan–Mai 2026 dokumentiert)

| Monat | Brutto (EBV) | Netto | Besonderheit |
|---|---|---|---|
| Jan 2026 | 5.487,10 € | 3.160,40 € | Anteilig 27/31 Tage (Eintritt 05.01) |
| Feb 2026 | 6.664 € | 3.638,82 € | Voller Monat |
| Mär 2026 | 6.664 € | 3.638,82 € | Voller Monat |
| Apr 2026 | 15.197 € | 8.249,96 € | **Q1-Bonus 8.533 € brutto** |
| Mai 2026 | 6.664 € | 3.638,82 € | Voller Monat |
| **Kumulativ Jan–Mai** | **41.040 €** | **22.327 €** | |

---

## Q1-Bonus & Jahresprognose

### Q1-Bonus (April 2026)

| | |
|---|---|
| **Betrag brutto** | 8.533 € |
| **In Abrechnungsmonat** | April 2026 |
| **Netto (geschätzt)** | ~6.611 € (basierend auf Märzrate + höhere Steuerkl.) |

### Jahresprognose 2026 (bei 3 angenommenen Quartals-Boni)

| | |
|---|---|
| **Laufendes Gehalt (12 Mo.)** | 79.968 € brutto |
| **Q-Boni (3×, angenommen)** | 25.600 € brutto (geschätzt; Q1-Bonus als Vorlage) |
| **Gesamtbrutto 2026** | ~105.568 € brutto |
| **Geschätzte Netto 2026** | ~66.416 € netto |

> ⚠️ **Annahme:** Drei weitere Quartals-Boni (Q2, Q3, Q4) analog zum Q1-Bonus werden angenommen. Die tatsächliche Höhe ist zum Zeitpunkt dieses Quelldokuments unbekannt.

---

## Verknüpfungen & Abhängigkeiten

### Abhängig von dieser Quelle
- [[Doctolib GmbH – Gehalt 2026]] — Entitätsseite (summarisch)
- [[00 Finanz-Übersicht]] — Einnahmen-Seite (Fixgehalt ~3.638,82 €/Mo verwendet)
- [[ESt 2026]] — Steuererklärung 2026 (brutto + Sachbezug zu erfassen)

### Querverweise im Quelldokument
- [[Fixkosten Übersicht]] — 61% des Netto in Fixkosten
- [[Consorsbank Girokonto 0250120493]] — Gehalt-Eingang (Bankkonto)
- [[P2 Diesen Monat]] — Fahrtenbuch-Audit vermerkt

---

## Audit-Hinweise

| Punkt | Status | Aktion |
|---|---|---|
| **Fahrtenbuch vs. 1%-Regel** | Ausstehend | Prüfung durch Steuerberater [[SP STB]] empfohlen |
| **Internetzuschuss-Dokumentation** | ✅ Korrekt | 50 €/Mo pauschal steuerfrei nach §40 Abs. 2 EStG |
| **Bonus-Regelmäßigkeit** | TBD | Quartalsweise regelmäßig oder gelegentlich? Klärung erforderlich für Jahresprognose |

---

## Steuerliche Implikationen für ESt 2026

- **Lohnsteuerklasse:** 1 (Standardfall)
- **Sachbezug (geldwerter Vorteil):** 364 €/Mo steuerpflichtig
- **Internetzuschuss:** 50 €/Mo steuerfrei
- **Bonus:** Quartalsweise, in jeweiligem Monat abgerechnet (April, Juli, Oktober, Januar)
- **Steuererklärungspflicht:** Ja, falls Einkünfte von Wagglz GmbH oder Provisionen hinzukommen (siehe [[ESt 2026]])

---

## Verwandte Seiten

- [[Doctolib GmbH – Gehalt 2026]] — Entitätsseite mit Zusammenfassung
- [[00 Finanz-Übersicht]] — Privat-Finanzen-Übersicht (Einnahmen-Komponente)
- [[ESt 2026]] — Steuererklärung 2026 (dieses Gehalt zu erfassen)
- [[Fixkosten Übersicht]] — Ausgaben vs. Netto-Einnahmen-Verhältnis
- [[SP STB]] — Steuerberater (Audit der Fahrtenbuch-Regel empfohlen)
- [[Consorsbank Girokonto 0250120493]] — Empfänger-Girokonto
- [[Oleg Personal Context]] — Arbeitnehmer

---

*Quelldokument erstellt: 2026-06-12*  
*Letzte Aktualisierung: 2026-06-17*  
*Status: Aktiv (laufende Abrechnungen ab 2026-01-05)*
