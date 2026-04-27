#!/usr/bin/env python3
"""Extract text from HTML and PDF sources for the evidence ledger."""
import os
import sys
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pdfplumber

ROOT = Path("/Users/pedro/git_repos/big_impact")
DOCS = ROOT / "project-docs"
OUT = ROOT / "state" / "_raw_extract.json"

def extract_html(path: Path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    # remove scripts/styles
    for s in soup(["script", "style"]):
        s.decompose()
    sections = []
    # walk by headings to get sectioned text
    current = {"heading": None, "level": None, "text": []}
    for el in soup.find_all(["h1", "h2", "h3", "h4", "p", "li", "td", "th"]):
        tag = el.name
        text = el.get_text(" ", strip=True)
        if not text:
            continue
        if tag in ("h1", "h2", "h3", "h4"):
            if current["heading"] or current["text"]:
                sections.append(current)
            current = {"heading": text, "level": tag, "text": []}
        else:
            current["text"].append(text)
    if current["heading"] or current["text"]:
        sections.append(current)
    return sections

def extract_pdf(path: Path):
    pages = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            txt = page.extract_text() or ""
            pages.append({"page": i, "text": txt})
    return pages

def main():
    out = {"html": {}, "pdf": {}}
    # HTML files
    for p in sorted(DOCS.glob("*.html")):
        try:
            out["html"][p.name] = extract_html(p)
        except Exception as e:
            out["html"][p.name] = {"error": str(e)}
    # PDFs (root + project-docs)
    pdf_paths = list(ROOT.glob("*.pdf")) + list(DOCS.glob("*.pdf"))
    for p in sorted(pdf_paths):
        try:
            out["pdf"][p.name] = extract_pdf(p)
        except Exception as e:
            out["pdf"][p.name] = {"error": str(e)}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"Wrote {OUT}")
    # quick sizes
    for n, secs in out["html"].items():
        if isinstance(secs, list):
            print(f"HTML {n}: {len(secs)} sections")
    for n, pages in out["pdf"].items():
        if isinstance(pages, list):
            print(f"PDF {n}: {len(pages)} pages")

if __name__ == "__main__":
    main()
