# 09 — Mock internal audit and corrective action programme

**Entirely fictional ISMS rehearsal, not an internal audit performed by a real organization.** Exercise date: 8 December 2026 (future scenario date).

## Audit objective, criteria and scope

- Objective: practise evaluating whether the proposed Selene ISMS has documented and operating processes, rather than checking only the presence of draft text.
- Scope: selected Clauses 5.2, 6.1.3, 7.3, 8.1, 9.1 and 9.2 and risk-related Annex A references within the payment platform, staff devices, cloud management, security operations, and governance boundary.
- Criteria: selected ISO/IEC 27001:2022 management-system concepts (summarized, not copied from licensed text) and fictional internal policy expectations.
- Sampling: **nine synthetic desk samples** using v0.1 evidence and v0.2 provisional applicability decisions. Neither a 93-control effectiveness audit nor a statistically representative sample.
- Auditor impartiality: role separation **assumed in the fictional design**, not verified by an actual appointment.

## Results

| Classification | Count | Interpretation |
| --- | ---: | --- |
| Major nonconformity candidate (illustrative) | 5 | ISMS governance, provisional SoA approval, privileged IAM, overdue vulnerabilities, and restoration assurance |
| Minor nonconformity candidate (illustrative) | 3 | Policy approval, monitoring completeness, awareness training |
| Limited positive observation | 1 | Synthetic encryption sample covers 15/15 known laptops, but no conclusion about other devices |
| Unverified necessary Annex A controls | 70 | **Still unverified**, not automatically failed or passed |

The eight proposed findings are documented in `phase3/data/mock_audit_findings.csv`. No actual audit opinion has been issued, and severity is not an automatic criterion from the ISO standard.

## Corrective-action lifecycle

Each mock finding has:
1. A reference to one original risk treatment action rather than a duplicate unconnected risk.
2. An **unconfirmed root-cause hypothesis** (to validate with the real owner in a genuine engagement).
3. A proposed immediate containment or correction.
4. A systemic corrective action addressing recurrence.
5. A specific independent effectiveness test and proposed review date.

The eight corresponding actions are in `phase3/data/corrective_actions.csv`; **all remain OPEN / NOT_APPROVED**. A due date, an owner named in a sample, or a draft procedure never constitutes closure.

## Examples of defensible judgment

**F-304 — Privileged IAM:** Synthetic EV-002 says only four of seven privileged human accounts enforce MFA. Proposed correction is to restrict exposed admin access pending validation. Systemic treatment is approved enrollment and account lifecycle review. Closure needs **7/7 enforced coverage** and independent inspection of exceptions.

**F-307 — Recoverability:** No exercise report was supplied. This means there is no credible evidence of whole-service recovery, **not** necessarily that backups are absent. Rehearse the payment API and database end to end; record actual RTO/RPO results in a future simulated step.

## Technical limits

This project neither claims that all ISO requirements are satisfied nor that a real internal auditor determined nonconformity. A real organization would need actual approval of the scope, qualified/impartial audit sampling, genuine documentary evidence, authority to accept findings, and follow-up proof.
