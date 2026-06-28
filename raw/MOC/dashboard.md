---
title: Intelligence Hub Dashboard
type: moc
tags: [dashboard, navigation, moc]
created: 2026-06-28
updated: 2026-06-28
---

# Intelligence Hub Dashboard

> Zentraler Einstiegspunkt. Alle Live-Abfragen via Dataview.

---

## Aktive Projekte

```dataview
TABLE status, priority, modul
FROM "raw/Business/Cafe/performance-cafe/research"
WHERE status != "fertig"
SORT priority ASC
```

---

## Research Sprints (offen)

```dataview
TABLE question, started, confidence_overall
FROM "wiki/syntheses" OR "outputs/notes"
WHERE type = "research-sprint" AND status = "in-progress"
SORT started DESC
```

---

## Wiki Neueste Seiten

```dataview
TABLE type, summary
FROM "wiki"
WHERE type != "index"
SORT file.mtime DESC
LIMIT 15
```

---

## Offene Tasks

```tasks
not done
path includes raw
group by path
limit 20
```

---

## Synthesen & Vergleiche

```dataview
TABLE type, summary, file.mtime as "Erstellt"
FROM "wiki/syntheses" OR "wiki/comparisons"
SORT file.mtime DESC
```

---

## Schnell-Navigation

| Bereich | Link |
|---------|------|
| Performance Cafe | [[raw/Business/Cafe/performance-cafe/CLAUDE]] |
| Wagglz | [[raw/Business/Wagglz/Wagglz GmbH]] |
| OK Capital | [[raw/Business/OK-Capital/OK Capital UG]] |
| Finanzen | [[raw/Privat/Finanzen/00 Finanz-Uebersicht]] |
| Cyprus | [[wiki/concepts/Cyprus Tax Regime]] |
| Wiki Index | [[wiki/index]] |

---

## Claude Code Befehle

```bash
# Research Sprint
python3 tools/research_sprint.py "Deine Frage" --type synthesis
python3 tools/research_sprint.py "A vs B" --type comparison
python3 tools/research_sprint.py "Thema" --output slides

# Wiki
python3 tools/search.py "Suchbegriff"
python3 tools/ingest.py --scope inbox
python3 tools/status.py
python3 tools/lint.py
```
