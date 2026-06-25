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

WICHTIG — Sprache: Schreibe ALLE Wiki-Seiten auf DEUTSCH (Fließtext, Überschriften, summary).
Etablierte englische Fachbegriffe/Eigennamen bleiben englisch (Performance Coffee, Longevity,
Blueprint, EFSA, Novel Food, Hyrox, Zone 2, NSDR, COGS, Cashflow). Frontmatter-Feldnamen bleiben englisch.

Ingest the raw source into the existing wiki:
1. Create/update a source summary page in wiki/sources/
2. Create/update relevant entity and concept pages
3. Add Obsidian wikilinks [[Page Name]] throughout
4. Note contradictions with existing wiki content when found
5. Update index.md with categorized entries (one-line summaries)
6. Use YAML frontmatter on every page (title, type, tags, sources, created, updated, summary)

Respond using this EXACT delimiter format (no JSON — avoids escaping issues with markdown):

%%LOG%%
One-line summary of what changed.
%%ENDLOG%%

%%INDEX%%
(full updated wiki/index.md content here)
%%ENDINDEX%%

%%ARTICLE%%
NAME: Human Readable Title
TYPE: source|entity|concept|synthesis|comparison
(full markdown content of this wiki page including YAML frontmatter)
%%ENDARTICLE%%

Repeat %%ARTICLE%%...%%ENDARTICLE%% for each page you create or update.
NAME must be a clean human-readable title — no .md suffix, no path prefixes.
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


def parse_delimited_response(response: str, path) -> dict:
    """Parse the delimiter-based ingest response — no JSON escaping issues."""
    import re as _re

    def extract(tag: str) -> str:
        m = _re.search(rf"%%{tag}%%\n?(.*?)%%END{tag}%%", response, _re.DOTALL)
        return m.group(1).strip() if m else ""

    log_notes = extract("LOG") or f"Ingested {rel_path(path)}"
    index_md = extract("INDEX") or None

    articles = []
    for block in _re.findall(r"%%ARTICLE%%\n?(.*?)%%ENDARTICLE%%", response, _re.DOTALL):
        block = block.strip()
        name_m = _re.match(r"NAME:\s*(.+)", block)
        type_m = _re.search(r"\nTYPE:\s*(.+)", block)
        if not name_m:
            continue
        name = name_m.group(1).strip()
        art_type = type_m.group(1).strip() if type_m else "source"
        # Content is everything after the NAME/TYPE header lines
        content = _re.sub(r"^NAME:.*\n?", "", block)
        content = _re.sub(r"^TYPE:.*\n?", "", content, count=1).strip()
        articles.append({"name": name, "type": art_type, "content": content})

    if not articles:
        # Fallback: try old JSON format
        try:
            from common import extract_json
            data = extract_json(response)
            return data
        except Exception as e:
            print(f"Warning: no articles parsed for {rel_path(path)}: {e}", file=sys.stderr)

    return {"articles": articles, "index_md": index_md, "log_notes": log_notes}


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

    data = parse_delimited_response(response, path)
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
