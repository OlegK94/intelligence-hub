#!/bin/bash
# Re-index vault after ingest or wiki edits
set -euo pipefail

VAULT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$VAULT"

if ! command -v qmd &>/dev/null; then
  echo "QMD not installed. Run: bash scripts/qmd-setup.sh"
  exit 1
fi

echo "=== QMD update ==="
qmd update

if [[ "${1:-}" == "--embed" ]]; then
  echo "=== QMD embed ==="
  qmd embed
fi

qmd status
