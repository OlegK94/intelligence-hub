---
title: "Claude Session — Finanzen (Template)"
type: source
tags: [template, claude, finance, privat-finanzen, kontext, session-struktur, finanzen-modul]
sources: ["raw/Privat/Finanzen/Templates/Claude Session – Finanzen.md"]
created: 2026-06-13
updated: 2026-06-17
summary: Reusable Claude conversation template für Finanzen-Themen; Kontext-Block (Person, Einkommen, Ausgaben, Unternehmen, Rehabilitation-Plan); 4 häufige Session-Typen (Bank-Statement-Analyse, Unternehmens-Entscheidung, Provisions-Allokation, Gesamtanalyse); Deutsch direkt & konkret
---

# Claude Session — Finanzen (Template)

## Überblick

Dieses Template ist ein **vordefinierter Gesprächsrahmen** für Claude-Sessions zum Thema **Privatfinanzen**. Es richtet sich an die Situation von [[Oleg Personal Context|Oleg]] und dient als Schnellstart-Struktur für wiederkehrende finanzielle Fragestellungen.

Der Template enthält:
1. Einen **universellen Kontext-Block** (Person, Einkommen, Ausgaben, Unternehmen)
2. Vier **häufige Session-Typen** mit vordefinierten Prompt-Strukturen
3. Ton-Vorgaben (direkt, konkret, keine Absicherungen, Deutsch)

## Kontext-Block (immer einfügen)

```
KONTEXT — NICHT NEU ERKLÄREN

Person: Oleg Kober, 32 J., Berlin. Sales bei Doctolib GmbH.

Privatfinanzen:
- Netto-Fixgehalt: 3.638,82 €/Mo
- Quartals-Provision: ~4.611 € netto (Jan/Apr/Jul/Okt)
- Kontostand: −1.405 € (Dispo) | Ersparnisse: 1,10 € | Depot: keines
- Strukturelles Jahresdefizit: −7.970 €
- VW-Bank Kredit: 681,57 €/Mo bis 11/2028 (ursprgl. Crypto-Investment → Wagglz)
- Kieferorthopädie: 176,53 €/Mo (Dr. Wiemann)
- Gesellschafterdarlehnen: ~357 €/Mo (Privat → Unternehmen)

Unternehmen:
- Wagglz GmbH (GF: Oleg Kober) — Jahresabschlüsse fällig 5.000 €
- OK Capital UG (GF: Oleg Kober) — gleiche Fälligkeit
- Gesamtbelastung Unternehmen: ~8.000 €/Jahr
- Rückflüsse aus Unternehmen: keine

Rehabilitationsplan aktiv — Phase 1 (Stabilisierung), Phase 2 (Juli-Reset geplant).

Ton: Direkt, konkret, keine Absicherungen. Deutsch.
```

## Session-Typ 1: Bank-Statement-Analyse

**Anwendungsfall:** Wo weicht die Realität von Schätzungen ab? Welche Hebel zur Defizitreduzierung?

```
[Kontext-Block oben]

Ich lade jetzt meine Kontoauszüge hoch (CSV-Export, [Zeitraum]).
Analysiere:
1. Tatsächliche monatliche Ein- und Ausgaben kategorisiert
2. Wo weicht die Realität von meinen Schätzungen ab?
3. Die 3 größten Hebel zur Defizitreduzierung
```

**Erwartete Claude-Outputs:**
- Kategorisierte Ausgabenanalyse
- Deviation-Report gegen Schätzungen
- Prioritäts-Ranking der Hebel (z.B. Fixkosten-Kürzungen vs. Einkommenserhöhung vs. Darlehen-Restrukturierung)

---

## Session-Typ 2: Unternehmens-Entscheidung

**Anwendungsfall:** Sollte Wagglz/OK Capital liquidiert, dormant bleiben oder weitergeführt werden?

```
[Kontext-Block oben]

Konkreter Kontext: [Wagglz / OK Capital — aktueller Stand]
Frage: [Liquidation / Dormancy / Weiterführung — was ist der optimale Weg?]
Entscheidungsgrundlage: [welche Dokumente sind vorhanden]
```

**Erwartete Claude-Outputs:**
- Pro/Contra-Analyse für jede Option
- Liquidations-Szenarien (Schulden, Verlustvortrag, Haftung)
- Kosten-Vergleich (Dormancy vs. Aktivität)
- Empfehlung mit Begründung

---

## Session-Typ 3: Provisions-Allokation

**Anwendungsfall:** Quartalsweise Provision €4.611 netto — wie soll sie optimiert eingesetzt werden?

```
[Kontext-Block oben]

Juli-Provision ~4.611 € netto steht an.
Aktuelle Verbindlichkeiten: [aktueller Dispo-Stand / offene Fälligkeiten]
Erstelle optimale Allokation nach Rehabilitation Plan Prioritäten.
```

**Erwartete Claude-Outputs:**
- Allokations-Matrix (Dispo-Ausgleich, Notfall-Puffer, Unternehmens-Kosten, Puffer für Phase 2)
- Liquidity-Szenarios (best-case / worst-case bei Provision-Verzögerung)
- Empfohlene Auszahlungs-Reihenfolge

---

## Session-Typ 4: Gesamtanalyse mit Dokumenten

**Anwendungsfall:** Umfassende Finanzplanung unter Einbezug von Steuererklärungen, Bankkonten, Unternehmens-Dokumenten

```
→ Nutze [[Master Prompt – Gesamtanalyse]] — vollständig kopieren
```

**Besonderheit:** Dieser Typ referenziert ein separates **Master-Prompt-Dokument** mit erweiterten Anforderungen. Siehe [[Master Prompt – Gesamtanalyse]] für vollständige Struktur.

---

## Ton-Vorgaben

- ✅ **Direkt & konkret** — keine akademische Ausschweifung
- ✅ **Zahlengetrieben** — konkrete €, %, Szenarien
- ✅ **Deutsch** — keine englischen Fachbegriffe, außer etabliert (Cashflow, COGS, EBIT)
- ❌ **Keine Absicherungen** — nicht „könnte", „möglicherweise", „unter Umständen"
- ❌ **Keine Platitüden** — nicht „es ist wichtig zu sparen" (offensichtlich)

## Verwendung

1. **Kopiere den Kontext-Block** am Anfang jedes Claude-Gesprächs
2. **Wähle einen Session-Typ** basierend auf der Fragestellung
3. **Ergänze die Placeholders** ([Zeitraum], [aktueller Stand], etc.)
4. **Sende an Claude** — der Template aktiviert sofort die richtige Analystiefef

## Verknüpfungen

- [[00 Finanz-Übersicht]] — Quelle für Kontext-Block-Daten
- [[Rehabilitation Plan]] — Philosophie hinter Session-Typ 3 (Provisions-Allokation)
- [[Wagglz GmbH]], [[OK Capital UG]] — Unternehmens-Entscheidung Kontext (Session-Typ 2)
- [[SP STB]] — Steuerberater (für Gesamtanalyse notwendig)
- [[Doctolib GmbH]] — Provision-Quelle
- [[Master Prompt – Gesamtanalyse]] — Extended version für Session-Typ 4
