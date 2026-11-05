import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_phase3 import p3_load, validate_phase3

class MockAuditTests(unittest.TestCase):
    def test_complete_integrity(self):
        self.assertTrue(validate_phase3())

    def test_findings_remain_open(self):
        findings = p3_load("mock_audit_findings.csv")
        capas = p3_load("corrective_actions.csv")
        self.assertEqual(len(findings), 8)
        self.assertEqual(len(capas), 8)
        self.assertTrue(all(f["status"] == "OPEN" for f in findings))
        self.assertTrue(all(c["status"] == "OPEN" and
                            c["approval_status"] == "NOT_APPROVED" for c in capas))

    def test_management_proposals_are_not_approved(self):
        proposals = p3_load("management_review_proposals.csv")
        self.assertEqual(len(proposals), 6)
        self.assertTrue(all(p["status"] == "PROPOSED_ONLY" and
                            p["authorization"] == "NONE" for p in proposals))

    def test_limited_positive_not_called_nonconformity(self):
        samples = p3_load("mock_audit_samples.csv")
        findings = {f["sample_id"] for f in p3_load("mock_audit_findings.csv")}
        positives = [s for s in samples if s["sample_result"] == "Limited positive observation"]
        self.assertEqual(len(positives), 1)
        self.assertEqual(positives[0]["sample_id"], "S-309")
        self.assertNotIn("S-309", findings)

    def test_no_unsupported_approval(self):
        for row in p3_load("management_review_inputs.csv"):
            self.assertEqual(row["status"], "DRAFT_FOR_FICTIONAL_REVIEW")

if __name__ == "__main__":
    unittest.main()
