# 02 — Qualitative risk and evidence methodology

## Risk scale

Likelihood and impact each use a **1–5 qualitative scale**. Scores are products for prioritization, not empirical probability estimates.

| Likelihood | Working interpretation | Impact | Working interpretation |
| ---: | --- | ---: | --- |
| 1 | Rare with convincing preventive evidence | 1 | Negligible reversible loss |
| 2 | Unlikely with scoped operating controls | 2 | Minor limited incident |
| 3 | Plausible exposure or mixed assurance | 3 | Moderate local business impact |
| 4 | Likely due to significant gaps/exposure | 4 | Major service or data impact |
| 5 | Near-continuous credible exposure | 5 | Severe disruption or broad compromise |

**Risk score = likelihood × impact.** Bands: Low **1–4**, Medium **5–9**, High **10–16**, Critical **17–25**.

## Inherent and residual

**Inherent risk** models the scenario without crediting existing protective controls. **Residual risk** considers only existing, sufficiently supported controls. Planned treatments do not lower current residual scores. An unsupported assertion does not prove a control is ineffective; it does not justify assurance either.

For this simulated baseline, **ISMS-R07** is the only risk with credited controls: fictional evidence EV-007 models 15/15 in-scope employee laptops with full-disk encryption plus sample checks. Its residual likelihood changes **4 → 2** while impact remains **3**, so score changes **12 High → 6 Medium**. This is a hypothetical teaching judgment, **not real technical verification**. Other nine risk ratings receive no reduction due to inadequate evidence.

## Risk appetite used for the case

- **Critical residual:** default no deployment/expansion of the affected high-risk activity; urgent management escalation and treatment.
- **High residual:** formal owner treatment plan and management review; do not silently accept.
- **Medium residual:** remediation with assigned owner and target; monitor.
- **Low residual:** normal monitoring, still subject to mandatory obligations.

The sample has no authorized high/critical exceptions. The treatment register proposes activities but **does not claim management formally accepted any risk**.

## Evidence confidence

We use **Missing**, **Low**, or **Medium-in-simulation** to separate absent supporting material, mere statements/drafts, and scoped fictional verification. A control may be partially implemented but not independently validated. The assessor must record what was checked, date, exclusions, and how confidence affects a specific threat mechanism.

## Gap status terms

- **Gap:** documented deficiency or required record absent in the synthetic scenario.
- **Partial:** some described practice exists but no convincing evidence of full operation.
- **Not assessed:** no conclusion; do not count as a failed or passed control.

## Limitation

This case is **not a production audit**. ISO/IEC 27001 is a management-system standard; numerical risk treatment alone cannot establish that its operational requirements are met. Refer to [the clause/SoA explanation](03-gaps-and-soa.md).
