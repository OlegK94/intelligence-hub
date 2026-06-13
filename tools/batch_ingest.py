#!/usr/bin/env python3
"""Batch-ingest all pending raw/ and Clippings/ markdown files."""

from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT, ensure_layout, load_env_file
from ingest import ingest_file, get_client

LOG = ROOT / "outputs" / "notes" / "batch-ingest-log.md"


def pending_files() -> list[Path]:
    manifest = json.loads((ROOT / "wiki" / ".ingest_manifest.json").read_text())
    ingested = set(manifest.get("ingested", []))
    ext = {".md", ".txt", ".markdown"}
    skip = {"index.md", "log.md"}
    out: list[Path] = []
    for base in ("raw", "Clippings"):
        root = ROOT / base
        if not root.exists():
            continue
        for p in sorted(root.rglob("*")):
            if not p.is_file() or p.suffix.lower() not in ext or p.name in skip:
                continue
            rel = str(p.relative_to(ROOT))
            if rel not in ingested:
                out.append(p)
    return out


def main() -> None:
    ensure_layout()
    load_env_file()
    client = get_client()
    files = pending_files()
    LOG.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# Batch Ingest — {len(files)} files\n"]
    ok, fail = 0, 0

    for i, path in enumerate(files, 1):
        rel = str(path.relative_to(ROOT))
        print(f"[{i}/{len(files)}] {rel}", flush=True)
        try:
            if ingest_file(client, path):
                ok += 1
                lines.append(f"- ✅ `{rel}`")
            else:
                fail += 1
                lines.append(f"- ⏭️ `{rel}` — skipped (empty)")
        except Exception as exc:
            fail += 1
            err = str(exc).split("\n")[0][:200]
            lines.append(f"- ❌ `{rel}` — {err}")
            print(f"  ERROR: {err}", flush=True)
        LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines.append(f"\n## Done: {ok} ok, {fail} failed/skipped")
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nFinished: {ok} ok, {fail} failed/skipped")


if __name__ == "__main__":
    main()
