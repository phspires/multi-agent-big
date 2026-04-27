# Value Hypothesis (Draft) — BT-03 PT private oncology white-label

## Slide 1 — campos de preenchimento

### Hipótese de valor (principal) — `(preencher)` ≤100 caracteres

> **Monitorização adaptativa entre consultas reduz PHQ-9/GAD-7 em BCS pós-tratamento (semanas 0-12).**

(96/100 caracteres. Nomeia o mecanismo JITAI — "monitorização adaptativa entre consultas" — e ancora o efeito num endpoint clínico padrão DTx.)

### Métricas — `(preencher)` (lista de 3 linhas: principal + 2 suporte)

- **(principal)** Redução média PHQ-9 ≥3 pontos e GAD-7 ≥2 pontos às 12 semanas em BCS consentidas, com replicação da AUC 0.78 [EV-043, internal_only] na deteção de recaída entre consultas em cohort PT independente.
- **(suporte 1)** Precisão/recall da deteção de deterioração entre consultas: precisão ≥0.70, recall ≥0.65 contra avaliação clínica de referência (PHQ-9/GAD-7 ≥10 confirmatório), com volume de alertas bounded ≤2/clínico/semana.
- **(suporte 2)** ≥2 unidades de senologia privada PT (CUF / Lusíadas / Luz Saúde) assinam LOI ou piloto pago a ≥€200/clínico/mês até semana 12 [EV-047], com DPIA GDPR co-assinado por DPO hospitalar [EV-062].

---

## Detalhe estendido (working doc — não vai para a slide)

### Principal Metric

- **Nome**: Delta clínico PHQ-9/GAD-7 + replicação out-of-sample da AUC de deteção de depressão.
- **Baseline**:
  - Endpoint clínico: SMD agregado mHealth -0.49 depressão / -0.68 ansiedade [EV-023]; comparador adaptativo Wysa -30% GAD-7 [EV-031]; SilverCloud >80% melhoram [EV-033]; JITAI g=0.15 sustentado a 6 meses [EV-022].
  - Deteção: AUC 0.78 PerSense N=126 em 2 hospitais [EV-043, internal_only] — PRECISA replicação externa (open issue do thesis-selector e do problem-definer).
  - Burden de doença: 30–40% das BCS desenvolvem ansiedade/depressão clínica [EV-019]; <20% recebem apoio formal [EV-016].
- **Target (12 semanas)**:
  - PHQ-9 -≥3 pontos, GAD-7 -≥2 pontos (clinicamente meaningful change, alinhado com SMD ≈ -0.5 em [EV-023]).
  - AUC ≥0.72 em hold-out PT independente (relaxe de 0.06 face a [EV-043] para tolerar shift de cohort; 0.72 ainda é aceitável como sinal DTx).
- **Method**: Avaliações PHQ-9/GAD-7 nas semanas 0/4/8/12 via EMA in-app + confirmação clínica. Modelo PerSense corre em background sobre dados passivos + EMA breve; alertas enviados para dashboard de senologia. Ground truth para AUC = PHQ-9/GAD-7 ≥10 nas avaliações agendadas.

### Support Metric 1 (segunda métrica clínica / detection-quality)

- **Nome**: Precisão/recall da deteção de deterioração entre consultas, com bounded clinician burden.
- **Hipótese**: precisão ≥0.70, recall ≥0.65; volume de alertas ≤2/clínico/semana (limite negociado com a equipa de senologia, contratualizado como sucesso/falha do piloto — alinhado com problem.md open issue 3 e thesis demand "clinician burden quantified and bounded").
- **Rationale**: A AUC sozinha não fala ao buyer; precisão/recall + alert rate fala. Liga o endpoint clínico ao buyer's pain (P3 do VPC: alert overload). Sem este número, GC2 do VPC fica aspiracional.

### Support Metric 2 (WTP / unit-economics)

- **Nome**: LOI / piloto pago de unidades de senologia privada PT.
- **Hipótese**: ≥2 unidades senologia (CUF / Lusíadas / Luz Saúde) assinam LOI ou piloto pago a ≥€200/clínico-ou-hospital/mês até semana 12; DPIA GDPR executado e co-assinado por DPO hospitalar em pelo menos 1 sítio.
- **Rationale**: É o demand não-negociável de BT-03 [EV-047] e a única métrica que valida a tese de receita. O âncora €200/mês é o threshold do PoV; o teto BT-03 (€800–1500/hospital/mês) só se justifica depois desta validação. DPIA GDPR signed neutraliza o risco existencial [EV-062 €2.3M precedent].

### Modelo de negócio (linha verbatim para Evidence Notes)

> **Modelo de negócio**: Se o piloto atingir o delta clínico (PHQ-9 -≥3, GAD-7 -≥2) com alertas ≤2/clínico/semana, então BT-03 (SaaS senology white-label PT, CUF/Lusíadas/Luz Saúde) é defensável a €800–1500/hospital/mês [EV-084], com ACV €10–18K/hospital — ~5× mais barato que um FTE psico-oncologista (€60–80K/ano) que o head de senologia não consegue contratar.

### Wedge & Expansion (Trojan Horse — principle 3)

- **Wedge**: BCS PT 0–24 meses pós-tratamento, em follow-up senologia hospitalar privada, via referenciamento clínico-mediado (não auto-onboarding).
- **Expansion**: Com (i) replicação externa da AUC 0.78, (ii) endpoint PHQ-9/GAD-7 limpo, (iii) ≥2 sites ativos, desbloqueia-se: BT-02 contratos pharma research-services €20–60K/contrato [EV-073] no mesmo deployment; BT-01 dossier DiGA reembolso €200–600/paciente/ano [EV-060] em 73M segurados GKV [EV-061] como Yr3+ play; coortes oncológicas adjacentes (colorectal, ongoing-treatment) sobre o mesmo motor JITAI.

### Buyer empathy (principle 4)

A métrica principal traduz-se diretamente em itens do quality report do head de senologia: "alerts caught vs missed", "time-to-intervention", "PHQ-9/GAD-7 trajectory" — números que ele pode pôr no relatório de acreditação. A métrica de WTP é o cheque de Terça-feira: sem 2 LOI a €200/mês até semana 12, a tese SaaS não existe.

### End-user benefit (principle 6)

Para a sobrevivente: deteção de recaída emocional **semanas antes** da próxima consulta agendada (3–6 meses), abrindo janela de intervenção curta e contextual em vez de escalar para crise. Operacionalmente: dias até contacto clínico útil (telefonema, mensagem segura, ou consulta antecipada) reduzem-se em ≥30% face ao status quo de triagem episódica.

---

## Evidence References

**Externos (verificados):**
- **EV-016**: <20% das BCS recebem apoio psicológico formal — magnitude da treatment gap.
- **EV-019**: 30–40% das BCS desenvolvem ansiedade/depressão clínica em PT.
- **EV-022**: Meta-análise JITAI 2025 K=23 N=2563, g=0.15 sustentado a 6m — efeito real mas pequeno; ancora o realismo do target.
- **EV-023**: Meta-análise mHealth 2025 N=19.233, SMD -0.68 ansiedade / -0.49 depressão — ancora o delta PHQ-9/GAD-7 esperado.
- **EV-031**: Wysa -30% GAD-7 — comparador adaptativo escalado.
- **EV-033**: SilverCloud >80% melhoram — comparador white-label hospital.
- **EV-026**: Limbic 33% adoção referenciamentos NHS — ancora o modelo clinician-mediated.
- **EV-039**: iOS sensing penalty 40–50% vs Android — confounder potencial da AUC.
- **EV-040**: EMA/JITAI compliance baseline 43% — denominator-risk para suporte 1.
- **EV-047**: Threshold PoV ≥2 buyers @ ≥€200/mês — o WTP signal.
- **EV-060**: DiGA €200–600/paciente/ano — expansão.
- **EV-061**: GKV 73M segurados — TAM da expansão DiGA.
- **EV-062**: GDPR €2.3M precedent — risco existencial a neutralizar com DPIA.
- **EV-073**: Pharma research-services €20–60K/contrato — expansão BT-02.
- **EV-083**: White-label B2B €15–50K/ano hospital — anchor de pricing.
- **EV-084**: PerSense Phase-2 dashboard €500–2K/mês — anchor primário de pricing.

**Internal-only (PerSense proprietary, marcados honestamente — principle 7):**
- **EV-041 [internal_only]**: 34% consent rate iNNOVSensing (99/291).
- **EV-042 [internal_only]**: 52.7% screen-fail PerSense/iNNOVSensing.
- **EV-043 [internal_only]**: AUC 0.78 deteção depressão BCS, N=126, 2 hospitais — o número que precisa de replicação externa no piloto.

---

## Open Issues / Não Resolvido

1. **Replicação out-of-sample da AUC 0.78 [EV-043, internal_only]** — modelo treinado em 2 hospitais; sem hold-out PT independente. Se não replicar a ≥0.72, a métrica principal colapsa parcialmente (delta PHQ-9/GAD-7 ainda pode existir, mas o "detection moat" cai). Esta é a aposta científica central do piloto.
2. **Bound numérico de "alertas/clínico/semana absorvíveis" não negociado** — o teto de 2/semana é proposto pela tese mas não tem assinatura da equipa de senologia. Sem confirmação por escrito antes do kickoff, o suporte 1 fica indefenido.
3. **Conversão LOI sem âncora hospitalar pré-existente** — não há LOI assinado de CUF/Lusíadas/Luz Saúde. €200/mês é threshold mínimo [EV-047]; o pricing-alvo BT-03 (€800–1500/mês) só se valida após o piloto. Risco: se 0–1 LOI assinado até semana 12, o suporte 2 falha e BT-03 colapsa — fallback é BT-04 (consórcio EU) com tempo de revenue muito maior.
4. **iOS sensing penalty** — cobertura sensores iOS 40–50% vs Android [EV-039] pode enviesar a coorte com replicação AUC. Mitigação: report do mix iOS/Android e estratificação dos resultados.
5. **EMA compliance baseline 43% [EV-040]** — se replicar Beiwe, metade das BCS não responde aos EMA; precisão/recall medidos só sobre os respondentes pode inflacionar artificialmente os números. Mitigação: report explícito de denominator (intent-to-treat vs respondent-only).

---

## Validation Checklist

- [x] Hipótese principal ≤100 caracteres (96/100)
- [x] Mecanismo JITAI explícito ("monitorização adaptativa entre consultas")
- [x] Métrica principal ancorada em endpoint clínico (PHQ-9/GAD-7 + replicação AUC 0.78 baseline EV-043)
- [x] Suporte 1 = segunda métrica clínica/detection-quality (precisão/recall + alert burden)
- [x] Suporte 2 = WTP signal alinhado a BT-03 (≥2 LOI @ ≥€200/mês [EV-047])
- [x] Linha "Modelo de negócio" presente, ligando endpoint clínico à lógica de receita BT-03
- [x] EV-IDs internal_only marcados explicitamente (EV-041, EV-042, EV-043)
- [x] Open Issues / Não Resolvido sub-section presente
- [x] Buyer pain referenciado (head senology quality report; €60–80K FTE não-aprovável)
- [x] End-user benefit referenciado (deteção semanas antes da consulta)
- [x] Wedge + Expansion declarados (Trojan Horse)
