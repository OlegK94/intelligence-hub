# Clippings/ — Web-Clips & Artikel

Gespeicherte Artikel aus Safari, Obsidian Web Clipper oder manuell kopierte Inhalte.

## Was hierher kommt
- Safari Web Clips (via Obsidian Web Clipper oder Reader)
- LinkedIn-Posts (als MD gespeichert)
- Newsletter, Blog-Artikel, Research-Snippets
- Alles was du "für später" gespeichert hast

## Ingest
```bash
python3 tools/ingest.py --scope clippings
```

Claude liest alle .md/.pdf Dateien, erstellt Source-Seiten im Wiki und verlinkt relevante Entitäten.
