# ISO/IEC 27001:2022 — ISMS Governance & Gap Assessment

**Independent cybersecurity/GRC portfolio project · Version 0.4 (integrated portfolio dashboard and quality review) · 5 November 2026**

> **COMPLETELY FICTIONAL CASE STUDY.** Selene Payments Ltd, its infrastructure, employees, policies, documents, control checks, risk ratings and outcomes are synthetic. This repository is **not** an ISO certification, third-party audit, legal compliance opinion or evidence of professional employment.

## Purpose

A fictional EU payments technology business is preparing to formalize its **Information Security Management System (ISMS)**. The assignment is to define a limited but defensible ISMS scope, identify assets and accountability, assess risks, evaluate evidence against selected ISO/IEC 27001:2022 requirements and Annex A controls, prepare a **provisional** Statement of Applicability (SoA), and propose risk treatment and executive priorities.

This project complements, but does not duplicate, a separate third-party supplier-risk case study. Here the assessment is about **the company's internal management system**.

## Phase 2 — Provisional control-selection review (v0.2)

The [new Phase 2 review](phase2/README.md) documents individual **provisional necessity decisions for all 93 Annex A identifiers**, including 91 necessary safeguards and two **proposed exclusions awaiting validation**. The original 23 focused controls are preserved; across the reviewed register, 11 have existing Gap findings, 10 Partial findings, 70 have implementation **not verified**, and two are conditional exclusions. The distinction between choosing a control and demonstrating it operates is fundamental.

See the [complete selection register](phase2/data/soa_applicability_review.csv), [evidence workstreams](phase2/data/control_follow_up_actions.csv) and [companion workbook](phase2/SoA_Review_v0.2.xlsx). **This is not a management-approved SoA or certification audit.**

## Phase 3 — Internal audit and management review rehearsal (v0.3)

The [Phase 3 dossier](phase3/README.md) contains **ten synthetic audit samples**, **nine indicative audit-style findings** (six Major-style and three Minor-style as *training priorities*, not formal auditor grades), nine corrective-action cases, two explicitly fictional follow-up samples, six KPI measures and seven **unsigned role-play management directions**.

In the made-up follow-up, scoped 7/7 privileged human MFA evidence allows a **provisional** change of ISMS-R01 from 20 Critical to **10 High**. Training attendance improves from 16/30 to 30/30, but without demonstrated learning, ISMS-R09 remains **9 Medium**. The other risks do not change, leaving **one Critical, seven High, two Medium**. **No finding is formally closed; no manager has approved risk treatment or the provisional SoA.**

See the [audit sampling method](phase3/docs/09-internal-audit-method.md), [management review rehearsal](phase3/docs/10-management-review.md), [corrective-action/effectiveness analysis](phase3/docs/11-effectiveness-review.md) and [executive closeout](phase3/docs/12-executive-closeout.md). Original v0.1 and v0.2 source registers and their two workbooks are retained. This is **not a performed independent internal audit or an ISO certification assessment**.

## Phase 4 — Integrated portfolio dashboard and QA review (v0.4)

The [GitHub-native management dashboard](phase4/dashboard.md) combines all ten fictional risk scores, the 93-control provisional SoA, 24 selected ISO/IEC 27001 requirements checkpoints, ten simulated audit samples, nine open CAPAs, performance indicators, and **seven unsigned role-play proposals**. The [final quality review](phase4/docs/final-quality-review.md) documents corrected historical-management input references, data provenance, and limitations.

**Latest fictional risk state: one Critical, seven High and two Medium.** The dashboard is not a compliance score or evidence of ISO certification. The v0.1 and v0.2 Excel workbooks remain historical snapshots; no dashboard numbers are represented as real business results.

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
9. [Phase 3 audit and management review exercise](phase3/README.md)
10. [Integrated management dashboard and final review](phase4/README.md)

Source data are in [`data/`](data/), clearly marked synthetic artifacts in [`evidence/`](evidence/), templates in [`templates/`](templates/) and governance drafts in [`policies/`](policies/).

## Reproduce the checks

Requires Python 3.10 or later; **no external Python packages for validation**.

```sh
python scripts/validate_project.py
python scripts/validate_phase2.py
python scripts/validate_phase3.py
python scripts/validate_portfolio.py
python scripts/validate_workbook.py
python scripts/validate_manifest.py
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

**Portfolio note:** v0.4 completes the integrated synthetic assessment and cross-phase consistency review. The mock company is **not certified**, the provisional SoA has no real authorization, and the 70 unverified controls are still unverified. Retain the repository as **private** until the owner personally reviews its contents and explicitly elects to publish.
