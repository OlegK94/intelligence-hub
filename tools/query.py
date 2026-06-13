#!/usr/bin/env python3
"""Query the wiki and write answers to outputs/."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    INDEX_FILE,
    append_log,
    apply_wiki_articles,
    call_claude,
    dated_output_path,
    ensure_layout,
    extract_json,
    get_client,
    load_wiki_content,
    write_index,
)

SYSTEM = """\
You are the research assistant for an Intelligence Hub LLM Wiki (Karpathy pattern).

Answer the user's question by reading the wiki index and pages provided.
- Cite wiki pages with [[wikilinks]]
- Synthesize across multiple pages when needed
- File valuable findings back into the wiki

Respond ONLY with valid JSON:
{
  "answer_md": "full markdown answer with citations",
  "file_to_wiki": true or false,
  "wiki_articles": [
    {"name": "...", "type": "synthesis|comparison|concept", "content": "..."}
  ],
  "index_md": "updated index if wiki pages added, else null",
  "slug": "short-filename-slug"
}

For slides output, answer_md should be valid Marp markdown starting with:
---
marp: true
theme: default
---
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the wiki")
    parser.add_argument("question", help="Question to answer")
    parser.add_argument(
        "--output",
        choices=["notes", "slides", "charts"],
        default="notes",
        help="Output format (default: notes)",
    )
    args = parser.parse_args()

    ensure_layout()
    client = get_client()

    index = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    wiki = load_wiki_content()

    user = f"""\
Question: {args.question}

Output format: {args.output}

=== WIKI INDEX ===
{index}

=== WIKI PAGES ===
{wiki}
"""

    response = call_claude(client, SYSTEM, user)
    data = extract_json(response)

    slug = data.get("slug", "query-answer")
    out_path = dated_output_path(args.output, slug)
    answer = data.get("answer_md", "")
    if answer:
        out_path.write_text(answer.strip() + "\n", encoding="utf-8")
        print(f"Wrote {out_path}")

    if data.get("file_to_wiki") and data.get("wiki_articles"):
        touched = apply_wiki_articles(data["wiki_articles"])
        if data.get("index_md"):
            write_index(data["index_md"])
        pages = ", ".join(f"[[{n}]]" for n in touched)
        append_log(
            f'query | "{args.question[:80]}"\n'
            f"- Output: {out_path.name}\n"
            f"- Filed back: {pages}"
        )
    else:
        append_log(
            f'query | "{args.question[:80]}"\n'
            f"- Output: {out_path.name}"
        )


if __name__ == "__main__":
    main()
