#!/bin/bash
# PreCompact hook: saves important context before Claude compresses conversation

VAULT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/IntelligenceHub"
DATE=$(date "+%Y-%m-%d %H:%M")
OUT="$VAULT_DIR/outputs/notes/compact-snapshots.md"

# Append current open tasks + log snippet before compaction
cat >> "$OUT" 2>/dev/null << SNAPSHOT

## Komprimierung — $DATE

### Offene Tasks
$(cat "$VAULT_DIR/outputs/notes/open-tasks.md" 2>/dev/null)

### Letzte Log-Einträge
$(tail -20 "$VAULT_DIR/wiki/log.md" 2>/dev/null)

---
SNAPSHOT

exit 0
