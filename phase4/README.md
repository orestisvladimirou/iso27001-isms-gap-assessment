# Phase 4 — Integrated ISMS dashboard and publication-quality review

**Version 0.4. A fictional, non-certification training exercise.**

The earlier phases stay intact: **v0.1 baseline**, **v0.2 provisional applicability**, **v0.3 simulated audit/review**. This phase creates the unified management view, fixes inconsistent source references, and adds integrity checks. It **does not** turn synthetic examples into real assurance or approved controls.

Start with the [integrated portfolio dashboard](dashboard.md). It compares the ten risks, 93 Annex A selections, 24 management-system checkpoints, nine indicative audit findings, nine open corrective actions, and seven unsigned role-play management proposals.

Use the [quality review and remaining limitations](docs/final-quality-review.md) for the checks performed, case-study constraints, and conditions before public release.

The accompanying machine-readable data files are:

- [Dashboard indicators](data/dashboard_indicators.csv)
- [Risk score evolution](data/risk_evolution.csv)
- [Audit finding to CAPA crosswalk](data/audit_action_crosswalk.csv)

**Existing Excel files are versioned historical snapshots** (`ISMS_Gap_Assessment.xlsx` and `phase2/SoA_Review_v0.2.xlsx`); the integrated dashboard is GitHub-native Markdown rather than a misleading overwritten workbook.

Run `python scripts/validate_portfolio.py` along with the full suite in [the project README](../README.md). Keep the GitHub repository private until its owner explicitly approves publication.
