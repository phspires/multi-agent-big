# Review: pilot.md

**Verdict**: PASS
**Reviewed at**: 2026-04-27T00:00:00Z
**Ledger version**: 2026-04-27T15:09:20.338363Z

## Blockers
- (none)

## Non-blocking suggestions
- pilot.md line 15: "rácios de espera elevados na região Centro, EV-003" — EV-003 is a prevalence statistic (24% Centro, 24,9% Alentejo), not a wait-time figure. Wait times live in EV-013 (Santarém 300 d, Aveiro 254 d, Chaves 240 d). Either rephrase as "prevalência elevada na região Centro (EV-003)" or swap to EV-013 if the intent is wait time. Not a blocker because the claim is directionally correct and the EV-ID exists; it's a precision nit.
- pilot.md line 34: "Redução média GAD-7/PHQ-9 ≥20% wk 8" — wording matches value.md, but consider clarifying "completers" denominator already mentioned in support metric (`≥50% dos completers com Δ ≥4`) is the population for the 20% mean to reduce ambiguity for evaluators.
- pilot.md line 56 budget total €8.500–11.000 slightly exceeds the €5–10K EV-046 anchor at the upper end; the rationale ("acrescida de tempo clínico in-kind") is sound, but explicitly flagging that €3K of clinical time is in-kind would keep cash burn ≤€8K and stay safely within the 2–5-person band.
- pilot.md line 5 hypothesis sentence is very long (~480 chars). Readable, but consider splitting for slide adaptation.

## Checklist Result

| Check | Result |
|---|---|
| Cohort size & segment tied to problem.md (estudantes 18–25, 1.º contacto digital SNS/linha municipal) | PASS |
| Timeline fits 8–12 weeks (10 sem activas + 2 sem setup) | PASS |
| Budget realistic for 2–5-person team (€8.5–11K, in-kind clinical) | PASS |
| Platform anchored to mindLAMP/Stack A with rationale (EV-038 cost, GDPR self-host, EV-040 compliance baseline) | PASS |
| Assumptions specific & falsifiable (named SASUs GAPsi FCUL / SAS Coimbra; carta de compromisso pré-sem –2; baseline mensal de contactos do parceiro) | PASS |
| Risk mitigations for top 3 (recrutamento, capacidade clínica, privacidade) | PASS |
| Primary metric matches value.md (retenção ≥70% @4 sem vs baseline 47% EV-042) | PASS |
| All EV-IDs resolve in ledger | PASS (EV-003 cited adjacent-but-not-exact for wait times — see suggestions) |
| Quantitative claims match ledger numbers | PASS (47% ← 100−52.7 EV-042; 43% EV-040; 34% EV-041; €30–50/mês EV-038; €120K EV-048; €2,3M EV-062; ≥€200/mês EV-047; 60–70% EV-021; iOS 40–50% EV-039) |
| No fabrication / invented sources | PASS |
| Solution-neutral where appropriate (mindLAMP justified as Stack A choice, not as the conclusion) | PASS |
| Specificity of segment, context, timeframe | PASS |
| Risk escalation for ideação activa included | PASS |

## Notes for orchestrator

All ground rules pass; suggestions are stylistic/precision nits and do not block promotion. Recommend forwarding the EV-003 vs EV-013 citation swap to the originating agent as a polish pass before deliverable rendering, but pilot.md is PROMOTION-READY as-is.
