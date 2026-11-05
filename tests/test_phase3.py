import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_phase3 import validate_phase3, p3_load

class Phase3AuditTests(unittest.TestCase):
    def test_full_integrity(self):
        self.assertTrue(validate_phase3())

    def test_nine_findings_are_not_closed(self):
        findings = p3_load("audit_findings.csv")
        actions = p3_load("corrective_actions.csv")
        self.assertEqual(len(findings), 9)
        self.assertFalse(any(a["followup_state"] == "CLOSED" for a in actions))
        self.assertEqual(sum(x["indicative_severity"] == "Major-style" for x in findings), 6)

    def test_followup_mechanism_and_training_caution(self):
        risks = {r["risk_id"]: r for r in p3_load("risk_follow_up.csv")}
        self.assertEqual((risks["ISMS-R01"]["baseline_score"], risks["ISMS-R01"]["followup_score"]), ("20","10"))
        self.assertEqual((risks["ISMS-R09"]["baseline_score"], risks["ISMS-R09"]["followup_score"]), ("9","9"))
        self.assertEqual(risks["ISMS-R09"]["new_evidence_ids"], "P3-E02")

    def test_no_real_management_approval_claimed(self):
        decisions = p3_load("management_decisions.csv")
        self.assertEqual(len(decisions), 7)
        self.assertTrue(all(d["no_real_approval"] == "Yes" for d in decisions))
        self.assertTrue(all(d["decision_status"] == "ROLE-PLAY PROPOSAL" for d in decisions))

    def test_two_explanations_have_no_formal_closure(self):
        followups = p3_load("effectiveness_reviews.csv")
        self.assertEqual(len(followups), 2)
        self.assertTrue(all(x["finding_disposition"].startswith("OPEN") for x in followups))
        self.assertTrue(all(x["independent_signoff"] == "NOT OBTAINED" for x in followups))
