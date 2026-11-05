#!/usr/bin/env python3
"""Validate a hypothetical control-selection review without inflating assurance."""
import csv
from collections import Counter
from pathlib import Path
from validate_project import ROOT, load, validate

PHASE2 = ROOT / 'phase2' / 'data'

def p2_load(name):
    with (PHASE2 / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def validate_phase2():
    validate()  # v0.1 baseline must remain consistent and unaltered
    baseline = {r['control_id']:r for r in load('statement_of_applicability.csv')}
    actions = {r['action_id'] for r in load('treatment_plan.csv')}
    risks = {r['risk_id'] for r in load('risk_register.csv')}
    evidence = {r['evidence_id'] for r in load('evidence_register.csv')}
    rows = p2_load('soa_applicability_review.csv')
    workstreams = p2_load('control_follow_up_actions.csv')
    follow_ups = {r['action_ref']:r for r in workstreams}
    ids = [r['control_id'] for r in rows]
    assert len(rows) == len(ids) == len(set(ids)) == 93, 'Missing or duplicate SoA control'
    assert set(ids) == set(baseline), 'Phase 2 must cover exactly the original 93 references'
    assert len(workstreams) == len(follow_ups) == 9, 'Missing or duplicate follow-up workstream'
    assert all(x.startswith('P2-A') for x in follow_ups)
    expected = {'Necessary - provisional':91, 'Proposed exclusion':2}
    assert dict(Counter(x['necessity_decision'] for x in rows)) == expected
    expected_status = {'Gap':11,'Partial':10,'Not verified':70,
                       'Not applicable if assumption confirmed':2}
    assert dict(Counter(x['implementation_status'] for x in rows)) == expected_status
    excluded = {x['control_id'] for x in rows if x['necessity_decision']=='Proposed exclusion'}
    assert excluded == {'A.7.6','A.8.30'}, 'Proposed exclusions need explicit boundary justification'
    for r in rows:
        old = baseline[r['control_id']]
        assert r['theme']==old['theme']
        assert r['decision_review_status'].startswith('Awaiting')
        assert r['control_focus'] and 'review pending' not in r['control_focus'].lower()
        assert len(r['inclusion_or_exclusion_reason'])>=50
        assert len(r['specific_evidence_request'])>=30
        assert r['accountable_role']
        assert r['review_trigger']
        for eid in r['evidence_ids'].split(';'):
            if eid: assert eid in evidence
        for rid in r['linked_risks'].split(';'):
            if rid: assert rid in risks
        ref = r['treatment_ref']
        assert ref in actions or ref in follow_ups, f'Unknown treatment reference {ref}'
        if old['assessment_status'] in ('Gap','Partial'):
            assert r['implementation_status']==old['assessment_status'], 'No silent baseline finding changes'
            assert r['evidence_ids']==old['evidence_ids']
        elif r['necessity_decision']=='Necessary - provisional':
            assert r['implementation_status']=='Not verified', 'No invented positive assurance'
        else:
            assert r['implementation_status']=='Not applicable if assumption confirmed'
            assert 'validate' in r['inclusion_or_exclusion_reason'].lower()
            assert r['treatment_ref'] in follow_ups
    assert len({r['inclusion_or_exclusion_reason'] for r in rows}) == 93, 'Control reasons must be specific'
    for a in workstreams:
        assert a['proposed_owner'] and a['required_verification']
        assert a['status']=='Open - scenario'
        assert a['owner_approval']=='Not obtained - simulated'
        ref_ids = {x for x in a['related_control_ids'].split(';') if x}
        assert ref_ids, 'Workstream without control'
        assert ref_ids == {r['control_id'] for r in rows if r['treatment_ref']==a['action_ref']}
    assert sum(r['project_control_focus']=='Annex A control reference — review pending' for r in baseline.values())==70
    print('PASS Phase 2: 93 unique provisional decisions (91 necessary, 2 conditional exclusions); '
          '11 gap, 10 partial, 70 unverified; 9 follow-up workstreams; no approvals fabricated.')
    return True

if __name__ == '__main__':
    validate_phase2()
