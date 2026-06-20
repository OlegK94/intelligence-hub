#!/bin/bash
# PreToolUse guard: blocks dangerous bash commands and logs all commands
# Reads JSON from stdin: {"tool_name": "Bash", "tool_input": {"command": "..."}}

VAULT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/IntelligenceHub"
LOG="$VAULT_DIR/outputs/notes/bash-guard.log"

# Extract command from stdin JSON
CMD=$(cat | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('command',''))" 2>/dev/null)

# Log the command
echo "[$(date '+%Y-%m-%d %H:%M:%S')] $CMD" >> "$LOG" 2>/dev/null

# Block dangerous patterns
DANGER_PATTERNS=(
    "rm -rf /"
    "rm -rf ~"
    "rm -rf \$HOME"
    "git push --force.*main"
    "git push --force.*master"
    "git reset --hard HEAD~[0-9][0-9]"
    "DROP TABLE"
    "DROP DATABASE"
    "mkfs"
    "dd if=.*of=/dev"
)

for pattern in "${DANGER_PATTERNS[@]}"; do
    if echo "$CMD" | grep -qE "$pattern" 2>/dev/null; then
        echo "{\"continue\": false, \"stopReason\": \"Bash-Guard blockiert: Gefährliches Kommando erkannt — '$pattern'. Bitte manuell bestätigen.\"}"
        exit 0
    fi
done

# Allow all others silently
exit 0
