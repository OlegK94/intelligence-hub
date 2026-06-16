#!/bin/bash
# Intelligence Hub — Mac Setup Script
# Einmalig ausführen: bash ~/Documents/Intelligence-Hub/scripts/mac-setup.sh
# Danach läuft alles automatisch im Hintergrund.

set -e

VAULT="$HOME/Documents/Intelligence-Hub"
USER_NAME="$(whoami)"
LAUNCH_AGENTS="$HOME/Library/LaunchAgents"

echo ""
echo "═══════════════════════════════════════════"
echo "  Intelligence Hub — Mac Setup"
echo "  Vault: $VAULT"
echo "  User:  $USER_NAME"
echo "═══════════════════════════════════════════"
echo ""

# ── 1. Vault-Existenz prüfen ──────────────────────────────────────────────────
if [ ! -d "$VAULT" ]; then
    echo "❌ Vault nicht gefunden: $VAULT"
    echo "   Stelle sicher dass iCloud synchronisiert ist und der Ordner existiert."
    exit 1
fi
echo "✅ Vault gefunden: $VAULT"

# ── 2. Outputs-Ordner anlegen ─────────────────────────────────────────────────
mkdir -p "$VAULT/outputs/notes"
mkdir -p "$VAULT/outputs/slides"
mkdir -p "$VAULT/outputs/charts"
echo "✅ Outputs-Ordner bereit"

# ── 3. .env Datei ─────────────────────────────────────────────────────────────
if [ ! -f "$VAULT/.env" ]; then
    echo ""
    echo "🔑 Anthropic API Key wird benötigt."
    echo "   Zu finden unter: https://console.anthropic.com/settings/keys"
    echo ""
    printf "   API Key eingeben (wird nicht angezeigt): "
    read -rs API_KEY
    echo ""
    if [ -z "$API_KEY" ]; then
        echo "⚠️  Kein Key eingegeben — .env wird ohne Key erstellt. Später manuell ergänzen."
        echo "ANTHROPIC_API_KEY=" > "$VAULT/.env"
    else
        echo "ANTHROPIC_API_KEY=$API_KEY" > "$VAULT/.env"
        echo "✅ .env erstellt"
    fi
else
    echo "✅ .env bereits vorhanden"
fi

# ── 4. Python dependencies ────────────────────────────────────────────────────
if [ -f "$VAULT/requirements.txt" ]; then
    echo "📦 Python-Pakete installieren..."
    pip3 install -q -r "$VAULT/requirements.txt" && echo "✅ Python-Pakete installiert" || echo "⚠️  pip3 Fehler — ggf. manuell: pip3 install -r requirements.txt"
fi

# ── 5. LaunchAgents Ordner ────────────────────────────────────────────────────
mkdir -p "$LAUNCH_AGENTS"

# ── 6. Clipper Sync plist generieren & laden ─────────────────────────────────
CLIPPER_PLIST="$LAUNCH_AGENTS/com.user.clippersync.plist"
ICLOUD_CLIPPER="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Clipper"

cat > "$CLIPPER_PLIST" << PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.en.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.clippersync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>$VAULT/tools/clipper_sync.sh</string>
    </array>
    <key>WatchPaths</key>
    <array>
        <string>$ICLOUD_CLIPPER</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>$VAULT/outputs/notes/launchd_stdout.log</string>
    <key>StandardErrorPath</key>
    <string>$VAULT/outputs/notes/launchd_stderr.log</string>
</dict>
</plist>
PLIST

launchctl unload "$CLIPPER_PLIST" 2>/dev/null || true
launchctl load "$CLIPPER_PLIST"
echo "✅ Clipper Sync Watcher geladen"

# ── 7. Weekly Research plist generieren & laden ───────────────────────────────
WEEKLY_PLIST="$LAUNCH_AGENTS/com.user.weekly-research.plist"
API_KEY_VALUE=$(grep ANTHROPIC_API_KEY "$VAULT/.env" 2>/dev/null | cut -d= -f2)

cat > "$WEEKLY_PLIST" << PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.en.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.weeklyresearch</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>$VAULT/tools/weekly_research.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>EnvironmentVariables</key>
    <dict>
        <key>ANTHROPIC_API_KEY</key>
        <string>$API_KEY_VALUE</string>
    </dict>
    <key>WorkingDirectory</key>
    <string>$VAULT</string>
    <key>StandardOutPath</key>
    <string>$VAULT/outputs/notes/weekly_research_stdout.log</string>
    <key>StandardErrorPath</key>
    <string>$VAULT/outputs/notes/weekly_research_stderr.log</string>
</dict>
</plist>
PLIST

launchctl unload "$WEEKLY_PLIST" 2>/dev/null || true
launchctl load "$WEEKLY_PLIST"
echo "✅ Weekly Research Watcher geladen (Montag 07:00)"

# ── 8. Raw-Folder Watcher — auto git+ingest bei neuen Dateien ─────────────────
RAW_PLIST="$LAUNCH_AGENTS/com.user.rawwatcher.plist"

cat > "$RAW_PLIST" << PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.en.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.rawwatcher</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>$VAULT/scripts/raw-watcher.sh</string>
    </array>
    <key>WatchPaths</key>
    <array>
        <string>$VAULT/raw</string>
    </array>
    <key>RunAtLoad</key>
    <false/>
    <key>StandardOutPath</key>
    <string>$VAULT/outputs/notes/rawwatcher_stdout.log</string>
    <key>StandardErrorPath</key>
    <string>$VAULT/outputs/notes/rawwatcher_stderr.log</string>
</dict>
</plist>
PLIST

launchctl unload "$RAW_PLIST" 2>/dev/null || true
launchctl load "$RAW_PLIST"
echo "✅ Raw-Folder Watcher geladen (auto git+ingest bei neuen Dateien)"

# ── 8. Claude Code hooks prüfen ───────────────────────────────────────────────
CLAUDE_SETTINGS="$VAULT/.claude/settings.json"
if [ -f "$CLAUDE_SETTINGS" ]; then
    echo "✅ Claude Code Hooks bereits konfiguriert"
else
    echo "⚠️  Claude Code Hooks fehlen — werden aus Vault-Vorlage kopiert (falls vorhanden)"
fi

# ── 9. Status ─────────────────────────────────────────────────────────────────
echo ""
echo "═══════════════════════════════════════════"
echo "  Status LaunchAgents:"
launchctl list | grep com.user || echo "  (keine com.user Agents aktiv)"
echo ""
echo "  Nächste Schritte:"
echo "  • Ersten Ingest testen:"
echo "    cd $VAULT && python3 tools/ingest.py"
echo ""
echo "  • Inbox-Dateien sofort ingesten:"
echo "    cd $VAULT && python3 tools/ingest.py --scope raw"
echo ""
echo "✅ Mac Setup abgeschlossen!"
echo "═══════════════════════════════════════════"
echo ""
