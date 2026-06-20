# /lint — Wiki Health Check

Audit the wiki for inconsistencies, orphan pages, and stale claims.

## Usage

```
/lint           # report only
/lint --fix     # propose and apply fixes
```

## What to check

1. **Contradictions** — claims on different pages that conflict
2. **Stale claims** — content superseded by newer sources
3. **Orphan pages** — pages with no inbound wikilinks
4. **Missing entity pages** — entities mentioned in wikilinks but no page exists
5. **Missing cross-references** — obvious links that are absent
6. **Outdated index** — `wiki/index.md` entries missing or with wrong summaries

## CLI

```bash
python3 tools/lint.py
python3 tools/lint.py --fix
```

## Output

- Write a lint report to `outputs/notes/YYYY-MM-DD-lint-report.md`
- Append one entry to `wiki/log.md`
- If `--fix`: apply fixes and summarize what changed
