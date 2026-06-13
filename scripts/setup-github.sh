#!/bin/bash
# Connect Intelligence Hub vault to a GitHub remote (private repo recommended)
set -euo pipefail
cd "$(dirname "$0")/.."

echo "=== Git Status ==="
git status -sb
echo ""
echo "Remote:"
git remote -v || true
echo ""

if git remote get-url origin &>/dev/null; then
  echo "✅ origin already set: $(git remote get-url origin)"
  echo "Run: git push -u origin main"
  exit 0
fi

echo "GitHub ist noch NICHT verbunden."
echo ""
echo "Schritte:"
echo "1. https://github.com/new → neues PRIVATE Repo: intelligence-hub"
echo "2. Kein README/License/gitignore hinzufügen (Vault hat schon Inhalt)"
echo "3. URL kopieren, dann:"
echo ""
echo "   git remote add origin git@github.com:DEIN-USER/intelligence-hub.git"
echo "   git push -u origin main"
echo ""
echo "Oder HTTPS:"
echo "   git remote add origin https://github.com/DEIN-USER/intelligence-hub.git"
echo "   git push -u origin main"
