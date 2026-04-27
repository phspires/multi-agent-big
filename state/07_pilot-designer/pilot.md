# Pilot Sketch (Draft) — BCS JITAI PoV, BT-03 anchor

## Operational hypothesis (one sentence)

Se implementarmos monitorização passiva + EMA breve com alertas clinician-mediated via mindLAMP (Stack A) numa coorte de 30–50 BCS PT 0–24 meses pós-tratamento em senologia privada durante 12 semanas, então (i) replicamos AUC ≥0.72 hold-out na deteção de deterioração entre consultas, (ii) observamos delta clínico PHQ-9 ≥3 / GAD-7 ≥2 e (iii) obtemos ≥2 LOIs hospitalares a ≥€200/mês — falsificando ou validando BT-03.

---

## Slide 2 — campos para preencher

### Pilot Sketch — `(preencher)` (ONE text box)

> **Piloto 12 semanas, mindLAMP Stack A, N=30–50 BCS 0–24 meses pós-tratamento ativo, recrutadas em consulta de senologia privada PT (CUF Oncologia primário; Lusíadas e Luz Saúde paralelos; IPO backup). Onboarding mediado pela equipa de senologia (modelo Limbic, EV-026). EMA PHQ-9/GAD-7 nas semanas 0/4/8/12 + sensing passivo + alertas priorizados ao dashboard de senologia (≤2/clínico/semana). Endpoint principal: delta PHQ-9 ≥3 / GAD-7 ≥2 e replicação AUC ≥0.72 em hold-out PT independente face a EV-043 (AUC 0.78, internal_only). Endpoint comercial: ≥2 LOIs hospitalares a ≥€200/clínico/mês [EV-047]. DPIA GDPR co-assinado com DPO hospitalar [EV-062]. Custo €5–10K externo ao orçamento da instituição-anfitriã [EV-046]; orçamento hospitalar €0 e zero novas contratações.**

### Budget Range — `(preencher)` (ONE text box)

> **€5–10K, externo ao orçamento da instituição-anfitriã (host hospitalar €0, sem novas contratações). Anchor: EV-046 — desenvolvedor 30h €3–6K + infra mindLAMP Hetzner 3m €120 [EV-038] + 10 Fitbits reutilizáveis €2–3K + DPIA/contingência. Comparável: iNNOVSensing custou €120K para output estratégico equivalente [EV-048].**

### Pressupostos — **EXACTLY 3** `(preencher)` strings (slide order = ranked by criticality)

1. **A equipa de senologia de pelo menos um hospital privado PT (CUF / Lusíadas / Luz Saúde) refere ≥50% das BCS elegíveis ao piloto e absorve ≤2 alertas/clínico/semana sem novas contratações nem aumento de orçamento hospitalar.**

2. **A AUC 0.78 da deteção de depressão em BCS [EV-043, internal_only, N=126] replica em hold-out PT independente a ≥0.72, com EMA-compliance ≥50% e mix iOS/Android documentado [EV-039, EV-040].**

3. **Pelo menos 2 unidades de senologia privada PT assinam LOI ou piloto pago a ≥€200/clínico/mês até semana 12 [EV-047], com DPIA GDPR co-assinado pelo DPO hospitalar para neutralizar o risco precedente de €2.3M [EV-062].**

---

## Working detail (Evidence Notes body, NOT slide)

### Cohort, recruitment, setting

- **Segment**: BCS, 0–24 meses pós-tratamento ativo, follow-up senologia/oncologia hospitalar privada PT (alinha com problem.md).
- **N**: 30–50 consentidas (target 40). Triagem 80–100 elegíveis assumindo screen-fail de 52.7% [EV-042, internal_only] e taxa de consentimento alvo ≥50% (lift sobre 34% baseline iNNOVSensing [EV-041, internal_only], suportado pela mediação clínica modelo Limbic [EV-026]).
- **Sites primários**: CUF Oncologia (primário — maior volume senologia privada PT); Lusíadas Saúde (paralelo); Luz Saúde (paralelo).
- **Backup site**: IPO Lisboa / IPO Porto (público) caso 0/3 sites privados confirmem ≥2 LOIs até semana 8 — o modelo de revenue muda mas o sinal clínico mantém-se.
- **Recrutamento**: clinician-mediated em consulta de senologia agendada (não auto-onboarding). Fluxo Limbic-style [EV-026]. Onboarding presencial mediado por enfermeiro de senologia mais consent rate > triagem digital fria.

### Timeline (12 semanas)

| Semana | Atividade | Deliverable |
|---|---|---|
| -2 a 0 | DPIA + contratos + LOI prospects + onboarding equipa senologia | DPIA assinado por ≥1 DPO; mindLAMP Stack A em produção em Hetzner DE (€30–50/mês [EV-038]); 3 sites contactados |
| 1–2 | Recrutamento + onboarding pacientes + baseline PHQ-9/GAD-7 | N=30–50 consentidas; consent rate medido; mix iOS/Android reportado |
| 3–8 | EMA semanal + sensing passivo contínuo + alertas priorizados ao dashboard senologia + intermediate PHQ-9/GAD-7 (semana 4, 8) | Logs de adaptação; alert volume/clínico/semana; engagement weekly active |
| 9–11 | Endpoint PHQ-9/GAD-7 (semana 12) + AUC hold-out + LOI conversion | Delta clínico; AUC out-of-sample; LOIs assinadas |
| 12 | Análise + relatório + entrega de dashboard + 2-3 entrevistas qualitativas com BCS (signal end-user) | Relatório final + 2 LOIs ≥€200/mês ou pivot documentado |

### Success metrics (full)

**Principal** (verbatim de value.md):
- Redução média PHQ-9 ≥3 e GAD-7 ≥2 às 12 semanas; replicação AUC ≥0.72 em hold-out PT independente face a EV-043 (AUC 0.78, internal_only).

**Suporte 1** (clinical detection quality):
- Precisão ≥0.70, recall ≥0.65 contra avaliação clínica (PHQ-9/GAD-7 ≥10 confirmatório).
- Volume de alertas ≤2/clínico/semana — bound contratualizado pré-piloto com a equipa de senologia (resolve open issue 3 de problem.md).

**Suporte 2** (WTP signal — BT-03 demand):
- ≥2 unidades de senologia privada PT assinam LOI ou piloto pago a ≥€200/clínico/mês até semana 12 [EV-047].
- DPIA GDPR co-assinado por ≥1 DPO hospitalar [EV-062].

**Operational secondary** (não na slide, mas medidos):
- Consent rate ≥50% das BCS elegíveis abordadas (lift vs 34% [EV-041]).
- Engagement: ≥60% weekly active across 8+ weeks (anchor: Limbic 33% NHS [EV-026]).
- ≥70% dados esperados em ≥80% participantes [EV-047].
- ≥1 sinal qualitativo end-user (entrevista breve, NPS, ou in-app feedback — principle 6).

### Budget breakdown (anchored to EV-046)

| Categoria | Custo | Notas |
|---|---|---|
| Developer time (30h) | €3–6K | EV-046 |
| mindLAMP Hetzner DE 3m | €120 | EV-038 (€30–50/mês) |
| 10 Fitbits (reutilizáveis) | €2–3K | EV-046 |
| DPIA / consentimento PT | €0–500 | leveraged hospital DPO time, no cash to host |
| Contingência (~20%) | €500–1K | |
| **Total** | **€5–10K** | externo ao orçamento da instituição-anfitriã; **host hospitalar €0**; sem novas contratações |

**Disambiguation (verbatim)**: *"€5–10K externo ao orçamento da instituição-anfitriã (host hospitalar €0, sem novas contratações)."* Compatível com não-negociáveis BIG Impact e methodology brief: o team PoV financia externamente; o hospital não contrata FTE nem desbloqueia capex.

### Top 3 risks + EV-anchored mitigations (principle 5)

| # | Risco | EV-anchor / falsifiable check | Mitigação |
|---|---|---|---|
| 1 | **AUC 0.78 não replica em hold-out PT independente** (modelo treinado N=126, 2 hospitais [EV-043, internal_only]) — colapso parcial da métrica principal. | Falsifiable check intra-piloto: hold-out de ≥30% da coorte mantido fora do treino; AUC reportada à semana 11. SMD agregado mHealth -0.49 / -0.68 [EV-023] e Untire d=0.32 QoL [EV-024] sustentam que o delta PHQ-9/GAD-7 pode existir mesmo se AUC cair. | Reportar AUC + delta clínico em separado — falha parcial (AUC <0.72 mas delta atingido) ainda valida a tese DTx; falha total pivota para BT-04 (consórcio EU). |
| 2 | **Consent rate fica ≤34% e equipa de senologia não absorve carga de alertas >2/clínico/semana** — buyer story colapsa. | EV-anchor: Limbic 33% NHS adoption via referral pathway [EV-026]; Ksana >70% em onboarding hospitalar [EV-034]. Falsifiable check: medir consent na semana 2; renegociar protocolo (EMA mais curta, Fitbit opcional) se <40%. | Bound de 2 alertas/clínico/semana negociado e contratualizado por escrito antes do kickoff — se equipa não assinar, é open issue antes do piloto, não risco oculto. |
| 3 | **0–1 LOIs assinadas até semana 12** — BT-03 falha → pivot para BT-04 ou downgrade para BT-01 Yr3+. | EV-anchor: EV-047 estabelece ≥2 buyers @ €200/mês como threshold de PoV; EV-084 €500–2K/mês é o anchor de pricing realista. Falsifiable check: 3 reuniões executivas (CUF, Lusíadas, Luz) até semana 4; se 0/3 mostram sinal, ativar IPO backup imediatamente. | LOI templates + DPIA pre-cooked para reduzir fricção de assinatura; pricing inicial €200/mês (chão EV-047, não €800–1500 BT-03 target) para maximizar conversão; backup IPO mantém validação clínica mesmo se BT-03 falha. |

### Technology stack — Stack A (mindLAMP) justification

- mindLAMP é Stack A do oss_platform_analysis.html: MVP-grade, Docker Hetzner DE €30–50/mês [EV-038], GDPR-aligned.
- Beiwe-style sensing layer; EMA configurável; alertas para dashboard customizado.
- Não-CE-marked research-mode mas arquitetura de dados MDR Class-IIa-compatible (anchor: EV-057 €300–700K, EV-058 24–36m — declarado para mostrar que o team conhece o pathway sem compromisso de capex).

### Buyer empathy (principle 4) — what the head of senology gets at week 12

- Dashboard quality-report-ready: alertas caught vs missed, time-to-intervention, PHQ-9/GAD-7 trajectory, consent/engagement métricas.
- Custo zero ao orçamento hospitalar; bound de carga clínica documentado.
- Pricing pós-piloto €800–1500/hospital/mês [EV-084] ≈ ACV €10–18K — ~5× mais barato que FTE psico-oncologista €60–80K/ano não-aprovável.

### End-user benefit (principle 6)

Para a sobrevivente: deteção de recaída emocional semanas antes da próxima consulta agendada (3–6m), abrindo janela de intervenção curta e contextual. Operacionalmente: dias até contacto clínico útil reduzem-se vs status quo. Pelo menos 1 sinal qualitativo (entrevista breve / NPS in-app) recolhido na semana 12.

---

## Open Issues / Não Resolvido

1. **Bound de alertas/clínico/semana ainda não assinado pela equipa de senologia** — proposto a 2/semana; sem assinatura por escrito, o pressuposto 1 fica aspiracional. Resolver antes do kickoff (semana -2).
2. **Nenhuma LOI pré-existente de CUF/Lusíadas/Luz Saúde** — pricing €200/mês é threshold mínimo [EV-047]; sem prospect concreto até semana 4, ativar IPO backup. Pressuposto 3 é a aposta comercial central.
3. **Definição operacional de "contacto clínico útil"** — telefone clínico, mensagem segura, ou consulta antecipada? A definir no protocolo na semana -1 (herda de problem.md open issue 4).
4. **iOS sensing penalty** [EV-039] — cobertura de sensores iOS 40–50% vs Android pode enviesar a coorte; mitigação: report estratificado iOS/Android.
5. **EMA compliance baseline 43%** [EV-040] — denominator-risk em precisão/recall; mitigação: report intent-to-treat + respondent-only.
6. **Hold-out design para AUC** — não decidido se random hold-out ou novo hospital (mais defensável mas mais lento). Decidir na semana -1 com biostat advisor.
7. **Backup IPO altera modelo de revenue** (BT-04 consórcio EU vez de BT-03 SaaS) — se ativado, o piloto valida ciência mas não tese comercial; necessário gate explícito na semana 4.

---

## Validation Checklist

- [x] 8–12 semanas (12)
- [x] Cohort 30–50 BCS 0–24m PT senology privada (CUF/Lusíadas/Luz primary; IPO backup)
- [x] Stack A mindLAMP justificado, Hetzner DE [EV-038]
- [x] Budget ≤€10K externo ao host; host €0; no new hires — disambiguation explícita verbatim
- [x] EV-046 anchor para budget; EV-048 comparable
- [x] Métrica principal verbatim de value.md (PHQ-9 ≥3 / GAD-7 ≥2 + AUC ≥0.72)
- [x] Métricas suporte 1 (precisão/recall + ≤2 alerts/clínico/sem) e suporte 2 (≥2 LOIs ≥€200/mês) cobrem demands de BT-03
- [x] Top 3 risks com EV-anchor ou falsifiable check (principle 5)
- [x] EXACTLY 3 Pressupostos strings, ranked by criticality
- [x] Open Issues / Não Resolvido sub-section presente (principle 7)
- [x] Buyer pain referenciado (principle 4) + end-user signal qualitativo (principle 6)
- [x] Internal_only EVs (EV-041/042/043) flagged honestly
