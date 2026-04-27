---
description: Run the full BIG Impact PoV pipeline end-to-end. Optional arg = step name or number to start from (e.g., `/run-pipeline 4` to start at step 4). Default = 1 (full run).
---

You are the orchestrator for the BIG Impact PoV multi-agent pipeline. Execute the steps below **in order**, dispatching each subagent via the Agent tool with `subagent_type: general-purpose` and the agent definition file as the prompt anchor (since project subagents aren't auto-registered in this harness).

**Starting step**: $ARGUMENTS (default: step 1).

**After every successful agent run, commit with a structured message**:
```
git add -A && git commit -q -m "[<agent-name>] <one-line context>"
```

If any review returns REVISE, re-invoke the originating agent with the review attached and loop until PASS. After all four reviews PASS, run the renderer.

---

## Steps

### Step 0 — Preflight (always run)
- Confirm git working tree is clean (`git status -s` must be empty).
- Confirm `state/thinking_framework.md` exists. If not, abort and tell the user.
- Read `state/00_template-inspector/template_fields.md` if it exists; if not, run step 0a first.

### Step 0a — Template inspection (if `template_fields.md` missing)
- Dispatch `template-inspector`: read `.claude/agents/template-inspector.md`, follow exactly. Output: `state/00_template-inspector/template_fields.md`.

### Step 1 — Evidence + methodology (parallel, both required)
Dispatch in **a single message with two parallel Agent calls**:
- `evidence-curator` (3-phase: extract → verify → augment) → `state/01_evidence-curator/ledger.json`
- `case-methodology-reader` → `state/02_case-methodology-reader/methodology_brief.md`

Skip whichever already has a recent file unless the user passed `--force`.

### Step 2 — Problem definition
Dispatch `problem-definer`. Default segment is **Breast Cancer Survivors (BCS)** unless the user explicitly named another segment in $ARGUMENTS. The agent file enforces the moat-segment rule. Output: `state/03_problem-definer/problem.md`.

### Step 3 — Business theses
Dispatch `business-thesis-generator` (3–5 candidates, each with wedge + expansion + buyer_pain + open_issues). Output: `state/04_business-thesis-generator/business_theses.json`.

### Step 4 — Thesis selection
Dispatch `thesis-selector`. By default picks highest composite score. If the user passed `BT-XX` in $ARGUMENTS, select that one. Output: `state/05_thesis-selector/chosen_thesis.md` (with full Value Proposition Canvas section).

### Step 5 — Value hypothesis
Dispatch `value-hypothesis`. Reads chosen_thesis.md. Must include ≥1 clinical endpoint AND ≥1 willingness-to-pay metric AND a `Modelo de negócio` line. Output: `state/06_value-hypothesis/value.md`.

### Step 6 — Pilot design
Dispatch `pilot-designer`. Reads chosen_thesis.md. Must produce **exactly 3** assumption strings for Slide 2 Pressupostos boxes. Budget must be disambiguated (host institution €0; PoV team external funding allowed). Output: `state/07_pilot-designer/pilot.md`.

### Step 7 — Evidence table
Dispatch `evidence-table-builder`. Plain-text 4–6 lines (`Aspecto · Número · Fonte`). Not a structured table. Output: `state/08_evidence-table-builder/evidence_table.json`.

### Step 8 — Partner mapping (parallel with step 7 if reordered, sequential by default)
Dispatch `partner-mapper`. Includes Mom-Test discovery questions for top 5 partners. Output: `state/09_partner-mapper/{partner_map.json, partner_map.md, discovery_questions.md}`.

### Step 9 — Critical review (4 parallel calls)
Dispatch `critical-reviewer` four times in **a single message** (parallel), one per artifact:
- problem.md → `state/10_critical-reviewer/problem.review.md`
- value.md → `state/10_critical-reviewer/value.review.md`
- pilot.md → `state/10_critical-reviewer/pilot.review.md`
- evidence_table.json → `state/10_critical-reviewer/evidence_table.review.md`

If any returns **REVISE**: re-dispatch the originating agent with the review file attached as input. Loop until all four are **PASS**.

### Step 10 — Render deliverables
Dispatch `deliverable-renderer`. Verifies all four reviews are PASS, then runs `scripts/render_deliverables.py` to produce `outputs/PoV_Review_PerSense.pptx` and `outputs/Evidence_Notes_PerSense.docx`.

---

## Final report

After step 10, print:
- Git log of commits made during this run (`git log --oneline -N` where N = number of steps run)
- Output file paths + sizes
- Any REVISE→PASS loops that happened (which artifact, how many iterations)
- Any open issues aggregated across drafts
- Suggested next outreach action (top 1 from partner_map.md)

---

## Notes

- Each agent definition is in `.claude/agents/<name>.md`. The full agent file is the operating spec; pass relative context (paths to inputs, what changed) in the dispatch prompt rather than re-stating the spec.
- Because project subagents aren't auto-registered, use `subagent_type: general-purpose` and tell the agent to read `.claude/agents/<name>.md` first.
- Run agents sequentially when there's a data dependency; parallelize when independent (steps 1 and 9 are the parallel-friendly ones).
- Auto mode: do not stop to ask for confirmation between steps. Proceed unless an agent returns an unrecoverable error or the user interrupts.
