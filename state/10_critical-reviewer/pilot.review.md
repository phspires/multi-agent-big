# Review: pilot.md (BCS JITAI PoV, BT-03 anchor)

**Verdict**: PASS
**Reviewed at**: 2026-04-27T00:00:00Z
**Ledger version**: 2026-04-27T15:09:20.338363Z

## Blockers
- (none)

## Non-blocking suggestions
- Line 13 (Pilot Sketch box): box is dense — ~900 chars. Renders, but on the slide it will look heavy. Consider trimming inline cites to a footnote-style tail to recover ~80 chars of breathing room. Not a blocker.
- Line 87 risk #3: explicitly mark €200/mo as the *PoV threshold* (not the BT-03 target €800–1500) to pre-empt a reviewer asking "why so cheap vs the thesis price". Implicit but could be one extra clause.
- Line 93 references EV-057/EV-058 (MDR Class IIa) for "team knows the pathway"; not load-bearing for the pilot — could move to Open Issues to declutter the stack-justification block.
- Line 76 supporting-doc prose: "leveraged hospital DPO time" — "leveraged" is a banned bromide per principle 2. Slide-facing copy is clean; flagged as suggestion only. Replace with "uses".

## Checklist Result

### Framework Compliance (thinking_framework.md)
| Check | Result |
|---|---|
| 1. Laser focus (one segment / buyer / wedge / metric) | PASS — BCS 0–24m PT senology privada; one principal metric (PHQ-9/GAD-7 + AUC ≥0.72) |
| 2. Personalized to PerSense (named facts) | PASS — AUC 0.78 N=126 [EV-043], CUF/Lusíadas/Luz, Stack A mindLAMP, 34% iNNOVSensing baseline |
| 3. No banned bromides (slide-facing) | PASS on slide-facing copy. Suggestion: "leveraged" line 76 in supporting doc |
| 4. Trojan Horse declared | PASS — wedge BCS senology privada PT; expansion via BT-02/BT-01 inherited from value.md; risk #3 names BT-04 fallback |
| 5. Buyer empathy (with a number) | PASS — buyer-empathy section lines 95–99: €60–80K FTE non-approvable vs €10–18K ACV |
| 6. Risks have mitigations (top 3, EV-anchor or falsifiable check) | PASS — all 3 risks carry both an EV-anchor AND a falsifiable check (lines 85–87) |
| 7. End-user pain visible (and benefit) | PASS — line 103 names user-side benefit (detection weeks before scheduled visit) + qualitative signal |
| 8. Open Issues sub-section present and substantive | PASS — 7 numbered issues, all material |

### BIG Impact Universal Ground Rules
| Check | Result |
|---|---|
| 1. Evidence > opinion (every quant claim has EV-ID) | PASS |
| 2. Verification chain (EV-IDs resolve in ledger) | PASS — all 16 EV-IDs cited (EV-023, 024, 026, 034, 038, 039, 040, 041, 042, 043, 046, 047, 048, 057, 058, 062) resolve in ledger; numbers match |
| 3. Clarity > complexity | PASS |
| 4. No fabrication | PASS |
| 5. Specificity (named segments, sites, timeframes) | PASS — CUF Oncologia primary, Lusíadas/Luz parallel, IPO backup; 12 weeks; N=30–50 |
| 6. Problem ≠ Solution | PASS |
| 7. Portuguese where required (slide-facing) | PASS — Pilot Sketch, Budget, all three Pressupostos in PT |
| 8. Thesis fidelity (JITAI-in-DTx, not wellness-app) | PASS — EMA + passive sensing + clinician-mediated alerts to senology dashboard; PHQ-9/GAD-7; DPIA GDPR; MDR pathway acknowledged |
| 9. Business-model coherence with chosen_thesis.md | PASS — secondary metric is the BT-03 WTP demand verbatim (≥2 LOIs ≥€200/mo, EV-047); €200 PoV → €800–1500 BT-03 path articulated |

### Per-Artifact (pilot.md)
| Check | Result |
|---|---|
| Cohort size + segment tied to problem.md (BCS 0–24mo PT senology privada) | PASS — lines 33–37 align with problem.md segment definition |
| Timeline 8–12 weeks | PASS — 12 weeks, week-by-week table lines 41–47 |
| **Exactly 3 Pressupostos strings for Slide 2** | PASS — three numbered strings lines 21–25; supporting detail correctly relegated to Evidence Notes body |
| **Budget disambiguation explicit** (host €0; PoV team external €5–10K) | PASS — line 79 verbatim: *"€5–10K externo ao orçamento da instituição-anfitriã (host hospitalar €0, sem novas contratações)"*; reiterated in Pressuposto 1 and Budget box |
| Budget realistic for 2–5 person team (€3K–€10K) | PASS — €5–10K, anchored to EV-046; comparable EV-048 €120K |
| Stack A mindLAMP justified (oss_platform_analysis) | PASS — lines 90–93: Stack A, Hetzner DE €30–50/mo [EV-038], MDR-IIa-compatible architecture |
| Assumptions specific and falsifiable | PASS — named hospitals, ≤2 alerts/clinician/wk bound, AUC ≥0.72, ≥2 LOIs threshold, clinician-mediated onboarding |
| Risk mitigations exist for top 3 constraints | PASS — line 83–87, each row has EV-anchor + falsifiable check + mitigation |
| Primary metric matches value.md principal | PASS — verbatim: "Redução média PHQ-9 ≥3 e GAD-7 ≥2 às 12 semanas; replicação AUC ≥0.72 em hold-out PT independente face a EV-043" |
| Secondary metrics include BT-03 WTP signal (≥2 LOIs ≥€200/mo, EV-047) | PASS — line 59 + Pressuposto 3 + Endpoint comercial in Pilot Sketch box |
| Pilot would materially de-risk BT-03 (not just clinical effect) | PASS — resolves all three open issues from chosen_thesis.md (PR3 alert-bound, PR2 LOI conversion, GC2 AUC replication); risk #3 names BT-04 fallback |
| Internal_only EVs flagged honestly | PASS — EV-041/042/043 tagged `internal_only` consistently |

## Plain-language summary
pilot.md is rigorous and well-anchored. It satisfies the three previously-flagged constraints: the Pressupostos are exactly three slide-sized strings; the budget disambiguation is verbatim ("host €0, PoV team external €5–10K"); the secondary WTP metric matches the BT-03 demand signal verbatim. The 12-week timeline, mindLAMP Stack A justification, top-3-risk table with paired EV-anchors and falsifiable checks, and Open Issues section all clear the framework bar. No blockers. Orchestrator can promote to deliverable-renderer.
