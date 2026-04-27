# Proof of Value Review — PerSense

**Programa**: BIG Impact 2026 — Phase 1 PoV Review
**Equipa / startup**: PerSense (iNNOVSensing)
**Tese de produto**: JITAI-enabled adaptive Digital Therapeutic
**Tese de negócio**: BT-03 — PT private oncology white-label (CUF / Lusíadas / Luz Saúde)
**Data**: 2026-04-29

---

## Slide 1

### Problem Statement *(max. 500 caracteres)*

> Para sobreviventes de cancro da mama (BCS) nos primeiros 24 meses pós-tratamento, em follow-up senologia/oncologia hospitalar (PT), o problema é a recaída emocional entre consultas: 30–40% desenvolvem ansiedade/depressão clínica [EV-019] e <20% recebem apoio formal [EV-016]. Picos fora da consulta ficam invisíveis (medir PHQ-9/GAD-7 e dias até contacto). Status quo falha por triagem episódica → sintomas escalam sem deteção. Pergunta: que sinal passivo as BCS aceitam sem sobrecarregar a equipa?

*(498/500 caracteres. Inclui hipótese causal "triagem episódica → sintomas escalam sem deteção" e pergunta crítica em aberto. Não menciona PerSense, JITAI nem DTx.)*

### Hipótese de valor *(principal)*

> **Monitorização adaptativa entre consultas reduz PHQ-9/GAD-7 em BCS pós-tratamento (semanas 0-12).**

*(96/100 caracteres. Mecanismo JITAI nomeado.)*

### Métricas

- **(principal)** Redução média PHQ-9 ≥3 pontos e GAD-7 ≥2 pontos às 12 semanas em BCS consentidas, com replicação da AUC 0.78 [EV-043, internal_only] na deteção de recaída entre consultas em cohort PT independente.
- **(suporte 1)** Precisão/recall da deteção de deterioração entre consultas: precisão ≥0.70, recall ≥0.65 contra avaliação clínica de referência (PHQ-9/GAD-7 ≥10 confirmatório), com volume de alertas bounded ≤2/clínico/semana.
- **(suporte 2)** ≥2 unidades de senologia privada PT (CUF / Lusíadas / Luz Saúde) assinam LOI ou piloto pago a ≥€200/clínico/mês até semana 12 [EV-047], com DPIA GDPR co-assinado por DPO hospitalar [EV-062].

### Tabela de Evidências

| Aspecto | Número | Fonte | EV-ID |
|---|---|---|---|
| Sobreviventes cancro mama (BCS) — PT e UE | ~36K (PT); ~750K (UE) | Relatório Saúde Mental Digital (GLOBOCAN 2022) | EV-020 |
| BCS com ansiedade/depressão clínica | 30–40% | Relatório Saúde Mental Digital — Epidemiologia | EV-019 |
| BCS que recebem apoio psicológico formal | <20% | Relatório Saúde Mental Digital — Treatment gap | EV-016 |
| mHealth: redução de ansiedade / depressão | SMD -0,68 / -0,49 (139 RCTs, N=19.233) | Meta-análise mHealth, 2025 | EV-023 |
| Reembolso DiGA por paciente/ano (DE, GKV) | €200–600 (cobertura 73M segurados) | BfArM — Modelo DiGA / GKV | EV-060 |

---

## Slide 2

### Pilot Sketch

> **Piloto 12 semanas, mindLAMP Stack A, N=30–50 BCS 0–24 meses pós-tratamento ativo, recrutadas em consulta de senologia privada PT (CUF Oncologia primário; Lusíadas e Luz Saúde paralelos; IPO backup). Onboarding mediado pela equipa de senologia (modelo Limbic, EV-026). EMA PHQ-9/GAD-7 nas semanas 0/4/8/12 + sensing passivo + alertas priorizados ao dashboard de senologia (≤2/clínico/semana). Endpoint principal: delta PHQ-9 ≥3 / GAD-7 ≥2 e replicação AUC ≥0.72 em hold-out PT independente face a EV-043 (AUC 0.78, internal_only). Endpoint comercial: ≥2 LOIs hospitalares a ≥€200/clínico/mês [EV-047]. DPIA GDPR co-assinado com DPO hospitalar [EV-062]. Custo €5–10K externo ao orçamento da instituição-anfitriã [EV-046]; orçamento hospitalar €0 e zero novas contratações.**

### Budget Range

> **€5–10K, externo ao orçamento da instituição-anfitriã (host hospitalar €0, sem novas contratações).**
> Anchor: EV-046 — desenvolvedor 30h €3–6K + infra mindLAMP Hetzner 3m €120 [EV-038] + 10 Fitbits reutilizáveis €2–3K + DPIA/contingência. Comparável: iNNOVSensing custou €120K para output estratégico equivalente [EV-048].

### Pressupostos *(3)*

1. **A equipa de senologia de pelo menos um hospital privado PT (CUF / Lusíadas / Luz Saúde) refere ≥50% das BCS elegíveis ao piloto e absorve ≤2 alertas/clínico/semana sem novas contratações nem aumento de orçamento hospitalar.**

2. **A AUC 0.78 da deteção de depressão em BCS [EV-043, internal_only, N=126] replica em hold-out PT independente a ≥0.72, com EMA-compliance ≥50% e mix iOS/Android documentado [EV-039, EV-040].**

3. **Pelo menos 2 unidades de senologia privada PT assinam LOI ou piloto pago a ≥€200/clínico/mês até semana 12 [EV-047], com DPIA GDPR co-assinado pelo DPO hospitalar para neutralizar o risco precedente de €2.3M [EV-062].**
