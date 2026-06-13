#!/usr/bin/env python3
"""Print Intelligence Hub wiki status."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, WIKI_DIR, collect_wiki_pages, collect_ingest_candidates

manifest = json.loads((ROOT / "wiki" / ".ingest_manifest.json").read_text())
ingested = manifest.get("ingested", [])
pending = collect_ingest_candidates()
pages = collect_wiki_pages()

by_dir: dict[str, int] = {}
for path in pages.values():
    rel = path.parent.name
    by_dir[rel] = by_dir.get(rel, 0) + 1

print("Intelligence Hub — Status")
print("=" * 40)
print(f"Ingested sources:  {len(ingested)}")
print(f"Pending sources:   {len(pending)}")
print(f"Wiki articles:     {len(pages)}")
print()
print("Wiki by folder:")
for folder, count in sorted(by_dir.items()):
    print(f"  {folder}: {count}")
if pending:
    print()
    print("Next pending:")
    for p in pending[:5]:
        try:
            print(f"  - {p.relative_to(ROOT)}")
        except ValueError:
            print(f"  - {p}")
