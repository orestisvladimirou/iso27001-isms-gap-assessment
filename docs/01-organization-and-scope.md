# 01 — Fictional organization and ISMS boundary

**Selene Payments Ltd** is an invented EU payments software provider. To avoid asserting actual licensing or regulatory status, it is **not represented as a real regulated business**. The case assumes it operates digital payment software for business customers and processes customer-related records.

## Proposed ISMS scope (draft)

> The ISMS covers the engineering, administration and operation of Selene's payment-processing API, customer information storage, cloud tenant, identity services, employee endpoints, supporting CI/CD pipelines, monitoring and recovery processes, and relevant personnel and contractors supporting those services.

**Physical scope:** Fictional leased office, remote staff and cloud regions supporting the service. Physical protections operated by the landlord require separate evidence; the assessment does not assume their effectiveness.

**Interfaces:** Infrastructure hosting and identity providers are external service dependencies; vendor due diligence is relevant but *outside the detailed focus* of this project. In-scope management remains accountable for its own configuration, access decisions, continuity and outsourcing interfaces.

**Known gaps:** No approved ISMS scope statement; unknown cloud data-store candidates; physical access information incomplete; shared-responsibility boundaries require management approval.

## Internal and external context

The company is assumed to have approximately 30 employees, a cloud-hosted engineering team, a small security function and no prior formal ISMS. Business priorities are customer trust, integrity of payment records, rapid recovery and controlled handling of confidential data.

External interested parties might include business customers, data subjects, contractors, cloud service providers, regulators where applicable and auditors. Specific legal obligations **must be established for a real company**, not presumed because the scenario mentions payments.

ISO 27001:2022 Amendment 1:2024 relates to considering climate change in the organizational context and interested-party needs. Whether climate change is relevant to Selene's ISMS would require assessment of facilities, service continuity and stakeholder expectations. It is **currently an uncompleted checkpoint**.

## Governance roles (fictional)

| Role | ISMS responsibility |
| --- | --- |
| Managing Director | Accountable sponsor and resource/risk policy approver |
| Information Security Manager | Coordinates the ISMS and monitors security objectives |
| Service / asset owners | Confirm criticality, data classification and risk treatment |
| Engineering Lead | Secure changes, patching, cloud hardening |
| Security Operations Lead | Logging, event response and monitoring |
| HR Lead | Security awareness and personnel controls |
| Internal auditor | Assesses documented ISMS operation with independence from audited tasks |
| Risk committee | Reviews significant risk acceptance and remediation exceptions |

In version 0.1 the governance arrangements above are **proposed roles, not verified appointments or approvals**.

## Assets

The [`asset inventory`](../data/asset_inventory.csv) records 10 sample assets with owners and locations. It is deliberately marked incomplete: the training evidence identifies additional possible cloud stores needing discovery. Do not infer full inventory coverage.

## In-scope security objectives (proposals, not approved targets)

1. Consistently enforce administrative MFA on all in-scope human privileged identities.
2. Assign approved owners and classifications to all discovered in-scope information stores.
3. Restore the simulated critical processing workload inside business-approved RTO and RPO objectives.
4. Monitor defined high-value authentication and cloud activity from all identified required sources.
5. Train in-scope staff and exercise the incident escalation path.

Metrics and thresholds in the roadmap are **suggested management objectives**, not statements of current performance.
