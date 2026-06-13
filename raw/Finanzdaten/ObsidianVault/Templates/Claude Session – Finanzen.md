---
tags: [template, claude, finance]
created: 2026-06-13
---

# Template — Claude Session: Finanzen

> Für neue Gespräche zum Thema Finanzen. Kontext oben einfügen, dann konkrete Frage stellen.

---

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

---

## Häufige Session-Typen

### Bank-Statement-Analyse
```
[Kontext-Block oben]

Ich lade jetzt meine Kontoauszüge hoch (CSV-Export, [Zeitraum]).
Analysiere:
1. Tatsächliche monatliche Ein- und Ausgaben kategorisiert
2. Wo weicht die Realität von meinen Schätzungen ab?
3. Die 3 größten Hebel zur Defizitreduzierung
```

### Unternehmens-Entscheidung
```
[Kontext-Block oben]

Konkreter Kontext: [Wagglz / OK Capital — aktueller Stand]
Frage: [Liquidation / Dormancy / Weiterführung — was ist der optimale Weg?]
Entscheidungsgrundlage: [welche Dokumente sind vorhanden]
```

### Provisions-Allokation
```
[Kontext-Block oben]

Juli-Provision ~4.611 € netto steht an.
Aktuelle Verbindlichkeiten: [aktueller Dispo-Stand / offene Fälligkeiten]
Erstelle optimale Allokation nach Rehabilitation Plan Prioritäten.
```

### Gesamtanalyse mit Dokumenten
→ Nutze [[Master Prompt – Gesamtanalyse]] — vollständig kopieren

