#!/bin/bash
# Wird nach jeder Claude Code Session automatisch ausgeführt (Stop Hook)
# Prüft ob neue Dateien vorhanden sind und triggert smart_ingest

VAULT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$VAULT_DIR/outputs/notes/hooks.log"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] post-session: prüfe neue Dateien..." >> "$LOG"

# Prüfe ob neue Dateien in inbox oder Clippings
NEW_IN_INBOX=$(ls "$VAULT_DIR/raw/inbox/"*.md 2>/dev/null | wc -l | tr -d ' ')
NEW_IN_CLIPPINGS=$(ls "$VAULT_DIR/Clippings/"*.md 2>/dev/null | wc -l | tr -d ' ')

if [ "$NEW_IN_INBOX" -gt 0 ] || [ "$NEW_IN_CLIPPINGS" -gt 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] post-session: $NEW_IN_INBOX inbox + $NEW_IN_CLIPPINGS clippings → smart_ingest" >> "$LOG"
    cd "$VAULT_DIR"
    source .env 2>/dev/null || true
    python3 tools/smart_ingest.py >> "$LOG" 2>&1
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] post-session: keine neuen Dateien" >> "$LOG"
fi
