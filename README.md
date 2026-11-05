# ISO/IEC 27001:2022 — ISMS Governance & Gap Assessment

**Independent cybersecurity/GRC portfolio project · Version 0.1 (foundation) · 5 November 2026**

> **COMPLETELY FICTIONAL CASE STUDY.** Selene Payments Ltd, its infrastructure, employees, policies, documents, control checks, risk ratings and outcomes are synthetic. This repository is **not** an ISO certification, third-party audit, legal compliance opinion or evidence of professional employment.

## Purpose

A fictional EU payments technology business is preparing to formalize its **Information Security Management System (ISMS)**. The assignment is to define a limited but defensible ISMS scope, identify assets and accountability, assess risks, evaluate evidence against selected ISO/IEC 27001:2022 requirements and Annex A controls, prepare a **provisional** Statement of Applicability (SoA), and propose risk treatment and executive priorities.

This project complements, but does not duplicate, a separate third-party supplier-risk case study. Here the assessment is about **the company's internal management system**.

## Status and scope of first version

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

### What the SoA does **not** claim

The ISO reference list is complete by **control ID**, but only 23 controls were chosen for focused gap review. The remaining 70 are explicitly awaiting evaluation. Consequently, **this is not a completed SoA or full ISO 27001 conformity assessment**. Every necessary-control selection and every eventual exclusion would need an approved, risk-based justification.

## Start here

1. [Fictional company, ISMS scope and stakeholders](docs/01-organization-and-scope.md)
2. [Risk and evidence scoring methodology](docs/02-assessment-method.md)
3. [Requirements and Annex A gap approach](docs/03-gaps-and-soa.md)
4. [Executive report and actions](docs/04-executive-report.md)
5. [Remediation and governance roadmap](docs/05-roadmap.md)
6. [Standards mapping and sources](docs/06-sources-and-limitations.md)

Source data are in [`data/`](data/), clearly marked synthetic artifacts in [`evidence/`](evidence/), templates in [`templates/`](templates/) and governance drafts in [`policies/`](policies/).

## Reproduce the checks

Requires Python 3.10 or later; **no external Python packages for validation**.

```sh
python scripts/validate_project.py
python -m unittest discover -s tests -v
```

The risk spreadsheet is **`ISMS_Gap_Assessment.xlsx`**. Source CSVs are authoritative for the project; updating a CSV does not automatically rewrite the workbook.

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

**Development note:** v0.1 establishes a defendable, checkable case-study baseline. Next work should complete the remaining SoA justifications and strengthen internal audit, management review and evidence acceptance, rather than simply treating empty controls as passed.
