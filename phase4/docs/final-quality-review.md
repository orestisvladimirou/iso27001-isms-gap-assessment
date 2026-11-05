# Final quality review — portfolio version 0.4

**Review scope:** source-data consistency, evidence provenance, document navigation, the full provisional SoA, Phase 3 audit exercise and management-review inputs. **This is a review of a fictional teaching artifact, not an ISO internal audit or certification readiness assurance.**

## Corrections made

| Review ID | Observation | Disposition |
| :-- | :-- | :-- |
| QA-401 | Management input MRI-302 referenced a retired `mock_audit_findings.csv` file and eight findings rather than the final nine. | **Corrected** to the canonical `phase3/data/audit_findings.csv`; independent source-path validation added |
| QA-402 | Management input MRI-306 cited eight corrective actions, but the final CAPA register contains nine. | **Corrected** and cross-checked against current CAPAs |
| QA-403 | Management input MRI-303/304 mixed historical metrics with later fictional follow-up figures without explaining the timepoints. | **Clarified** the original and follow-up scenarios and linked source registers |
| QA-404 | Executive and roadmap documents from the original assessment can be mistaken for the latest result. | New integrated dashboard is linked prominently as the **latest hypothetical summary**; older reports remain immutable historical snapshots |
| QA-405 | Evidence selection decisions risk being confused with implemented operating controls. | Dashboard separates applicability, Gap/Partial, Not verified, proposed exclusions and approval state |
| QA-406 | No quick cross-phase view of risk scores, findings, CAPAs and management inputs. | Added auditable CSV snapshots and a source-linked dashboard; validators recompute quantities |

## Technical checks

- Verify ten baseline and follow-up risk IDs, arithmetic, bands, and the **single justified hypothetical score change**.
- Ensure SoA contains 93 control references, 91 provisional necessary, two proposed exclusions and 70 necessary controls marked **Not verified**.
- Verify 10 samples, nine indicative findings, nine open CAPAs, six KPIs and seven **unapproved** management proposals.
- Require that every management-review source path exists; retired paths are not permitted.
- Validate all local Markdown links in the **committed source tree**.
- Run the v0.1, v0.2 and v0.3 regressions, v0.2 workbook check and v0.4 manifest integrity check in GitHub Actions.

## What remains unproven — by design

- No independent internal audit, real technical control assessment or production evidence was obtained.
- **70** provisionally necessary Annex A controls do not have implementation verification.
- Neither proposed SoA exclusion was independently confirmed or formally approved.
- The nine corrective actions have no independent closure and no actual top-management sign-off exists.
- Quantitative risk ratings are *subjective scenario prioritization*, not measured security event probabilities.
- A real ISO/IEC 27001 conformity assessment requires the licensed standard, genuine operating evidence and qualified impartial auditors.

These are **limitations of the scenario**, not silently resolved issues. The project should be described as **an independent simulated ISMS gap assessment and governance documentation project**, not certification, employer work or an audit delivered to an actual company.

## Portfolio release criteria

- [x] Integrated summary reproduces authoritative source numbers.
- [x] Historical baseline and later hypothetical follow-up stay separated.
- [x] Fictional nature is prominent in reports and dashboard.
- [x] Source links and automated consistency checks are included.
- [ ] Owner reviews content and can personally explain risk scoring, SoA distinctions and corrective-action logic.
- [ ] Owner explicitly authorizes making this repository public. **No visibility change is implied by this review.**

See [dashboard](../dashboard.md) and the [repository README](../../README.md).
