---
description: Print which pipeline artifacts exist, which are stale relative to upstream, and which are missing. Read-only — no agent dispatch.
---

You are reporting the current state of the BIG Impact PoV pipeline. Do not dispatch any agents.

## Procedure

1. Run `git log --oneline -10` to show recent activity.
2. For each expected artifact, check existence and last-modified time:
   - `state/00_template-inspector/template_fields.md`
   - `state/01_evidence-curator/ledger.json`
   - `state/02_case-methodology-reader/methodology_brief.md`
   - `state/03_problem-definer/problem.md`
   - `state/04_business-thesis-generator/business_theses.json`
   - `state/05_thesis-selector/chosen_thesis.md`
   - `state/06_value-hypothesis/value.md`
   - `state/07_pilot-designer/pilot.md`
   - `state/08_evidence-table-builder/evidence_table.json`
   - `state/09_partner-mapper/partner_map.md`
   - `state/09_partner-mapper/discovery_questions.md`
   - `state/10_critical-reviewer/{problem,value,pilot,evidence_table}.review.md`
   - `outputs/PoV_Review_PerSense.pptx`
   - `outputs/Evidence_Notes_PerSense.docx`

3. For each downstream artifact, check if its mtime is **older than any of its inputs**. If so, mark it STALE.

4. Print a single status table:

```
| Step | Artifact | Status | Notes |
|---|---|---|---|
| 0  | template_fields.md  | ✅ FRESH  |  |
| 1a | ledger.json         | ✅ FRESH  |  |
| 1b | methodology_brief   | ✅ FRESH  |  |
| 2  | problem.md          | ⚠️ STALE  | older than template_fields.md  |
| .. | ..                  | ❌ MISSING |  |
```

5. List the **smallest set of agents** that need to re-run to bring everything fresh (deduplicated).

6. Suggest the exact `/run-pipeline N` command to use.

Tools: `Bash` (stat / git log), `Read` only as needed. Do not write files. Do not dispatch agents.
