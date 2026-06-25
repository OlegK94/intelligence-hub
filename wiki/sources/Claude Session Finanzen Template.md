---
title: Claude Session Finanzen Template
type: source
tags: [template, claude, finanzen, session]
sources: ["raw/Privat/Finanzen/Templates/Claude Session – Finanzen.md"]
created: 2026-06-16
updated: 2026-06-16
summary: Template für Claude Finance-Sessions — kompakter Kontext-Block + vier vordefinierte Session-Typen (Kontoauszug-Analyse, Unternehmens-Entscheidung, Provisions-Allokation, Gesamtanalyse)
---

Claude Session Finanzen Template ist das Kurzformat-Template für neue Claude-Gespräche zu Finanzthemen. Im Gegensatz zum vollständigen [[Master Prompt Gesamtfinanzanalyse Source Detail]] ist es für schnelle, fokussierte Sessions konzipiert (source: [[Claude Session Finanzen Template]]).

## Verwendung

Kontext-Block oben in jede neue Session einfügen, dann konkrete Frage stellen. Der Block enthält alle Kernfakten von [[Oleg Personal Context]] in kompakter Form — keine Neuexploration nötig.

## Vier Session-Typen

**Bank-Statement-Analyse:** CSV-Export hochladen → Ausgaben kategorisieren → Abweichung von Schätzwerten → 3 größte Hebel zur Defizitreduzierung.

**Unternehmens-Entscheidung:** Aktuellen Wagglz/OK Capital Status beschreiben → konkrete Entscheidungsfrage stellen (Liquidation/Dormancy/Weiterführung) → Entscheidungsgrundlage angeben.

**Provisions-Allokation:** Juli-Provision ~4.611 € netto → aktuelle Verbindlichkeiten → optimale Allokation nach [[Finanz Rehabilitation Plan Source Detail]] Prioritäten.

**Gesamtanalyse mit Dokumenten:** → [[Master Prompt Gesamtfinanzanalyse Source Detail]] verwenden.

## Kontext-Block (Kern-Fakten)

Das Template enthält einen vorkonfigurierten Kontext-Block mit:
- Netto-Fixgehalt: 3.638,82 €/Mo
- Quartals-Provision: ~4.611 € netto (Jan/Apr/Jul/Okt)
- Kontostand: −1.405 € (Dispo)
- Strukturelles Jahresdefizit: −7.970 €
- VW-Bank Kredit: 681,57 €/Mo bis 11/2028
- Wagglz GmbH + OK Capital UG: Gesamtbelastung ~8.000 €/Jahr

## Verknüpfte Seiten

- [[Master Prompt Gesamtfinanzanalyse Source Detail]] — vollständiges Analyse-Template
- [[Claude Session Template Performance]] — Performance-Equivalent
- [[Finanz Rehabilitation Plan Source Detail]] — Rehabilitation-Prioritäten
- [[Oleg Personal Context]] — vollständige Personenbeschreibung
