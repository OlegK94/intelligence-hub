---
title: Heute Abend — Setup ToDos
type: todo
tags: [setup, automation, health]
created: 2026-06-15
priority: hoch
---

# Heute Abend erledigen ✅

## Mac Automation Setup

- [ ] `git pull origin claude/optimistic-cannon-4ypdkl` im Intelligence-Hub Ordner
- [ ] `chmod +x tools/clipper_sync.sh scripts/post-session.sh scripts/on-file-change.sh`
- [ ] Clipper Sync aktivieren:
  ```bash
  cp scripts/launchd/com.user.clippersync.plist ~/Library/LaunchAgents/
  sed -i '' "s/DEIN_BENUTZERNAME/$(whoami)/g" ~/Library/LaunchAgents/com.user.clippersync.plist
  launchctl load ~/Library/LaunchAgents/com.user.clippersync.plist
  ```
- [ ] Weekly Research aktivieren:
  ```bash
  cp scripts/launchd/com.user.weekly-research.plist ~/Library/LaunchAgents/
  nano ~/Library/LaunchAgents/com.user.weekly-research.plist
  # → DEIN_BENUTZERNAME ersetzen + API Key eintragen
  launchctl load ~/Library/LaunchAgents/com.user.weekly-research.plist
  ```

## Apple Reminders anlegen (Script Editor auf Mac)

- [ ] Script Editor öffnen (Spotlight → "Script Editor")
- [ ] Folgenden Code einfügen und ▶️ drücken:

```applescript
tell application "Reminders"
    set myList to list "Erinnerungen"
    make new reminder in myList with properties {name:"🛒 Kreatin Creapure Bulk bestellen (~8€)", due date:date "16. Juni 2026 10:00:00", remind me date:date "16. Juni 2026 10:00:00"}
    make new reminder in myList with properties {name:"🩸 Omega-3 Index Test bestellen — cerascreen.de (~35€)", due date:date "16. Juni 2026 10:00:00", remind me date:date "16. Juni 2026 10:00:00"}
    make new reminder in myList with properties {name:"🩺 Blutbild machen (Vit D, hs-CRP, HbA1c, ApoB)", due date:date "20. Juni 2026 10:00:00", remind me date:date "20. Juni 2026 10:00:00"}
    make new reminder in myList with properties {name:"📊 Check-in: Gewicht + Bauchumfang messen", due date:date "29. Juni 2026 08:00:00", remind me date:date "29. Juni 2026 08:00:00"}
end tell
```

## Health — Sofort

- [ ] Kreatin Dosis heute noch auf 10g erhöhen (5g + 5g)
- [ ] Letzter Kaffee ab morgen: 13:00
- [ ] Letzte Mahlzeit ab morgen: 20:00
