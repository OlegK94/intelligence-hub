# Intelligence Hub Dashboard

> LLM maintains `wiki/` · You curate `raw/` · Obsidian is the viewer

## System Status

```bash
python3 tools/status.py
```

## Quick Actions

| Aktion | Befehl |
|--------|--------|
| Inbox ingesten | `python3 tools/ingest.py` |
| Alles pending | `python3 tools/batch_ingest.py` |
| Frage stellen | `python3 tools/query.py "..."` |
| Wiki prüfen | `python3 tools/lint.py` |
| Suchen | `python3 tools/search.py "..."` |

**Workflow:** Clip → `Cmd+Shift+D` → ingest

## Aktive Prioritäten (privat)

| P | Thema | Nächster Schritt |
|---|-------|------------------|
| P0 | [[Café Berlin — Partnership Hai]] | Session 14.06.2026 |
| P1 | [[Hyrox 10-Week Training]] | Wettkampf anmelden |
| P1 | [[Health Protocol Master]] | Protokoll + Scan Sep 2026 |
| P2 | [[Password Manager Migration]] | Proton Pass evaluieren |
| P2 | [[Allianz Insurance Consolidation]] | 3 Angebote |

## Ordnerstruktur raw/

| Bereich | Pfad |
|---------|------|
| **Privat** | `raw/Privat/` — Performance, Tech, Finanzen, Versicherungen |
| **Business** | `raw/Business/Wagglz/`, `Business/Cafe/`, `Business/OK-Capital/` |
| **Inbox** | `raw/inbox/` — neue Quellen |
| **Archiv** | `raw/_archiv/Work/` — nicht ingesten |

→ Details: `raw/README.md`


## Wiki Status

```dataview
TABLE WITHOUT ID
  file.link AS Article,
  type AS Type,
  summary AS Summary,
  updated AS Updated
FROM "wiki"
WHERE file.name != "index" AND file.name != "log" AND file.name != "Dashboard"
SORT updated DESC
LIMIT 25
```

## Open Tasks

```tasks
not done
path includes raw
priority is above none
sort by priority
group by priority
limit 15
```

## Recent Ingests

```dataview
TABLE WITHOUT ID
  file.link AS Source
FROM "wiki/sources"
SORT file.mtime DESC
LIMIT 10
```

## Index & Log

→ [[index]] · [[log]] · Setup: `SETUP-TODOS.md`
