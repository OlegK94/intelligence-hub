#!/usr/bin/env python3
"""Rebuild .ingest_manifest.json from existing wiki/sources/ YAML frontmatter."""

import json
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
WIKI_DIR = VAULT / "wiki"
MANIFEST_FILE = WIKI_DIR / ".ingest_manifest.json"

def extract_sources_from_frontmatter(text: str) -> list[str]:
    m = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return []
    fm = m.group(1)
    # sources: ["raw/path/to/file.md"] or sources: ["a", "b"]
    sources_m = re.search(r'^sources:\s*\[([^\]]*)\]', fm, re.MULTILINE)
    if not sources_m:
        return []
    raw = sources_m.group(1)
    return [s.strip().strip('"').strip("'") for s in raw.split(",") if s.strip()]

def main():
    existing = set()
    if MANIFEST_FILE.exists():
        data = json.loads(MANIFEST_FILE.read_text())
        existing = set(data.get("ingested", []))

    found = set(existing)

    for md_file in WIKI_DIR.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue
        for src in extract_sources_from_frontmatter(text):
            if src.startswith("raw/"):
                found.add(src)

    # Also add any raw files that exist on disk
    raw_dir = VAULT / "raw"
    for raw_file in raw_dir.rglob("*"):
        if raw_file.is_file() and raw_file.suffix in (".md", ".txt", ".csv", ".pdf"):
            rel = str(raw_file.relative_to(VAULT))
            # Only add if a wiki source page exists referencing it
            # (we already collected those above)

    manifest = {"ingested": sorted(found)}
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"Manifest rebuilt: {len(found)} files tracked ({len(found) - len(existing)} added)")

if __name__ == "__main__":
    main()
