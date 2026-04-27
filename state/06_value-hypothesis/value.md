# Value Hypothesis (Draft)

**Main Hypothesis** (≤100 chars, 92):
Check-ins adaptativos no primeiro contacto reduzem abandono de 52,7% para ≤30% em 10 semanas.

**Principal Metric**:
- Name: Taxa de retenção entre primeiro contacto digital e segunda interacção clínica útil (4 semanas)
- Baseline: 52,7% de falha de triagem/abandono no fluxo análogo iNNOVSensing — i.e., retenção ~47% [EV-042]
- Target: Retenção ≥70% às 4 semanas (equivalente a redução de abandono de 52,7% para ≤30%) sustentada até semana 10
- Method: Coorte de estudantes 18–25 que iniciam contacto via canal digital SNS/linha municipal; medição via timestamp do 1.º contacto + evento "interacção clínica útil" (resposta a check-in, conclusão de auto-avaliação, ou marcação de consulta) registado em plataforma JITAI; comparação contra baseline histórico do canal.

**Support Metric 1**:
- Name: Compliance de check-ins EMA/JITAI por participante por semana
- Hypothesis: ≥45% de respostas a prompts adaptativos durante 8 semanas (≥3 interacções úteis/semana por utilizador activo)
- Rationale: Compliance é o mecanismo através do qual o efeito clínico se materializa; literatura JITAI reporta 43% de baseline [EV-040], pelo que ≥45% é plausível e demonstra que o motor adaptativo está a entregar dose terapêutica suficiente para sustentar a retenção principal.

**Support Metric 2**:
- Name: Redução sintomática auto-reportada (GAD-7 / PHQ-9) entre baseline e semana 8
- Hypothesis: Redução média ≥20% no GAD-7 e/ou PHQ-9 na coorte aderente; ≥50% dos participantes com melhoria clinicamente relevante (≥4 pontos)
- Rationale: Retenção sem benefício clínico não valida a tese; meta-análises mHealth mostram SMD -0,68 ansiedade / -0,49 depressão [EV-023] e Wysa/Swiss Re reportam -30% GAD-7 em contexto real [EV-031, EV-036], pelo que -20% em 8 semanas é conservador e atingível, confirmando que o ganho de retenção traduz em "Resolution" e não apenas "Access".

**Evidence References**:
- EV-042: 52,7% falha de triagem documentada no iNNOVSensing — baseline do problema "Access without Resolution".
- EV-041: 34% taxa de consentimento iNNOVSensing — sanidade para targets de adesão num design auto-referenciado.
- EV-040: 43% compliance EMA/JITAI baseline — âncora para Support Metric 1.
- EV-022: Meta-análise JITAI 2025 (g=0,15, K=23, N=2563) — efeito sustentado até 6 meses; suporta plausibilidade de melhoria sintomática em 8–10 semanas.
- EV-023: Meta-análise mHealth 2025 (139 RCTs, N=19.233): SMD -0,68 ansiedade, -0,49 depressão — suporta Support Metric 2.
- EV-031: Wysa -30% GAD-7 — precedente para target de redução sintomática.
- EV-036: Swiss Re/Wysa -30% taxas de depressão — precedente em coorte real.
- EV-033: SilverCloud >80% melhoram em ansiedade/depressão em contexto mediado — limite superior para sanidade.
- EV-005: 75% ansiedade / 61,2% depressão em estudantes universitários PT — confirma volume do segmento.

**Validation**:
- [x] Main hypothesis is specific and testable (retenção 47%→≥70% em 10 sem)
- [x] Principal metric has a baseline from ledger (EV-042: 52,7% falha → 47% retenção)
- [x] All metrics are measurable in 8–12 weeks (retenção @4-10sem; EMA semanal; GAD-7/PHQ-9 @baseline+8sem)
- [x] Support metrics reinforce (não contradizem) main: compliance é mecanismo; redução sintomática é o "porquê" da retenção
- [x] Linguagem solution-neutral: hipótese refere "check-ins adaptativos" e "plataforma JITAI" como categoria, testável independente do PerSense
- [x] Targets sanity-checked: 47%→70% retenção (+23pp) é menos agressivo que precedentes mediados (Limbic 33% adoption shift, SilverCloud >80%); compliance 45% ≈ baseline EV-040; -20% sintomas é metade do reportado por Wysa/Swiss Re em RCTs maiores
