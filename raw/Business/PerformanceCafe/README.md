# Performance Café — Projekt-Setup

**Perform now. Live longer.**

---

## Setup in 3 Schritten

### 1. Ordner als Obsidian Vault öffnen
Obsidian → "Open folder as vault" → diesen Ordner wählen.
Alle `.md` Dateien erscheinen sofort in der Sidebar.

### 2. In Cursor öffnen
Cursor → "Open Folder" → diesen Ordner wählen.
`.cursor/rules/performance_cafe.mdc` wird automatisch als Projektkontext geladen.
Jede AI-Anfrage in Cursor kennt das Produkt, die Zielgruppe, die kritischen Blocker.

### 3. Claude Code verbinden
Claude Code liest `CLAUDE.md` zu Beginn jeder Session automatisch.
```bash
cd performance-cafe
claude  # startet Claude Code mit vollem Projektkontext
```

---

## Workflow

### Research-Module ausführen (Claude Code)
```bash
# Einzelnes Modul
claude "Arbeite Modul 1 (Ingredienzen Datenbank) aus.
Lies research/00_master_brief.md für den vollständigen Auftrag.
Schreibe Ergebnisse nach research/02_ingredienzen_db.md"

# Priorität: Regulatorik zuerst (Blocker!)
claude "Kläre den EU Novel Food Status für NMN, Urolithin A und Spermidine.
Schreibe Ergebnisse nach research/06_regulatorik.md"

# Module verknüpfen
claude "Lies research/02_ingredienzen_db.md und research/06_regulatorik.md.
Identifiziere alle Inhaltsstoffe mit regulatorischen Blocker.
Aktualisiere CLAUDE.md mit den Erkenntnissen."
```

### In Cursor (AI-Anfragen mit @-Referenzen)
```
@research/02_ingredienzen_db.md Welche Inhaltsstoffe haben Patent-Konflikte?
@research/06_regulatorik.md Erstelle eine Prioritätsliste der regulatorischen Risiken
@models/unit_economics.py Fülle die Rohstoffpreise aus @models/ingredient_db.csv
```

### In Obsidian
- Alle Research-Outputs erscheinen direkt als Notizen
- `[[wikilinks]]` zwischen Modulen funktionieren automatisch
- Graph View zeigt Verbindungen zwischen Modulen
- Dataview Plugin: Modul-Status-Tabelle aus Frontmatter

---

## Prioritäts-Reihenfolge

```
1. research/06_regulatorik.md   ⚠️ KRITISCH — bestimmt welche Stoffe erlaubt sind
2. legal/ip_landscape.md        ⚠️ KRITISCH — Amazentis + Chromadex Patente
3. research/02_ingredienzen_db.md  → erst nach Regulatorik sinnvoll
4. research/03_kaffee_specs.md
5. research/04_marktanalyse.md
6. research/05_prototyp_partner.md
7. research/07_business_case.md    → erst wenn COGS-Daten aus Modul 1+4 vorliegen
8. models/unit_economics.py        → erst wenn Rohstoffpreise bekannt
```

---

## Dateistruktur

```
performance-cafe/
├── CLAUDE.md                      ← Claude Code Kontext (master)
├── README.md                      ← du bist hier
├── .cursor/rules/
│   └── performance_cafe.mdc       ← Cursor AI Kontext
├── research/
│   ├── 00_master_brief.md         ← vollständiger Research-Auftrag
│   ├── 01_longevity_science.md    ← Modul 0
│   ├── 02_ingredienzen_db.md      ← Modul 1 ⭐
│   ├── 03_kaffee_specs.md         ← Modul 2
│   ├── 04_marktanalyse.md         ← Modul 3
│   ├── 05_prototyp_partner.md     ← Modul 4
│   ├── 06_regulatorik.md          ← Modul 5 ⚠️
│   └── 07_business_case.md        ← Modul 6
├── brand/
│   └── naming_brief.md            ← Modul 7
├── legal/
│   ├── ip_landscape.md            ← Modul 8 ⚠️
│   └── entity_structure.md        ← GmbH, Markenanmeldung
├── models/
│   ├── unit_economics.py          ← COGS + Margin Kalkulation
│   └── ingredient_db.csv          ← Strukturierte Inhaltsstoff-DB
└── ops/
    ├── supplier_list.md           ← Rohstoff-Lieferanten
    └── certification_roadmap.md   ← Kölner Liste → Informed Sport → NSF
```

---

## Bekannte Kritische Entscheidungen (vor Prototyp klären)

| Frage | Blocker für | Datei |
|-------|------------|-------|
| NMN EU Novel Food Status 2025? | Stack-Entscheidung | research/06_regulatorik.md |
| Amazentis Patent Urolithin A — Lizenz? | Stack + Kosten | legal/ip_landscape.md |
| NAC Geruchs-Maskierung — wie? | Prototyp | research/05_prototyp_partner.md |
| Lebensmittel vs. NEM — welcher Weg? | Regulatorik + Marketing | research/06_regulatorik.md |
| Kölner Liste CMO-Anforderungen? | CMO-Auswahl | ops/certification_roadmap.md |
