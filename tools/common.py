"""Shared utilities for Intelligence Hub LLM Wiki tools."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
INBOX_DIR = RAW_DIR / "inbox"
WIKI_DIR = ROOT / "wiki"
OUTPUTS_DIR = ROOT / "outputs"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"
MANIFEST_FILE = WIKI_DIR / ".ingest_manifest.json"
MODEL = os.environ.get("WIKI_MODEL", "claude-sonnet-4-6")

WIKI_SUBDIRS = ("entities", "concepts", "sources", "syntheses", "comparisons")
INGEST_EXTENSIONS = {".md", ".txt", ".markdown"}


def load_env_file() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


def get_client():
    load_env_file()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set.")
    import anthropic

    return anthropic.Anthropic(api_key=api_key)


def ensure_layout() -> None:
    for sub in WIKI_SUBDIRS:
        (WIKI_DIR / sub).mkdir(parents=True, exist_ok=True)
    for sub in ("notes", "slides", "charts"):
        (OUTPUTS_DIR / sub).mkdir(parents=True, exist_ok=True)
    INBOX_DIR.mkdir(parents=True, exist_ok=True)


def extract_json(text: str) -> dict:
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    else:
        brace = re.search(r"\{.*\}", text, re.DOTALL)
        if brace:
            text = brace.group(0)
    return json.loads(text)


def call_claude(client, system: str, user: str, max_tokens: int = 16384) -> str:
    message = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user}],
    )
    return "".join(block.text for block in message.content if block.type == "text")


def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*]', "", name.strip())
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "Untitled"


def normalize_page_name(name: str) -> str:
    name = name.strip()
    name = re.sub(r"\.md$", "", name, flags=re.IGNORECASE)
    name = re.sub(
        r"^wiki(?:entities|concepts|sources|syntheses|comparisons)",
        "",
        name,
        flags=re.IGNORECASE,
    )
    if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", name):
        name = " ".join(part.capitalize() for part in name.split("-"))
    return sanitize_filename(name)


def rel_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return str(path)


def load_manifest() -> dict:
    if MANIFEST_FILE.exists():
        return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    return {"ingested": []}


def save_manifest(manifest: dict) -> None:
    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def is_ingested(path: Path, manifest: dict) -> bool:
    rel = rel_path(path)
    return rel in manifest.get("ingested", [])


def mark_ingested(path: Path, manifest: dict) -> None:
    rel = rel_path(path)
    ingested = manifest.setdefault("ingested", [])
    if rel not in ingested:
        ingested.append(rel)
    save_manifest(manifest)


def collect_wiki_pages() -> dict[str, Path]:
    pages: dict[str, Path] = {}
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if path.name in ("index.md", "log.md"):
            continue
        pages[path.stem] = path
    return pages


def load_wiki_content(max_chars: int = 120_000) -> str:
    parts: list[str] = []
    total = 0
    for name, path in sorted(collect_wiki_pages().items()):
        content = path.read_text(encoding="utf-8")
        chunk = f"--- {rel_path(path)} ---\n{content}\n"
        if total + len(chunk) > max_chars:
            parts.append(f"... truncated ({len(collect_wiki_pages()) - len(parts)} more pages)")
            break
        parts.append(chunk)
        total += len(chunk)
    return "\n".join(parts) if parts else "(empty wiki)"


def read_file_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in INGEST_EXTENSIONS or suffix == ".txt":
        return path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader

            reader = PdfReader(str(path))
            return "\n\n".join(page.extract_text() or "" for page in reader.pages)
        except ImportError:
            return f"[PDF file: {rel_path(path)} — install pypdf for text extraction]"
    return path.read_text(encoding="utf-8", errors="replace")


def apply_wiki_articles(articles: list[dict]) -> list[str]:
    touched: list[str] = []
    subdir_map = {
        "entity": "entities",
        "entities": "entities",
        "concept": "concepts",
        "concepts": "concepts",
        "source": "sources",
        "sources": "sources",
        "synthesis": "syntheses",
        "syntheses": "syntheses",
        "comparison": "comparisons",
        "comparisons": "comparisons",
    }

    for entry in articles:
        if not isinstance(entry, dict):
            continue
        name = normalize_page_name(str(entry.get("name", "")))
        content = entry.get("content", "")
        page_type = str(entry.get("type", "concepts")).lower()
        if not name or not isinstance(content, str) or not content.strip():
            continue

        subdir = subdir_map.get(page_type, "concepts")
        target = WIKI_DIR / subdir / f"{name}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.strip() + "\n", encoding="utf-8")
        touched.append(name)

    return touched


def write_index(index_md: str | None) -> None:
    if index_md and index_md.strip():
        INDEX_FILE.write_text(index_md.strip() + "\n", encoding="utf-8")
    else:
        rebuild_index_fallback()


def rebuild_index_fallback() -> None:
    sections: dict[str, list[str]] = {
        "entities": [],
        "concepts": [],
        "sources": [],
        "syntheses": [],
        "comparisons": [],
    }
    for sub, label in sections.items():
        folder = WIKI_DIR / sub
        if folder.exists():
            for path in sorted(folder.glob("*.md")):
                sections[sub].append(f"- [[{path.stem}]]")

    lines = ["# Wiki Index\n", "Catalog of all compiled knowledge.\n"]
    for sub, items in sections.items():
        title = sub.capitalize()
        lines.append(f"\n## {title}\n\n")
        if items:
            lines.extend(f"{item}\n" for item in items)
        else:
            lines.append("_(none)_\n")

    INDEX_FILE.write_text("".join(lines), encoding="utf-8")


def append_log(entry: str) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = f"\n## [{stamp}] {entry}\n"
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(block)


def collect_ingest_candidates(
    file_arg: str | None = None,
    *,
    include_ingested: bool = False,
    scope: str = "inbox",
) -> list[Path]:
    manifest = load_manifest()
    candidates: list[Path] = []

    if file_arg:
        path = Path(file_arg)
        if not path.is_absolute():
            path = ROOT / path
        if path.is_file():
            return [path]
        raise FileNotFoundError(f"File not found: {file_arg}")

    scope_roots = {
        "inbox": [INBOX_DIR],
        "clippings": [ROOT / "Clippings"],
        "raw": [RAW_DIR],
    }
    search_roots = scope_roots.get(scope, [INBOX_DIR])

    for root in search_roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in INGEST_EXTENSIONS:
                continue
            if path.name in ("index.md", "log.md"):
                continue
            if not include_ingested and is_ingested(path, manifest):
                continue
            candidates.append(path)

    return candidates


def dated_output_path(kind: str, slug: str, ext: str = ".md") -> Path:
    date = datetime.now().strftime("%Y-%m-%d")
    safe = re.sub(r"[^a-z0-9-]", "-", slug.lower())[:60].strip("-")
    folder = OUTPUTS_DIR / kind
    folder.mkdir(parents=True, exist_ok=True)
    return folder / f"{date}-{safe}{ext}"
