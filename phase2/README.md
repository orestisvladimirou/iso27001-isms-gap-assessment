# Phase 2 — Provisional Statement of Applicability selection review

**Version 0.2 · 5 November 2026 · Fully fictional training assessment**

This phase completes **control-selection decisions** against all 93 ISO/IEC 27001:2022 Annex A reference identifiers, while preserving the original v0.1 gap-assessment observations in `data/`. It is **not** evidence that all 93 controls operate, that the decisions were approved, or that the company meets ISO/IEC 27001 certification requirements.

## Outcomes

| Assessment dimension | Count | Meaning |
| --- | ---: | --- |
| Annex A identifiers with documented provisional decisions | 93 | All reference IDs covered |
| Controls selected as necessary (provisional) | 91 | Scope/risk rationale and evidence request recorded |
| Proposed exclusions | 2 | Pending explicit scope validation and formal approval |
| Existing synthetic Gap findings carried forward | 11 | Deficiencies identified in v0.1, not re-tested |
| Existing Partial findings carried forward | 10 | Some practice claimed, full effectiveness unverified |
| Necessary controls with implementation **not verified** | 70 | Neither passed nor failed; request evidence |
| New evidence-collection workstreams | 9 | Proposed owners; all open and unapproved |

## Read and reproduce

1. [Decision method and proposed exclusions](docs/07-applicability-decisions.md)
2. [Evidence collection and approval approach](docs/08-evidence-and-approval-plan.md)
3. [Full 93-control decision register](data/soa_applicability_review.csv)
4. [Nine follow-up evidence workstreams](data/control_follow_up_actions.csv)
5. [Companion review workbook](SoA_Review_v0.2.xlsx) (not a replacement for the baseline workbook)

From repository root:

```sh
python scripts/validate_project.py
python scripts/validate_phase2.py
python -m unittest discover -s tests -v
```

### Important separation

**Selection/applicability** asks whether a safeguard is needed for the ISMS boundary. **Implementation status** asks whether the fictional organization demonstrably operates it. **Management approval** is a third, independent requirement; no approval is simulated as genuine.

The earlier `data/statement_of_applicability.csv` and `ISMS_Gap_Assessment.xlsx` remain the immutable v0.1 baseline. The new data and workbook document *follow-up applicability decisions*, not a completed operating-control audit. Neither contains licensed ISO normative control wording; focus descriptions are independent summaries.

Source context: ISO/IEC 27001:2022 Clause 6.1.3 and Annex A; obtain a licensed standard for real conformity work. See <https://committee.iso.org/standard/27001>.
