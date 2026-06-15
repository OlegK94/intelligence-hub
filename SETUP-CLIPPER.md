# Clipper Sync Setup — YouTube → Obsidian Automation

Automatisierung: YouTube via Obsidian Clipper → Claude Haiku komprimiert → `Clippings/` → `tools/ingest.py` → Wiki

---

## Was passiert

1. Du clippst ein YouTube-Video mit dem Obsidian Web Clipper (inkl. Transkript)
2. Die Datei landet in iCloud unter `Clipper/`
3. `launchd` erkennt die neue Datei sofort (Dateisystem-Watcher)
4. `tools/clipper_sync.sh` verschiebt sie sicher in einen Temp-Ordner
5. Claude Haiku (80% günstiger als Sonnet) komprimiert das Transkript zu einer strukturierten Notiz
6. Ergebnis landet in `Clippings/` — bereit für `tools/ingest.py`
7. Bei Fehler: Originaldatei bleibt in `raw/inbox/` zur manuellen Prüfung

**Kostenschutz:** Dateien >50 KB (≈30–45 Min Video) → `raw/inbox/zu_lang_autosync/` (kein API-Aufruf)

---

## Einrichtung auf dem Mac (einmalig)

### Schritt 1: Vault-Pfad im Script anpassen

```bash
nano ~/Documents/intelligence-hub/tools/clipper_sync.sh
```

Ändere Zeile 20:
```bash
VAULT_DIR="$HOME/Documents/intelligence-hub"   # ← deinen echten Pfad eintragen
```

### Schritt 2: Script ausführbar machen

```bash
chmod +x ~/Documents/intelligence-hub/tools/clipper_sync.sh
```

### Schritt 3: launchd plist kopieren und anpassen

```bash
cp ~/Documents/intelligence-hub/scripts/launchd/com.user.clippersync.plist \
   ~/Library/LaunchAgents/com.user.clippersync.plist
```

Dann in der Datei **DEIN_BENUTZERNAME** an allen Stellen ersetzen:
```bash
# Deinen echten Username einsetzen (z.B. oleg):
sed -i '' 's/DEIN_BENUTZERNAME/$(whoami)/g' ~/Library/LaunchAgents/com.user.clippersync.plist
# ODER manuell mit nano:
nano ~/Library/LaunchAgents/com.user.clippersync.plist
```

### Schritt 4: Wächter aktivieren

```bash
launchctl load ~/Library/LaunchAgents/com.user.clippersync.plist
```

Prüfen ob er läuft:
```bash
launchctl list | grep clippersync
```

### Schritt 5: Obsidian Web Clipper konfigurieren

In den Clipper-Einstellungen:
- **Output-Ordner:** `iCloud Drive → Clipper/` (NICHT direkt in den Vault)
- **Transkript aktivieren:** ✓ (YouTube-Transkript mitclipppen)
- Format: Markdown

### Schritt 6: Obsidian Dashboard (optional)

Füge das in deine Daily Note oder Homepage ein (benötigt **Dataview Plugin**):

```markdown
## ⚡ YouTube-Analysen

### 🛠️ Offene To-Dos
\`\`\`dataview
TASK
FROM "Clippings"
WHERE !completed AND type = "youtube"
\`\`\`

### 💡 Letzte Analysen
\`\`\`dataview
TABLE url AS "Quelle", file.mtime AS "Analysiert"
FROM "Clippings"
WHERE type = "youtube" AND status = "processed"
SORT file.mtime DESC
LIMIT 5
\`\`\`
```

---

## Testen

```bash
# Manuelle Testdatei erstellen:
echo "---
title: Test Video
url: https://youtube.com/watch?v=test
---
# Test Transkript
Das ist ein Testtranskript." > ~/Library/Mobile\ Documents/com~apple~CloudDocs/Clipper/test_video.md

# Logs beobachten:
tail -f ~/Documents/intelligence-hub/outputs/notes/clipper_sync.log
```

---

## Logs & Debugging

```bash
# Sync-Log:
cat ~/Documents/intelligence-hub/outputs/notes/clipper_sync.log

# launchd Fehler:
cat ~/Documents/intelligence-hub/outputs/notes/launchd_stderr.log

# Wächter neu starten:
launchctl unload ~/Library/LaunchAgents/com.user.clippersync.plist
launchctl load ~/Library/LaunchAgents/com.user.clippersync.plist

# Manuell triggern (zum Testen):
bash ~/Documents/intelligence-hub/tools/clipper_sync.sh
```

---

## Dateien

| Datei | Zweck |
|---|---|
| `tools/clipper_sync.sh` | Hauptskript (korrigiert, getestet) |
| `scripts/launchd/com.user.clippersync.plist` | macOS Hintergrunddienst |
| `raw/inbox/zu_lang_autosync/` | Zu große Dateien (manuell verarbeiten) |
| `outputs/notes/clipper_sync.log` | Sync-Protokoll |
