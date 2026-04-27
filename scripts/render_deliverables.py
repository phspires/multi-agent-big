#!/usr/bin/env python3
"""Render BIG Impact PoV Review deliverables (PerSense, BCS+BT-03 case).

Fills the .pptx and .docx templates with content from per-agent state/ outputs.
The contract is `state/00_template-inspector/template_fields.md`:

PPTX Slide 1:
  - Group 21 / TextBox 8  -> Problem Statement (500-char block)
  - Group 6  / TextBox 10 -> Hipótese de valor (≤100 chars)
  - TextBox 18 (in Group 16) -> Métrica principal line
  - TextBox 35 / 36          -> Métricas suporte 1 / 2
  - Group 4 / TextBox 12     -> Tabela de Evidências (5 plain-text lines)
PPTX Slide 2:
  - Group 4 / TextBox 12     -> Pilot Sketch
  - Group 20 / TextBox 23    -> Budget Range
  - TextBox 27 (in Group 25) -> Pressuposto 1
  - TextBox 39               -> Pressuposto 2
  - TextBox 40               -> Pressuposto 3

DOCX:
  - Replace project-name "(preencher)" with "PerSense"
  - Leave contact "(preencher)" intentionally blank for the human to fill
  - Append free-form Notas Adicionais body: thesis appendix, alternatives table,
    top-5 partner first-contacts, per-EV provenance, methodology, Open Issues.
"""

from __future__ import annotations

import copy
import json
import re
import sys
import zipfile
from pathlib import Path

from pptx import Presentation
from docx import Document
from docx.shared import Pt as DocxPt
from lxml import etree

ROOT = Path("/Users/pedro/git_repos/big_impact")
STATE = ROOT / "state"
PPTX_TEMPLATE = ROOT / "BIG Impact - Proof of Value Review Template.pptx"
DOCX_TEMPLATE = ROOT / "Big Impact - PoV Review - Evidence Notes Template.docx"
OUT_DIR = ROOT / "outputs"
PPTX_OUT = OUT_DIR / "PoV_Review_PerSense.pptx"
DOCX_OUT = OUT_DIR / "Evidence_Notes_PerSense.docx"

PROJECT_NAME = "PerSense"

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"

EV_RE = re.compile(r"\bEV-\d{3}\b")


# --------------------------------------------------------------------------- #
# Input loaders                                                               #
# --------------------------------------------------------------------------- #

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def load_inputs() -> dict:
    return {
        "problem_md": read(STATE / "03_problem-definer" / "problem.md"),
        "value_md": read(STATE / "06_value-hypothesis" / "value.md"),
        "pilot_md": read(STATE / "07_pilot-designer" / "pilot.md"),
        "evidence_table": json.loads(read(STATE / "08_evidence-table-builder" / "evidence_table.json")),
        "ledger": json.loads(read(STATE / "01_evidence-curator" / "ledger.json")),
        "theses": json.loads(read(STATE / "04_business-thesis-generator" / "business_theses.json")),
        "chosen_thesis_md": read(STATE / "05_thesis-selector" / "chosen_thesis.md"),
        "partner_map_md": read(STATE / "09_partner-mapper" / "partner_map.md"),
    }


# --------------------------------------------------------------------------- #
# Draft parsers                                                               #
# --------------------------------------------------------------------------- #

def extract_problem_block(problem_md: str) -> str:
    """Extract the 500-char Slide-facing block from problem.md.

    Block lives between `## Slide-facing block` heading and the next `---`
    delimiter; the actual sentence is the first `> ...` blockquote line(s).
    """
    m = re.search(r"## Slide-facing block.*?\n(.+?)\n---", problem_md, re.S)
    if not m:
        raise ValueError("Slide-facing block section not found in problem.md")
    sect = m.group(1)
    # Pull the blockquote line(s) — start with "> "
    quote_lines = []
    for line in sect.splitlines():
        s = line.strip()
        if s.startswith(">"):
            quote_lines.append(s.lstrip("> ").strip())
    if not quote_lines:
        raise ValueError("Could not find blockquote in slide-facing block")
    text = " ".join(quote_lines).strip()
    return text


def extract_main_hypothesis(value_md: str) -> str:
    """Extract the ≤100-char main hypothesis from value.md."""
    # Look under "### Hipótese de valor (principal)" heading; pull the bold blockquote
    m = re.search(r"### Hipótese de valor \(principal\).*?\n+>\s*\*\*(.+?)\*\*", value_md, re.S)
    if not m:
        # fallback: any bold line in a quote near the heading
        m = re.search(r"### Hipótese de valor \(principal\).*?\n+>\s*(.+?)\n", value_md, re.S)
        if not m:
            raise ValueError("Main hypothesis not found in value.md")
        return m.group(1).strip().strip("*")
    return m.group(1).strip()


def extract_metrics_block(value_md: str) -> str:
    """Extract the principal + suporte 1 + suporte 2 metric lines as one combined block."""
    # Section starts at "### Métricas" and ends at next "###"
    m = re.search(r"### Métricas.*?\n+(.+?)(?=\n---|\n### )", value_md, re.S)
    if not m:
        raise ValueError("Métricas section not found in value.md")
    sect = m.group(1)
    bullets = []
    for line in sect.splitlines():
        s = line.strip()
        if s.startswith("- "):
            bullets.append(s[2:].strip())
    if len(bullets) < 3:
        raise ValueError(f"Expected 3 metric bullets, got {len(bullets)}")
    # Strip markdown bold
    bullets = [re.sub(r"\*\*", "", b) for b in bullets[:3]]
    return bullets  # list of 3 strings: principal, suporte1, suporte2


def extract_pilot_sketch(pilot_md: str) -> str:
    """Pilot Sketch narrative — the bold blockquote under '### Pilot Sketch'."""
    m = re.search(r"### Pilot Sketch.*?\n+>\s*\*\*(.+?)\*\*\s*\n", pilot_md, re.S)
    if not m:
        raise ValueError("Pilot Sketch block not found in pilot.md")
    return m.group(1).strip()


def extract_budget_range(pilot_md: str) -> str:
    m = re.search(r"### Budget Range.*?\n+>\s*\*\*(.+?)\*\*\s*\n", pilot_md, re.S)
    if not m:
        raise ValueError("Budget Range block not found in pilot.md")
    return m.group(1).strip()


def extract_pressupostos(pilot_md: str) -> list[str]:
    """Three numbered Pressupostos strings."""
    m = re.search(r"### Pressupostos.*?\n+(.+?)(?=\n---|\n## )", pilot_md, re.S)
    if not m:
        raise ValueError("Pressupostos section not found in pilot.md")
    sect = m.group(1)
    items = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*\s*$", sect, re.M | re.S)
    if len(items) != 3:
        # Try multi-line with non-greedy across lines
        items = []
        for m_a in re.finditer(r"^\d+\.\s+\*\*(.+?)\*\*\s*\n", sect, re.M | re.S):
            items.append(" ".join(m_a.group(1).split()))
    if len(items) != 3:
        raise ValueError(f"Expected 3 Pressupostos, got {len(items)}")
    return [" ".join(s.split()) for s in items]


def extract_open_issues(md: str) -> list[str]:
    m = re.search(r"## Open Issues[^\n]*\n+(.+?)(?=\n## |\Z)", md, re.S)
    if not m:
        return []
    out = []
    for m_a in re.finditer(r"^\d+\.\s+(.+?)(?=\n\d+\.\s|\Z)", m.group(1), re.S | re.M):
        out.append(" ".join(m_a.group(1).split()))
    return out


def extract_top5_partners(partner_map_md: str) -> list[dict]:
    """Pull the 5 rows from the 'Top 5 — Recommended First Contact' markdown table."""
    m = re.search(r"## Top 5.*?\n(.+?)\n\n", partner_map_md, re.S)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7 or cells[0].startswith("---") or cells[0] == "#":
            continue
        out.append({
            "rank": cells[0],
            "partner": re.sub(r"\*\*", "", cells[1]),
            "program": cells[2],
            "ask": cells[3],
            "channel": cells[4],
            "ttlOI": cells[5],
            "this_week_action": cells[6],
        })
    return out


# --------------------------------------------------------------------------- #
# PPTX helpers                                                                #
# --------------------------------------------------------------------------- #

def find_shape_by_id(shapes, sid):
    for s in shapes:
        if s.shape_id == sid:
            return s
        if s.shape_type == 6:  # GROUP
            r = find_shape_by_id(s.shapes, sid)
            if r is not None:
                return r
    return None


def replace_textbox(shape, lines: list[str]) -> None:
    """Replace text in a textbox, preserving original run/paragraph formatting.

    Captures the first run's <a:rPr> and the first paragraph's <a:pPr>, then
    rebuilds the text body with one paragraph per line.
    """
    tf = shape.text_frame
    txBody = tf._txBody

    # Capture template formatting from the first run/paragraph
    template_rPr = None
    template_pPr = None
    for p_el in txBody.findall(f"{{{A_NS}}}p"):
        pPr = p_el.find(f"{{{A_NS}}}pPr")
        if pPr is not None and template_pPr is None:
            template_pPr = copy.deepcopy(pPr)
        for r_el in p_el.findall(f"{{{A_NS}}}r"):
            rPr = r_el.find(f"{{{A_NS}}}rPr")
            if rPr is not None:
                template_rPr = copy.deepcopy(rPr)
                break
        if template_rPr is not None:
            break

    # Remove existing paragraphs
    for p_el in list(txBody.findall(f"{{{A_NS}}}p")):
        txBody.remove(p_el)

    for line in lines:
        p_el = etree.SubElement(txBody, f"{{{A_NS}}}p")
        if template_pPr is not None:
            p_el.append(copy.deepcopy(template_pPr))
        r_el = etree.SubElement(p_el, f"{{{A_NS}}}r")
        if template_rPr is not None:
            r_el.append(copy.deepcopy(template_rPr))
        else:
            etree.SubElement(r_el, f"{{{A_NS}}}rPr", {"lang": "pt-PT"})
        t_el = etree.SubElement(r_el, f"{{{A_NS}}}t")
        t_el.text = line if line else ""


def shrink_font(shape, size_pt: float) -> None:
    for r in shape.text_frame._txBody.iter(f"{{{A_NS}}}rPr"):
        r.set("sz", str(int(size_pt * 100)))


# --------------------------------------------------------------------------- #
# Render PPTX                                                                 #
# --------------------------------------------------------------------------- #

def render_pptx(ctx: dict) -> tuple[Path, list[str]]:
    warnings: list[str] = []
    prs = Presentation(str(PPTX_TEMPLATE))
    s1, s2 = prs.slides[0], prs.slides[1]

    # ---------------- Slide 1 ----------------

    # Problem Statement: 500-char block -> shape id 8 inside Group 21
    tb_problem = find_shape_by_id(s1.shapes, 8)
    problem_text = ctx["problem_text"]
    if len(problem_text) > 500:
        warnings.append(f"Problem block {len(problem_text)} > 500 chars")
    replace_textbox(tb_problem, [problem_text])
    shrink_font(tb_problem, 11.0)

    # Hipótese: shape 10 inside Group 6
    tb_hyp = find_shape_by_id(s1.shapes, 10)
    hyp_text = ctx["main_hypothesis"]
    if len(hyp_text) > 110:
        warnings.append(f"Main hypothesis {len(hyp_text)} > 110 chars (soft cap)")
    replace_textbox(tb_hyp, [hyp_text])

    # Métricas: principal=18, suporte1=35, suporte2=36
    pm, sm1, sm2 = ctx["metrics"]
    tb_pm = find_shape_by_id(s1.shapes, 18)
    tb_s1 = find_shape_by_id(s1.shapes, 35)
    tb_s2 = find_shape_by_id(s1.shapes, 36)
    replace_textbox(tb_pm, [pm])
    shrink_font(tb_pm, 9.0)
    replace_textbox(tb_s1, [sm1])
    shrink_font(tb_s1, 9.0)
    replace_textbox(tb_s2, [sm2])
    shrink_font(tb_s2, 9.0)

    # Tabela de Evidências: shape 12 inside Group 4
    tb_evid = find_shape_by_id(s1.shapes, 12)
    evid_lines = []
    for row in ctx["evidence_rows"]:
        evid_lines.append(
            f"{row['aspect_pt']} · {row['number']} · {row['source']} [{row['evidence_id']}]"
        )
    replace_textbox(tb_evid, evid_lines)
    shrink_font(tb_evid, 10.0)

    # ---------------- Slide 2 ----------------

    # Pilot Sketch: shape 12 inside Group 4
    tb_pilot = find_shape_by_id(s2.shapes, 12)
    replace_textbox(tb_pilot, [ctx["pilot_sketch"]])
    shrink_font(tb_pilot, 9.0)

    # Budget Range: shape 23 inside Group 20
    tb_budget = find_shape_by_id(s2.shapes, 23)
    replace_textbox(tb_budget, [ctx["budget_range"]])
    shrink_font(tb_budget, 9.0)

    # Pressupostos x3: shape 27 (in Group 25), 39, 40
    tb_a1 = find_shape_by_id(s2.shapes, 27)
    tb_a2 = find_shape_by_id(s2.shapes, 39)
    tb_a3 = find_shape_by_id(s2.shapes, 40)
    p1, p2, p3 = ctx["pressupostos"]
    replace_textbox(tb_a1, [p1])
    shrink_font(tb_a1, 8.5)
    replace_textbox(tb_a2, [p2])
    shrink_font(tb_a2, 8.5)
    replace_textbox(tb_a3, [p3])
    shrink_font(tb_a3, 8.5)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    prs.save(str(PPTX_OUT))
    return PPTX_OUT, warnings


# --------------------------------------------------------------------------- #
# Render DOCX                                                                 #
# --------------------------------------------------------------------------- #

def render_docx(ctx: dict, evids_in_deck: list[str]) -> tuple[Path, list[str]]:
    warnings: list[str] = []
    doc = Document(str(DOCX_TEMPLATE))

    # The header paragraph (index 4) contains both labels in one paragraph with
    # a line break. Replace only the project-name (preencher); leave contact
    # (preencher) intact for the human to fill.
    target = None
    for p in doc.paragraphs:
        if "Nome do projeto/startup" in p.text and "(preencher)" in p.text:
            target = p
            break
    if target is None:
        raise RuntimeError("Project-name (preencher) paragraph not found in docx")

    # Replace only the FIRST occurrence of "(preencher)" in the runs.
    replaced = False
    for run in target.runs:
        if not replaced and "(preencher)" in run.text:
            run.text = run.text.replace("(preencher)", PROJECT_NAME, 1)
            replaced = True
    if not replaced:
        # If runs are split, fall back to whole-text replace via single run.
        full = target.text.replace("(preencher)", PROJECT_NAME, 1)
        for i, run in enumerate(target.runs):
            run.text = full if i == 0 else ""

    # ----- Body content -----
    ledger_by_id = {e["id"]: e for e in ctx["ledger"]["entries"]}

    def add_h(text: str, size: int = 13) -> None:
        p = doc.add_paragraph()
        r = p.add_run(text)
        r.bold = True
        r.font.size = DocxPt(size)

    def add_p(text: str, size: int = 10, bold: bool = False) -> None:
        p = doc.add_paragraph()
        r = p.add_run(text)
        r.bold = bold
        r.font.size = DocxPt(size)

    add_h("Methodology — 3-phase evidence curation", 12)
    add_p(
        "Three-phase pipeline anchored to the original PerSense dossier: (1) extract — "
        "scripts/extract_text.py + scripts/find_claims.py pulled quantitative claims "
        "from PDFs/HTML and assigned stable EV-IDs (EV-001 … EV-088); (2) verify — "
        "ledger.json records source_file + page + section + original_context, and "
        "every claim was cross-referenced against external sources before slide use; "
        "(3) augment — internal_only EV-IDs (EV-041, EV-042, EV-043) are flagged "
        "honestly and never appear on slide-facing magnitude lines. Discrepancies "
        f"resolved by preferring the externally-verified figure. Total ledger size: "
        f"{len(ctx['ledger']['entries'])} entries; sources scanned: "
        f"{len(ctx['ledger']['metadata'].get('sources_scanned', []))}."
    )

    add_h("Chosen business thesis — BT-03 PT private oncology white-label", 12)
    # Strip markdown headings/blocks from chosen_thesis_md and inline as paragraphs.
    for block in ctx["chosen_thesis_md"].split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("# "):
            continue  # already covered by the heading above
        if block.startswith("## "):
            add_p(block[3:].strip(), bold=True, size=11)
        elif block.startswith("### "):
            add_p(block[4:].strip(), bold=True, size=10)
        else:
            # Strip simple markdown emphasis
            txt = re.sub(r"\*\*(.+?)\*\*", r"\1", block)
            add_p(txt, size=10)

    add_h("Alternative theses considered (one-line each)", 12)
    for t in ctx["theses"]["theses"]:
        if t["id"] == ctx["theses"]["recommended_id"]:
            continue
        line = (
            f"{t['id']} — {t['name']} | customer: {t['customer']} | "
            f"time-to-revenue: {t['time_to_first_revenue_months']} mo | "
            f"composite: {t['score']['composite']} | one-line: {t['one_line']}"
        )
        add_p(line, size=9)

    add_h("Top-5 partner first-contacts (BCS+BT-03)", 12)
    for row in ctx["top5_partners"]:
        add_p(
            f"{row['rank']}. {row['partner']} — {row['program']} — "
            f"ask: {row['ask']} — channel: {row['channel']} — "
            f"time-to-LOI: {row['ttlOI']} — this-week: {row['this_week_action']}",
            size=9,
        )

    add_h("Per-EV provenance (EV-IDs cited on slides)", 12)
    documented: list[str] = []
    for evid in evids_in_deck:
        e = ledger_by_id.get(evid)
        add_p(evid, bold=True, size=10)
        if e is None:
            add_p("Not found in ledger.", size=9)
            continue
        documented.append(evid)
        add_p(f"Claim: {e.get('claim_pt','—')}", size=9)
        meta = (
            f"Number: {e.get('number') or '—'} | "
            f"Topic: {e.get('topic') or '—'} | "
            f"Confidence: {e.get('confidence') or '—'} | "
            f"Source: {e.get('source_file') or '—'}"
            + (f" — {e['source_section']}" if e.get("source_section") else "")
            + (f" (p.{e['source_page']})" if e.get("source_page") else "")
        )
        add_p(meta, size=9)
        if e.get("original_context"):
            add_p(f"Original: \"{e['original_context']}\"", size=9)
        if e.get("notes"):
            add_p(f"Notes: {e['notes']}", size=9)

    add_h("Open Issues / Não Resolvido (aggregated)", 12)
    for label, items in ctx["open_issues"].items():
        if not items:
            continue
        add_p(f"From {label}:", bold=True, size=10)
        for it in items:
            add_p(f"• {it}", size=9)

    add_h("Coverage check", 12)
    add_p(f"EV-IDs cited in deck: {len(evids_in_deck)} — {', '.join(evids_in_deck)}", size=9)
    add_p(f"EV-IDs documented in this notes file: {len(documented)} — {', '.join(documented)}", size=9)
    missing = sorted(set(evids_in_deck) - set(documented))
    if missing:
        add_p(f"Missing from notes: {', '.join(missing)}", bold=True, size=9)
        warnings.append(f"DOCX missing EV-IDs: {missing}")

    add_h("Sources scanned (internal dossier)", 12)
    for s in ctx["ledger"]["metadata"].get("sources_scanned", []):
        add_p(f"• {s}", size=9)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc.save(str(DOCX_OUT))
    return DOCX_OUT, warnings


# --------------------------------------------------------------------------- #
# Validation                                                                  #
# --------------------------------------------------------------------------- #

def evids_in_zip(path: Path, only_slides: bool = False) -> set[str]:
    found: set[str] = set()
    with zipfile.ZipFile(path, "r") as z:
        for name in z.namelist():
            if not name.endswith(".xml"):
                continue
            if only_slides and "/slides/slide" not in name:
                continue
            data = z.read(name).decode("utf-8", errors="ignore")
            stripped = re.sub(r"<[^>]+>", "", data)
            found.update(EV_RE.findall(stripped))
    return found


def count_placeholder_in_zip(path: Path, token: str = "(preencher)") -> int:
    n = 0
    with zipfile.ZipFile(path, "r") as z:
        for name in z.namelist():
            if not name.endswith(".xml"):
                continue
            data = z.read(name).decode("utf-8", errors="ignore")
            stripped = re.sub(r"<[^>]+>", "", data)
            n += stripped.count(token)
    return n


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #

def main() -> int:
    inp = load_inputs()

    metrics = extract_metrics_block(inp["value_md"])
    pressupostos = extract_pressupostos(inp["pilot_md"])

    ctx = {
        "problem_text": extract_problem_block(inp["problem_md"]),
        "main_hypothesis": extract_main_hypothesis(inp["value_md"]),
        "metrics": metrics,
        "evidence_rows": inp["evidence_table"]["rows"],
        "pilot_sketch": extract_pilot_sketch(inp["pilot_md"]),
        "budget_range": extract_budget_range(inp["pilot_md"]),
        "pressupostos": pressupostos,
        "ledger": inp["ledger"],
        "theses": inp["theses"],
        "chosen_thesis_md": inp["chosen_thesis_md"],
        "top5_partners": extract_top5_partners(inp["partner_map_md"]),
        "open_issues": {
            "problem.md": extract_open_issues(inp["problem_md"]),
            "value.md": extract_open_issues(inp["value_md"]),
            "pilot.md": extract_open_issues(inp["pilot_md"]),
        },
    }

    pptx_path, ppw = render_pptx(ctx)
    pptx_evids = sorted(evids_in_zip(pptx_path, only_slides=True),
                        key=lambda x: int(x.split("-")[1]))
    docx_path, dpw = render_docx(ctx, pptx_evids)
    docx_evids = sorted(evids_in_zip(docx_path), key=lambda x: int(x.split("-")[1]))

    pptx_size = pptx_path.stat().st_size
    docx_size = docx_path.stat().st_size

    pptx_ph = count_placeholder_in_zip(pptx_path)
    docx_ph = count_placeholder_in_zip(docx_path)

    coverage_missing = sorted(set(pptx_evids) - set(docx_evids))

    print("=" * 70)
    print("RENDER SUMMARY")
    print(f"  pptx: {pptx_path} ({pptx_size//1024} KB, "
          f"(preencher) remaining: {pptx_ph})")
    print(f"  docx: {docx_path} ({docx_size//1024} KB, "
          f"(preencher) remaining: {docx_ph} [contact field intentionally left for human])")
    print(f"  EV-IDs cited in deck ({len(pptx_evids)}): {pptx_evids}")
    print(f"  EV-IDs documented in notes ({len(docx_evids)}): {docx_evids}")
    cov = 100.0 if not pptx_evids else 100.0 * len(set(pptx_evids) & set(docx_evids)) / len(pptx_evids)
    print(f"  Coverage: {cov:.0f}%")
    if coverage_missing:
        print(f"  Missing in notes: {coverage_missing}")
    if ppw or dpw:
        print("  Warnings:")
        for w in ppw + dpw:
            print(f"    - {w}")

    failures = []
    if pptx_size < 20_000:
        failures.append(f"pptx size {pptx_size} < 20KB")
    if docx_size < 10_000:
        failures.append(f"docx size {docx_size} < 10KB")
    if pptx_ph != 0:
        failures.append(f"pptx still has {pptx_ph} (preencher) tokens")
    if docx_ph != 1:
        failures.append(f"docx (preencher) count {docx_ph} != 1 (expected: only the contact field left)")
    if coverage_missing:
        failures.append(f"EV-IDs in deck missing from notes: {coverage_missing}")

    if failures:
        print("  FAILURES:")
        for f in failures:
            print(f"    - {f}")
        print("=" * 70)
        return 1
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
