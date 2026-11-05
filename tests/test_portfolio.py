import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_portfolio import p4_load, validate_links, validate_portfolio

class PortfolioQualityTests(unittest.TestCase):
    def test_integrated_validation(self):
        self.assertTrue(validate_portfolio())

    def test_single_modelled_score_change(self):
        items = p4_load("risk_evolution.csv")
        changed = {x["risk_id"]: x["score_change"] for x in items if x["score_change"] != "0"}
        self.assertEqual(changed, {"ISMS-R01": "-10"})

    def test_non_assurance_language_visible(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / "phase4" / "dashboard.md").read_text(encoding="utf-8")
        self.assertIn("NOT ISO/IEC 27001 CERTIFIED", text)
        self.assertIn("70", text)
        self.assertIn("formally closed", text)
        self.assertIn("Management", text)

    def test_all_local_links_resolve(self):
        self.assertTrue(validate_links())

    def test_source_crosswalk_preserves_open_capa(self):
        items = p4_load("audit_action_crosswalk.csv")
        self.assertEqual(len(items), 9)
        self.assertTrue(all(x["independent_closure"] == "NOT OBTAINED" for x in items))
