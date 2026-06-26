---
title: "Claude Session – Finanzen Template"
type: source
tags: [template, claude, finance, oleg, doctolib, wagglz, ok-capital, rehabilitationsplan, provisions-allokation, bank-statement, kontoauszug]
sources: ["raw/Finanzdaten/ObsidianVault/Templates/Claude Session – Finanzen.md"]
created: 2026-06-13
updated: 2026-06-13
summary: Template für Claude-Finanz-Sessions von Oleg Kober — enthält standardisierten Kontext-Block (Netto-Fixgehalt, Provision, Dispo, Unternehmen, Rehabilitationsplan) sowie vier Session-Typen: Bank-Statement-Analyse, Unternehmens-Entscheidung, Provisions-Allokation und Gesamtanalyse; konsolidiert alle finanziellen Schlüsselparameter in einem wiederverwendbaren Prompt-Format
---

# Claude Session – Finanzen Template

## Überblick

Dieses Quelldokument ist ein **Prompt-Template** für neue Claude-Gespräche zum Thema Finanzen. Es enthält einen standardisierten **Kontext-Block**, der die wesentlichen Finanzdaten von [[Oleg Personal Context|Oleg Kober]] zusammenfasst, sowie vier strukturierte Session-Typen für wiederkehrende Finanzanalysen.

> Dieses Template ist primär eine **Referenzquelle** — die darin enthaltenen Finanzdaten fließen in die Entitätsseite [[Oleg Personal Context]] und in die [[MOC Finanzen]] ein.

---

## Kontext-Block (Schlüsselparameter)

### Person

| Parameter | Wert |
|---|---|
| **Name** | Oleg Kober |
| **Alter** | 32 Jahre |
| **Wohnort** | Berlin |
| **Arbeitgeber** | Doctolib GmbH (Sales) |

### Privatfinanzen (Snapshot)

| Parameter | Wert |
|---|---|
| **Netto-Fixgehalt** | 3.638,82 €/Monat |
| **Quartals-Provision** | ~4.611 € netto (Jan/Apr/Jul/Okt) |
| **Kontostand** | −1.405 € (Dispo) |
| **Ersparnisse** | 1,10 € |
| **Depot** | keines |
| **Strukturelles Jahresdefizit** | −7.970 € |

### Verbindlichkeiten / Laufende Belastungen

| Posten | Betrag/Mo | Anmerkung |
|---|---|---|
| **VW-Bank Kredit** | 681,57 € | bis 11/2028; ursprgl. Crypto-Investment → Wagglz |
| **Kieferorthopädie Dr. Wiemann** | 176,53 € | laufend |
| **Gesellschafterdarlehen** | ~357 € | Privat → Unternehmen |

> **Wichtiger Kontext:** Der VW-Bank-Kredit wurde ursprünglich für ein Crypto-Investment aufgenommen und in Wagglz geflossen — er ist damit direkt mit dem Unternehmensengagement verknüpft.

### Unternehmen

| Unternehmen | Rolle | Belastung |
|---|---|---|
| [[Wagglz GmbH]] | Geschäftsführer | Jahresabschlüsse ~5.000 € fällig |
| [[OK Capital UG]] | Geschäftsführer | Jahresabschlüsse ~5.000 € fällig |
| **Gesamtbelastung Unternehmen** | — | ~8.000 €/Jahr |
| **Rückflüsse aus Unternehmen** | — | keine |

### Rehabilitationsplan

- **Phase 1:** Stabilisierung (aktiv)
- **Phase 2:** Juli-Reset (geplant)
- **Provisions-Allokation:** Juli-Provision (~4.611 €) ist der nächste große Hebel

---

## Session-Typen

Das Template definiert vier strukturierte Prompt-Typen für wiederkehrende Finanzanalysen:

### 1. Bank-Statement-Analyse

**Ziel:** Tatsächliche monatliche Ein- und Ausgaben analysieren, Abweichungen von Schätzungen identifizieren, 3 größte Hebel zur Defizitreduzierung finden.

**Ablauf:**
1. Kontext-Block einfügen
2. Kontoauszug als CSV hochladen (Zeitraum angeben)
3. Kategorisierung + Abweichungsanalyse + Top-3-Hebel

### 2. Unternehmens-Entscheidung

**Ziel:** Optimalen Weg für [[Wagglz GmbH]] oder [[OK Capital UG]] bestimmen (Liquidation / Dormancy / Weiterführung).

**Ablauf:**
1. Kontext-Block einfügen
2. Aktuellen Unternehmensstand beschreiben
3. Entscheidungsgrundlage (verfügbare Dokumente) angeben

### 3. Provisions-Allokation

**Ziel:** Optimale Allokation der Juli-Provision (~4.611 €) nach Rehabilitationsplan-Prioritäten.

**Ablauf:**
1. Kontext-Block einfügen
2. Aktuellen Dispo-Stand + offene Fälligkeiten angeben
3. Prioritätsbasierte Allokationsempfehlung erhalten

### 4. Gesamtanalyse mit Dokumenten

**Ziel:** Vollständige Finanzanalyse mit allen Dokumenten.

**Verweis:** → [[Master Prompt Gesamtanalyse]] — vollständig kopieren

---

## Datenqualität und Einordnung

| Parameter | Status |
|---|---|
| **Kontostand** | Momentaufnahme (Stand Erstellungsdatum 2026-06-13) — kann abweichen |
| **Provision** | ~4.611 € ist Schätzung/historischer Wert — tatsächliche Auszahlung variiert |
| **Unternehmenszahlen** | Schätzwerte (5.000 €/Unternehmen für Jahresabschlüsse) |
| **Kreditraten** | Präzise (681,57 €/Mo VW-Bank, 176,53 €/Mo KFO) |
| **Gesellschafterdarlehen** | ~357 €/Mo (Schätzwert) |

---

## Verhältnis zu anderen Templates

| Template | Fokus |
|---|---|
| **Claude Session – Finanzen** (diese Seite) | Finanzen, Unternehmensstruktur, Rehabilitationsplan |
| [[Claude Session Template Performance]] | Körper, Training, Supplements, Gesundheitsmetriken |
| [[Master Prompt Gesamtanalyse]] | Vollständige Gesamtanalyse (referenziert aus diesem Template) |

---

## Schlüsselbeobachtungen für das Wiki

1. **Strukturelles Defizit −7.970 €/Jahr** — dies ist der zentrale Problemparameter, der alle Finanzentscheidungen rahmt
2. **Provisions-Allokation als Haupthebel** — vierteljährliche ~4.611 € sind die einzige größere diskretionäre Einnahme
3. **Doppelte Unternehmensbelastung** — ~8.000 €/Jahr für Jahresabschlüsse bei null Rückfluss macht [[Wagglz GmbH]] und [[OK Capital UG]] zu primären Optimierungskandidaten
4. **Gesellschafterdarlehen ~357 €/Mo** — Oleg leiht dem eigenen Unternehmen Geld (aus bereits defizitären Privatmitteln)
5. **VW-Bank-Kredit bis 11/2028** — langfristige Belastung, die direkt aus dem Unternehmensengagement stammt

---

## Verwandte Seiten

- [[Oleg Personal Context]] — Zentrales Personenprofil (enthält diese Finanzdaten aggregiert)
- [[MOC Finanzen]] — Übergeordnete Finanz-MOC
- [[Wagglz GmbH]] — Erstes Unternehmen (Jahresabschlüsse, keine Rückflüsse)
- [[OK Capital UG]] — Zweites Unternehmen (gleiche Situation)
- [[Rehabilitationsplan Finanzen]] — Phase 1 (Stabilisierung) + Phase 2 (Juli-Reset)
- [[Claude Session Template Performance]] — Schwester-Template für Performance-Themen
- [[Master Prompt Gesamtanalyse]] — Vollständige Analyse-Vorlage (aus diesem Template referenziert)
- [[Fixkosten Übersicht]] — Monatliche Fixkosten im Detail
- [[Provisions-Allokation Juli 2026]] — Konkreter Anwendungsfall Session-Typ 3
