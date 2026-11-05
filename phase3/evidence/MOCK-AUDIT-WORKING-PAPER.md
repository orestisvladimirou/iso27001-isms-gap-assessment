# Synthetic audit sampling working paper — v0.3

**TRAINING SIMULATION ONLY.** Scenario audit date: **8 December 2026**. This is a hypothetical future review, not an event that took place. No actual interview, site inspection, live system access or independent professional audit occurred.

The fictional reviewer is assumed organizationally independent of the functions being sampled. **Independence is a scenario assumption, not evidence that an independent auditor has been appointed.** Findings are *mock nonconformity candidates* requiring a competent real audit to verify scope, criteria and severity.

## Method and limitations

The desk review uses *only* the original fictional evidence register and the provisional v0.2 SoA, with one sample drawn from each chosen risk/control domain. Missing evidence blocks positive assurance; it does not prove an unseen control is absent. This is deliberately **risk-based, not full certification coverage**.

| Sample | Existing fictional evidence | Scoped outcome |
| --- | --- | --- |
| S-301 | EV-012 (missing programme) | No approved internal audit schedule or impartial auditor assignment documented |
| S-302 | EV-001 (draft policy) | Security policy has no owner approval or dissemination proof |
| S-303 | v0.2 provisional SoA | All selection decisions await management; exclusions A.7.6 and A.8.30 unconfirmed |
| S-304 | EV-002 (seven privileged identities) | Three have no enforced MFA; no complete entitlement review |
| S-305 | EV-004 (critical vulnerability backlog) | Six overdue critical findings; no verified closure |
| S-306 | EV-005 (log-source inventory) | Five of nine priority feeds forwarded |
| S-307 | EV-006 (missing restore report) | No completed workload-specific recovery test supplied |
| S-308 | EV-009 (training attendance) | Sixteen of thirty staff show attendance; outcome untested |
| S-309 | EV-007 (device encryption) | Fifteen of fifteen *known, sampled* devices show encryption; do not extrapolate |

**No new technical evidence** is invented for this audit phase. Sample S-309 is a bounded positive observation, **not blanket conformity**; the original v0.1 risk score for endpoint loss stays unchanged. All original risk and SoA scores and statuses are preserved.

## Independence and reporting controls

In a genuine internal audit, choose an impartial reviewer, define approved criteria, schedule and scope, assess independent source records, report to management and maintain audit workpapers. A fictional project cannot appoint that person or obtain actual sign-off.

Severity labels in `mock_audit_findings.csv` are illustrative prioritization judgments, not ISO-prescribed pass/fail grades or findings issued by an accredited certification body.
