#!/bin/bash

# ==========================================
# CLIPPER SYNC — Intelligence Hub
# ==========================================
# Überwacht den iCloud-Clipper-Ordner, komprimiert YouTube-Transkripte
# via Claude Haiku (80% günstiger als Sonnet) und legt das Ergebnis
# in Clippings/ ab — dann greift tools/ingest.py automatisch darüber.
#
# Setup:
#   1. VAULT_DIR unten auf deinen Mac-Vault-Pfad anpassen
#   2. chmod +x ~/clipper_sync.sh
#   3. launchd plist laden (siehe scripts/launchd/com.user.clippersync.plist)
# ==========================================

# ── Konfiguration ────────────────────────────────────────────────────
ICLOUD_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Clipper"
VAULT_DIR="$HOME/Documents/Intelligence-Hub"          # iCloud-Vault: $HOME/Library/Mobile\ Documents/com~apple~CloudDocs/Intelligence-Hub
CLIPPINGS_DIR="$VAULT_DIR/Clippings"
INBOX_DIR="$VAULT_DIR/raw/inbox"
TOO_LARGE_DIR="$VAULT_DIR/raw/inbox/zu_lang_autosync"
TMP_DIR="$HOME/Downloads/clipper_tmp"
LOCK_FILE="/tmp/clipper_sync.lock"
LOG_FILE="$VAULT_DIR/outputs/notes/clipper_sync.log"
MAX_SIZE_KB=50    # ~30–45 Min Video-Limit (Kostenschutz)
MODEL="claude-haiku-4-5-20251001"   # Haiku: 80% günstiger als Sonnet
# ─────────────────────────────────────────────────────────────────────

# Lock-File mit automatischem Cleanup bei Exit/Crash
trap "rm -f '$LOCK_FILE'" EXIT
if [ -f "$LOCK_FILE" ]; then
    exit 0
fi
touch "$LOCK_FILE"

# Neue Dateien prüfen
if ! ls "$ICLOUD_DIR"/*.md 1>/dev/null 2>&1; then
    exit 0
fi

# Ordner sicherstellen
mkdir -p "$TMP_DIR" "$CLIPPINGS_DIR" "$INBOX_DIR" "$TOO_LARGE_DIR"

# Dateien sicher aus iCloud in Temp-Ordner verschieben
mv "$ICLOUD_DIR"/*.md "$TMP_DIR"/

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Verarbeite $(ls "$TMP_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ') Datei(en)" >> "$LOG_FILE"

for file in "$TMP_DIR"/*.md; do
    [ -e "$file" ] || continue
    filename=$(basename "$file")

    # KOSTENSCHUTZ: Datei zu groß?
    file_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file")
    max_bytes=$((MAX_SIZE_KB * 1024))

    if [ "$file_size" -gt "$max_bytes" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ZU GROSS ($((file_size/1024))KB): $filename → zu_lang_autosync/" >> "$LOG_FILE"
        mv "$file" "$TOO_LARGE_DIR/"
        continue
    fi

    # Dateiinhalt einlesen
    file_content=$(cat "$file")
    output_file="$CLIPPINGS_DIR/${filename}"

    # Claude Haiku: komprimiere Transkript → strukturierte Notiz
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Verarbeite: $filename ($((file_size/1024))KB)" >> "$LOG_FILE"

    claude --model "$MODEL" -p "Du bist der Wiki-Maintainer eines persönlichen Intelligence Hubs (Obsidian Vault).

Hier ist eine neue Datei aus dem YouTube-Clipper:

$file_content

Analysiere das Transkript und erstelle eine komprimierte, strukturierte Markdown-Notiz auf Deutsch. Nutze exakt dieses Format:

---
title: [Titel des Videos]
type: youtube
status: processed
url: [Original-URL aus dem Frontmatter/Inhalt, falls vorhanden]
date: $(date '+%Y-%m-%d')
tags: [3-5 relevante Tags]
---

# [Titel]

## Sofortige Action Items
Konkrete, direkt umsetzbare Aufgaben aus dem Video. Format: - [ ] Aufgabe (Kontext)

## Kern-Erkenntnisse
3-5 Bullet-Points mit den wichtigsten Ideen. Präzise, keine Füllwörter.

## Frameworks & Modelle
Wenn das Video ein Modell/Framework beschreibt: als Markdown-Tabelle. Sonst weglassen.

## Verknüpfungen
Schlage 3 interne Obsidian-Links vor: [[Notiz-Name]] — kurz begründen warum.

---
WICHTIG: Gib NUR den Markdown-Inhalt zurück, kein Kommentar drumherum. Kein rohes Transkript." \
    > "$output_file"

    # Prüfen ob Claude erfolgreich war
    if [ $? -eq 0 ] && [ -s "$output_file" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✓ Fertig: $filename → Clippings/" >> "$LOG_FILE"
        rm "$file"
    else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✗ Fehler bei: $filename → raw/inbox/ (manuell prüfen)" >> "$LOG_FILE"
        mv "$file" "$INBOX_DIR/"
        rm -f "$output_file"  # Leere/fehlerhafte Output-Datei entfernen
    fi
done

# Optional: ingest.py direkt triggern wenn Claude Code im Vault läuft
# cd "$VAULT_DIR" && python3 tools/ingest.py --scope clippings

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Sync abgeschlossen." >> "$LOG_FILE"
