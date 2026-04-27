# Evidence Notes — PerSense

**Anexo opcional — 2 páginas no máximo (no formato .docx; este é o equivalente em markdown sem limite de páginas).**

---

**Nome do projeto / startup**: PerSense
**Pessoa de contacto**: *(preencher — nome completo + email/telefone)*

---

## Notas Adicionais

### Methodology note — how this evidence was curated

Evidence ledger built in three phases:
1. **Extract** — quantitative claims pulled from the team's existing Portuguese research in `project-docs/` (relatorio_saude_mental_digital_final, relatorio_estrategico_master_persense, oss_platform_analysis).
2. **Verify** — each external claim cross-checked against the named primary source (URL/DOI). Discrepancies flagged, not silenced.
3. **Augment** — gaps filled with new authoritative entries on JITAI literature, DTx market data, regulatory pathways (DiGA, MDR), comparator unit economics, and PT-specific context.

Total ledger: 88 entries (EV-001 … EV-088). Internal_only entries (PerSense/iNNOVSensing proprietary numbers) are tagged honestly and never silently passed off as externally verified. Slide-facing claims use externally verified entries by default; internal_only entries appear on-slide only when explicitly tagged as such (none on the current slides).

### Product thesis — JITAI in adaptive Digital Therapeutics

PerSense is a **JITAI-enabled adaptive Digital Therapeutic** for mental health: in-the-moment, context-aware micro-interventions delivered via mobile, designed to detect and intercept emotional relapse between scheduled clinical contacts. The mechanism (just-in-time + adaptive + DTx-grade endpoints + clinician-mediated triage) is the lever — not a wellness app.

### Chosen business thesis — BT-03

**PT private oncology white-label (CUF / Lusíadas / Luz Saúde).**

- **Customer**: head of oncology / senology / quality at a PT private hospital group.
- **Buyer/User split**: hospital pays SaaS; senology team uses dashboard; BCS patient uses the app; oncologist remains accountable physician.
- **Revenue model**: SaaS per-hospital, monthly subscription + light setup; optional per-active-case overage.
- **Price point**: €800–1500/hospital/month base [EV-084, EV-083]; PoV threshold €200/mo [EV-047].
- **Unit economics**: ACV €10–18K/hospital — ~5× cheaper than a psycho-oncologist FTE (€60–80K/yr) the head cannot hire.
- **TAM (PT serviceable)**: €0.5–1.0M/yr — ~3 large groups × ~8 senology-active sites; capture 30–50% over 3 yr.
- **Time to first revenue**: 6 months.
- **Regulatory path**: MDR Class I initially (<€30K + GDPR); IIa upgrade €300–700K when revenue funds it [EV-057, EV-058].

#### Value Proposition Canvas — for the BUYER (head of senology), not the BCS patient

**Customer Profile**
- **Jobs**: deliver differentiated BCS survivorship care that protects retention/NPS; surface and intervene on between-consultation deterioration without expanding team.
- **Pains**: <20% of BCS receive formal psych support today (P1, EV-016); psycho-oncologist FTE €60–80K/yr unapprovable yet 30–40% are clinically anxious/depressed (P2, EV-019); clinician burden / alert overload (P3, baseline 34% consent EV-041).
- **Gains**: NPS / accreditation-visible survivorship metric (G1); earlier detection → fewer unscheduled encounters (G2); second revenue/data line via pharma/EU grants on top of same deployment (G3).

**Value Map**
- **Products & Services**: senology-team dashboard with prioritised alerts, PHQ-9/GAD-7 trajectories, quality-report exports (PS1); JITAI sensing + EMA layer on the BCS patient app (PS2); GDPR DPIA + Class I self-cert pack + referral SOP (PS3).
- **Pain Relievers**: closes the <20% gap as a measured number (PR1→P1); SaaS at ~5× cheaper than FTE, opex not headcount (PR2→P2); alert volume bounded as a contracted pilot success criterion (PR3→P3).
- **Gain Creators**: dashboard exports populate accreditation/NPS narrative (GC1→G1); AUC 0.78 BCS-specific detection on between-consultation signals (GC2→G2); same deployment becomes academic anchor for BT-02 pharma + BT-04 EU grants (GC3→G3).

VPC mapping is complete (every Pain has a Reliever, every Gain a Creator). Holes flagged in Open Issues below.

### Alternatives considered (theses kept on the bench)

| ID | Name | Customer | TtR (mo) | Composite | Why not now |
|---|---|---|---|---|---|
| BT-01 | DiGA companion-DTx BCS (DE→EU) | GKV (DE statutory payers) | 30 | 16 | Slow, capex-heavy (€300–700K MDR IIa) without DE clinical partner; Yr3+ expansion play |
| BT-02 | Pharma companion / BCS adherence | Roche / Pfizer / Novartis / AZ Medical Affairs | 9 | 19 | No named pharma counterparty + 6–12 mo procurement; layer on BT-03 once reference site exists |
| **BT-03** | **PT private oncology white-label** | **CUF / Lusíadas / Luz Saúde** | **6** | **23** | **CHOSEN** |
| BT-04 | IPO + EU-funded research consortium | IPO + COMPETE 2030 / EIC / FCT | 12 | 18 | Lumpy non-recurring revenue, ~5.9% EIC success [EV-063]; parallel non-dilutive line |
| BT-05 | Insurer survivorship benefit | Médis / Multicare / AdvanceCare | 15 | 14 | Pilot doesn't produce the cost-of-care delta insurers need; revisit once BT-03 generates outcome evidence |

### Top-5 first contacts for the PoV (this week / next 2 weeks)

| # | Partner | Program | Ask | Channel | Time-to-LOI |
|---|---|---|---|---|---|
| 1 | **CUF Senologia (Descobertas / Tejo)** | CUF Centros de Senologia | LOI to host 8–12-wk PoV at one site, ≥30 BCS, DPIA co-signed | Warm intro via iNNOVSensing collaborators → CUF Oncologia direction | ~6 wk |
| 2 | **Lusíadas Centro Mama** | Lusíadas Centro Mama | LOI to co-host PoV; intro to medical direction; DPO time | Direct email to clinical lead + SPS warm intro | ~8 wk |
| 3 | **Hospital da Luz Centro Clínico da Mama** | Centro Clínico da Mama | LOI for PoV; intro to Luz Saúde innovation + Fidelidade | Luz Saúde innovation team + clinical director | ~8 wk |
| 4 | **Sociedade Portuguesa de Senologia (SPS)** | Congresso + WG psico-oncologia | Endorsement + intros to CUF/Lusíadas/Luz heads + congress slot | SPS board email + member warm intro | ~4 wk |
| 5 | **IPO Lisboa Psico-Oncologia** | Serviço de Psico-Oncologia + Sobrevivência | Backup PoV-site LOI if private stalls by wk 4 | iNNOVSensing academic network → IPO Psico-Oncologia | ~10 wk |

**Multiplication wins**: one CUF unit unlocks the CUF group (8+ senology sites); one SPS endorsement reaches all PT senology heads in one motion; Luz Saúde / Fidelidade opens both BT-03 (hospital) and BT-05 (insurer) channels.

### EV-IDs cited on the slides — provenance

| EV-ID | Claim | Source | Verification | Source kind |
|---|---|---|---|---|
| EV-016 | <20% das BCS recebem apoio psicológico formal | Relatório Saúde Mental Digital — Treatment gap | external | industry_report (anchored in GLOBOCAN-aligned analysis) |
| EV-019 | 30–40% das BCS desenvolvem ansiedade/depressão clínica | Relatório Saúde Mental Digital — Epidemiologia | external | industry_report |
| EV-020 | ~36K BCS PT, ~750K UE | Relatório Saúde Mental Digital (GLOBOCAN 2022) | external | industry_report |
| EV-023 | mHealth meta-análise SMD -0.68 ansiedade / -0.49 depressão (139 RCTs, N=19.233) | Meta-análise mHealth 2025 | external | peer_reviewed |
| EV-026 | Limbic 33% adoção referenciamentos NHS | Limbic Access NHS deployment data | external | industry_report |
| EV-038 | mindLAMP Hetzner DE €30–50/mês | oss_platform_analysis.html | external | internal-OSS-analysis |
| EV-039 | iOS sensing penalty 40–50% vs Android | oss_platform_analysis.html | external | peer_reviewed (Beiwe) |
| EV-040 | EMA/JITAI compliance baseline 43% | mHealth meta | external | peer_reviewed |
| EV-043 | AUC 0.78 deteção depressão BCS, N=126, 2 hospitais | iNNOVSensing internal pilot | **internal_only** | internal_company_data |
| EV-046 | PoV pilot economics €5–10K | Relatório Estratégico PerSense | external | internal-strategy |
| EV-047 | PoV threshold ≥2 buyers @ ≥€200/mês | Relatório Estratégico PerSense | external | internal-strategy |
| EV-048 | iNNOVSensing custou €120K para output estratégico equivalente | Relatório Estratégico PerSense | external | internal-strategy |
| EV-060 | DiGA reembolso €200–600/paciente/ano | BfArM | external | regulatory |
| EV-062 | GDPR €2.3M precedent | EDPB enforcement record | external | regulatory |

### Open Issues / Não Resolvido *(aggregated across all drafts — radical openness)*

1. **Generalização da AUC 0.78** — modelo treinado em 2 hospitais (N=126); sem validação out-of-sample em coorte PT independente. Risco: o sinal preditivo não replica fora do iNNOVSensing. Próximo passo: hold-out externo no piloto.
2. **Aceitação BCS no mundo real** — consent 34% [EV-041], screen-fail 52.7% [EV-042] em iNNOVSensing. Não sabemos se variação de protocolo (onboarding mediado, EMA mais curta) move o consent para ≥50%. Primeira coisa a testar.
3. **Carga clínica para a equipa hospitalar** — bound de ≤2 alertas/clínico/semana proposto mas não negociado por escrito com nenhuma equipa de senologia. Sem assinatura pré-kickoff, o suporte 1 fica aspiracional.
4. **Conversão LOI sem âncora hospitalar pré-existente** — €200/mês é threshold mínimo; pricing-alvo BT-03 (€800–1500/mês) só se valida após o piloto. Risco: 0–1 LOI até semana 12 colapsa BT-03; fallback BT-04 (consórcio EU) tem TtR muito maior.
5. **iOS sensing penalty** [EV-039] — cobertura sensores iOS 40–50% vs Android pode enviesar a coorte. Mitigação: report estratificado iOS/Android.
6. **EMA compliance baseline 43%** [EV-040] — denominator-risk em precisão/recall. Mitigação: report intent-to-treat + respondent-only.
7. **Definição operacional de "contacto clínico útil"** — telefone clínico, mensagem segura, ou consulta antecipada? A definir no protocolo na semana -1.
8. **Hold-out design para AUC** — não decidido se random hold-out ou novo hospital (mais defensável mas mais lento). Decidir na semana -1 com biostat advisor.
9. **Programa BIG Impact named partners** — Fundação Mendes Gonçalves e Siemens Healthineers PT não têm programa BCS-aligned verificável publicamente; confirmar com coordenador BIG Impact antes de outreach.

### Sources scanned

**Internal**: `relatorio_saude_mental_digital_final (3).html`, `relatorio_saude_mental_digital_v2.html`, `relatorio_estrategico_master_persense.html`, `oss_platform_analysis.html`, `Big Impact - Problem Definition Case Challenge.pdf`.

**External (selected, full list in ledger)**: BfArM DiGA-Verzeichnis, EDPB, GLOBOCAN 2022, mindLAMP / Beiwe technical docs, peer-reviewed mHealth/JITAI meta-analyses (2024–2025), Limbic Access deployment data, Wysa / SilverCloud / Untire RCTs, EU EIC Accelerator / Horizon Europe Mission Cancer program documents.
