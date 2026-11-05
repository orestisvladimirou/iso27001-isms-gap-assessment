# 11 — Corrective action, evidence progression and effectiveness

**This is a fully invented follow-up exercise; no actual controls were changed or independently tested.** Hypothetical follow-up date: 18 December 2026.

## Cause, correction and corrective action are different

A **correction** addresses an observed instance (for example, securing an unprotected privileged account). A **corrective action** addresses the underlying process deficiency and should be checked for repeated or similar weaknesses. A credible **effectiveness test** must show that the root cause has been controlled, not simply that a new policy or attendance sheet exists.

The nine CAPAs in `corrective_actions.csv` include root-cause hypotheses, immediate corrections, systemic responses, evidence tests, owners, dates and open status. None is formally closed.

## Two intentionally contrasting follow-up outcomes

| Item | Original condition | New synthetic evidence | Reassessment | Closure status |
| --- | --- | --- | --- | --- |
| F-303 / CAPA-303 | Three of seven privileged humans lacked enforced MFA | P3-E01 models 7/7 covered, no bypass and four hypothetical challenge tests | ISMS-R01 likelihood 4 → 2, impact stays 5; residual **20 → 10 High** | **Open:** independent effectiveness/ongoing monitoring absent; result after original proposed deadline |
| F-308 / CAPA-308 | Only 16/30 staff recorded training attendance | P3-E02 models 30/30 completion of training | Attendance improved but no behavioral/reporting test; ISMS-R09 remains **9 Medium** | **Open:** training effectiveness untested |

An assessor can provisionally revise risk after sufficiently scoped **fictional** preventive-control evidence without claiming a formal audit disposition. The assessment model uses qualitative scores: a reduction is not a statistical probability calculation. Other eight risks are carried forward unchanged.

## Follow-up decision logic

1. Link the original finding to source, risk and treatment, without deleting history.
2. Record the new evidence's date, population and test limitations.
3. Decide whether the evidence supports *likelihood*, *impact* or neither; explain the mechanism.
4. Keep CAPA open until an impartial verifier can demonstrate sustained effectiveness and the competent owner signs closure.
5. Treat management risk acceptance and ISO SoA approval as separate governance steps.

The original risk register and provisional SoA remain unchanged. The latest hypothetical scores are in `risk_follow_up.csv`, with an explicit warning that **one Critical residual risk persists** and no real high/critical acceptance exists.
