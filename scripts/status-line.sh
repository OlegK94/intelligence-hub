#!/bin/bash
# Status line: shown in Claude Code terminal footer

VAULT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/IntelligenceHub"

# Count open tasks
OPEN_TASKS=$(grep -c '^\- \[ \]' "$VAULT_DIR/outputs/notes/open-tasks.md" 2>/dev/null || echo "0")

# Count inbox files
INBOX=$(ls "$VAULT_DIR/raw/inbox/" 2>/dev/null | grep -v '^\.' | wc -l | tr -d ' ')

# Last ingest time from log
LAST_INGEST=$(grep "^## \[" "$VAULT_DIR/wiki/log.md" 2>/dev/null | tail -1 | sed 's/## \[\(.*\)\] .*/\1/')

echo "📋 Tasks: $OPEN_TASKS offen  |  📥 Inbox: $INBOX  |  🔄 Letzter Ingest: ${LAST_INGEST:-—}"
