# POL-002 — Access Control Policy (DRAFT, synthetic)

**Status:** Unapproved teaching draft. No real identity provider is configured or accessed.

## Scope

All in-scope staff, contractors, privileged administrators and cloud service accounts.

## Proposed requirements

- Grant access through documented role ownership and least-privilege business need.
- Require appropriate MFA for all privileged human accounts; explicitly monitor emergency identities and exceptions.
- Joiner/mover/leaver access changes must be traceable to authorized requests.
- Review privileged access at least quarterly in this fictional risk tier, track missing records and remove orphan permissions.
- Protect non-human credentials with restricted scopes, rotation or short-lived identity federation; review service accounts separately from human MFA.
- Log significant changes and unauthorized-access attempts; verify whether log destinations and alert rules are actually operating.
- Approve time-bounded exceptions through named risk authority rather than a blanket technical bypass.

## Evidence to demand

Account inventory; policy-enforcement export; emergency-account protections; sample access recertification; approved JML samples; exception expiry log; sampled administrative event trail.

## Example deficiency

The invented EV-002 extract lists three of seven privileged human identities without enforced MFA. This is **not** compliant with the proposal and is tracked as ISMS-R01 / ACT-01.
