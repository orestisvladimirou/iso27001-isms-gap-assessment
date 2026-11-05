# Phase 3 — Simulated internal audit, corrective action and management review

**Entirely fictional teaching exercise.** No qualified independent auditor performed a real audit; no management approvals, signed records or external certification exist.

This phase builds upon the unmodified v0.1 baseline and the v0.2 provisional SoA review. It models selected evidence sampling, audit-style findings, root-cause corrective action, a hypothetical verification round and management decision tracking.

The internal audit model is deliberately **sample-based** and is not a certification assessment of all 93 Annex A controls. Decisions are instructional proposals; existing unresolved findings and the two unapproved exclusions are explicitly retained.

- [Audit scope and independence limitations](docs/09-internal-audit-method.md)
- [Management review report](docs/10-management-review.md)
- [Correction and evidence follow-up](docs/11-effectiveness-review.md)
- [Audit samples](data/audit_samples.csv), [findings](data/audit_findings.csv), [corrective actions](data/corrective_actions.csv)
- [Management review inputs](data/management_review_inputs.csv), [proposed management actions](data/management_decisions.csv), [risk trend](data/risk_follow_up.csv), and [performance indicators](data/kpi_snapshot.csv)

Run `python scripts/validate_phase3.py` and `python -m unittest discover -s tests -v` after downloading the full repository.
