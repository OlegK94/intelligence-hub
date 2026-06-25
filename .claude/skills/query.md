# /query — Wiki Query

Answer a question using the wiki and file valuable answers back.

## Usage

```
/query "How do my health protocols relate to Hyrox training?"
/query "Compare OK Capital vs Wagglz tax structure" --output slides
/query "What supplements am I taking?"
```

## Steps

1. Read `wiki/index.md` to locate relevant pages.
2. Run `python3 tools/search.py "query"` — hybrid BM25/vector search.
3. Read the top-matching wiki pages in full.
4. Synthesize a clear answer with citations: `[[Wiki Page]]`.
5. Write output to:
   - `outputs/notes/YYYY-MM-DD-slug.md` (default)
   - `outputs/slides/YYYY-MM-DD-slug.md` (Marp, when `--output slides`)
   - `outputs/charts/YYYY-MM-DD-slug.png` (matplotlib, when `--output chart`)
6. If the answer is valuable and reusable, file it back into `wiki/syntheses/` or `wiki/comparisons/`.
7. Append one entry to `wiki/log.md`.

## Output style

- Apple-style HTML for visualizations (dark accent `#0071E3`, background `#F5F5F7`, SF Pro fonts, large numbers, generous whitespace)
- Markdown for notes and slides
