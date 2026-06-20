#!/bin/bash
# Send session summary email after Claude Code stops
# Uses macOS built-in sendmail / mail command

VAULT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/IntelligenceHub"
TO="accounts@ok-holding.com"
DATE=$(date "+%Y-%m-%d %H:%M")

# Collect recent log entries (last 20 lines of wiki log)
LOG_SNIPPET=""
if [ -f "$VAULT_DIR/wiki/log.md" ]; then
    LOG_SNIPPET=$(tail -30 "$VAULT_DIR/wiki/log.md" 2>/dev/null)
fi

# Count files changed in last hour
CHANGED=$(find "$VAULT_DIR/wiki" -newer "$VAULT_DIR/.last-session-notify" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
touch "$VAULT_DIR/.last-session-notify" 2>/dev/null

# Only send if something changed
if [ "$CHANGED" -eq "0" ] && [ -z "$LOG_SNIPPET" ]; then
    exit 0
fi

SUBJECT="IntelligenceHub Session — $DATE ($CHANGED wiki pages updated)"

BODY="Claude Code Session abgeschlossen: $DATE

Wiki-Änderungen: $CHANGED Dateien aktualisiert

=== Aktueller Log (letzte Einträge) ===
$LOG_SNIPPET

---
IntelligenceHub Automation
"

echo "$BODY" | mail -s "$SUBJECT" "$TO" 2>/dev/null || \
    python3 -c "
import smtplib, os
from email.mime.text import MIMEText
msg = MIMEText('''$BODY''')
msg['Subject'] = '''$SUBJECT'''
msg['From'] = '''accounts@ok-holding.com'''
msg['To'] = '''$TO'''
# Falls kein lokaler Mailserver: Auskommentieren und SMTP-Daten eintragen
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login('user', 'pass')
# s.send_message(msg)
# s.quit()
print('Email configured but SMTP not set up yet')
" 2>/dev/null

exit 0
