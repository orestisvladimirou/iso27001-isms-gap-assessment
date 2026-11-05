# 09 — Desk-based simulated ISMS internal audit

**FICTIONAL AUDIT REHEARSAL, not an actual ISO/IEC 27001 internal audit or certification assessment.** Modeled sampling date: **19 November 2026**. This date describes a constructed scenario, not work completed for a real organization.

## Scope and auditor independence

The audit programme models the draft Selene Payments Ltd ISMS boundary: payment API, cloud identity, employee endpoints, monitoring and recovery, internal governance and staff awareness. It uses selected ISO/IEC 27001:2022 Clauses 4–10 and relevant Annex A control themes as a **learning reference**. A real audit requires authorized criteria, trained independent auditors, complete records and impartiality; no actual organizational auditor or manager signed this exercise.

The hypothetical audit role is different from the hypothetical owners of sampled services. **That role separation exists only on paper and does not establish actual auditor independence.**

## Sampling design and limits

The audit uses **ten deliberately nonrandom samples**, chosen because baseline material already identified important weaknesses. Nine samples yield **indicative findings**, and the tenth is a narrowly scoped positive observation on employee-device encryption. Sampling is not statistically representative, so these results cannot prove performance of all 93 Annex A controls or full clause conformity.

| Sample | Topic | Existing basis | Model observation |
| --- | --- | --- | --- |
| S-301 | Policy approval / controlled information | EV-001 | Draft is unapproved |
| S-302 | Internal audit process | EV-012 | Audit programme missing |
| S-303 | Privileged access | EV-002 | Three of seven human admins lack enforced MFA |
| S-304 | Vulnerability management | EV-004 | Six overdue critical findings |
| S-305 | Backup and critical service recovery | EV-006 | Workload-specific restoration not demonstrated |
| S-306 | Management review | Missing | Management reviews unrecorded |
| S-307 | Risk treatment / SoA | Phase 2 register | Two exclusions unapproved; 70 necessary controls unverified |
| S-308 | Awareness | EV-009 | Only 16/30 attendance initially |
| S-309 | Monitoring / logging | EV-005 | Four of nine priority source classes missing |
| S-310 | Endpoint encryption | EV-007 | Fictional scoped 15/15 check; no broader assurance |

## Severity and nonconformity caveat

The labels **Major-style** and **Minor-style** reflect *training priorities*, not accredited auditor classifications. A real nonconformity must connect a specific applicable requirement to sufficient objective evidence and be evaluated by a qualified impartial auditor. Our source records are invented; they are insufficient for declaring a real organizational nonconformity.

The exercise shows **six Major-style and three Minor-style indicative findings**. Root causes in the corrective-action register are *hypotheses* that would require interviews and corroboration. The positive encryption sample does not cancel any negative findings.

## Evidence and decision boundaries

- Original v0.1 data and v0.2 provisional applicability selection remain the historical record.
- A simulated audit observation does **not** demonstrate that an operating internal audit programme exists under Clause 9.2.
- An audit follow-up can acknowledge technical progress without formally closing a finding or accepting residual risk.
- Management review, remediation, SoA exclusions and audit conclusions require **real** authorization in a real organization.
- This report paraphrases control themes rather than reproducing licensed normative text.

## Practical next step

A genuine-style implementation would validate audit independence, select an impartial auditor, confirm the approved criteria and business scope, obtain source records, issue findings with independently substantiated root cause, and then run a formally authorized management review.
