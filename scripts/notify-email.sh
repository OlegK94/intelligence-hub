#!/bin/bash
# Send session summary email via macOS Mail.app (works with any configured account)

VAULT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/IntelligenceHub"
TO="accounts@ok-holding.com"
DATE=$(date "+%Y-%m-%d %H:%M")

# Count wiki files changed since last notification
MARKER="$VAULT_DIR/.last-session-notify"
CHANGED=0
if [ -f "$MARKER" ]; then
    CHANGED=$(find "$VAULT_DIR/wiki" -newer "$MARKER" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
fi
touch "$MARKER" 2>/dev/null

# Collect last log entries
LOG_SNIPPET=$(tail -20 "$VAULT_DIR/wiki/log.md" 2>/dev/null | sed "s/'/\'/g" | head -c 2000)

SUBJECT="IntelligenceHub — $DATE ($CHANGED Seiten aktualisiert)"
BODY="Claude Code Session abgeschlossen: $DATE

Wiki-Änderungen: $CHANGED Dateien aktualisiert

=== Letzte Log-Einträge ===
$LOG_SNIPPET"

osascript <<APPLEEOF
set msgBody to "$BODY"
set msgSubject to "$SUBJECT"
set toAddr to "$TO"

tell application "Mail"
    set newMsg to make new outgoing message with properties {subject:msgSubject, content:msgBody, visible:false}
    tell newMsg
        make new to recipient with properties {address:toAddr}
    end tell
    send newMsg
end tell
APPLEEOF

exit 0
