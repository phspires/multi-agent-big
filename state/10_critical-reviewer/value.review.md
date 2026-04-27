# Review: value.md (BT-03 PT private oncology white-label)

**Verdict**: PASS
**Reviewed at**: 2026-04-27T00:00:00Z
**Ledger version**: 2026-04-27T15:09:20.338363Z

## Blockers
- (none)

## Non-blocking suggestions
- L13: principal-metric line is dense (two endpoints + AUC replication in one bullet). Consider splitting "delta clínico" and "replicação AUC" into nested bullets for slide readability when the renderer crops to the `(preencher)` box.
- L15/L43: phrase "€200/clínico-ou-hospital/mês" hedges the unit. EV-047 reads "terapeutas/hospitais ≥€200/mês" — pick one unit (preferably per-hospital, since BT-03 is hospital-SaaS) before slide render to avoid buyer confusion.
- L30: "relaxe de 0.06 face a [EV-043]" — relaxation rationale (cohort shift) is sound but light; one extra sentence on what shift specifically (geography? sensor mix? sample-size CI) would harden the claim.
- L47/L82: `Modelo de negócio` €800–1500/mo anchor leans on EV-084 (€500–2K/mo). EV-083 (€15–50K/yr ≈ €1.25–4.2K/mo) could be cited alongside as the white-label B2B ceiling-vs-floor framing.
- Banned-bromide grep: clean.

## Checklist Result

### Framework Compliance
| Check | Result |
|---|---|
| Laser focus (1 segment, 1 buyer, 1 wedge, 1 principal metric) | PASS — BCS 0–24mo, head of senology, monitorização adaptativa entre consultas, PHQ-9/GAD-7 + AUC |
| Personalized to PerSense | PASS — EV-041, EV-043 cited; CUF/Lusíadas/Luz Saúde named |
| No banned bromides | PASS |
| Trojan Horse declared | PASS — Wedge + Expansion explicit (BT-02, BT-01, adjacent oncology cohorts) |
| Buyer empathy with number | PASS — head senology quality report; €60–80K FTE benchmark; €800–1500/mo SaaS |
| Risks have mitigations | PASS — Open Issues 1–5 each have falsifiable check / mitigation |
| End-user pain visible | PASS — "deteção semanas antes da consulta", ≥30% reduction time-to-clinical-contact |
| Open Issues sub-section present | PASS — 5 items |

### Universal Ground Rules
| Check | Result |
|---|---|
| Evidence > opinion (every # has EV-ID) | PASS |
| Verification chain | PASS — internal_only EV-041/042/043 tagged honestly |
| Clarity > complexity | PASS |
| No fabrication | PASS |
| Specificity (segment/context/timeframe) | PASS |
| Problem ≠ Solution | PASS |
| Portuguese where required | PASS — hipótese + métricas in PT |
| Thesis fidelity (JITAI-in-adaptive-DTx) | PASS — mechanism named, DTx endpoints, GDPR DPIA flagged |
| Business-model coherence with chosen_thesis | PASS — `Modelo de negócio` ties PHQ-9/GAD-7 + alert bound to BT-03 SaaS €800–1500/mo |

### value.md per-artifact
| Check | Result |
|---|---|
| Main hypothesis ≤100 chars | PASS (96/100) |
| Main hypothesis in Portuguese | PASS |
| JITAI mechanism named in hypothesis | PASS ("monitorização adaptativa entre consultas") |
| Principal metric baseline cited by EV-ID | PASS — EV-023, EV-031, EV-033, EV-022 (clinical); EV-043 (AUC baseline) |
| Target plausibly achievable in 12 wks (sanity vs Wysa/SilverCloud) | PASS — PHQ-9 -≥3 / GAD-7 -≥2 conservative vs Wysa -30% GAD-7 (EV-031), SilverCloud >80% (EV-033), mHealth SMD -0.49/-0.68 (EV-023) |
| Two support metrics, each with rationale | PASS — Suporte 1 (precision/recall + alert burden); Suporte 2 (LOI WTP) |
| Solution-neutral at metric level | PASS — PHQ-9/GAD-7 + AUC platform-agnostic |
| ≥1 clinical endpoint (PHQ-9/GAD-7 or AUC) | PASS — both |
| ≥1 WTP/unit-economics signal aligned to BT-03 (≥2 LOIs ≥€200/mo) | PASS — EV-047 cited, named hospitals, week-12 deadline, DPIA add-on |
| `Modelo de negócio` line ties principal metric to BT-03 revenue | PASS — clinical delta + alert bound → €800–1500/mo SaaS, ACV €10–18K, 5× FTE benchmark |
| Open Issues / Não Resolvido sub-section | PASS — 5 items (AUC replication, alert bound, LOI conversion, iOS penalty, EMA compliance) |

### EV-ID Resolution
| EV-ID | Cited # | Ledger # | Match |
|---|---|---|---|
| EV-016 | <20% BCS psych | <20% | PASS |
| EV-019 | 30–40% BCS anxiety/dep | 30–40% | PASS |
| EV-022 | g=0.15, 6m | g=0.15 IC 0.05–0.26, 6m | PASS |
| EV-023 | SMD -0.49 dep / -0.68 anx | -0.49 / -0.68, N=19,233 | PASS |
| EV-026 | Limbic 33% NHS | 33% | PASS |
| EV-031 | Wysa -30% GAD-7 | -30% GAD-7 | PASS |
| EV-033 | SilverCloud >80% | >80% | PASS |
| EV-039 | iOS 40–50% sensor coverage | 40–50% | PASS |
| EV-040 | 43% EMA | 43% EMA + 43% JITAI | PASS |
| EV-041 | 34% (99/291) | 34% (99/291) | PASS, internal_only tagged |
| EV-042 | 52.7% screen-fail | 52.7% | PASS, internal_only tagged |
| EV-043 | AUC 0.78, N=126, 2 hosp | AUC 0.78, N=126, 2 hosp | PASS, internal_only tagged + replication open issue |
| EV-047 | ≥2 @ ≥€200/mo | ≥2 @ ≥€200/mo | PASS |
| EV-060 | DiGA €200–600/pat/yr | €200–600/pat/yr | PASS |
| EV-061 | 73M GKV | 73M | PASS |
| EV-062 | €2.3M GDPR | €2.3M | PASS |
| EV-073 | Pharma €20–60K/contract | €20–60K | PASS |
| EV-083 | White-label B2B €15–50K/yr | €15–50K/yr hospital | PASS |
| EV-084 | PerSense €500–2K/mo | €500–2K/mo Phase-2 | PASS |

## Verdict rationale
All required hypothesis attributes (≤100 chars, PT, JITAI mechanism named), both clinical endpoints (PHQ-9/GAD-7 delta + AUC replication), and the BT-03-aligned WTP signal (≥2 LOIs @ ≥€200/mo + DPIA) are present and tied to resolvable EV-IDs. `Modelo de negócio` line correctly chains principal metric → BT-03 SaaS pricing → ACV vs FTE alternative. Open Issues honestly surface the AUC-replication bet, unsigned alert bound, and LOI conversion risk. 12-week clinical targets are conservative vs Wysa (EV-031) and SilverCloud (EV-033) precedents. No blockers; suggestions are slide-render polish only. PASS.
