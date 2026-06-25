#!/bin/bash
# SessionStart hook: loads current wiki context into Claude's context window

VAULT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/IntelligenceHub"

# Recent log (last 10 entries)
LOG=$(tail -40 "$VAULT_DIR/wiki/log.md" 2>/dev/null | head -c 1500)

# Open tasks from outputs (if exists)
TASKS=""
if [ -f "$VAULT_DIR/outputs/notes/open-tasks.md" ]; then
    TASKS=$(cat "$VAULT_DIR/outputs/notes/open-tasks.md" 2>/dev/null | head -c 800)
fi

# Inbox files waiting for ingest
INBOX=$(ls "$VAULT_DIR/raw/inbox/" 2>/dev/null | grep -v "^$" | head -20)
INBOX_COUNT=$(echo "$INBOX" | grep -c "." 2>/dev/null || echo "0")

# Recent wiki changes (last 24h)
RECENT=$(find "$VAULT_DIR/wiki" -name "*.md" -newer "$VAULT_DIR/wiki/log.md" -mtime -1 2>/dev/null | xargs -I{} basename {} 2>/dev/null | head -10)

DATE=$(date "+%Y-%m-%d %H:%M")

MSG="=== IntelligenceHub Session Start — $DATE ===

INBOX: $INBOX_COUNT Dateien warten auf Ingest
$([ -n "$INBOX" ] && echo "$INBOX" | sed 's/^/  - /')

OFFENE AUFGABEN:
${TASKS:-Keine offenen Tasks in outputs/notes/open-tasks.md}

LETZTE LOG-EINTRÄGE:
$LOG"

# Output as JSON systemMessage so Claude sees it
python3 -c "
import json, sys
msg = sys.stdin.read()
print(json.dumps({'systemMessage': msg}))
" <<< "$MSG"
