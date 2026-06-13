#!/usr/bin/env python3
"""Ingest raw sources into the LLM-maintained wiki."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    append_log,
    apply_wiki_articles,
    call_claude,
    collect_ingest_candidates,
    ensure_layout,
    extract_json,
    get_client,
    load_manifest,
    load_wiki_content,
    mark_ingested,
    read_file_text,
    rel_path,
    write_index,
)

SYSTEM = """\
You are the wiki maintainer for an Intelligence Hub knowledge base (Karpathy LLM Wiki pattern).

Ingest the raw source into the existing wiki:
1. Create/update a source summary page in wiki/sources/
2. Create/update relevant entity and concept pages
3. Add Obsidian wikilinks [[Page Name]] throughout
4. Note contradictions with existing wiki content when found
5. Update index.md with categorized entries (one-line summaries)
6. Use YAML frontmatter on every page (title, type, tags, sources, created, updated, summary)

Respond ONLY with valid JSON:
{
  "articles": [
    {"name": "Human Readable Title", "type": "source|entity|concept|synthesis|comparison", "content": "full markdown"}
  ],
  "index_md": "full updated index.md content",
  "log_notes": "brief summary of changes"
}

Important: "name" must be a clean human-readable title (e.g. "Andrew Huberman", "HIIT Training") — no .md suffix, no path prefixes.
"""


def build_user_prompt(source_path, source_text: str, wiki_content: str) -> str:
    return f"""\
Ingest this raw source into the wiki. Raw files are immutable — integrate knowledge into wiki pages only.

=== SOURCE ({rel_path(source_path)}) ===
{source_text}

=== EXISTING WIKI ===
{wiki_content}

=== CURRENT INDEX ===
Read and extend the index. Organize by: Entities, Concepts, Sources, Syntheses, Comparisons.
"""


def ingest_file(client, path) -> bool:
    manifest = load_manifest()
    text = read_file_text(path)
    if not text.strip():
        print(f"Skipping empty file: {rel_path(path)}", file=sys.stderr)
        return False

    wiki_content = load_wiki_content()
    response = call_claude(
        client,
        SYSTEM,
        build_user_prompt(path, text, wiki_content),
    )
    data = extract_json(response)

    touched = apply_wiki_articles(data.get("articles", []))
    write_index(data.get("index_md"))
    mark_ingested(path, manifest)

    notes = data.get("log_notes", f"Ingested {rel_path(path)}")
    pages = ", ".join(f"[[{n}]]" for n in touched) or "no page changes"
    append_log(f"ingest | {rel_path(path)}\n- Pages: {pages}\n- {notes}")

    print(f"Ingested {rel_path(path)} → {len(touched)} pages updated")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest raw sources into wiki")
    parser.add_argument("--file", help="Specific file to ingest")
    parser.add_argument(
        "--scope",
        choices=["inbox", "clippings", "raw"],
        default="inbox",
        help="Where to scan for new sources (default: inbox)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Re-ingest already processed files in scope",
    )
    args = parser.parse_args()

    ensure_layout()
    candidates = collect_ingest_candidates(
        args.file,
        include_ingested=args.all,
        scope=args.scope,
    )
    if not candidates:
        return

    client = get_client()
    for path in candidates:
        try:
            ingest_file(client, path)
        except Exception as exc:
            if type(exc).__module__.startswith("anthropic"):
                print(f"API error for {rel_path(path)}: {exc}", file=sys.stderr)
            else:
                print(f"Error for {rel_path(path)}: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
