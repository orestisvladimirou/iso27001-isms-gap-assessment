# 08 — Evidence collection, review ownership and approval gates

**Fictional exercise. No actual technical controls have been newly tested in this phase.** The nine workstreams in [`control_follow_up_actions.csv`](../data/control_follow_up_actions.csv) are proposed tasks, not closed corrective actions or management-approved commitments.

## Workstream priorities and evidence tests

| Ref | Evidence focus | Acceptance check (future scenario) |
| --- | --- | --- |
| P2-A01 | Governance and leadership | Policy and role authority are formally approved; a legal obligations inventory and audit timetable exist |
| P2-A02 | Information lifecycle and privacy | Inventory identifies owner/classification and data transfer, deletion, masking and retention evidence for chosen samples |
| P2-A03 | Identity lifecycle | Joiner/mover/leaver, MFA, emergency access and privilege approvals are checked across all relevant identities |
| P2-A04 | Cloud and ICT dependencies | Dependency list, security requirements, change notices and ownership are verified against in-scope providers |
| P2-A05 | Incident and continuity | Exercise shows event triage, evidence preservation, crisis operation and real restoration objectives |
| P2-A06 | Personnel safeguards | Role screening, confidentiality, remote work, training and departures have auditable sample records |
| P2-A07 | Office and physical safeguards | Walkthrough and landlord documentation cover entry, workspace, maintenance and scope of any secure areas |
| P2-A08 | Platform and endpoint protection | Targeted system exports demonstrate patching, logging, networking, endpoint protections and backup coverage |
| P2-A09 | Secure engineering | Release/change records show security gates, test-data controls and whether external development is used |

These are **evidence acceptance proposals**, not proof of control operation. For a real assessment, selection should be based on actual business impact, verified inventory, legal requirements, contracts, risk treatment, and scope; the assessor should record sample selection and coverage limitations.

## Approval decisions that remain open

- **ISMS owner:** confirm exact organizational and technical boundary, including subcontractor work, office space and cloud responsibilities.
- **Risk owners:** sign off risk treatment plans and the acceptance or escalation of residual risks. The modeled critical and high risks remain open.
- **Control owners:** provide dated evidence and justify applicable controls before operational conclusions are drawn.
- **Authorized management:** approve the SoA and both exclusions, or return proposed exclusions to `Necessary` where assumptions fail.
- **Independent audit role:** subsequently assess requirements and selected controls against evidence, without treating this desk exercise as audit assurance.

In the current records, **all approvals are absent**. Do not label the ISMS compliant, certified, implemented, or officially audited because the register is filled out.

## Versioning

- **Baseline v0.1:** `data/statement_of_applicability.csv` and `ISMS_Gap_Assessment.xlsx` record an incomplete initial assessment.
- **Follow-up v0.2:** `phase2/data/soa_applicability_review.csv` and `phase2/SoA_Review_v0.2.xlsx` supply 93 provisional selection decisions; implementation evidence remains largely unverified.
- **Next phase:** construct *simulated* internal audit samples, corrective-action root causes, hypothetical remediation evidence, and management-review decisions, keeping historic records intact.
