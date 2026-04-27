# Problem Statement (Draft)

**Case Challenge Angle**: Access without Resolution

*Justificação do ângulo*: o gap mais saliente e específico para BCS é o de acesso — <20% recebem apoio psicológico formal apesar de 30–40% prevalência clínica de ansiedade/depressão. Não é "duplicação" (não há serviço sobreposto) nem "exclusão invisível" (a doença é visível e seguida); é o intervalo entre a consulta de oncologia e um cuidado de saúde mental que nunca chega a tempo nem em contexto.

**Segment**: Sobreviventes de cancro da mama em Portugal, nos primeiros 24 meses pós-tratamento activo (cirurgia/quimio/radio concluídas), em seguimento em consulta hospitalar de senologia/oncologia (ex.: IPO, hospitais universitários) — fase de sobrevivência precoce, marcada por medo de recorrência e sintomas afectivos sub-clínicos a clínicos entre consultas espaçadas.

**Draft** (character count: 493/500):

Sobreviventes de cancro da mama nos primeiros 24 meses pós-tratamento activo, seguidas em consulta hospitalar de senologia em PT, sofrem ansiedade/depressão clínicas em 30–40% [EV-019] mas <20% recebem apoio psicológico formal, por escassez de psico-oncologistas, distância e custo [EV-016]. Em 36K BCS PT (~750K UE) [EV-020], dados internos mostram 52,7% de falha de triagem e 34% de consentimento [EV-042, internal_only]: o sofrimento entre consultas fica sem resposta atempada e contextual.

**Evidence References**:
- EV-019 (externally verified): "Mais de 36.000 sobreviventes de cancro da mama em PT em acompanhamento activo; 30–40% desenvolvem ansiedade/depressão clinicamente significativas."
- EV-016 (externally verified): "<20% dos sobreviventes de cancro da mama recebem apoio psicológico formal; escassez de psico-oncologistas, distância e custo."
- EV-020 (externally verified): "~750K BCS UE, 36K PT."
- EV-042 (**internal_only** — coorte iNNOVSensing): "Falha de triagem 52,7%."
- EV-041 (**internal_only**): "34% taxa de consentimento (99/291 BCS)."
- EV-043 (**internal_only**): "ML AUC 0,78 para depressão em BCS, validado em N=126 em 2 hospitais." [contexto de moat para secções subsequentes; não citado in-line por limite de caracteres]

**Validation**:
- [x] Specific segment named (BCS, primeiros 24 meses pós-tratamento, consulta hospitalar de senologia PT)
- [x] Observable pain point described (sofrimento entre consultas; falha de triagem; baixo consentimento)
- [x] 1-2 numbers cited with EV-IDs (30–40% [EV-019]; <20% [EV-016]; 36K/750K [EV-020]; 52,7% [EV-042])
- [x] Status quo / root cause explained (escassez de psico-oncologistas, distância, custo; consultas espaçadas)
- [x] Urgency mentioned (janela de sobrevivência precoce; sofrimento sem resposta atempada)
- [x] Character count ≤500 (493)
- [x] PerSense / JITAI / DTx **não** mencionados no statement
- [x] EV-042 marcado honestamente como internal_only

**Buyer-side echo (para coerência com value.md)**: o director de psico-oncologia hospitalar não tem capacidade clínica para cobrir a coorte de sobrevivência; o chefe da consulta de senologia não tem visibilidade sobre o estado afectivo das suas pacientes entre visitas. Ambos são compradores plausíveis para uma camada de cuidado adaptativo entre consultas.

## Open Issues / Não Resolvido

- **EV-016 e EV-019 derivam do mesmo relatório interno do projecto** (relatorio_saude_mental_digital_final). A fonte primária externa (e.g., revisão sistemática psico-oncologia, dados RON/IPO Portugal) precisa de ser confirmada por evidence-curator antes da entrega final — risco de citação circular.
- **Definição operacional de "primeiros 24 meses"**: convenção clínica razoável (período de maior risco de FCR — fear of cancer recurrence) mas **não** ancorada num EV-ID. Precisa de citação ou justificação clínica adicional.
- **52,7% de falha de triagem [EV-042]**: numerador/denominador exacto e critério de triagem do iNNOVSensing não documentados no ledger. Defensável internamente, frágil sob escrutínio externo.
- **34% de consentimento [EV-041]**: ambíguo se é "barreira do utente" ou "fricção do desenho de estudo". A interpretação muda a moldura do problema — se for desenho, é menos generalizável.
- **Fear of recurrence (FCR)** clinicamente reconhecido como sintoma mais distintivo da fase de sobrevivência precoce, mas **não** consta do ledger como EV. Adicioná-lo reforçaria a especificidade do segmento e o "porquê agora".
- **Heterogeneidade do segmento**: BCS em terapia hormonal adjuvante prolongada (tamoxifeno/AI) vs. BCS em vigilância pura têm perfis de risco distintos. O statement agrupa-os; pode precisar de afunilamento.
- **Disponibilidade de smartphone/literacia digital** no perfil etário típico (mediana ~55–65 anos) não está quantificada — risco para qualquer intervenção mediada por mobile.
- **Preferência por suporte presencial** referida em EV-042 mas não isolada como número independente — pode tensionar a aceitação de uma intervenção digital.
