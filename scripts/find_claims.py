#!/usr/bin/env python3
"""Identify candidate quantitative claims from the raw extract."""
import json
import re
from pathlib import Path

ROOT = Path("/Users/pedro/git_repos/big_impact")
RAW = ROOT / "state" / "_raw_extract.json"

# match numbers w/ %, or thousand separators, or currency, or "milhão/mil"
NUM_RE = re.compile(
    r"(?ix)("
    r"\d+[\.,]?\d*\s?(?:%|por\s?cento)|"          # percentages
    r"(?:€|EUR|US\$|\$)\s?\d[\d\.,]*|"             # currencies
    r"\d[\d\.,]+\s?(?:€|EUR|US\$|\$)|"
    r"\d+[\.,]?\d*\s?(?:mil|milh[õo]es?|bilh[õo]es?|mi|bn|M|k)\b|"  # scale words
    r"\d{4,}[\.,]?\d*|"                            # large bare numbers
    r"\b\d+[\.,]\d+\b"                             # decimals
    r")"
)

def candidates_in_text(text):
    sentences = re.split(r"(?<=[\.\!\?])\s+|\n", text)
    hits = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        if NUM_RE.search(s):
            hits.append(s)
    return hits

def main():
    raw = json.loads(RAW.read_text())
    out = {"html": {}, "pdf": {}}
    for fname, secs in raw["html"].items():
        if not isinstance(secs, list):
            continue
        out["html"][fname] = []
        for sec in secs:
            blob = " \n".join(sec.get("text", []))
            for h in candidates_in_text(blob):
                out["html"][fname].append({
                    "heading": sec.get("heading"),
                    "sentence": h,
                })
    for fname, pages in raw["pdf"].items():
        if not isinstance(pages, list):
            continue
        out["pdf"][fname] = []
        for pg in pages:
            for h in candidates_in_text(pg["text"]):
                out["pdf"][fname].append({"page": pg["page"], "sentence": h})
    Path(ROOT / "state" / "_candidates.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )
    # print counts
    for k, v in out["html"].items():
        print(f"HTML {k}: {len(v)} candidates")
    for k, v in out["pdf"].items():
        print(f"PDF  {k}: {len(v)} candidates")

if __name__ == "__main__":
    main()
