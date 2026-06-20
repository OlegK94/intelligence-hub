#!/bin/bash
# Send session summary email via macOS Mail.app

VAULT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/IntelligenceHub"
TO="accounts@ok-holding.com"
DATE=$(date "+%Y-%m-%d %H:%M")

MARKER="$VAULT_DIR/.last-session-notify"
CHANGED=0
if [ -f "$MARKER" ]; then
    CHANGED=$(find "$VAULT_DIR/wiki" -newer "$MARKER" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
fi
touch "$MARKER" 2>/dev/null

LOG_SNIPPET=$(tail -20 "$VAULT_DIR/wiki/log.md" 2>/dev/null | head -c 1500)

SUBJECT="IntelligenceHub — $DATE ($CHANGED Seiten aktualisiert)"
BODY="Claude Code Session: $DATE
Wiki-Änderungen: $CHANGED Dateien

=== Log ===
$LOG_SNIPPET"

osascript - "$TO" "$SUBJECT" "$BODY" <<'APPLEEOF'
on run {toAddr, msgSubject, msgBody}
    tell application "Mail"
        set newMsg to make new outgoing message
        tell newMsg
            set subject to msgSubject
            set content to msgBody
            set visible to false
            make new to recipient with properties {address:toAddr}
        end tell
        send newMsg
    end tell
end run
APPLEEOF

exit 0
