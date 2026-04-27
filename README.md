# BIG Impact PoV — Multi-Agent Architecture (v3)

Orchestration map for the Phase 1 PoV deliverable (deadline **2026-04-29**). Product thesis: **JITAI-enabled adaptive Digital Therapeutic** (PerSense), built on the team's existing research in `project-docs/` and verified against external authoritative sources. **Business model is explored explicitly** — multiple revenue theses are generated, scored, and the chosen one drives the pilot's success criteria.

## What changed in v6

1. **`template-inspector` (new, haiku)** — runs first. Unzips the .pptx and .docx, lists every actual placeholder + label, writes `state/00_template-inspector/template_fields.md`. This file is the **contract**: every drafting agent reads it and is forbidden from inventing fields the templates don't have.
2. **Resolved a class of mismatches** between the methodology brief (which references a teaching-case full pitch deck with Slide 9 PS template + Slide 11 6-column evidence table) and the actual deliverable (a 2-slide PoV Review .pptx with no table XML, plus a .docx with two name/contact placeholders + free-form body). Rule: **template_fields.md wins for what fields exist; methodology_brief.md wins for how to write inside them**.
3. **Problem-definer** now packs the methodology brief's PS template (causal hypothesis + open critical question) inside the 500-char block. Multi-section schemas live in the working `problem.md` for downstream consumption, NOT on the slide.
4. **Pilot-designer** now produces exactly three assumption strings for the three Pressupostos `(preencher)` boxes (the slide actually has three, not one). Disambiguates the methodology brief's "no budget increase" rule: applies to the host institution, not the PoV team's external budget.
5. **Evidence-table-builder** produces 4–6 plain-text lines (`Aspecto · Número · Fonte`), not a structured table. The .pptx has no table XML to fill.
6. **Critical-reviewer** added template-fidelity checks across all four artifact types.

## What changed in v5

1. **Segment-defaulting rule** in `problem-definer.md`: when multiple segments are plausible, the segment with PerSense's strongest internal evidence wins by default. For this project that is **Breast Cancer Survivors** (N=126 cohort, AUC 0.78). Choosing a non-moat segment (e.g., university students) requires a written `Segment Choice Rationale` defending the deviation. `critical-reviewer` blocks on missing/weak rationale.
2. **Two startup frameworks adopted (only the ones that close real gaps)**:
   - **Value Proposition Canvas (Osterwalder)** baked into `thesis-selector.md` — forces explicit Customer Profile (Jobs / Pains / Gains for the BUYER) and Value Map (Products / Pain Relievers / Gain Creators) with 1:1 mapping. Holes in the mapping go into Open Issues.
   - **The Mom Test (Fitzpatrick)** baked into `partner-mapper.md` — for each top-5 partner, the agent now generates 5–7 discovery questions following the Mom Test rules (concrete past behavior, no hypotheticals, commitment over compliments). Output: `state/09_partner-mapper/discovery_questions.md`.
3. **Frameworks deliberately NOT adopted**: Lean Startup, Customer Development, Business Model Canvas, North Star — already implicit in the existing artifact structure. Adding them would be jargon overlay.

## What changed in v4

1. **`state/thinking_framework.md`** — seven non-negotiable conceptualization principles (laser focus, anti-AI-generic, Trojan Horse, sellable, risks-solvable, end-user-centric, radical openness). Every drafting agent reads it. Critical-reviewer enforces it as blockers via a Framework Compliance Checklist.
2. **business-thesis-generator** now requires per-thesis `wedge`, `expansion_path`, `buyer_pain`, and `open_issues` fields. Aloe-vera theses are dropped at this stage.
3. **deliverable-renderer** adds an "Open Issues / Não Resolvido" section to the Evidence Notes — aggregated from every artifact plus internal_only EV-IDs and ledger discrepancies.

## What changed in v3

1. **Business-thesis-generator** (new, opus) — generates 3–5 candidate revenue theses (DiGA payer, university B2B, employer wellness, clinic white-label, pharma companion, etc.), each anchored in ledger evidence with bottom-up TAM, time-to-revenue, regulatory path, capital intensity, defensibility, PoV-pilot fit, and a composite score. Output: `state/04_business-thesis-generator/business_theses.json`.
2. **Thesis-selector** (new, sonnet) — picks one thesis (highest composite score by default; user can override in invocation prompt). Output: `state/05_thesis-selector/chosen_thesis.md`. Drives the pilot's commercial success criteria.
3. **Value-hypothesis is now thesis-aware** — must include at least one willingness-to-pay / unit-economics metric tied to the chosen buyer. Adds a `Modelo de negócio` line.
4. **Pilot-designer is now thesis-aware** — secondary success metrics must include a buyer signal (LOI, paid follow-on commitment, DiGA-grade dossier readiness), not only clinical numbers.
5. **Critical-reviewer** adds rule #9: business-model coherence. A pilot that proves a feature but not a business is a blocker.
6. **Evidence Notes appendix** now includes both the chosen thesis (full) and alternatives considered (one-liners) — investors see the team stress-tested the revenue model.

## What changed in v2

1. **Evidence-curator is now 3-phase**: extract from project-docs → verify each claim against external URLs/DOIs → augment with newly-discovered relevant data. Every entry carries internal anchor + external source + verification status.
2. **Case PDFs are methodology, not content**: a new `case-methodology-reader` compresses both PDFs into a single `methodology_brief.md` that drafting agents read.
3. **JITAI-in-adaptive-DTx framing is explicit**: drafting agents must defend the *mechanism* (just-in-time + adaptive + DTx-grade endpoints + clinician-mediated triage), not a generic "mental-health-app".
4. **Per-agent model assignment** in frontmatter:
   - `opus`: problem-definer, value-hypothesis, pilot-designer, critical-reviewer, business-thesis-generator (high-stakes reasoning + judgment)
   - `sonnet`: evidence-curator, evidence-table-builder, deliverable-renderer, thesis-selector (heavy I/O, structured selection, code execution)
   - `haiku`: case-methodology-reader (small, semantic compression)
5. **Critical-reviewer blocks** on unverified external claims, discrepancies, "wellness app" framing, and (v3) business-model incoherence.

## Pipeline

```
        ┌──────────────────┐    ┌───────────────────────────┐
        │ evidence-curator │    │ case-methodology-reader   │
        │ (sonnet)         │    │ (haiku)                   │
        │ extract→verify→  │    │ reference PDFs → brief    │
        │ augment          │    │                           │
        └────────┬─────────┘    └────────┬──────────────────┘
                 │ ledger.json            │ methodology_brief.md
                 └────────┬───────────────┘
                          ▼
                 ┌────────────────┐
                 │ problem-       │
                 │ definer (opus) │
                 └────────┬───────┘
                          │ problem.md
                          ▼
                 ┌──────────────────────────┐
                 │ business-thesis-         │
                 │ generator (opus)         │
                 │ 3–5 revenue candidates   │
                 └────────┬─────────────────┘
                          │ business_theses.json
                          ▼
                 ┌──────────────────┐
                 │ thesis-selector  │   ← user can override
                 │ (sonnet)         │
                 └────────┬─────────┘
                          │ chosen_thesis.md
                          ▼
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
 ┌──────────────┐                   ┌──────────────┐
 │ value-       │                   │ pilot-       │
 │ hypothesis   │ ───────────────→  │ designer     │
 │ (opus)       │                   │ (opus)       │
 └──────┬───────┘                   └──────┬───────┘
        │ value.md                         │ pilot.md
        ▼                                  ▼
        └────────┬─────────────────┬───────┘
                 ▼                 ▼
        ┌──────────────────┐  ┌──────────────────┐
        │ evidence-table-  │  │ critical-        │
        │ builder (sonnet) │  │ reviewer (opus)  │
        └────────┬─────────┘  └─────────┬────────┘
                 │ evidence_table.json  │ reviews per artifact
                 └──────────┬───────────┘
                            ▼
                  all four PASS?
                            │
                            ▼
                  ┌──────────────────────┐
                  │ deliverable-renderer │
                  │ (sonnet)             │
                  └──────────┬───────────┘
                             ▼
                  outputs/PoV_Review_PerSense.pptx
                  outputs/Evidence_Notes_PerSense.docx
                    (with chosen thesis + alternatives appendix)
```

## Run order

1. **In parallel**: `evidence-curator` + `case-methodology-reader`
2. `problem-definer`
3. `business-thesis-generator`
4. `thesis-selector` (auto-pick highest composite, or user passes `select BT-XX` in the prompt)
5. **Sequential**: `value-hypothesis` → `pilot-designer` (both consume `chosen_thesis.md`)
6. `evidence-table-builder` after problem.md and value.md exist
7. `critical-reviewer` once per artifact (4 invocations, can be parallel)
8. If any review = REVISE → re-invoke originating agent with the review attached. Loop to PASS.
9. `deliverable-renderer` only after all four reviews PASS.

## State layout

```
big_impact/
├── BIG Impact - Problema, Publico e Evidencia.pdf       ← methodology (read by case-methodology-reader)
├── BIG Impact - Proof of Value Review Template.pptx     ← Slide 1+2 template
├── Big Impact - PoV Review - Evidence Notes Template.docx ← evidence notes template
├── Big Impact - Problem Definition Case Challenge.pdf   ← methodology (read by case-methodology-reader)
├── project-docs/                                        ← team's prior research (Portuguese)
│   ├── relatorio_saude_mental_digital_final (3).html    ← primary mental health report
│   ├── relatorio_saude_mental_digital_v2.html
│   ├── relatorio_estrategico_master_persense.html       ← PerSense / iNNOVSensing strategy + voice
│   └── oss_platform_analysis.html                       ← Stack A (mindLAMP) rationale
├── scripts/
│   ├── requirements.txt                                 ← python-pptx, python-docx, beautifulsoup4
│   └── render_deliverables.py                           ← created by deliverable-renderer
├── state/
│   ├── evidence_ledger.json                             ← from evidence-curator (3-phase)
│   ├── methodology_brief.md                             ← from case-methodology-reader
│   ├── drafts/
│   │   ├── problem.md
│   │   ├── business_theses.json                         ← from business-thesis-generator
│   │   ├── chosen_thesis.md                             ← from thesis-selector
│   │   ├── value.md
│   │   ├── pilot.md
│   │   └── evidence_table.json
│   └── reviews/
│       ├── problem.review.md
│       ├── value.review.md
│       ├── pilot.review.md
│       └── evidence_table.review.md
└── outputs/
    ├── PoV_Review_PerSense.pptx
    └── Evidence_Notes_PerSense.docx
```

## Ground rules (enforced by critical-reviewer)

1. **Evidence > opinion** — every number cites a resolvable EV-ID
2. **Verification chain** — each EV-ID has either an external URL/DOI or `internal_only` flag with a clear internal anchor
3. **Clarity > complexity** — concrete sentences, named segments
4. **AI-assisted ≠ proof** — no fabricated sources
5. **All claims need baseline / number / source**
6. **Thesis fidelity** — drafts read as a JITAI-in-adaptive-DTx PoV, not a generic app

## How to run

From a top-level Claude Code session in this repo, dispatch each agent with the Agent tool. Project subagent names may not auto-register as `subagent_type` values in every harness; if so, use `subagent_type: general-purpose` and pass the agent file path in the prompt with "follow it exactly".

Quick start:
> "Run evidence-curator and case-methodology-reader in parallel."

Then:
> "Run problem-definer."  → "Run value-hypothesis." → "Run pilot-designer." → "Run evidence-table-builder." → "Review all four drafts." → "Render the deliverables."
