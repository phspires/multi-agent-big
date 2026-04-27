#!/usr/bin/env python3
"""Build state/evidence_ledger.json from curated quantitative claims.

Each claim is a Python dict — ID is auto-assigned (EV-001, ...).
Curation philosophy: prefer the FINAL HTML (relatorio_saude_mental_digital_final (3).html)
when there is overlap with v2; capture distinct claims from the strategic master,
oss platform analysis, and case challenge PDF; mark PDF slide deck as no-data.
"""
import json
from datetime import datetime
from pathlib import Path

ROOT = Path("/Users/pedro/git_repos/big_impact")
OUT = ROOT / "state" / "evidence_ledger.json"

FINAL = "relatorio_saude_mental_digital_final (3).html"
V2 = "relatorio_saude_mental_digital_v2.html"
MASTER = "relatorio_estrategico_master_persense.html"
OSS = "oss_platform_analysis.html"
CASE = "Big Impact - Problem Definition Case Challenge.pdf"
SLIDES = "BIG Impact - Problema, Publico e Evidencia.pdf"
PDFV2 = "relatorio_saude_mental_digital_v2.pdf"

claims = []

def add(**kw):
    kw.setdefault("source_page", None)
    kw.setdefault("notes", "")
    kw.setdefault("is_direct_quote", True)
    claims.append(kw)


# ============================================================
# MARKET SIZE / GROWTH
# ============================================================
add(
    claim_pt="O mercado global de saúde mental digital cresce a 14–19% ao ano (CAGR até 2034).",
    number="14-19%",
    metric="cagr_pct",
    source_file=FINAL,
    source_section="Panorama do Mercado Global de Saúde Mental Digital / Dimensão e trajectória de crescimento",
    topic="cost",
    confidence="high",
    original_context="O mercado global de saúde mental digital cresce a 14–19% ao ano e oncologia é o segmento mais financiado da saúde digital europeia ($810M em 2024).",
    notes="Convergência entre múltiplas firmas de análise; também aparece em v2.",
)
add(
    claim_pt="Oncologia é o segmento mais financiado da saúde digital europeia, com $810M em 2024.",
    number="$810M",
    metric="funding_usd",
    source_file=FINAL,
    source_section="Panorama do Mercado Global de Saúde Mental Digital",
    topic="cost",
    confidence="high",
    original_context="oncologia é o segmento mais financiado da saúde digital europeia ($810M em 2024).",
)
add(
    claim_pt="Mercado global de saúde mental digital situa-se em 27–28 mil milhões de dólares em 2024 e projecta-se em 150–180 mil milhões até 2034.",
    number="27-28B USD (2024); 150-180B USD (2034)",
    metric="market_size_usd",
    source_file=FINAL,
    source_section="Dimensão e trajectória de crescimento",
    topic="cost",
    confidence="high",
    original_context="o consenso situa o mercado em 27–28 mil milhões de dólares em 2024 e projecta 150–180 mil milhões até 2034.",
)
add(
    claim_pt="Mercado dos EUA de saúde mental digital: $7,5B em 2025, com CAGR ~20%.",
    number="$7.5B; 20%",
    metric="market_size_usd; cagr",
    source_file=FINAL,
    source_section="Geografias: dados concretos",
    topic="cost",
    confidence="high",
    original_context="EUA $7,5B 20% (Alta — FDA De Novo, CMS reimbursement desde Jan 2025).",
)
add(
    claim_pt="Mercado alemão de saúde mental digital: ~€1,2B em 2025, CAGR ~15%.",
    number="€1.2B; 15%",
    metric="market_size_eur; cagr",
    source_file=FINAL,
    source_section="Geografias: dados concretos",
    topic="cost",
    confidence="high",
    original_context="Alemanha ~€1,2B 15%",
)
add(
    claim_pt="Mercado UK de saúde mental digital: ~€0,9B em 2025, CAGR ~16%.",
    number="€0.9B; 16%",
    metric="market_size_eur; cagr",
    source_file=FINAL,
    source_section="Geografias: dados concretos",
    topic="cost",
    confidence="high",
    original_context="Reino Unido ~€0,9B 16%",
)
add(
    claim_pt="Mercado francês de saúde mental digital: ~€0,7B em 2025, CAGR ~14%.",
    number="€0.7B; 14%",
    metric="market_size_eur; cagr",
    source_file=FINAL,
    source_section="Geografias: dados concretos",
    topic="cost",
    confidence="high",
    original_context="França ~€0,7B 14%",
)
add(
    claim_pt="Mercado português de saúde mental digital: ~€40–60M em 2025, CAGR 12–15%.",
    number="€40-60M; 12-15%",
    metric="market_size_eur; cagr",
    source_file=FINAL,
    source_section="Geografias: dados concretos",
    topic="cost",
    confidence="medium",
    original_context="Portugal ~€40–60M (est.) 12–15%",
    notes="Estimativa; sem pathway de reembolso digital específico.",
)
add(
    claim_pt="Mercado espanhol de saúde mental digital: ~€200–300M em 2025, CAGR 13%.",
    number="€200-300M; 13%",
    metric="market_size_eur; cagr",
    source_file=FINAL,
    source_section="Geografias: dados concretos",
    topic="cost",
    confidence="medium",
    original_context="Espanha ~€200–300M 13%",
)
add(
    claim_pt="Mercado espanhol de saúde mental digital de aproximadamente €420M em 2024, projectado para €2,7B em 2035 (CAGR ~18,5%).",
    number="€420M (2024); €2.7B (2035); 18.5% CAGR",
    metric="market_size_eur; cagr",
    source_file=FINAL,
    source_section="Espanha — Mercado e Oportunidade",
    topic="cost",
    confidence="medium",
    original_context="A Espanha tem um mercado de saúde mental digital de aproximadamente €420M em 2024, projectado para €2,7B em 2035 (CAGR ~18,5%).",
)

# ============================================================
# PREVALENCE / EPIDEMIOLOGY (PT, EU)
# ============================================================
add(
    claim_pt="Em 2019 Portugal tinha 8.671 casos de perturbação de ansiedade por 100.000 habitantes — a maior prevalência registada globalmente nesse ano.",
    number="8671 / 100,000",
    metric="prevalence_per_100k",
    source_file=FINAL,
    source_section="Prevalência e carga de doença",
    topic="prevalence",
    confidence="high",
    original_context="Segundo a WHO (2019), Portugal tinha 8.671 casos de perturbação de ansiedade por 100.000 habitantes — a maior prevalência registada globalmente nesse ano.",
    notes="Fonte: WHO 2019.",
)
add(
    claim_pt="Ansiedade e depressão afectavam conjuntamente 21% dos utentes dos Centros de Saúde do SNS no início de 2022.",
    number="21%",
    metric="prevalence_pct",
    source_file=FINAL,
    source_section="Prevalência e carga de doença",
    topic="prevalence",
    confidence="high",
    original_context="Ansiedade e depressão afectavam conjuntamente 21% dos utentes dos Centros de Saúde do SNS no início de 2022 (SIM@SNS, dados 2019–2022)",
    notes="Fonte: SIM@SNS (dados 2019–2022).",
)
add(
    claim_pt="Alentejo (24,9%) e Centro (24%) têm as prevalências mais elevadas de ansiedade/depressão; Norte registou maior aumento (+2,6%) no período pandémico.",
    number="24.9% Alentejo; 24% Centro; +2.6% Norte",
    metric="prevalence_pct",
    source_file=FINAL,
    source_section="Prevalência e carga de doença",
    topic="prevalence",
    confidence="high",
    original_context="As regiões do Alentejo (24,9%) e Centro (24%) têm as prevalências mais elevadas; o Norte registou o maior aumento (+2,6%) no período pandémico.",
)
add(
    claim_pt="No SNS, a depressão afecta cerca de 12% e a ansiedade 9% da população de forma isolada.",
    number="12% depressão; 9% ansiedade",
    metric="prevalence_pct",
    source_file=FINAL,
    source_section="Prevalência e carga de doença",
    topic="prevalence",
    confidence="high",
    original_context="A depressão afecta cerca de 12% e a ansiedade 9% da população SNS de forma isolada.",
)
add(
    claim_pt="Em estudo 2024 com 3.399 estudantes universitários portugueses, 75% reportaram sintomas de ansiedade e 61,2% sintomas depressivos (ligeiros a graves).",
    number="75% ansiedade; 61.2% depressão; N=3399",
    metric="prevalence_pct",
    source_file=FINAL,
    source_section="Prevalência e carga de doença",
    topic="prevalence",
    confidence="high",
    original_context="Num estudo de 2024 com 3.399 estudantes universitários portugueses (Amaro et al.), 75% reportaram sintomas de ansiedade ligeiros a graves e 61,2% sintomas depressivos ligeiros a graves.",
    notes="Fonte: Amaro et al. 2024.",
)
add(
    claim_pt="25–30% dos estudantes universitários apresentam ansiedade/depressão.",
    number="25-30%",
    metric="prevalence_pct",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="prevalence",
    confidence="medium",
    original_context="25–30% estudantes universitários com ansiedade/depressão.",
)
add(
    claim_pt="Prevalência anual de depressão em adultos da UE: 7%.",
    number="7%",
    metric="prevalence_pct",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="prevalence",
    confidence="medium",
    original_context="Depressão: 7% adultos EU/ano.",
)
add(
    claim_pt="Prevalência de bipolar 1–3% e esquizofrenia 1% na população EU.",
    number="1-3% bipolar; 1% esquizofrenia",
    metric="prevalence_pct",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="prevalence",
    confidence="medium",
    original_context="Bipolar: 1–3%. Esquizofrenia: 1%.",
)
add(
    claim_pt="Burnout afecta 20–30% dos colaboradores na UE; custo de absentismo >€600B/ano na UE.",
    number="20-30%; >€600B/ano",
    metric="prevalence_pct; cost_eur_year",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="cost",
    confidence="medium",
    original_context="Burnout: 20–30% colaboradores EU. Custo absentismo: >€600B/ano na EU.",
)
add(
    claim_pt="Burden económico de doenças mentais na UE: >€100B/ano.",
    number=">€100B/ano",
    metric="cost_eur_year",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="cost",
    confidence="medium",
    original_context="Burden económico: >€100B/ano na EU.",
)
add(
    claim_pt="Incidência de psicoses na UE: 26.6 por 100.000 por ano.",
    number="26.6/100k/ano",
    metric="incidence_per_100k",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="prevalence",
    confidence="medium",
    original_context="Incidência psicoses: 26.6/100K/ano EU.",
)
add(
    claim_pt="40–50% dos doentes com perturbações mentais graves não têm acesso a cuidados adequados (mercado depressão/bipolar/esquizofrenia).",
    number="40-50%",
    metric="access_gap_pct",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="access",
    confidence="medium",
    original_context="Crítico — 40–50% sem acesso a cuidados adequados.",
)

# ============================================================
# ACCESS GAPS / SNS CAPACITY
# ============================================================
add(
    claim_pt="O SNS conta com aproximadamente 1.100 psicólogos para uma população de 10,3 milhões — muito abaixo do objetivo legal de 1 psicólogo por 5.000 habitantes.",
    number="~1100 psicólogos; ratio ~1:9.400; objetivo 1:5000",
    metric="provider_ratio",
    source_file=FINAL,
    source_section="Serviços de saúde mental: estrutura e défices",
    topic="access",
    confidence="high",
    original_context="O SNS conta com aproximadamente 1.100 psicólogos para uma população de 10,3 milhões — um rácio muito abaixo do objetivo legal de 1 psicólogo por 5.000 habitantes (Resolução da AR n.º 158/2021).",
    notes="Fonte: Resolução AR n.º 158/2021.",
)
add(
    claim_pt="Em 2024 o tempo médio de espera para consulta de psicologia ultrapassava 300 dias em Santarém, 254 em Aveiro e 240 em Chaves.",
    number="300 dias Santarém; 254 Aveiro; 240 Chaves",
    metric="wait_time_days",
    source_file=FINAL,
    source_section="Serviços de saúde mental: estrutura e défices",
    topic="access",
    confidence="high",
    original_context="Em 2024, o tempo médio de espera para consulta de psicologia ultrapassava 300 dias em Santarém, 254 em Aveiro e 240 em Chaves.",
)
add(
    claim_pt="Apenas 317.000 consultas de psicologia foram realizadas no SNS num ano — manifestamente insuficiente.",
    number="317,000 consultas/ano",
    metric="service_volume",
    source_file=FINAL,
    source_section="Serviços de saúde mental: estrutura e défices",
    topic="access",
    confidence="high",
    original_context="Apenas 317.000 consultas de psicologia foram realizadas no SNS num ano — manifestamente insuficiente para a dimensão do problema.",
)
add(
    claim_pt="Ordem dos Psicólogos Portugueses tem 27.000 profissionais inscritos.",
    number="27,000",
    metric="provider_count",
    source_file=FINAL,
    source_section="Serviços de saúde mental: estrutura e défices",
    topic="access",
    confidence="high",
    original_context="OPP (Ordem dos Psicólogos Portugueses): 27.000 profissionais inscritos.",
)

# ============================================================
# ONCOLOGY (BCS) — TARGET POPULATION
# ============================================================
add(
    claim_pt="O cancro da mama é o mais frequente nas mulheres em Portugal: ~7.000 novos casos/ano; colorrectal ~4.500; colo do útero ~900.",
    number="~7000 mama; ~4500 colorrectal; ~900 colo útero",
    metric="incidence_year",
    source_file=FINAL,
    source_section="Epidemiologia",
    topic="prevalence",
    confidence="high",
    original_context="O cancro da mama é o mais frequente nas mulheres (~7.000 novos casos/ano), seguido do colorrectal (~4.500) e do colo do útero (~900).",
    notes="Fonte: GLOBOCAN 2022.",
)
add(
    claim_pt="Sobrevivência a 5 anos para cancro da mama em Portugal ~83%, próximo da média europeia.",
    number="~83%",
    metric="survival_pct",
    source_file=FINAL,
    source_section="Epidemiologia",
    topic="prevalence",
    confidence="high",
    original_context="A sobrevivência a 5 anos para cancro da mama em Portugal (~83%) aproxima-se da média europeia",
)
add(
    claim_pt="Estima-se que existam mais de 36.000 sobreviventes de cancro da mama em acompanhamento activo em Portugal; 30–40% desenvolvem ansiedade ou depressão clinicamente significativas.",
    number=">36,000 sobreviventes; 30-40% prevalência ansiedade/depressão",
    metric="population_size; prevalence_pct",
    source_file=FINAL,
    source_section="Epidemiologia",
    topic="user_segment",
    confidence="high",
    original_context="Estima-se que existam mais de 36.000 sobreviventes de cancro da mama em Portugal em acompanhamento activo, com 30–40% a desenvolver ansiedade ou depressão clinicamente significativas",
)
add(
    claim_pt="Treatment gap em psico-oncologia: <20% dos sobreviventes de cancro da mama recebem apoio psicológico formal.",
    number="<20%",
    metric="access_gap_pct",
    source_file=FINAL,
    source_section="Epidemiologia",
    topic="access",
    confidence="high",
    original_context="O tratamento gap é crítico: menos de 20% recebe apoio psicológico formal, por escassez de psicooncologistas, distância geográfica, e custo.",
)
add(
    claim_pt="População alvo BCS: ~750K sobreviventes na UE, 36K em Portugal.",
    number="~750K UE; 36K PT",
    metric="population_size",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="user_segment",
    confidence="high",
    original_context="~750K BCS EU, 36K PT.",
)

# ============================================================
# CLINICAL EVIDENCE — JITAI / mHealth
# ============================================================
add(
    claim_pt="Meta-análise 2025 (K=23, N=2563) sobre JITAIs: efeito g=0,15 (IC 95% 0,05–0,26), pequeno mas significativo, sustentado até 6 meses.",
    number="g=0.15 (95% CI 0.05-0.26); K=23; N=2563",
    metric="effect_size",
    source_file=FINAL,
    source_section="Evidência clínica: estado da arte em JITAIs",
    topic="digital_health",
    confidence="high",
    original_context="Uma meta-análise de 2025 (K=23 estudos, N=2563 participantes) quantificou pela primeira vez a eficácia agregada das JITAIs: o efeito entre grupos foi pequeno (g=0,15, IC 95% 0,05–0,26) mas estatisticamente significativo, com benefícios que se mantêm até 6 meses",
)
add(
    claim_pt="Meta-análise 2025 (N=19.233, 139 RCTs): mHealth reduz ansiedade (SMD=-0.68) e depressão (SMD=-0.49).",
    number="SMD -0.68 ansiedade; -0.49 depressão; N=19233; 139 RCTs",
    metric="effect_size_smd",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="digital_health",
    confidence="high",
    original_context="Meta-análise 2025 (N=19.233, 139 RCTs): mHealth reduz ansiedade (SMD=-0.68) e depressão (SMD=-0.49).",
)
add(
    claim_pt="CBT em populações de risco psicótico reduz transição para psicose em 43% a 12 meses vs controlo.",
    number="-43%",
    metric="risk_reduction_pct",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado, evidência e posição competitiva",
    topic="digital_health",
    confidence="medium",
    original_context="CBT reduz transição 43% a 12 meses vs controlo. Meta-análise 2021",
)
add(
    claim_pt="RCT Untire (N=799, Psycho-Oncology 2020): redução de fadiga (d=0.40), interferência (d=0.35) e QoL (d=0.32) vs lista de espera.",
    number="d=0.40 fadiga; 0.35 interferência; 0.32 QoL; N=799",
    metric="effect_size_cohen_d",
    source_file=FINAL,
    source_section="Mapa do ecossistema — três categorias de produto",
    topic="digital_health",
    confidence="high",
    original_context="RCT N=799 publicado em Psycho-Oncology (2020): redução significativa de fadiga (d=0.40), interferência (d=0.35) e QoL (d=0.32) vs lista de espera.",
)
add(
    claim_pt="Wysa (parceria MassMutual): 30% redução em GAD-7; integrado no NHS.",
    number="-30% GAD-7",
    metric="symptom_reduction_pct",
    source_file=FINAL,
    source_section="Players Adjacentes Relevantes",
    topic="digital_health",
    confidence="medium",
    original_context="30% redução GAD-7; parceria MassMutual; NHS integrated.",
)
add(
    claim_pt="Wysa: $466M levantados; 10M+ vidas cobertas (Spring Health benchmark).",
    number="$466M; 10M+ vidas",
    metric="funding_usd; lives_covered",
    source_file=FINAL,
    source_section="Players Adjacentes Relevantes",
    topic="cost",
    confidence="high",
    original_context="$466M levantados, 10M+ vidas cobertas. Spring Health (EUA, $466M levantados).",
)
add(
    claim_pt="Zanadio (DiGA obesidade): evidência de 8% de perda de peso média.",
    number="-8%",
    metric="weight_loss_pct",
    source_file=FINAL,
    source_section="Mapa do ecossistema — três categorias de produto",
    topic="digital_health",
    confidence="medium",
    original_context="Zanadio tem DiGA aprovado (obesidade) com evidência de 8% perda de peso média.",
)
add(
    claim_pt="Jasper Health levantou $31.8M (Series A General Catalyst 2022); 12% dos utilizadores em remissão (programa survivorship).",
    number="$31.8M; 12% remissão",
    metric="funding_usd; remission_pct",
    source_file=FINAL,
    source_section="Mapa do ecossistema — três categorias de produto",
    topic="digital_health",
    confidence="high",
    original_context="$31.8M levantados (General Catalyst Series A 2022). 12% dos utilizadores estão em remissão",
)

# ============================================================
# PERSENSE / iNNOVSensing — internal evidence
# ============================================================
add(
    claim_pt="Taxa de consentimento no iNNOVSensing: 34% — das 291 BCS convidadas, apenas 99 consentiram.",
    number="34% (99/291)",
    metric="consent_rate_pct",
    source_file=MASTER,
    source_section="Barreira 1: Taxa de consentimento de 34%",
    topic="pilot_metric",
    confidence="high",
    original_context="Das 291 BCS convidadas para o iNNOVSensing, apenas 99 consentiram (34%).",
)
add(
    claim_pt="Falha de triagem documentada no PerSense/iNNOVSensing: 52,7%.",
    number="52.7%",
    metric="screen_fail_pct",
    source_file=MASTER,
    source_section="Modelos de Desenvolvimento — Inovação e Translação",
    topic="pilot_metric",
    confidence="high",
    original_context="taxa de consentimento de 34%, falha de triagem de 52.7%, e preferência por suporte presencial.",
)
add(
    claim_pt="ML PerSense: AUC 0,78 para depressão em BCS, validado em N=126 pacientes em 2 hospitais.",
    number="AUC 0.78; N=126",
    metric="auc; sample_size",
    source_file=MASTER,
    source_section="Síntese final — o argumento de investimento",
    topic="pilot_metric",
    confidence="high",
    original_context="o único produto europeu de DP adaptativo para saúde mental em BCS, com dados reais de N=126 pacientes e ML validado em dois hospitais (AUC 0.78 depressão).",
)
add(
    claim_pt="Adoption esperada de DP mediada por clínico vs autónoma: 60–70% (cuidado padrão) vs 30–40% (auto-referenciamento).",
    number="60-70% vs 30-40%",
    metric="adoption_pct",
    source_file=MASTER,
    source_section="Modelo clinician-mediated vs autonomous JITAI",
    topic="user_segment",
    confidence="medium",
    original_context="60–70% (contexto de cuidado padrão); 30–40% (auto-referenciamento).",
)
add(
    claim_pt="Limbic AI atinge 33% dos referenciamentos NHS (modelo de integração mediado).",
    number="33%",
    metric="adoption_pct",
    source_file=FINAL,
    source_section="Desafio 1 — Baixas taxas de consentimento",
    topic="digital_health",
    confidence="high",
    original_context="Limbic AI: integração no referral pathway NHS aumentou adoption para 33% de todos os referenciamentos.",
)
add(
    claim_pt="SilverCloud: >80% utilizadores em hospitais parceiros melhoram em ansiedade/depressão.",
    number=">80%",
    metric="improvement_pct",
    source_file=FINAL,
    source_section="Competidores europeus white-label",
    topic="digital_health",
    confidence="medium",
    original_context="80% dos utilizadores reportam melhoria em ansiedade/depressão.",
)
add(
    claim_pt="Ksana Health: onboarding em contexto hospitalar pediátrico atinge consent rate >70%.",
    number=">70%",
    metric="consent_rate_pct",
    source_file=FINAL,
    source_section="Desafio 1 — Baixas taxas de consentimento",
    topic="digital_health",
    confidence="medium",
    original_context="Ksana Health: onboarding em contexto hospitalar pediátrico atinge 70%+ de consent rate.",
)

# ============================================================
# REGULATION / DiGA / CE MARK COSTS
# ============================================================
add(
    claim_pt="Custo total estimado para CE mark MDR Classe IIa: €300.000–€700.000.",
    number="€300K-€700K",
    metric="cost_eur",
    source_file=FINAL,
    source_section="Guia Completo de Certificação MDR + AI Act",
    topic="cost",
    confidence="high",
    original_context="Custo total estimado: €300,000–€700,000 (consultores regulatórios, Notified Body fees, auditorias, geração de evidência clínica, certificação ISO).",
)
add(
    claim_pt="Processo MDR Classe IIa demora 24–36 meses.",
    number="24-36 meses",
    metric="timeline_months",
    source_file=FINAL,
    source_section="Desafio 4 — Custo e tempo de certificação MDR",
    topic="cost",
    confidence="high",
    original_context="O processo MDR Classe IIa custa €300–700K e demora 24–36 meses.",
)
add(
    claim_pt="Custo de submissão DiGA adicional: €20.000–€50.000; prazo de aprovação provisional: 3 meses.",
    number="€20K-€50K; 3 meses",
    metric="cost_eur; timeline_months",
    source_file=FINAL,
    source_section="DiGA — O pathway mais claro na Europa",
    topic="cost",
    confidence="high",
    original_context="Custo de submissão DiGA: €20,000–€50,000 adicionais; prazo: 3 meses para aprovação provisional.",
)
add(
    claim_pt="Reembolso DiGA pago por GKV: €200–600/paciente/ano.",
    number="€200-600/paciente/ano",
    metric="reimbursement_eur_pp_year",
    source_file=FINAL,
    source_section="Modelos de Desenvolvimento: DiGA",
    topic="cost",
    confidence="high",
    original_context="reembolso automático pós-aprovação (€200–600/paciente/ano directo das GKV).",
)
add(
    claim_pt="Sistema GKV alemão cobre 73 milhões de segurados.",
    number="73M",
    metric="population_covered",
    source_file=FINAL,
    source_section="Modelos de Desenvolvimento: DiGA",
    topic="cost",
    confidence="high",
    original_context="Reembolsado pelas GKV (73M segurados).",
)
add(
    claim_pt="42% das DiGA aprovadas são em saúde mental.",
    number="42%",
    metric="share_pct",
    source_file=FINAL,
    source_section="Modelos de Desenvolvimento: DiGA",
    topic="digital_health",
    confidence="medium",
    original_context="42% das DiGA aprovadas são saúde mental.",
)
add(
    claim_pt="GDPR: multa activa de €2,3M aplicada a desenvolvedor de mental health app na Irlanda.",
    number="€2.3M",
    metric="penalty_eur",
    source_file=FINAL,
    source_section="Os quatro pilares regulatórios",
    topic="cost",
    confidence="high",
    original_context="Fines activos (€2,3M a desenvolvedor de mental health app em Irlanda).",
)

# ============================================================
# FUNDING — GRANTS, VC
# ============================================================
add(
    claim_pt="EIC Accelerator: €2,5M grant + €0,5–15M equity por candidatura aprovada (~5,9% taxa de sucesso).",
    number="€2.5M + €0.5-15M; 5.9% sucesso",
    metric="grant_eur; success_rate_pct",
    source_file=FINAL,
    source_section="Programas europeus prioritários",
    topic="cost",
    confidence="high",
    original_context="€2,5M grant + €0,5–15M equity; Muito alta (~5,9% taxa de sucesso).",
)
add(
    claim_pt="EIC Pathfinder: €3–4M por projecto.",
    number="€3-4M",
    metric="grant_eur",
    source_file=FINAL,
    source_section="Programas europeus prioritários",
    topic="cost",
    confidence="high",
    original_context="EIC Pathfinder: €3–4M por projecto.",
)
add(
    claim_pt="EIC Transition: €2,5M (requer ≥€500k investimento privado já levantado).",
    number="€2.5M; req €500k privado",
    metric="grant_eur",
    source_file=FINAL,
    source_section="Programas europeus prioritários",
    topic="cost",
    confidence="high",
    original_context="EIC Transition: €2,5M; Requer ≥€500k investimento privado já levantado.",
)
add(
    claim_pt="PRR / COMPETE 2030 (Portugal): variável até €4M por projecto; €70B comprometidos em tech 2025–27.",
    number="up to €4M; €70B (2025-27)",
    metric="grant_eur",
    source_file=FINAL,
    source_section="Programas europeus prioritários",
    topic="cost",
    confidence="medium",
    original_context="PRR / COMPETE 2030 (Portugal): Variável — até €4M por projecto. €70B comprometidos em tech 2025–27 (inclui saúde).",
)
add(
    claim_pt="COMPETE 2030 tem dotação de €3,9 mil milhões para projectos em áreas incluindo saúde digital.",
    number="€3.9B",
    metric="grant_eur",
    source_file=FINAL,
    source_section="O que Portugal oferece genuinamente",
    topic="cost",
    confidence="high",
    original_context="O COMPETE 2030 tem dotação de €3,9 mil milhões para projectos em áreas incluindo saúde digital.",
)
add(
    claim_pt="PerSense FCT grant: €300K (resultado esperado meados 2026).",
    number="€300K",
    metric="grant_eur",
    source_file=MASTER,
    source_section="Não-dilutivo (grants e contratos) — prioritário",
    topic="pilot_metric",
    confidence="high",
    original_context="€300K. Resultado: meados 2026.",
)
add(
    claim_pt="PRODROMUS: €300K FLAD (psicose).",
    number="€300K",
    metric="grant_eur",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado",
    topic="pilot_metric",
    confidence="high",
    original_context="PRODROMUS em curso (€300K FLAD).",
)
add(
    claim_pt="Em Portugal um estudo de validação que custa €300k no NHS pode ser feito por €80–150k com parceiro universitário adequado.",
    number="€80-150K vs €300K NHS",
    metric="cost_eur",
    source_file=FINAL,
    source_section="O que Portugal oferece genuinamente",
    topic="cost",
    confidence="medium",
    original_context="Um estudo de validação que custa €300k no NHS pode ser possível por €80–150k em Portugal",
)

# ============================================================
# VC RANGES (per stage)
# ============================================================
add(
    claim_pt="Tickets típicos para early-stage health digital na Europa: VC seed €200K–€3M; £500K–£10M (UK); seed PT €0,5–5M; equity EIC até €0,5–15M; pre-seed €100K–€1,5M.",
    number="€200K-€3M; £500K-£10M; €0.5-5M; €0.5-15M; €100K-€1.5M",
    metric="ticket_size_eur",
    source_file=FINAL,
    source_section="VCs europeus activos em digital health / mental health (2024–2025)",
    topic="cost",
    confidence="medium",
    original_context="€200k–€3M; £500k–£10M; €5–30M; €0,5–5M; €0,5–15M equity; €100k–€1,5M",
)
add(
    claim_pt="Limbic AI: $14M Series A (2024), liderada por Khosla Ventures; valuation implícito $50–80M.",
    number="$14M Series A; valuation $50-80M",
    metric="funding_usd; valuation_usd",
    source_file=FINAL,
    source_section="Transacções Comparáveis",
    topic="cost",
    confidence="high",
    original_context="Series A, Mar 2024; $14M (Khosla Ventures); Valuation implícito: $50–80M.",
)
add(
    claim_pt="Mindler+ieso valuation implícito: €100–150M; total levantado €44.1M (Series A €30M).",
    number="€44.1M total; Series A €30M; valuation €100-150M",
    metric="funding_eur; valuation_eur",
    source_file=FINAL,
    source_section="Transacções Comparáveis",
    topic="cost",
    confidence="medium",
    original_context="€44.1M total (Series A €30M); Valuation implícito: €100–150M (estimativa).",
)
add(
    claim_pt="Pear Therapeutics: pico de $1,6B; primeira DTx; falência Abr 2023.",
    number="$1.6B peak",
    metric="valuation_usd",
    source_file=V2,
    source_section="Transacções Comparáveis",
    topic="cost",
    confidence="high",
    original_context="Pear Therapeutics FALÊNCIA ABR 2023. $1,6B no pico.",
)
add(
    claim_pt="Mindstrong: levantou $160M antes de encerrar (escala antes de evidência).",
    number="$160M",
    metric="funding_usd",
    source_file=FINAL,
    source_section="Transacções Comparáveis",
    topic="cost",
    confidence="high",
    original_context="Levantou $160M antes de encerrar. Sequenciação errada destruiu $160M de valor.",
)
add(
    claim_pt="Kintsugi Voice: gastou $16M em 4 anos de processo FDA antes de fechar (Fev 2026).",
    number="$16M; 4 anos",
    metric="cost_usd; timeline_years",
    source_file=FINAL,
    source_section="Razões documentadas de falha neste sector",
    topic="cost",
    confidence="high",
    original_context="A Kintsugi gastou $16M em 4 anos de trabalho FDA antes de fechar.",
)
add(
    claim_pt="Unmind: $26M Set 2025 (B2B employers).",
    number="$26M",
    metric="funding_usd",
    source_file=FINAL,
    source_section="Cinco populações — análise de mercado",
    topic="cost",
    confidence="high",
    original_context="Unmind ($26M Set 2025).",
)
add(
    claim_pt="HelloBetter: 30+ RCTs, DiGA aprovado, expansão França.",
    number="30+ RCTs",
    metric="rct_count",
    source_file=FINAL,
    source_section="Bloco C — Players Adjacentes",
    topic="digital_health",
    confidence="high",
    original_context="HelloBetter (Berlim, 30+ RCTs, DiGA aprovado, expansão França).",
)
add(
    claim_pt="ieso: 145K pacientes NHS, 640K horas de terapia; €31M total levantados.",
    number="145K pacientes; 640K horas; €31M",
    metric="patients_treated; therapy_hours; funding_eur",
    source_file=FINAL,
    source_section="Competidores europeus activos em white-label e-clinic",
    topic="digital_health",
    confidence="high",
    original_context="ieso: 145K pacientes NHS, 640K horas de terapia. €31M total levantados.",
)
add(
    claim_pt="Mindler + ieso: 1,8M sessões terapêuticas realizadas.",
    number="1.8M",
    metric="sessions_count",
    source_file=FINAL,
    source_section="Bloco C",
    topic="digital_health",
    confidence="high",
    original_context="Mindler + ieso (Suécia/UK, adquiriram ieso em Ago 2025, 1,8M sessões terapêuticas)",
)
add(
    claim_pt="Em 2024, 40% dos novos anúncios de parceria de empresas de saúde mental digital envolveram seguradoras ou planos de saúde.",
    number="40%",
    metric="partnership_share_pct",
    source_file=FINAL,
    source_section="Seguradoras — o pagador mais activo",
    topic="cost",
    confidence="high",
    original_context="40% de todos os novos anúncios de parceria para empresas de saúde mental digital envolveram seguradoras ou planos de saúde (dados Galen Growth 2024).",
)
add(
    claim_pt="Swiss Re + Wysa: 30% redução de taxas de depressão reportadas.",
    number="-30%",
    metric="symptom_reduction_pct",
    source_file=FINAL,
    source_section="Seguradoras — o pagador mais activo",
    topic="digital_health",
    confidence="medium",
    original_context="30% redução de taxas de depressão reportadas — KPI relevante para seguradoras",
)

# ============================================================
# PRICING / BUSINESS MODEL
# ============================================================
add(
    claim_pt="Pricing white-label B2B (hospital/clínica): €15–50K/ano por contrato; SaaS terapeuta €100–300/mês ou €20–50K/ano; per-user €5–15/mês.",
    number="€15-50K/ano hospital; €100-300/mês/terapeuta; €5-15/user/mês",
    metric="pricing_eur",
    source_file=FINAL,
    source_section="Modelo de pricing e estrutura contratual",
    topic="cost",
    confidence="medium",
    original_context="€15–30K/ano + €5–10K setup; €100–300/terapeuta/mês ou €20–50K/ano; €5–15/utilizador activo/mês.",
)
add(
    claim_pt="Subscrição hospitalar Dashboard PerSense: €500–2K/mês (Fase 2).",
    number="€500-2K/mês",
    metric="pricing_eur_month",
    source_file=MASTER,
    source_section="Combinação 1 — Recomendada",
    topic="cost",
    confidence="medium",
    original_context="Fase 2 (18–36 meses): Subscrição hospitalar do produto (€500–2K/mês).",
)
add(
    claim_pt="Contratos pharma research services: €20–60K/contrato.",
    number="€20-60K/contrato",
    metric="contract_eur",
    source_file=MASTER,
    source_section="Combinação 1",
    topic="cost",
    confidence="high",
    original_context="Contratos pharma (Roche, Lundbeck) por research services — €20–60K/contrato.",
)
add(
    claim_pt="Custo técnico estimado por fase: Fase 1 €20–40K dev + €300/sem infra; Fase 2 €60–100K/ano (1 dev FT); Fase 3 €150–200K/ano (CTO+dev).",
    number="€20-40K + €300/sem; €60-100K/ano; €150-200K/ano",
    metric="cost_eur",
    source_file=MASTER,
    source_section="Custo técnico estimado por fase",
    topic="cost",
    confidence="medium",
    original_context="€20–40K (dev) + €300 infra/semestre; €60–100K/ano; €150–200K/ano",
)
add(
    claim_pt="Mercado de formação em saúde mental digital — workshops €1.500–5.000/dia institucional; €150–400/participante presencial; consultoria €200–500/h.",
    number="€1.5-5K/dia; €150-400/participante; €200-500/h",
    metric="pricing_eur",
    source_file=FINAL,
    source_section="Mercado de formação em saúde mental digital",
    topic="cost",
    confidence="medium",
    original_context="Workshop institucional (€1.500–5.000/dia por equipa); €150–400 por evento presencial; Consultoria (€200–500/hora).",
)
add(
    claim_pt="Consultoria MDR: €150–400/hora; projecto QMS completo €50–120K; pre-submission NB €2–5K.",
    number="€150-400/h; €50-120K QMS; €2-5K pre-sub",
    metric="cost_eur",
    source_file=FINAL,
    source_section="Bloco D — Formação, Consultoria e Research Services",
    topic="cost",
    confidence="medium",
    original_context="Consultoria MDR: €150–400/hora. Projecto completo QMS: €50–120K. Pre-submission NB meeting: €2–5K.",
)
add(
    claim_pt="McKinsey/BCG: €15.000–30.000/semana; boutiques €5.000–15.000/dia; independentes €200–500/h.",
    number="€15-30K/semana (top); €5-15K/dia (boutique); €200-500/h",
    metric="pricing_eur",
    source_file=FINAL,
    source_section="Bloco D",
    topic="cost",
    confidence="medium",
    original_context="McKinsey/BCG: €15.000–30.000/semana. Boutiques: €5.000–15.000/dia. Independente: €200–500/hora.",
)

# ============================================================
# PILOT / PoV ECONOMICS
# ============================================================
add(
    claim_pt="Custo total do piloto PoV proposto: €5–10K (developer 30h €3–6K + infra mindLAMP €120 + 10 Fitbits €2–3K).",
    number="€5-10K",
    metric="cost_eur",
    source_file=FINAL,
    source_section="Cronograma do piloto PoV",
    topic="pilot_metric",
    confidence="high",
    original_context="Developer time (30h): €3–6K. Infraestrutura (mindLAMP Hetzner 3 meses): €120. Fitbits para sensing (10 unidades, reutilizáveis): €2–3K. Total: €5–10K.",
)
add(
    claim_pt="iNNOVSensing custou €120K para produzir dados equivalentes em valor estratégico ao piloto PoV proposto.",
    number="€120K",
    metric="cost_eur",
    source_file=FINAL,
    source_section="Cronograma do piloto PoV",
    topic="pilot_metric",
    confidence="medium",
    original_context="Por comparação, o iNNOVSensing custou €120K para produzir dados equivalentes em termos de valor estratégico para a startup.",
)
add(
    claim_pt="Métricas de sucesso PoV: ≥2 terapeutas/hospitais pagariam ≥€200/mês; ≥70% dados em ≥80% participantes; ≥50% pacientes elegíveis abordados.",
    number=">=2 buyers @ €200/mês; >=70% data; >=50% approached",
    metric="pilot_thresholds",
    source_file=FINAL,
    source_section="Métricas de sucesso do PoV",
    topic="pilot_metric",
    confidence="high",
    original_context="≥2 terapeutas/hospitais afirmam que pagariam ≥€200/mês pelo produto. ≥70% dados esperados recolhidos em ≥80% dos participantes. ≥50% pacientes elegíveis abordados.",
)

# ============================================================
# OSS PLATFORMS
# ============================================================
add(
    claim_pt="iOS restringe background sensing — cobertura de sensores 40–50% do que Android fornece.",
    number="40-50%",
    metric="sensor_coverage_pct",
    source_file=OSS,
    source_section="As seis plataformas open-source",
    topic="platform",
    confidence="medium",
    original_context="iOS restringe background sensing — cobertura de sensores 40-50% do que Android fornece.",
)
add(
    claim_pt="Beiwe: custo mensal $3.50/participante-mês (estudos grandes), $80/participante-mês (estudos pequenos).",
    number="$3.50-80/participante/mês",
    metric="cost_per_participant_usd",
    source_file=OSS,
    source_section="Papel na arquitectura PerSense",
    topic="platform",
    confidence="high",
    original_context="Custo mensal: $3.50/participante-mês em estudos grandes, $80/participante-mês em estudos pequenos.",
)
add(
    claim_pt="Beiwe: compliance 43% EMA + 43% JITAI reportada na literatura.",
    number="43% EMA; 43% JITAI",
    metric="compliance_pct",
    source_file=OSS,
    source_section="Papel na arquitectura PerSense",
    topic="platform",
    confidence="medium",
    original_context="Compliance de 43% EMA + 43% JITAI reportada.",
)
add(
    claim_pt="mindLAMP deployment: Docker auto-hospedável em Hetzner (DE, GDPR), €30–50/mês.",
    number="€30-50/mês",
    metric="cost_eur_month",
    source_file=FINAL,
    source_section="Análise comparativa das seis plataformas OSS relevantes",
    topic="platform",
    confidence="high",
    original_context="Deployment: Docker, auto-hospedável em Hetzner (DE, GDPR), €30-50/mês.",
)

# ============================================================
# CASE CHALLENGE PDF — Consulta Agora
# ============================================================
add(
    claim_pt="Caso 'Consulta Agora': município com ~150 mil habitantes lançou programa para reduzir barreiras de acesso (teleconsulta + chat triagem, unidades móveis, linha psicossocial).",
    number="~150,000 habitantes",
    metric="population_size",
    source_file=CASE,
    source_section="Contexto",
    source_page=1,
    topic="access",
    confidence="medium",
    original_context="Um município (≈ 150 mil habitantes) lançou o programa 'Consulta Agora' para reduzir barreiras de acesso aos cuidados de saúde primários e à saúde mental",
    notes="Cenário hipotético do case challenge.",
)

# ============================================================
# Notes about other sources
# ============================================================
# Slides PDF: no quantitative claims (process/program structure only)

# ============================================================
# Build output
# ============================================================
def main():
    # assign IDs
    entries = []
    # sort by topic then confidence
    order_topic = ["prevalence", "access", "user_segment", "digital_health",
                   "platform", "pilot_metric", "cost", "other"]
    order_conf = {"high": 0, "medium": 1, "low": 2}
    claims_sorted = sorted(
        claims,
        key=lambda c: (
            order_topic.index(c["topic"]) if c["topic"] in order_topic else 999,
            order_conf.get(c["confidence"], 9),
        ),
    )
    for i, c in enumerate(claims_sorted, 1):
        c2 = {"id": f"EV-{i:03d}"}
        c2.update(c)
        entries.append(c2)

    sources_scanned = sorted({c["source_file"] for c in claims})
    sources_skipped = [
        {
            "file": SLIDES,
            "reason": "Slide deck — only process/program text, no quantitative claims to extract.",
        },
        {
            "file": PDFV2,
            "reason": "Identical content to relatorio_saude_mental_digital_v2.html (also superseded by FINAL); skipped to avoid duplication.",
        },
    ]

    out = {
        "metadata": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "sources_scanned": sources_scanned,
            "sources_skipped": sources_skipped,
            "total_entries": len(entries),
            "schema_version": "1.0",
            "topic_taxonomy": order_topic,
        },
        "entries": entries,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    # quick summary
    from collections import Counter
    by_topic = Counter(e["topic"] for e in entries)
    by_conf = Counter(e["confidence"] for e in entries)
    print(f"Wrote {OUT} with {len(entries)} entries")
    print("By topic:", dict(by_topic))
    print("By confidence:", dict(by_conf))
    print("Sources scanned:", sources_scanned)


if __name__ == "__main__":
    main()
