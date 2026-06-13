#!/bin/bash
# Run remaining setup tasks after .env is configured
set -euo pipefail
VAULT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$VAULT"

if [[ ! -f .env ]]; then
  echo "❌ .env fehlt. Kopiere .env.example → .env und trage ANTHROPIC_API_KEY ein."
  exit 1
fi

python3 -c "
import sys
sys.path.insert(0,'tools')
from common import load_env_file
import os
load_env_file()
if not os.environ.get('ANTHROPIC_API_KEY'):
    sys.exit('❌ ANTHROPIC_API_KEY leer')
print('✅ API-Key geladen')
"

echo "=== Batch ingest (34 pending) ==="
python3 tools/batch_ingest.py

echo "=== Lint ==="
python3 tools/lint.py

echo "=== Status ==="
python3 tools/status.py
