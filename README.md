# ISO/IEC 27001:2022 — ISMS Governance & Gap Assessment

**Independent cybersecurity/GRC portfolio project · Version 0.2 (applicability review) · 5 November 2026**

> **COMPLETELY FICTIONAL CASE STUDY.** Selene Payments Ltd, its infrastructure, employees, policies, documents, control checks, risk ratings and outcomes are synthetic. This repository is **not** an ISO certification, third-party audit, legal compliance opinion or evidence of professional employment.

## Purpose

A fictional EU payments technology business is preparing to formalize its **Information Security Management System (ISMS)**. The assignment is to define a limited but defensible ISMS scope, identify assets and accountability, assess risks, evaluate evidence against selected ISO/IEC 27001:2022 requirements and Annex A controls, prepare a **provisional** Statement of Applicability (SoA), and propose risk treatment and executive priorities.

This project complements, but does not duplicate, a separate third-party supplier-risk case study. Here the assessment is about **the company's internal management system**.

## Phase 2 — Provisional control-selection review (v0.2)

The [new Phase 2 review](phase2/README.md) documents individual **provisional necessity decisions for all 93 Annex A identifiers**, including 91 necessary safeguards and two **proposed exclusions awaiting validation**. The original 23 focused controls are preserved; across the reviewed register, 11 have existing Gap findings, 10 Partial findings, 70 have implementation **not verified**, and two are conditional exclusions. The distinction between choosing a control and demonstrating it operates is fundamental.

See the [complete selection register](phase2/data/soa_applicability_review.csv), [evidence workstreams](phase2/data/control_follow_up_actions.csv) and [companion workbook](phase2/SoA_Review_v0.2.xlsx). **This is not a management-approved SoA or certification audit.**

## Version 0.1 baseline (retained unchanged)

| Area | v0.1 deliverable |
| --- | --- |
| Fictional organization and ISMS boundary | Documented |
| In-scope asset inventory | 10 sample assets (not claimed exhaustive) |
| Risk register and treatment | 10 scenarios, each with owner, inherent and residual scores, action |
| ISO 27001 management-system clauses | 24 selected checkpoints across Clauses 4–10 |
| Annex A reference catalogue | All **93 IDs** represented, **23 selected for deeper evaluation** |
| SoA status | **Provisional working register:** the other 70 entries are **Not assessed / Undetermined**, not excluded or compliant |
| Synthetic evidence | 12 logged items, including 9 clearly labelled fictional records |
| Governance templates | Sample security policy, risk acceptance and audit/management-review templates |
| Executive report | Gap priorities and 30/60/90-day roadmap |
| Automation | Standard-library Python validation and unit tests; Excel risk/SoA workbook |

### What the original v0.1 SoA does **not** claim

The ISO reference list is complete by **control ID**, but only 23 controls were chosen for focused gap review. The remaining 70 are explicitly awaiting evaluation. The initial **v0.1** SoA was an incomplete baseline. The separate **v0.2** register now records provisional selection reasons for 93/93 identifiers; **70 necessary controls still lack implementation evidence** and two exclusions await independent scope confirmation. Neither an approved SoA nor conformity is being claimed.

## Start here

1. [Fictional company, ISMS scope and stakeholders](docs/01-organization-and-scope.md)
2. [Risk and evidence scoring methodology](docs/02-assessment-method.md)
3. [Requirements and Annex A gap approach](docs/03-gaps-and-soa.md)
4. [Executive report and actions](docs/04-executive-report.md)
5. [Remediation and governance roadmap](docs/05-roadmap.md)
6. [Standards mapping and sources](docs/06-sources-and-limitations.md)
7. [Phase 2 applicability decisions](phase2/docs/07-applicability-decisions.md)
8. [Evidence plan and approval gates](phase2/docs/08-evidence-and-approval-plan.md)

Source data are in [`data/`](data/), clearly marked synthetic artifacts in [`evidence/`](evidence/), templates in [`templates/`](templates/) and governance drafts in [`policies/`](policies/).

## Reproduce the checks

Requires Python 3.10 or later; **no external Python packages for validation**.

```sh
python scripts/validate_project.py
python scripts/validate_phase2.py
python -m unittest discover -s tests -v
```

The original risk workbook is **`ISMS_Gap_Assessment.xlsx`** (v0.1 baseline). The new **`phase2/SoA_Review_v0.2.xlsx`** covers the separate applicability review. Source CSVs are authoritative; neither workbook automatically syncs with CSV edits.

## Caveats

- All scores are qualitative, judgment-based prioritization, not measured incident likelihoods or a certification score.
- Observations are synthetic training scenarios; even “demonstrated in simulation” does not equal actual supplier or organization evidence.
- **ISO/IEC 27001:2022 Clauses 4–10** concern ISMS requirements; Annex A contains **93 reference controls** in 37 Organizational, 8 People, 14 Physical and 34 Technological categories.
- The project paraphrases control themes and **does not reproduce the licensed standard's text**.
- ISO/IEC 27001:2022 has **Amendment 1:2024** relating to climate action context; the fictional scope records this as a checkpoint for discussion, not proof it has been addressed.
- No assertion of conformity, accreditation, live audit, employment, production security test or regulatory applicability is made.

## Official starting sources

- ISO official publication: https://committee.iso.org/standard/27001
- ISO standard overview: https://www.iso.org/standard/27001
- NIST CSF 2.0 Govern function (supplemental reference): https://www.nist.gov/cyberframework
- ISO/IEC 27001 licensed standard is required for a real audit.

**Development note:** v0.2 addresses the remaining selection justifications, but does not claim implementation evidence for the 70 unverified controls. Next work should model a genuine-style **fictional internal audit**, corrective actions and management review with strict evidence limits. Keep private while developing.
