#!/bin/bash
# raw-watcher.sh — Automatisch triggered wenn neue Dateien in raw/ landen
# Läuft via launchd WatchPaths auf raw/

VAULT_DIR="$HOME/Documents/Intelligence-Hub"
LOG="$VAULT_DIR/outputs/notes/raw-watcher.log"
LOCK="$VAULT_DIR/.raw-watcher.lock"

trap "rm -f '$LOCK'" EXIT

# Verhindere Doppelausführung
if [ -f "$LOCK" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] raw-watcher: bereits aktiv, skip" >> "$LOG"
    exit 0
fi
touch "$LOCK"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] raw-watcher: neue Dateien erkannt in raw/" >> "$LOG"

cd "$VAULT_DIR" || exit 1
source .env 2>/dev/null || true

# 1. Git: alle neuen Dateien committen und pushen
CHANGED=$(git status --porcelain raw/ 2>/dev/null | wc -l | tr -d ' ')

if [ "$CHANGED" -gt 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] raw-watcher: $CHANGED Änderungen → git commit + push" >> "$LOG"
    git add raw/
    git commit -m "auto: neue raw-Dateien [$(date '+%Y-%m-%d %H:%M')]" >> "$LOG" 2>&1
    git push origin claude/optimistic-cannon-4ypdkl >> "$LOG" 2>&1
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] raw-watcher: push abgeschlossen" >> "$LOG"

    # 2. Ingest: neue Dateien ins Wiki verarbeiten
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] raw-watcher: starte ingest..." >> "$LOG"
    python3 "$VAULT_DIR/tools/smart_ingest.py" >> "$LOG" 2>&1
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] raw-watcher: ingest abgeschlossen" >> "$LOG"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] raw-watcher: keine git-Änderungen" >> "$LOG"
fi
