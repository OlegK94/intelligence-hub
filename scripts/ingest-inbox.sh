#!/bin/bash
# Process new items in raw/inbox/ and Clippings/
set -euo pipefail
cd "$(dirname "$0")/.."
echo "=== Wiki Status ==="
python3 tools/status.py
echo ""
echo "=== Ingesting inbox ==="
python3 tools/ingest.py
echo ""
echo "=== Done ==="
python3 tools/status.py
