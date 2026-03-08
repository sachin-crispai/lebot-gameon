# OpenEnv Redbook

Canonical merged document for OpenEnv hackathon materials.

## Standard

- Output: `openenv-redbook-a4.pdf`
- Page size: **A4 landscape** (`841.89 x 595.28 pt`)
- Rule: every source page is scaled proportionally and centered on A4 landscape.

## Source Directory

Place source PDFs in:

- `books/openenv-redbook/sources/`

Use numeric prefixes for ordering, e.g.:

- `01-openenv-opening-slides.pdf`
- `02-openenv-hackathon-challenge.pdf`
- `03-openenv-technical-content.pdf`

## Build

```bash
uv pip install --python .venv/bin/python pypdf
./.venv/bin/python books/openenv-redbook/build_openenv_redbook.py
```

## Add More Material Later

1. Add the new PDF to `books/openenv-redbook/sources/` with the next numeric prefix.
2. Re-run the build command.
3. Commit both the source PDF and regenerated `openenv-redbook-a4.pdf`.
