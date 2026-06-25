#!/bin/bash
# PostToolUse Hook — läuft nach jedem Write/Edit in einer Claude Session
# Nur aktiv wenn Datei in raw/ oder Clippings/ geändert wurde

VAULT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$VAULT_DIR/outputs/notes/hooks.log"

# Letzten Edit aus Hook-Kontext prüfen (Claude Code setzt CLAUDE_TOOL_INPUT)
LAST_FILE="${CLAUDE_TOOL_INPUT:-}"

if echo "$LAST_FILE" | grep -qE "raw/inbox|Clippings|raw/Privat/Finanzen"; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] on-file-change: relevante Datei geändert → markiere für Ingest" >> "$LOG"
    touch "$VAULT_DIR/.pending_ingest"
fi
