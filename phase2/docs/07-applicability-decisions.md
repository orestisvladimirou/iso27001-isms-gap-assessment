# 07 — Defensible selection decisions for the 93 Annex A references

**Exercise assumption:** Selene Payments Ltd is a fabricated 30-person, cloud-operated payments software business with an internal development team, leased office, remote workers and external cloud/identity providers. No legal regulatory status or certification has been independently established. All records are fictional.

## Method

1. **Start with the ISMS boundary and risks.** The draft scope covers production payment APIs, cloud identities, CI/CD, customer-related data, staff endpoints, leased office, and continuity operations. Existing risk IDs `ISMS-R01`–`ISMS-R10` are linked where relevant. A single risk reference identifies a *plausible connection*, not a complete standalone risk treatment analysis.
2. **Determine control necessity.** For each of the 93 Annex A identifiers, record an independently paraphrased safeguard focus, a scenario-specific inclusion reason or exclusion assumption, a proposed accountable role and linked risk/treatment reference.
3. **Keep selection separate from implementation.** Twenty-one selected controls retain the v0.1 `Gap` (11) or `Partial` (10) findings. The other **70 necessary controls are `Not verified`**, not compliant, non-compliant, or implemented. No additional evidence has magically appeared.
4. **Request concrete proof.** Every row states what records, exports, walkthroughs or tests would be needed to make a later operational conclusion.
5. **Do not claim management approval.** All 93 decisions are provisional and require confirmation of the company's actual boundaries, risk treatment plan, owners, and any exclusion justifications. No real manager signed anything.

This is a **selection review**, not an independent audit, and should not be described as a complete assessment of control effectiveness. ISO/IEC 27001 Clause 6.1.3 calls for necessary controls, justifications, implementation information and exclusion justifications; our register is a draft exercise, pending organizational confirmation.

## Two proposed exclusions (neither approved)

| Control | Narrow working assumption | Necessary validation / reversal trigger |
| --- | --- | --- |
| **A.7.6** — restricted-area working practices | The fictional business has **no specially designated secure processing room**. Production services run in hosted cloud regions. General office-entry and equipment protection remain necessary and are assessed separately. | Facilities must confirm the layout, any restricted rooms and contractual expectations. If such a room exists, **include A.7.6**. |
| **A.8.30** — external software development oversight | Fictional custom payment software is assumed **developed internally**. Using cloud and identity providers does not itself prove an outsourced software development service. | Engineering/Procurement must examine contractor delivery and development contracts. If external software development occurs, **include A.8.30**. |

Both proposed exclusions are deliberately testable. Without owner validation, the actual SoA would not be approved; neither exclusion can be treated as a legal safe harbor or a claim that a protection is unneeded for all organizations.

## Review results

| Provisional treatment | Controls |
| --- | ---: |
| Necessary with existing Gap observation | 11 |
| Necessary with existing Partial observation | 10 |
| Necessary but implementation not independently established | 70 |
| Exclusion proposed pending scenario assumption validation | 2 |
| **Total** | **93** |

Of the 23 originally *focused* v0.1 references, two physical-scope references (A.7.2 and A.7.7) are now assessed as **necessary but not yet verified**. The original baseline is retained unchanged; no missing technical evidence was invented for them.

## Governance boundary

The 24 selected Clauses 4–10 checkpoints remain a separate requirement-level review with 14 Gap, 9 Partial and 1 Not assessed. **Annex A controls are not a substitute for management-system requirements**. A full ISMS assessment needs actual documented operation, independent internal audit, management review, follow-up, and approved risk-treatment decisions.

**Important copyright caveat:** Control focuses are independently written, practical paraphrases, not reproduction of the licensed standard. Acquire ISO/IEC 27001:2022 (and any applicable updates) for formal audit or certification work.
