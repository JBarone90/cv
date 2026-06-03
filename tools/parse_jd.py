#!/usr/bin/env python3
"""Extract plain text from a PDF or Word file and print to stdout."""

import sys
from pathlib import Path


def extract_pdf(path: Path) -> str:
    import pdfplumber
    pages = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
    return "\n\n".join(pages)


def extract_docx(path: Path) -> str:
    from docx import Document
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: parse_jd.py <file.pdf|file.docx>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)

    suffix = path.suffix.lower()
    if suffix == ".pdf":
        print(extract_pdf(path))
    elif suffix in (".docx", ".doc"):
        print(extract_docx(path))
    else:
        print(f"Unsupported format: {suffix}. Supported: .pdf, .docx", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
