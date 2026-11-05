import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_project import validate,load,band

class AssessmentTests(unittest.TestCase):
    def test_integrity(self):
        self.assertTrue(validate())

    def test_band_limits(self):
        expected = [(1,"Low"),(4,"Low"),(5,"Medium"),(9,"Medium"),
                    (10,"High"),(16,"High"),(17,"Critical"),(25,"Critical")]
        for score, name in expected:
            self.assertEqual(band(score),name)

    def test_control_catalogue(self):
        rows=load("statement_of_applicability.csv")
        self.assertEqual(len(rows),93)
        self.assertEqual({x["control_id"].split(".")[1] for x in rows},{"5","6","7","8"})
        self.assertEqual(sum(x["applicability"]=="Undetermined" for x in rows),72)

    def test_mitigation_limited_to_scope(self):
        risks={r["risk_id"]:r for r in load("risk_register.csv")}
        self.assertEqual((risks["ISMS-R07"]["inherent_score"],risks["ISMS-R07"]["residual_score"]),("12","6"))
        for rid,r in risks.items():
            if rid!="ISMS-R07":
                self.assertEqual(r["inherent_score"],r["residual_score"])

    def test_no_fake_approval(self):
        docs=list((Path(__file__).resolve().parents[1]/"policies").glob("*.md"))
        self.assertEqual(len(docs),2)
        for path in docs:
            self.assertIn("DRAFT",path.name)
            self.assertIn("DRAFT",path.read_text(encoding="utf-8").upper())

if __name__=="__main__":
    unittest.main()
