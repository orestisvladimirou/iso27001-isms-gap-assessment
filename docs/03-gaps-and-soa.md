# 03 — ISO requirements, Annex A and the provisional SoA

There are **two distinct assessment layers** in this exercise.

### A. Management-system requirement checkpoints

[`clauses_gap_assessment.csv`](../data/clauses_gap_assessment.csv) covers 24 selected checkpoints from Clauses 4–10. These concern organizational context, leadership, planning, support, operation, performance evaluation and improvement. **14 are marked Gap, 9 Partial, and 1 Not assessed**. This is not a count of conformity/nonconformity findings from a real audit.

Notable gaps: no approved ISMS scope or security policy, no management-approved risk criteria, no documented internal audit programme, no completed ISMS management review, no corrective-action governance.

### B. Annex A reference control evaluation

[`statement_of_applicability.csv`](../data/statement_of_applicability.csv) contains **all 93 identifiers**, split into:
- Organizational: A.5.1–A.5.37 (37)
- People: A.6.1–A.6.8 (8)
- Physical: A.7.1–A.7.14 (14)
- Technological: A.8.1–A.8.34 (34)

For **23 controls** the project documents a short, independently authored control focus and synthetic gap/evidence. **70 other entries are explicitly `Undetermined / Not assessed`**. They are not missing from the register, not excluded from the hypothetical ISMS, and **not evidence of implementation**.

A real Statement of Applicability must be based on risk treatment, justify selected necessary controls, state implementation and explain exclusions. Merely listing all 93 IDs does not satisfy this exercise's completion criterion for a real SoA. This is a **provisional working SoA**, with deliberate transparency about work left to do.

## Examples

| Control reference | Synthetic issue | Suggested response |
| --- | --- | --- |
| A.5.9 | Information asset inventory incomplete | Validate coverage and approved owners |
| A.5.24 | Incident response process unapproved | Set roles, triggers and tabletop test |
| A.6.3 | 16 of 30 staff completed training | Define targeted program and attendance verification |
| A.8.2 | 3 of 7 privileged identities lack enforcement | Enforce policy and independently check account coverage |
| A.8.8 | Six critical patch backlog entries | Remediate, validate or formally escalate exceptions |
| A.8.15 / A.8.16 | Four of nine event sources missing | Restore monitoring coverage and test detections |

**Do not infer full-clause or control conformity from a single sample.** Some evidence is *missing* even where a working control may exist.

## Boundaries

This project paraphrases selected control **themes** without reproducing ISO copyrighted requirement text. It does not represent an official accreditation or an authorized ISO audit; the organization and findings are all invented. Obtain the licensed standard for a real conformity assessment.

Official source: https://committee.iso.org/standard/27001

## Phase 2 update (version 0.2)

The original v0.1 register above is intentionally retained as a baseline. [Phase 2](../phase2/README.md) records a provisional applicability decision for each of the 93 control identifiers, including proposed exclusion justifications for A.7.6 and A.8.30. In that *separate* register, 91 controls are provisionally necessary but 70 of them lack operating evidence, and two exclusions require an owner-approved scope check. The v0.1 counts in this document remain historically accurate, not the newest selection status.
