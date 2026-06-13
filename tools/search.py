#!/usr/bin/env python3
"""Search Intelligence Hub — QMD hybrid search with BM25 fallback."""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT, WIKI_DIR, collect_wiki_pages


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9äöüß]+", text.lower())


def bm25_score(query_tokens: list[str], doc_tokens: list[str], df: Counter, n_docs: int) -> float:
    if not doc_tokens:
        return 0.0
    tf = Counter(doc_tokens)
    doc_len = len(doc_tokens)
    avgdl = 500.0
    k1, b = 1.5, 0.75
    score = 0.0
    for term in query_tokens:
        if term not in tf:
            continue
        idf = math.log((n_docs - df[term] + 0.5) / (df[term] + 0.5) + 1)
        freq = tf[term]
        score += idf * (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * doc_len / avgdl))
    return score


def search_fallback(query: str, limit: int) -> list[tuple[float, str, str]]:
    pages = collect_wiki_pages()
    docs: dict[str, list[str]] = {}
    for name, path in pages.items():
        docs[name] = tokenize(path.read_text(encoding="utf-8"))

    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    df: Counter = Counter()
    for tokens in docs.values():
        for term in set(tokens):
            df[term] += 1

    n_docs = len(docs)
    results: list[tuple[float, str, str]] = []
    for name, path in pages.items():
        score = bm25_score(query_tokens, docs[name], df, n_docs)
        if score > 0:
            text = path.read_text(encoding="utf-8")
            summary = text[:300].replace("\n", " ")
            results.append((score, name, summary))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:limit]


def qmd_available() -> bool:
    return shutil.which("qmd") is not None


def _parse_qmd_score(raw: object) -> float:
    if isinstance(raw, (int, float)):
        return float(raw)
    if isinstance(raw, str):
        cleaned = raw.strip().rstrip("%")
        try:
            val = float(cleaned)
            return val / 100.0 if "%" in raw else val
        except ValueError:
            return 0.0
    return 0.0


def _qmd_title(item: dict) -> str:
    for key in ("title", "name", "file", "path"):
        val = item.get(key)
        if isinstance(val, str) and val.strip():
            if key in {"file", "path"}:
                return Path(val).stem
            return val.strip()
    return "unknown"


def _qmd_summary(item: dict) -> str:
    for key in ("snippet", "content", "text", "context"):
        val = item.get(key)
        if isinstance(val, str) and val.strip():
            return val.replace("\n", " ").strip()
    return ""


def search_qmd(
    query: str,
    limit: int,
    *,
    mode: str = "query",
    collection: str | None = None,
) -> list[tuple[float, str, str, str]]:
    cmd = ["qmd", mode, query, "--json", "-n", str(limit)]
    if collection:
        cmd.extend(["-c", collection])

    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "qmd failed").strip().split("\n")[0]
        raise RuntimeError(err)

    payload = json.loads(proc.stdout)
    items = payload if isinstance(payload, list) else payload.get("results", payload.get("items", []))
    if not isinstance(items, list):
        raise RuntimeError("Unexpected QMD JSON output")

    results: list[tuple[float, str, str, str]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        score = _parse_qmd_score(item.get("score", item.get("relevance", 0)))
        title = _qmd_title(item)
        summary = _qmd_summary(item)
        location = str(item.get("file") or item.get("path") or "")
        results.append((score, title, summary, location))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:limit]


def search(
    query: str,
    limit: int = 10,
    *,
    engine: str = "auto",
    collection: str | None = None,
) -> tuple[str, list[tuple[float, str, str, str | None]]]:
    use_qmd = engine in {"auto", "qmd", "search", "vsearch", "query"}
    if use_qmd and qmd_available():
        mode = "query" if engine in {"auto", "qmd", "query"} else engine
        try:
            hits = search_qmd(query, limit, mode=mode, collection=collection)
            return ("qmd", [(s, t, sm, loc) for s, t, sm, loc in hits])
        except (RuntimeError, json.JSONDecodeError, OSError) as exc:
            if engine != "auto":
                raise
            print(f"QMD unavailable ({exc}); using wiki BM25 fallback.", file=sys.stderr)

    fallback = search_fallback(query, limit)
    return ("bm25", [(s, t, sm, None) for s, t, sm in fallback])


def main() -> None:
    parser = argparse.ArgumentParser(description="Search Intelligence Hub")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument(
        "--engine",
        choices=["auto", "qmd", "query", "search", "vsearch", "bm25"],
        default="auto",
        help="auto=qmd hybrid with fallback (default)",
    )
    parser.add_argument(
        "-c",
        "--collection",
        choices=["hub-wiki", "hub-raw", "hub-outputs"],
        help="Limit to one QMD collection",
    )
    args = parser.parse_args()

    if args.engine == "bm25" and not WIKI_DIR.exists():
        return

    engine, results = search(
        args.query,
        args.limit,
        engine=args.engine,
        collection=args.collection,
    )

    if not results:
        print("No matches.")
        return

    for score, name, summary, location in results:
        loc = f"  {location}" if location else ""
        print(f"{score:6.2f}  [[{name}]]{loc}  {summary[:120]}...")
    print(f"\n# engine: {engine}", file=sys.stderr)


if __name__ == "__main__":
    main()
