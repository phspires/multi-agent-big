# Review: problem.md (BCS, moat-aligned, draft v2)

**Verdict**: PASS
**Reviewed at**: 2026-04-27T00:00:00Z
**Ledger version**: 2026-04-27T15:09:20.338363Z

## Blockers

(none)

## Non-blocking suggestions

- L25: the slide block uses an em-dash arrow "→" inside "triagem episódica → sintomas escalam". Renders fine in PPTX but verify the template font supports it; if any doubt, swap to "leva a" to be safe.
- L25: "(medir PHQ-9/GAD-7 e dias até contacto)" reads as a parenthetical aside; consider whether the slide reader will parse it as the consequência mensurável. Not a blocker — methodology shape is preserved.
- L73 (Open Issue 5): the "EV-019 vs EV-016 sobreposição" honesty note is good. Could be tightened; not a blocker.
- L19: "the team already paid the cost" is colloquial. Suggestion only — keep if the voice is intentional.
- Internal_only EVs (EV-041, EV-042, EV-043) are correctly tagged and kept off the slide block. Good discipline.

## Checklist Result

### Framework Compliance
| Check | Result |
|---|---|
| Laser focus (one segment / buyer / wedge / metric) | PASS — BCS, hospital senology buyer, between-consultations wedge, PHQ-9/GAD-7 + days-to-contact |
| Personalized to PerSense | PASS — N=126/AUC 0.78, 34% consent, 52.7% screen-fail, iNNOVSensing, 2 hospitais |
| No banned bromides (slide block) | PASS — no leverage/innovative/synergistic/etc. in the 500-char block |
| Trojan Horse declared | PASS (rationale §5: BCS wedge → adjacent oncology + pharma research-services [EV-073]) |
| Buyer empathy | PASS — head of senology/psico-oncologia named with payer-relevant outcome framing |
| Risks have mitigations / open issues | PASS — Open Issues section enumerates 6 honest items, each with next step or surfacing |
| End-user pain visible | PASS — "recaída emocional entre consultas; picos fora da consulta ficam invisíveis" |
| Open Issues section present | PASS — 6 items, none empty |

### Universal Ground Rules
| Check | Result |
|---|---|
| Evidence > opinion | PASS |
| Verification chain (cited EVs resolve) | PASS — EV-016, EV-019, EV-020, EV-022, EV-024, EV-025, EV-039, EV-041, EV-042, EV-043, EV-050, EV-073 all resolve in ledger; numbers match |
| Internal_only flagged | PASS — EV-041, EV-042, EV-043 explicitly tagged `internal_only`, kept off slide block |
| Clarity > complexity | PASS |
| No fabrication | PASS |
| Specificity (segment/context/timeframe) | PASS — BCS, 24m post-treatment, PT hospital senology follow-up |
| Problem ≠ Solution | PASS — slide block does not name PerSense / JITAI / DTx |
| Portuguese on slide-facing copy | PASS — block is in PT |
| Thesis fidelity (JITAI-in-DTx) | PASS — mechanism (passive sensing + EMA between visits) implied without naming the product |

### Per-Artifact (problem.md)
| Check | Result |
|---|---|
| Case Challenge angle declared (one) | PASS — Acesso sem resolução |
| Specific segment (age band/condition/context) | PASS — BCS, primeiros 24m pós-tratamento, follow-up senologia/oncologia hospitalar PT |
| Segment anchored to PerSense moat (BCS default) | PASS |
| Segment Choice Rationale section present | PASS — 5 substantive defenses (defensibility, JITAI fit, buyer story, funded precedent, trojan-horse), and explicit non-invocation of "easier recruitment" |
| PS structure follows methodology shape ("Para [segmento] em [contexto]…") | PASS — opens with "Para sobreviventes de cancro da mama (BCS) nos primeiros 24 meses pós-tratamento, em follow-up senologia/oncologia hospitalar (PT), o problema é…" and contains "Status quo falha por…" |
| Causal hypothesis embedded in 500-char block | PASS — "triagem episódica → sintomas escalam sem deteção" |
| One open critical question inside block | PASS — "que sinal passivo as BCS aceitam sem sobrecarregar a equipa?" |
| Observable pain (measurable) | PASS — recaída emocional entre consultas; PHQ-9/GAD-7 + dias até contacto named |
| 1–2 magnitude numbers, each with EV-ID resolving | PASS — 30–40% [EV-019] and <20% [EV-016]; both verified external |
| Status quo / root cause | PASS — triagem episódica |
| Urgency hook | PASS — "primeiros 24 meses pós-tratamento" (clinical peak-risk window) |
| Character count ≤500 | PASS — 498/500 (verified) |
| Solution language absent | PASS — no PerSense/JITAI/DTx in slide block |

### EV-ID resolution audit
| EV-ID cited | Resolves in ledger | Number matches |
|---|---|---|
| EV-016 (<20% formal psych support) | YES | YES |
| EV-019 (>36k BCS PT; 30–40% ans/dep) | YES | YES |
| EV-020 (~750K UE; 36K PT) | YES | YES |
| EV-022 (g=0.15 JITAI meta) | YES | YES |
| EV-024 (Untire N=799) | YES | YES |
| EV-025 (Jasper $31.8M) | YES | YES |
| EV-039 (iOS 40–50% sensor coverage) | YES | YES |
| EV-041 (34% consent, 99/291) [internal_only] | YES | YES |
| EV-042 (52.7% screen-fail) [internal_only] | YES | YES |
| EV-043 (AUC 0.78, N=126) [internal_only] | YES | YES |
| EV-050 ($810M onco 2024) | YES | YES |
| EV-073 (€20–60K pharma contracts) | YES | YES |

## Plain-language summary

problem.md passes. BCS-anchored to the PerSense moat with an explicit Segment Choice Rationale that defends the choice on five distinct dimensions and pointedly refuses the "easier recruitment" trap. Slide-facing 500-char block follows the methodology shape, contains the causal hypothesis and the open critical question, cites two externally verified EVs, hits 498/500 chars, and keeps PerSense/JITAI/DTx unnamed. Internal-only EVs are honestly tagged in the working doc and kept off the slide. Open Issues section is honest and surfaces the EV-016/EV-019 gap-arithmetic limitation rather than hiding it. Forward without changes.
