from __future__ import annotations

from pathlib import Path

from pypdf import PageObject, PdfReader, PdfWriter, Transformation

A4_WIDTH = 841.8898  # pt, landscape
A4_HEIGHT = 595.2756  # pt, landscape

ROOT = Path(__file__).resolve().parent
SOURCES_DIR = ROOT / "sources"
OUTPUT_PDF = ROOT / "openenv-redbook-a4.pdf"


def source_pdfs() -> list[Path]:
    return sorted(p for p in SOURCES_DIR.glob("*.pdf") if p.is_file())


def normalize_to_a4_landscape(page) -> PageObject:
    src_w = float(page.mediabox.width)
    src_h = float(page.mediabox.height)

    scale = min(A4_WIDTH / src_w, A4_HEIGHT / src_h)
    draw_w = src_w * scale
    draw_h = src_h * scale
    dx = (A4_WIDTH - draw_w) / 2
    dy = (A4_HEIGHT - draw_h) / 2

    canvas = PageObject.create_blank_page(width=A4_WIDTH, height=A4_HEIGHT)
    transform = Transformation().scale(scale, scale).translate(dx, dy)
    canvas.merge_transformed_page(page, transform, over=True)
    return canvas


def build() -> None:
    files = source_pdfs()
    if not files:
        raise SystemExit(f"No PDFs found in {SOURCES_DIR}")

    writer = PdfWriter()
    total_pages = 0

    for path in files:
        reader = PdfReader(str(path))
        print(f"Including: {path.name} ({len(reader.pages)} pages)")
        for page in reader.pages:
            writer.add_page(normalize_to_a4_landscape(page))
            total_pages += 1

    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PDF.open("wb") as f:
        writer.write(f)

    print(f"Wrote: {OUTPUT_PDF}")
    print(f"Pages: {total_pages}")
    print(f"Page size: {A4_WIDTH:.2f} x {A4_HEIGHT:.2f} pt (A4 landscape)")


if __name__ == "__main__":
    build()
