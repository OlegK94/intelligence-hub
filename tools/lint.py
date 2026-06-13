#!/usr/bin/env python3
"""Health-check the wiki for contradictions, orphans, and gaps."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    INDEX_FILE,
    LOG_FILE,
    append_log,
    apply_wiki_articles,
    call_claude,
    collect_wiki_pages,
    ensure_layout,
    extract_json,
    get_client,
    load_wiki_content,
    write_index,
)

SYSTEM = """\
You are the wiki linter for an Intelligence Hub LLM Wiki (Karpathy pattern).

Audit the wiki for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound wikilinks)
- Concepts mentioned but lacking dedicated pages
- Missing cross-references
- Data gaps worth investigating

Respond ONLY with valid JSON:
{
  "report_md": "markdown health report with findings and suggested actions",
  "fixes": [
    {"name": "...", "type": "entity|concept|source|synthesis|comparison", "content": "..."}
  ],
  "index_md": "updated index if fixes applied, else null",
  "summary": "one-line lint summary"
}
"""


def find_orphans() -> list[str]:
    pages = collect_wiki_pages()
    all_content = ""
    for path in pages.values():
        all_content += path.read_text(encoding="utf-8") + "\n"

    orphans = []
    for name in pages:
        if f"[[{name}]]" not in all_content and name.lower() != "index":
            # index.md links to pages too
            if INDEX_FILE.exists() and f"[[{name}]]" in INDEX_FILE.read_text(encoding="utf-8"):
                continue
            orphans.append(name)
    return orphans


def main() -> None:
    parser = argparse.ArgumentParser(description="Lint the wiki")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply LLM-proposed fixes to wiki pages",
    )
    args = parser.parse_args()

    ensure_layout()
    orphans = find_orphans()
    wiki = load_wiki_content()
    index = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    log_tail = ""
    if LOG_FILE.exists():
        lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
        log_tail = "\n".join(lines[-40:])

    user = f"""\
Lint the wiki. {"Apply fixes to wiki pages." if args.fix else "Report only — do not change pages unless --fix."}

Detected orphan candidates (no inbound links): {orphans or "none"}

=== INDEX ===
{index}

=== WIKI ===
{wiki}

=== RECENT LOG ===
{log_tail}
"""

    client = get_client()
    response = call_claude(client, SYSTEM, user)
    data = extract_json(response)

    report = data.get("report_md", "")
    if report:
        print(report)

    if args.fix and data.get("fixes"):
        touched = apply_wiki_articles(data["fixes"])
        if data.get("index_md"):
            write_index(data["index_md"])
        pages = ", ".join(f"[[{n}]]" for n in touched)
        append_log(f"lint --fix\n- Fixed: {pages}\n- {data.get('summary', '')}")
    else:
        append_log(f"lint\n- {data.get('summary', 'Health check complete')}")


if __name__ == "__main__":
    main()
