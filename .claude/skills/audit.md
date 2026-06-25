# /audit — Setup & Config Audit

Audit the Intelligence Hub setup against best practices, current conventions, or a reference source.

## Usage

```
/audit                    # general setup health check
/audit claude-code        # check Claude Code configuration gaps
/audit wiki               # wiki structure and conventions audit
```

## Steps

1. Read `.claude/settings.json`, `CLAUDE.md`, `.mcp.json`, `wiki/index.md`, `wiki/log.md`.
2. Check against the relevant reference (e.g. CLAUDE.md conventions, 32-tricks checklist).
3. Produce an Apple-style HTML report in `outputs/notes/YYYY-MM-DD-audit-*.html`.
4. Append to `wiki/log.md`.

## Report format

- Stats bar: items done / gaps / optional / not relevant
- Gap cards with pill badges (fehlt / teilweise / optional)
- Done grid with checkmarks
- Apple design: `#F5F5F7` bg, `#0071E3` accent, SF Pro fonts
