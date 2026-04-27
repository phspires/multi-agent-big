# PerSense / BIG Impact PoV — Thinking Framework

This is the **conceptualization lens** every agent in this pipeline must apply. It is not optional. Critical-reviewer enforces it as blockers.

The seven principles below are stated short, then expanded into operational rules.

---

## 1. Simplify. Laser focus.

**No fan-out.** One segment, one buyer, one wedge use case, one principal metric, one pilot site type.

Operational rules:
- If a draft names more than one segment, rewrite for one. The others belong in a "later expansion" line, not the body.
- "And/or" lists in problem.md, value.md, pilot.md are a smell. Pick.
- The deck must be readable in 60 seconds. Anything that doesn't earn its place is cut.

---

## 2. Don't look AI-made. Personalize to PerSense.

**Generic = lazy.** A draft that could be lifted into any other digital-health pitch is failing this rule.

Operational rules:
- Every section must reference at least one **PerSense-specific fact** (internal pilot number, named clinical partner, explicit Stack A platform choice, the 34% consent / AUC 0.78 / 52.7% screen-fail figures, or named Portuguese institutions like GAPsi FCUL, SAS Coimbra, OE Psicólogos, INSA).
- Banned bromides: "leverage", "innovative", "synergistic", "transformative", "ecosystem of solutions", "empower users", "next-generation". If the sentence works after replacing the noun, the sentence is generic — rewrite.
- Numbers > adjectives. "300+ days wait in Santarém [EV-013]" beats "long wait times".

---

## 3. Trojan Horse, not Aloe Vera.

**Don't claim to solve everything.** Pick a narrow wedge that is over-served by your specific mechanism, then declare the expansion path explicitly.

Operational rules (apply to business-thesis-generator and value-hypothesis):
- Each thesis must declare two things: (a) the **wedge** — the one painful, narrow, well-evidenced use case PerSense enters through; (b) the **expansion** — the adjacent revenue lines the wedge unlocks once data/relationships are in place.
- Wedge candidate pattern: "<specific cohort> in <specific friction moment> via <specific channel>" — e.g., "PT university students 18–25 between first digital contact and second clinical contact, via campus counseling units".
- Expansion candidate pattern: "Once we have <data asset / clinical evidence / partner channel>, we unlock <next buyer> at <higher price>" — e.g., "Once we have GAD-7/PHQ-9 endpoint data + 2 university partners, we unlock employer wellness contracts and DiGA dossier feasibility".
- A thesis without a declared expansion path = an aloe vera product. Block.

---

## 4. Sellable. Empathic to the buyer.

**No empty problem-talk.** Every page should be answering: who pays, why they pay now, what specific pain we relieve for *them* (not just the end user).

Operational rules:
- value.md and pilot.md must each reference the **buyer's pain**, not only the end-user's. Examples:
  - University counseling director's pain: waiting list visibility, triage capacity, retention reporting to rectorate.
  - Clinic manager's pain: clinician burnout, dropout, regulatory liability, billable retention.
  - Insurer's pain: cost-of-care for untreated mild-to-moderate cases escalating to severe.
- The buyer pain must connect to a number: how much they lose today, how much they save tomorrow.
- "If we can't articulate why this person writes a cheque on Tuesday, we don't yet have a business" — every draft is sniff-tested with this question.

---

## 5. Risks are solvable — show the evidence.

**The deck is mostly a risk-collapse exercise.** Problem statement is a small share of the work; *de-risking* is the bulk. Make every risk frictionless to dismiss.

Operational rules:
- For each named risk, the draft must show: (a) the evidence that this risk is solvable (EV-ID, prior-art comparator, partner commitment, or completed mitigation step), or (b) the specific cheap test that resolves it within the pilot.
- Pilot.md must list its top 3 risks with a paired mitigation that has either an EV-anchor or a named falsifiable check (e.g., "Risk: GAPsi partnership stalls. Mitigation: signed letter of interest by week –2; backup channel SAS Coimbra has X% historical referral volume per EV-NN").
- If a risk has no mitigation, it's an open issue (see principle 7), not a hidden one.

---

## 6. End-user is the unit of solution.

**A solution that doesn't relieve the end-user's pain is a feature catalogue, not a DTx.** The user-side pain must be visible in problem.md and the user-side benefit must be visible in value.md.

Operational rules:
- problem.md describes the user's experience in concrete terms (the moment of friction, the dropout point), not the system's deficiency in the abstract.
- value.md states what changes for the user, not just what the metric does. Example: "User reaches a useful clinical contact within 14 days instead of 100+" beats "Retention ≥70%".
- Pilot.md includes at least one qualitative end-user signal (interview, NPS, in-app feedback) alongside the quantitative endpoint.

---

## 7. Radically open. No covering up.

**Hidden issues will be found. Stated openly, they become credibility.** Open issues are evidence of rigor, not weakness.

Operational rules:
- Every draft includes an **"Open Issues / Não Resolvido"** sub-section listing what is not yet validated, what assumption could break the thesis, what data is missing.
- Internal_only EV-IDs (PerSense pilot numbers without external validation) are explicitly tagged in the Evidence Notes — never silently passed off as externally verified.
- Discrepancies in the ledger (a number that disagrees with the public source) are surfaced, not silenced.
- The deliverable-renderer adds a final "Open Questions" page in the Evidence Notes summarizing every flagged item across the pipeline.

---

## How this is enforced

- **Every drafting agent** reads this file (`state/thinking_framework.md`) as a non-optional input.
- **Critical-reviewer** runs a Framework Compliance Checklist against every artifact and blocks on any FAIL.
- **Deliverable-renderer** adds an "Open Issues" section seeded from the framework's principle 7.

If a draft passes the BIG Impact rules but fails this framework, the draft is rejected. The framework is the higher bar.
