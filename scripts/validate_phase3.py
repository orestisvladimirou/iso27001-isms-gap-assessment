#!/usr/bin/env python3
"""Check linked fictional audit, corrective action, evidence and management records."""
import csv
from collections import Counter
from datetime import date
from pathlib import Path
from validate_project import load
from validate_phase2 import ROOT, p2_load, validate_phase2

P3 = ROOT / "phase3" / "data"

def p3_load(name):
    with (P3 / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))

def by_id(rows, key):
    ids = [r[key] for r in rows]
    assert len(ids) == len(set(ids)), "Repeated " + key
    return {r[key]: r for r in rows}

def band(score):
    return "Low" if score <= 4 else "Medium" if score <= 9 else "High" if score <= 16 else "Critical"

def validate_phase3():
    validate_phase2()
    original = by_id(load("risk_register.csv"), "risk_id")
    treatment = by_id(load("treatment_plan.csv"), "action_id")
    evidence = by_id(load("evidence_register.csv"), "evidence_id")
    soa = by_id(p2_load("soa_applicability_review.csv"), "control_id")
    audit = by_id(p3_load("audit_plan.csv"), "audit_id")
    samples = by_id(p3_load("audit_samples.csv"), "sample_id")
    findings = by_id(p3_load("audit_findings.csv"), "finding_id")
    actions = by_id(p3_load("corrective_actions.csv"), "capa_id")
    follow_evidence = by_id(p3_load("follow_up_evidence.csv"), "evidence_id")
    reviews = by_id(p3_load("effectiveness_reviews.csv"), "review_id")
    risks = by_id(p3_load("risk_follow_up.csv"), "risk_id")
    kpis = by_id(p3_load("kpi_snapshot.csv"), "kpi_id")
    proposals = by_id(p3_load("management_decisions.csv"), "decision_id")
    inputs = by_id(p3_load("management_review_inputs.csv"), "input_id")

    assert len(audit) == 1 and len(samples) == 10
    assert len(findings) == len(actions) == 9
    assert len(follow_evidence) == len(reviews) == 2
    assert len(risks) == len(original) == 10
    assert len(kpis) == 6 and len(proposals) == 7 and len(inputs) == 8
    assert list(audit.values())[0]["audit_status"] == "SIMULATED DESK REHEARSAL"
    assert Counter(x["result"] for x in samples.values()) == {
        "INDICATIVE FINDING": 9, "SCOPED POSITIVE OBSERVATION": 1
    }
    assert Counter(x["indicative_severity"] for x in findings.values()) == {
        "Major-style": 6, "Minor-style": 3
    }
    assert {x["finding_id"] for x in samples.values() if x["finding_id"]} == set(findings)

    for s in samples.values():
        assert s["audit_id"] in audit
        assert s["sampling_scope"] and s["evidence_observation"]
        if s["source_ref"].startswith("EV-"):
            assert s["source_ref"] in evidence
        elif s["source_ref"] != "MISSING":
            assert (ROOT / s["source_ref"]).is_file(), "Missing sampled source"
        if s["result"] == "SCOPED POSITIVE OBSERVATION":
            assert not s["finding_id"]
        else:
            assert s["finding_id"] in findings
    for f in findings.values():
        assert f["sample_id"] in samples
        assert f["finding_id"] == samples[f["sample_id"]]["finding_id"]
        assert f["criterion"] == samples[f["sample_id"]]["criterion"]
        assert f["baseline_evidence_ref"] == samples[f["sample_id"]]["source_ref"]
        assert f["baseline_action_id"] in treatment
        if f["related_risk"]:
            assert f["related_risk"] in original
            assert treatment[f["baseline_action_id"]]["risk_id"] == f["related_risk"]
        assert f["root_cause_hypothesis"] and f["status"] != "CLOSED"
        assert "REHEARSAL" in f["status"] or "FOLLOW-UP OPEN" in f["status"]
    assert {c["finding_id"] for c in actions.values()} == set(findings)
    for a in actions.values():
        assert a["owner_role"] and a["effectiveness_test"] and a["root_cause_correction"]
        assert a["followup_state"] not in ("CLOSED", "VERIFIED_CLOSED")
        assert a["closure_authority"] and date.fromisoformat(a["due_date"]) >= date(2026, 11, 19)

    for e in follow_evidence.values():
        assert e["finding_id"] in findings
        assert (ROOT / e["source_file"]).is_file()
        assert date.fromisoformat(e["scenario_date"]) >= date(2026, 11, 19)
        assert e["confidence"] and e["remaining_limit"]
    for r in reviews.values():
        assert r["finding_id"] in findings
        assert r["capa_id"] in actions and actions[r["capa_id"]]["finding_id"] == r["finding_id"]
        assert r["new_evidence_id"] in follow_evidence
        assert follow_evidence[r["new_evidence_id"]]["finding_id"] == r["finding_id"]
        assert r["independent_signoff"] == "NOT OBTAINED"
        assert r["finding_disposition"].startswith("OPEN")
        assert date.fromisoformat(r["review_date"]) >= date.fromisoformat(
            follow_evidence[r["new_evidence_id"]]["scenario_date"])

    changed = []
    for r in risks.values():
        old = original[r["risk_id"]]
        for part in ("likelihood", "impact", "score"):
            assert int(r["baseline_" + part]) == int(old["residual_" + part])
        l, i = int(r["followup_likelihood"]), int(r["followup_impact"])
        score = int(r["followup_score"])
        assert 1 <= l <= 5 and 1 <= i <= 5
        assert score == l * i and r["followup_band"] == band(score)
        assert r["approval_status"] == "NOT APPROVED - SIMULATED"
        new_ids = [x for x in r["new_evidence_ids"].split(";") if x]
        assert all(x in follow_evidence for x in new_ids)
        if score < int(r["baseline_score"]):
            assert new_ids and r["risk_id"] == "ISMS-R01", "Unexpected unverified reduction"
            changed.append(r["risk_id"])
    assert changed == ["ISMS-R01"]
    assert int(risks["ISMS-R01"]["followup_score"]) == 10
    assert int(risks["ISMS-R09"]["followup_score"]) == int(risks["ISMS-R09"]["baseline_score"])

    for k in kpis.values():
        assert k["interpretation"]
        assert int(k["denominator"]) > 0
        assert 0 <= int(k["baseline_numerator"]) <= int(k["denominator"])
        assert 0 <= int(k["followup_numerator"]) <= int(k["denominator"])
        for source in k["source_evidence"].split(";"):
            assert source in evidence or source in follow_evidence
    for m in proposals.values():
        assert m["decision_status"] == "ROLE-PLAY PROPOSAL" and m["no_real_approval"] == "Yes"
        assert m["simulated_direction"] and m["owner_role"]
        assert date.fromisoformat(m["followup_due"]) >= date.fromisoformat(m["scenario_meeting_date"])
    for record in inputs.values():
        assert record["status"] == "DRAFT_FOR_FICTIONAL_REVIEW"
        assert record["management_question"]
        assert (ROOT / record["source_reference"]).is_file()

    assert len(soa) == 93
    assert all(s["decision_review_status"].startswith("Awaiting") for s in soa.values())
    print("PASS Phase 3: 10 synthetic samples, 9 OPEN indicative findings, 9 unresolved CAPAs, "
          "2 qualified follow-up reviews, 10 checked risk scores, 7 unapproved role-play proposals.")
    return True

if __name__ == "__main__":
    validate_phase3()
