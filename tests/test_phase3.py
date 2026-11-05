import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_phase3 import p3_load, validate_phase3

class AuditRehearsalTests(unittest.TestCase):
    def test_integrity_and_references(self):
        self.assertTrue(validate_phase3())

    def test_positive_control_does_not_become_conformity_claim(self):
        samples = p3_load("audit_samples.csv")
        positive = [s for s in samples if s["result"] == "SCOPED POSITIVE OBSERVATION"]
        self.assertEqual(len(positive), 1)
        self.assertEqual(positive[0]["source_ref"], "EV-007")
        self.assertFalse(positive[0]["finding_id"])

    def test_no_finding_is_closed_or_approved(self):
        findings = p3_load("audit_findings.csv")
        actions = p3_load("corrective_actions.csv")
        self.assertEqual(len(findings), 9)
        self.assertTrue(all("CLOSED" not in f["status"] for f in findings))
        self.assertTrue(all("CLOSED" not in a["followup_state"] for a in actions))
        self.assertTrue(all(r["independent_signoff"] == "NOT OBTAINED"
                            for r in p3_load("effectiveness_reviews.csv")))

    def test_training_attendance_is_not_risk_reduction(self):
        risks = {r["risk_id"]: r for r in p3_load("risk_follow_up.csv")}
        self.assertEqual(risks["ISMS-R09"]["followup_score"], risks["ISMS-R09"]["baseline_score"])
        self.assertEqual(risks["ISMS-R01"]["followup_score"], "10")

    def test_proposals_have_no_real_approval(self):
        decisions = p3_load("management_decisions.csv")
        self.assertTrue(all(d["decision_status"] == "ROLE-PLAY PROPOSAL" and
                            d["no_real_approval"] == "Yes" for d in decisions))

if __name__ == "__main__":
    unittest.main()
