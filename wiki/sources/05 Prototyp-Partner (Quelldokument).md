TAGS: [performance-cafe, modul-04, prototyp-partner, recherche, placeholder, leer, claude-code, auftragsbrief]
SOURCES: ["raw/raw/Performance Coffee Brand/recherche/_archiv/05_prototyp_partner.md"]
CREATED: 2026-06-14
UPDATED: 2026-06-14
SUMMARY: Quelldokument Modul 04 (mislabeled als „05") — Prototyp-Partner Research für Performance Coffee Brand; Status: leer/noch nicht bearbeitet; Claude Code Auftrag zur Ausfüllung mit Web-Recherche nach aktuellen Prototyping- und CMO-Partner-Optionen (2024/2025); abhängig von Modul 00 Auftragsbrief; Quellenangaben am Ende jedes Abschnitts erforderlich

---

# 05 Prototyp-Partner — Quelldokument

## Überblick

Dieses Quelldokument (`raw/raw/Performance Coffee Brand/recherche/_archiv/05_prototyp_partner.md`, erstellt 2026-06-14) ist das **Modul 04-Placeholder** (intern als „05" benannt) der strukturierten [[Performance Coffee Brand]]-Recherche. Der Status ist explizit **leer — noch nicht bearbeitet** — es handelt sich um einen verwalteten Platzhalter mit folgendem Claude Code-Auftrag:

> **Claude Code Befehl:**  
> Arbeite Modul 4 (Prototyp-Partner) aus.  
> Lies recherche/00_Auftragsbrief.md für den vollständigen Auftrag.  
> Schreibe alle Ergebnisse nach recherche/_archiv/05_prototyp_partner.md.  
> Nutze web_search für aktuelle Daten (2024/2025).  
> Quellenangaben am Ende jedes Abschnitts.

---

## Metadaten

| | |
|---|---|
| **Status** | leer — noch nicht bearbeitet |
| **Modul** | 4 (Prototyp-Partner) — intern als „05" benannt |
| **Priorität** | mittel |
| **Datum Quelldokument** | 2026-06-14 |
| **Abhängigkeit** | recherche/00_Auftragsbrief.md (Modul 00) |
| **Pfad** | raw/raw/Performance Coffee Brand/recherche/_archiv/05_prototyp_partner.md |

---

## Erwartete Inhalte (aus der Struktur)

Das Modul ist als Platzhalter mit vermutlich folgender Struktur konzipiert:

1. **Prototyping-Optionen**
   - In-house Prototyping (mit [[Wagglz GmbH]] Partner-Röster oder Laborausstattung)
   - Third-Party Prototyping (spezialisierte Prototyping-Services)
   - CMO-Prototyping (Kandidaten aus der [[CMO Sourcing Performance Coffee]] Liste)

2. **Kandidaten-Evaluation**
   - ≥3–5 Partner-Quotes für Prototyping
   - Turnaround-Zeit (2–4 Wochen?)
   - Kosten pro Batch (Pilot: 500–2.000 Sachets)
   - Qualitätssicherung und Sensorische Tests

3. **Stack-A-Prototyp-Spezifikationen**
   - Formulierung Final (L-Theanin, L-Tyrosine, Alpha-GPC, Koffein, B-Vitamine, Ashwagandha, Kaffee-Blend)
   - Verpackungs-Spezifikation (Sachets, Materialien, Labels)
   - Dosierungskontrolle und Chargen-Rückverfolgbarkeit

4. **Sensory Testing Protocol**
   - Blind Panel-Design
   - Taster-Auswahl (n=5–10, Performance-fokussiert)
   - Bewertungs-Dimensionen (Geschmack, Mouthfeel, Wirkung-Wahrnehmung, NPS)

5. **Timeline & Milestones**
   - Prototyp-Anfrage Versand: Woche X
   - Prototyp-Rückkehr erwartet: Woche Y
   - Sensory Test durchführen: Woche Z
   - Formulierung Finalisierung: Woche Z+2

6. **Quellenangaben** — Web-Recherche-Belege für alle Kandidaten, Kosten, Lead-Times

---

## Claude Code — Auftragsdetails

Der Auftrag richtet sich explizit an Claude Code:

```
Arbeite Modul 4 (Prototyp-Partner) aus.
Lies recherche/00_Auftragsbrief.md für den vollständigen Auftrag.
Schreibe alle Ergebnisse nach recherche/_archiv/05_prototyp_partner.md.
Nutze web_search für aktuelle Daten (2024/2025).
Quellenangaben am Ende jedes Abschnitts.
```

**Interpretation:** Dieses Quelldokument ist ein verwalteter Arbeitsplatz für eine **Claude Code-Ausführung** — nicht für manuelles Eintippen konzipiert. Es beschreibt die erwartete Struktur und den Forschungsauftrag, dem Claude Code folgen soll.

---

## Status & Blockierende Abhängigkeiten

Dieses Modul ist blockiert durch:

1. **[[00 Auftragsbrief Performance Coffee]]** (Modul 00)
   - Finale Stack-A-Spezifikation erforderlich (Dosiering aller Inhaltsstoffe)
   - Zielformulierungen und Test-Kriterien
   - Budget für Prototyping

2. **[[02 Ingredienzen Datenbank Performance Coffee (Quelldokument)]]** (Modul 01)
   - Final-Inhaltsstoff-Sourcing muss verfügbar sein
   - Supplier-Kontakte für Prototyping-Charge

3. **[[03 Kaffee-Spezifikation Performance Coffee (Quelldokument)]]** (Modul 03)
   - Blend-Spezifikation muss feststehen
   - Röstprofil-Anforderungen

4. **[[CMO Sourcing Performance Coffee]]** (Parallel-Modul)
   - Prototyping-Partner könnte gleichzeitig CMO-Kandidat sein
   - Lead-Time-Überlegungen

---

## Verknüpfung im Projekt-Workflow

| Modul | Abhängigkeit | Status |
|---|---|---|
| **00 Auftragsbrief** | Primär | ✅ Existiert |
| **01 Ingredienzen DB** | Vorlage | ⏳ Ausstehend |
| **03 Kaffee-Spezifikation** | Vorlage | ⏳ Ausstehend |
| **04 Marktanalyse** | Parallel | ⏳ Ausstehend |
| **04-alt Prototyp-Partner** | Diese (Placeholder) | ⏳ Ausstehend (Claude Code) |
| **05 Recht & Regulatorik** | Parallel | ✅ Existiert |
| **Prototyping & Sensory Tests** | Abhängig von diesem Modul | ⏳ Blockiert |
| **06 Kalkulation & Pricing** | Abhängig von Prototyp-Kosten | ⏳ Blockiert (Prototyp-Budgets erforderlich) |

---

## Nächste Schritte

1. **Claude Code Ausführung:**
   - `python tools/ingest.py --claude-code 05_prototyp_partner`
   - oder manuelle Weiterleitung an Claude mit Auftrag + recherche/00_Auftragsbrief.md

2. **Validierung nach Ausfüllung:**
   - Überprüfung der Web-Recherche-Quellen (CMO-Websites, Prototyping-Service-Verzeichnisse)
   - Kosten-Schätzungen gegen [[CMO Sourcing Performance Coffee]] validieren
   - Lead-Time-Annahmen gegen bekannte CMO-SLAs prüfen

3. **Integration:**
   - Prototyping-Partner-Quoten in die [[CMO Sourcing Performance Coffee]]-Evaluation integrieren
   - Sensory-Test-Protokoll in [[02 Produkt & Rezeptur Performance Coffee]] einfließen lassen
   - Prototyping-Kosten in [[06 Kalkulation & Pricing Performance Coffee]] COGS-Modell aufnehmen

---

## Verwandte Seiten

- [[00 Auftragsbrief Performance Coffee]] — Parent-Modul mit Kontext
- [[Performance Coffee Brand]] — Projekt-Entität
- [[02 Ingredienzen Datenbank Performance Coffee (Quelldokument)]] — Modul 01 (vorgelagert)
- [[03 Kaffee-Spezifikation Performance Coffee (Quelldokument)]] — Modul 03 (vorgelagert)
- [[04 Marktanalyse & Wettbewerb (Quelldokument)]] — Modul 04 (parallel)
- [[CMO Sourcing Performance Coffee]] — Paralleles Evaluierungsmodul
- [[05 Recht & Regulatorik (EU Lebensmittel/Supplements)]] — Modul 05 (parallel, Compliance-Kontext)
- [[06 Kalkulation & Pricing Performance Coffee]] — abhängig (Prototyping-Kosten erforderlich)
- [[02 Produkt & Rezeptur Performance Coffee]] — nachgelagert (Formulierung wird durch Prototyping validiert)
- [[Prinova]], [[Lehvoss Nutrition]], [[Nutri-Epitech]], [[Aidea]], [[Herbafit]] — mögliche Prototyping-Partner
