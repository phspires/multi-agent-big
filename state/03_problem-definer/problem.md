# Problem Statement (Draft v2 — BCS, moat-aligned)

**Case Challenge Angle**: Acesso sem resolução (channel exists — hospital follow-up — but fails to resolve emotional relapse between visits)

**Segment**: Sobreviventes de cancro da mama (BCS), primeiros 24 meses pós-tratamento ativo, em follow-up de senologia/oncologia hospitalar em Portugal

---

## Segment Choice Rationale (defending against the moat-default rule)

The moat-default rule mandates BCS unless a non-moat segment is strategically superior. **This draft keeps BCS** — the rule applies as written, and the rationale below documents why BCS is also independently the right answer:

1. **Defensibility (PerSense moat).** PerSense holds the only proprietary cohort in this segment in Portugal: N=126 with ML AUC 0.78 for depression detection [EV-043, internal_only], 34% consent and 52.7% screen-fail data from iNNOVSensing [EV-041, EV-042, internal_only]. No competitor entering with university students or a generic anxious-adult segment can replicate this dataset; entering BCS the moat is ours, entering students it is anyone's.
2. **JITAI mechanism fit.** BCS in the first 24 months experience non-stationary, context-dependent affective spikes (medical anniversaries, surveillance-scan anxiety, fatigue waves). This is exactly the pain shape a just-in-time adaptive intervention is built for — context-sensitive, in-the-moment, between scheduled clinical contacts. Generic anxiety in students is more uniform and less differentiated from existing self-guided CBT apps (HelloBetter, SilverCloud, Wysa).
3. **Buyer story.** Hospital senology/oncology services have a named clinical pain (psycho-oncology gap, <20% receive formal support [EV-016]), an identifiable buyer (head of senology/psycho-oncology), a documented unmet treatment gap, and a payer-relevant outcome (depression escalation costs more than its prevention). The buyer for "students with mild anxiety" is more diffuse (university counselling director, no reimbursement pathway).
4. **Comparable funded precedent.** Jasper Health raised $31.8M Series A in oncology survivorship [EV-025]; Untire RCT N=799 shows the category works clinically [EV-024]; oncology = $810M / most-funded segment of European digital health 2024 [EV-050]. Defensible category, not a niche.
5. **Trojan-horse logic.** BCS is a narrow wedge (~36K PT, ~750K EU [EV-020]); the data asset and clinical relationships unlock adjacent oncology cohorts (colorectal survivors, ongoing-treatment patients) and a pharma research-services line [EV-073] without changing the underlying mechanism.

"Easier recruitment" is not invoked here. BCS is harder to recruit (consent 34% vs presumed higher in students) — and that *itself* is a moat: the team already paid the cost.

---

## Slide-facing block (character count: 498/500)

> Para sobreviventes de cancro da mama (BCS) nos primeiros 24 meses pós-tratamento, em follow-up senologia/oncologia hospitalar (PT), o problema é a recaída emocional entre consultas: 30–40% desenvolvem ansiedade/depressão clínica [EV-019] e <20% recebem apoio formal [EV-016]. Picos fora da consulta ficam invisíveis (medir PHQ-9/GAD-7 e dias até contacto). Status quo falha por triagem episódica → sintomas escalam sem deteção. Pergunta: que sinal passivo as BCS aceitam sem sobrecarregar a equipa?

(498 caracteres, dentro do limite de 500. Inclui a hipótese causal "triagem episódica → sintomas escalam sem deteção" e uma pergunta crítica em aberto. Não menciona PerSense, JITAI nem DTx.)

---

## Causal Hypothesis (expanded — working doc only)

**One-line form (embedded in slide):** *triagem episódica → sintomas escalam sem deteção*.

**Expanded:** A monitorização da saúde mental em BCS pós-tratamento depende de consultas presenciais espaçadas (3–6 meses) e de auto-relato no momento da consulta. Os picos de ansiedade/depressão entre consultas — desencadeados por exames de vigilância, dores residuais, fadiga, ou aniversários do diagnóstico — não são capturados pelo follow-up agendado. Como a deteção é episódica e não contextual, sintomas que poderiam ser intercetados precocemente progridem para quadros clínicos significativos antes da próxima consulta. A hipótese mecanística é que **monitorização contínua passiva (sensores, padrões de uso) + EMA breve permite detetar a divergência semanas antes da consulta**, abrindo uma janela de intervenção curta e contextual que o status quo não consegue oferecer. Internamente, a evidência preliminar PerSense (AUC 0.78 para depressão em N=126 [EV-043, internal_only]) sustenta a viabilidade da deteção — mas não substitui validação externa.

---

## Open Critical Question (expanded)

**Pergunta verbatim na slide:** *"que sinal passivo as BCS aceitam sem sobrecarregar a equipa?"*

**Por que esta é a pergunta crítica:** O ponto de falha conhecido não é a deteção (já demonstrada com AUC 0.78 internamente [EV-043, internal_only]) nem a eficácia agregada de JITAIs (g=0.15, sustentado a 6 meses [EV-022]). É a **aceitação simultânea por dois lados**: (i) a paciente — que tem 34% de consentimento histórico [EV-041, internal_only] e 52.7% de screen-fail [EV-042, internal_only], i.e., quase metade desiste mesmo depois de aceitar; e (ii) a equipa hospitalar — que não pode receber alertas que aumentem a carga clínica sem aumentar o orçamento. A pergunta orienta o piloto: testar a combinação mínima de sinais (passivo + EMA leve) que mantenha consent ≥50% e que produza alertas accionáveis a um ritmo que a equipa de senologia consiga absorver sem novos hires.

---

## Evidence References

External (verified in public report sources):
- **EV-016**: <20% das sobreviventes de cancro da mama recebem apoio psicológico formal — `relatorio_saude_mental_digital_final` / GLOBOCAN-aligned. Confidence: high.
- **EV-019**: >36.000 sobreviventes em acompanhamento ativo em PT; 30–40% desenvolvem ansiedade/depressão clínica. Confidence: high.
- **EV-020**: ~750K BCS na UE, ~36K em PT (population sizing). Confidence: high.
- **EV-022**: Meta-análise 2025 JITAIs K=23, N=2563, g=0.15 (IC 95% 0.05–0.26), efeito sustentado 6 meses. Confidence: high.
- **EV-024**: RCT Untire N=799 (Psycho-Oncology 2020), d=0.40 fadiga, d=0.32 QoL — prova que a categoria DTx em oncologia funciona. Confidence: high.
- **EV-025**: Jasper Health $31.8M Series A — comparável de financiamento survivorship. Confidence: high.
- **EV-050**: Oncologia = $810M / segmento mais financiado da saúde digital europeia 2024. Confidence: high.

Internal-only (PerSense proprietary; **flagged honestly — não validados externamente**):
- **EV-041 [internal_only]**: 34% taxa de consentimento (99/291 BCS) no iNNOVSensing.
- **EV-042 [internal_only]**: 52.7% falha de triagem no PerSense/iNNOVSensing.
- **EV-043 [internal_only]**: AUC 0.78 deteção depressão em BCS, N=126, 2 hospitais.

The two EV-IDs cited *inside the 500-char block* are **EV-019** and **EV-016** — both externally verified. Internal-only EVs are surfaced in this working doc and in the buyer/risk narrative but kept off the slide-facing magnitude line per ground rules.

---

## Open Issues / Não Resolvido

1. **Generalização da AUC 0.78** — modelo treinado em 2 hospitais com N=126; sem validação out-of-sample em coorte independente. Risco: o sinal preditivo não replica fora do iNNOVSensing. Próximo passo: piloto PoV deve incluir hold-out externo ou hospital novo.
2. **Aceitação BCS no mundo real (consent 34%, screen-fail 52.7%)** — internamente conhecido, externamente invisível. Não sabemos se variação de protocolo (onboarding hospitalar mediado, redução de wearables, EMA mais curta) move o consent para ≥50%. É a primeira coisa que o piloto tem de testar.
3. **Carga clínica para a equipa hospitalar** — não medida. Quantos alertas/semana a equipa de senologia consegue triar sem perda de qualidade? Sem este número, o buyer story colapsa.
4. **Definição operacional de "contacto útil"** — "dias até contacto" precisa de operacionalização (telefonema clínico vs consulta presencial vs mensagem segura via app). A definir antes do piloto.
5. **EV-019 vs EV-016 sobreposição** — o "30–40% desenvolvem" e o "<20% recebem apoio" combinam-se para uma "treatment gap" implícita; a forma exata da gap (% de mulheres com ansiedade/depressão clínica que NÃO recebem apoio) não é uma estatística citada diretamente, é uma inferência. Surface-level honesto: surfaced here, not silenced.
6. **iOS sensing penalty** — se o piloto usa Beiwe/mindLAMP, a cobertura de sensores em iOS é 40–50% da de Android [EV-039]. Pode enviesar quem entra no piloto. Mitigação: documentar mix iOS/Android nos resultados.

---

## Validation Checklist

- [x] Specific segment named (BCS, 24m pós-tratamento, follow-up senologia/oncologia hospitalar PT)
- [x] Concrete context (entre consultas espaçadas no follow-up hospitalar)
- [x] Observable pain (recaída emocional / picos invisíveis fora da consulta)
- [x] Frequency / magnitude with EV-IDs (30–40% [EV-019], <20% [EV-016])
- [x] Status quo / root cause (triagem episódica)
- [x] Urgency (window do 24m pós-tratamento — clinicamente o pico de risco)
- [x] Causal hypothesis embedded (triagem episódica → sintomas escalam sem deteção)
- [x] Open critical question embedded (sinal passivo aceite sem sobrecarga clínica)
- [x] ≤500 characters (498/500)
- [x] PerSense / JITAI / DTx not named in slide block
- [x] ≥2 EV-IDs cited in slide block (EV-019 + EV-016, both external)
- [x] Internal_only EVs honestly tagged in this working doc
- [x] Segment Choice Rationale present
