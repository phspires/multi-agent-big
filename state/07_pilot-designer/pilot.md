# Pilot Sketch (Draft)

## Pilot Design

**Operational Hypothesis**: If estudantes universitários portugueses (18–25) em primeiro contacto via canal digital SNS / linha municipal forem onboardados num fluxo de check-ins adaptativos (EMA + JITAI) entregue via mindLAMP (Stack A) com triagem ligeira mediada por psicólogo do SASU/serviço de aconselhamento, então a retenção entre 1.º contacto e 2.ª interacção clínica útil às 4 semanas será ≥70% (vs. baseline 47% derivado de EV-042), com compliance EMA ≥45% (EV-040) e redução média GAD-7/PHQ-9 ≥20% à semana 8 (EV-023, EV-031).

**Objectives**:
1. Recrutar coorte de 40 estudantes (18–25) em primeiro contacto digital, configurar mindLAMP self-hosted (Hetzner DE/GDPR), e operar protocolo de check-ins adaptativos durante 10 semanas.
2. Medir a métrica principal de retenção (1.º→2.º contacto útil @4 semanas) e métricas de suporte (compliance EMA, GAD-7/PHQ-9 @baseline e wk 8).
3. Recolher feedback estruturado de 2–3 psicólogos referenciadores sobre a viabilidade do fluxo (≥2 declarariam pagar ≥€200/mês — proxy EV-047).

## Cohort & Recruiting

- **N = 40 participantes** (alvo enrol; mínimo viável N=30 para sinal estatístico em retenção binária com baseline 47%).
- **Source**: Serviços de aconselhamento psicológico universitários (SASU / GAPsi-equivalentes). To confirm: parceria primária com **GAPsi FCUL/IST/FMUL** ou **SAS Universidade de Coimbra** (rácios de espera elevados na região Centro, EV-003); parceria de reserva com linha municipal "Consulta Agora" (EV-018).
- **Inclusion**: 18–25, estudante inscrito, primeiro contacto via formulário digital ou linha telefónica, sintomas ligeiros-moderados (PHQ-9 5–14 / GAD-7 5–14), smartphone Android ou iOS, consentimento informado.
- **Exclusion**: Risco suicidário activo, perturbação grave em tratamento, ideação activa (encaminhamento directo).

## Timeline (10 semanas)

| Sem | Actividade | Entregável |
|-----|-----------|------------|
| –2 a 0 | Setup mindLAMP em Hetzner; CE-internal review; protocolo ético submetido à Comissão de Ética da universidade parceira; scripts de check-in adaptativo (regras, não ML) | Plataforma online, parecer ético, manual do clínico |
| 1–2 | Recrutamento + onboarding (target 40 enrolled); baseline GAD-7/PHQ-9 | N enrolled, baseline data |
| 3–8 | Protocolo activo: 3 EMA/semana + JITAI rule-based; triagem semanal pelo psicólogo referenciador (≤30 min/semana); evento "2.º contacto clínico útil" registado | Logs semanais, retention checkpoint @sem 4 |
| 9–10 | Endpoint GAD-7/PHQ-9 wk 8; entrevistas semi-estruturadas com 8–10 utentes + 2–3 clínicos; análise | Relatório final + métricas |

## Success Criteria

**Primary** (mirrors value.md): Taxa de retenção entre 1.º contacto digital e 2.ª interacção clínica útil às 4 semanas ≥70% (baseline 47% via EV-042).

**Secondary**:
- Compliance EMA/JITAI ≥45% (≥3 respostas/semana por utilizador activo) — EV-040.
- Redução média GAD-7/PHQ-9 ≥20% wk 8; ≥50% dos completers com Δ ≥4 pontos — EV-023, EV-031, EV-036.
- ≥70% dos dados esperados em ≥80% dos participantes (proxy EV-047).
- ≥2 clínicos referenciadores afirmam que pagariam ≥€200/mês pelo dashboard (EV-047).

## Technology Stack

**Platform**: mindLAMP (Stack A — oss_platform_analysis.html). Self-hosted Docker em Hetzner DE (GDPR-compliant), €30–50/mês (EV-038). Configuração: EMA scheduler + adaptive prompts (rule-based, sem ML — ML fica fora do scope MVP), dashboard clínico, exportação CSV.

**Sensing**: Passive engagement logs apenas (app open, response latency); **sem wearables** nesta iteração para baixar fricção de consentimento (lição EV-041: 34% consent iNNOVSensing). iOS background sensing limitado (EV-039) é aceitável dado que sensing passivo não é primário.

**Integration**: Stand-alone — sem integração EHR. Encaminhamentos manuais via psicólogo referenciador.

## Budget Estimate

| Categoria | Custo | Notas |
|-----------|-------|-------|
| Developer / config mindLAMP (~40h) | €4.000–6.000 | Por analogia EV-046 |
| Hosting Hetzner (3 meses) | €120–150 | EV-038 |
| Tempo clínico psicólogos (2 × ~5h/sem × 10 sem @ €30/h) | €3.000 | Acordo com SASU; pode ser in-kind |
| Comissão de ética + materiais consentimento | €0–500 | Geralmente sem custo em universidade pública |
| Incentivos participantes (€10 voucher × 40) | €400 | |
| Contingência (~15%) | €1.000 | |
| **TOTAL** | **€8.500–11.000** | Alinhado com banda EV-046 (€5–10K) acrescida de tempo clínico; ~10× mais barato que iNNOVSensing €120K (EV-048) |

## Constraints

1. **Recrutamento**: Atingir N=40 em 2 semanas via SASU exige protocolo aprovado e fluxo de referenciamento já operacional — risco de atraso ético/administrativo (mitigar: pré-engagement antes da semana –2).
2. **Capacidade clínica**: Psicólogo referenciador precisa de ~5h/semana × 10 sem; só viável se houver compromisso institucional escrito (to confirm: 1 FTE-equivalente partilhado entre 2 psicólogos do SASU).
3. **Privacidade & consentimento**: GDPR + RGPD-saúde + parecer da Comissão de Ética da universidade. Multa precedente €2,3M (EV-062) reforça rigor; auto-hospedagem em Hetzner DE mitiga (EV-038).

## Critical Assumptions (specific & falsifiable)

1. **Referência institucional**: To confirm — pelo menos um SASU (alvo: GAPsi FCUL ou SAS Coimbra) atribui 1 psicólogo coordenador + 1 psicólogo referenciador com ≥5h/sem disponíveis durante 10 semanas. Falsificável por carta de compromisso pré-semana –2.
2. **Volume de fluxo**: O canal digital do parceiro recebe ≥80 primeiros-contactos elegíveis em 2 semanas (necessário para 50% conversion → N=40). Falsificável por dados históricos do parceiro (to confirm: pedir baseline mensal de novos contactos 18–25).
3. **Adesão à plataforma adaptativa mediada**: Coorte mediada por clínico atingirá ≥60% adoption (EV-021 baseline 60–70% para clinician-mediated) — i.e., ≥24/40 instalam mindLAMP e completam ≥1 EMA na semana 1.
4. **Ausência de ML no MVP não compromete o sinal**: Regras determinísticas (frequência, latência, score-based prompts) são suficientes para entregar dose terapêutica equivalente a 43% compliance literatura (EV-040).
5. **GAD-7/PHQ-9 self-report às 8 semanas é mensurável** sem perda >25% (drop-off realista para coorte universitária com incentivo).

## Risk Mitigations

- Coorte de reserva: linha "Consulta Agora" municipal (EV-018) se SASU primário falhar.
- Fallback SMS-only via mindLAMP messaging se adopção da app for <50% na semana 2.
- Pulse semanal de retenção: se @sem 2 retenção projectada <55%, accionar revisão de protocolo (cadência, copy).
- Encaminhamento de risco: protocolo pré-definido para escalonamento clínico se PHQ-9 ≥15 ou ideação positiva.
