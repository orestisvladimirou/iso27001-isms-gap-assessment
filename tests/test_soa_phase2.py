import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_phase2 import validate_phase2, p2_load

class Phase2ApplicabilityTests(unittest.TestCase):
    def test_complete_provisional_review(self):
        self.assertTrue(validate_phase2())

    def test_exclusions_require_confirmation(self):
        rows=p2_load('soa_applicability_review.csv')
        excluded={x['control_id']:x for x in rows if x['necessity_decision']=='Proposed exclusion'}
        self.assertEqual(set(excluded),{'A.7.6','A.8.30'})
        self.assertTrue(all('Awaiting' in x['decision_review_status'] for x in excluded.values()))

    def test_new_controls_are_not_invented_passes(self):
        rows=p2_load('soa_applicability_review.csv')
        self.assertFalse(any(x['implementation_status'] in ('Implemented','Compliant','Approved') for x in rows))
        self.assertEqual(sum(x['implementation_status']=='Not verified' for x in rows),70)

    def test_workstreams_cover_all_new_evidence_requests(self):
        rows=p2_load('soa_applicability_review.csv')
        workstreams={a['action_ref'] for a in p2_load('control_follow_up_actions.csv')}
        self.assertTrue(all(x['treatment_ref'] for x in rows))
        self.assertTrue(any(x['treatment_ref'] in workstreams for x in rows))

    def test_existing_gap_findings_are_preserved(self):
        from validate_project import load
        baseline={x['control_id']:x for x in load('statement_of_applicability.csv')}
        reviewed={x['control_id']:x for x in p2_load('soa_applicability_review.csv')}
        for cid,old in baseline.items():
            if old['assessment_status'] in ('Gap','Partial'):
                self.assertEqual(reviewed[cid]['implementation_status'],old['assessment_status'])

if __name__=='__main__':unittest.main()
