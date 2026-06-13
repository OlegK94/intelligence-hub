#!/bin/bash
# One-time QMD setup for Intelligence Hub (tobi/qmd)
set -euo pipefail

VAULT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$VAULT"

need() {
  if ! command -v "$1" &>/dev/null; then
    echo "Missing: $1"
    echo "$2"
    exit 1
  fi
}

if ! command -v node &>/dev/null; then
  echo "Node.js 22+ is required for QMD."
  echo "Install: brew install node"
  exit 1
fi

NODE_MAJOR="$(node -p 'process.versions.node.split(".")[0]')"
if [[ "$NODE_MAJOR" -lt 22 ]]; then
  echo "Node.js 22+ required (found $(node -v))."
  exit 1
fi

need npm "Install Node: brew install node"
need sqlite3 "On macOS: brew install sqlite"

if ! command -v qmd &>/dev/null; then
  echo "Installing @tobilu/qmd globally..."
  npm install -g @tobilu/qmd
fi

export QMD_EDITOR_URI="${QMD_EDITOR_URI:-cursor://file/{path}:{line}:{col}}"

add_collection() {
  local name="$1" path="$2" mask="${3:-**/*.md}"
  if qmd collection show "$name" &>/dev/null; then
    echo "Collection exists: $name"
    return 0
  fi
  qmd collection add "$path" --name "$name" --mask "$mask"
  echo "Added collection: $name → $path"
}

add_context() {
  local uri="$1" text="$2"
  qmd context add "$uri" "$text" 2>/dev/null || true
}

echo "=== QMD collections ==="
add_collection hub-wiki "$VAULT/wiki" "**/*.md"
add_collection hub-privat "$VAULT/raw/Privat" "**/*.md"
add_collection hub-business "$VAULT/raw/Business" "**/*.md"
add_collection hub-outputs "$VAULT/outputs" "**/*.md"

echo "=== QMD context ==="
add_context "qmd://hub-wiki" "LLM-maintained wiki: entities, concepts, sources, syntheses, comparisons"
add_context "qmd://hub-privat" "Personal raw sources: performance, tech, private finance, insurance"
add_context "qmd://hub-business" "Business raw sources: Wagglz GmbH, Café Berlin, OK Capital UG"
add_context "qmd://hub-outputs" "Query answers, slides, batch logs from tools/"

echo "=== Index update ==="
qmd update

if [[ "${1:-}" == "--embed" ]]; then
  echo "=== Generating embeddings (downloads ~2GB models on first run) ==="
  qmd embed
else
  echo ""
  echo "Keyword search ready. For semantic/hybrid search run:"
  echo "  bash scripts/qmd-sync.sh --embed"
fi

echo ""
qmd status
echo ""
echo "Try: python3 tools/search.py \"Hyrox training\""
