#!/usr/bin/env python3
"""Cross-phase consistency checks for an entirely fictional ISMS audit rehearsal."""
import csv
from collections import Counter
from datetime import date
from pathlib import Path

from validate_project import ROOT, load, band
from validate_phase2 import p2_load, validate_phase2

P3 = ROOT / "phase3" / "data"

def p3_load(filename):
    with (P3 / filename).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def check_ids(rows, key, n):
    values = [r[key] for r in rows]
    assert len(values) == len(set(values)) == n, f"Expected {n} unique {key}"
    return set(values)

def validate_phase3():
    validate_phase2()
    base_risks = {r["risk_id"]: r for r in load("risk_register.csv")}
    base_actions = {r["action_id"] for r in load("treatment_plan.csv")}
    base_evidence = {r["evidence_id"] for r in load("evidence_register.csv")}
    p2_controls = {r["control_id"] for r in p2_load("soa_applicability_review.csv")}

    plans = p3_load("audit_plan.csv")
    samples = p3_load("audit_samples.csv")
    findings = p3_load("audit_findings.csv")
    actions = p3_load("corrective_actions.csv")
    evidence = p3_load("follow_up_evidence.csv")
    reviews = p3_load("effectiveness_reviews.csv")
    kpis = p3_load("kpi_snapshot.csv")
    decisions = p3_load("management_decisions.csv")
    scores = p3_load("risk_follow_up.csv")

    assert len(plans) == 1 and plans[0]["audit_id"] == "AUD-301"
    assert plans[0]["audit_status"] == "SIMULATED DESK REHEARSAL"
    assert "not" in plans[0]["independence_limitation"].lower()
    sample_ids = check_ids(samples, "sample_id", 10)
    finding_ids = check_ids(findings, "finding_id", 9)
    capa_ids = check_ids(actions, "capa_id", 9)
    ev_ids = check_ids(evidence, "evidence_id", 2)
    review_ids = check_ids(reviews, "review_id", 2)
    check_ids(kpis, "kpi_id", 6)
    check_ids(decisions, "decision_id", 7)
    assert set(x["risk_id"] for x in scores) == set(base_risks) and len(scores) == 10
    assert dict(Counter(f["indicative_severity"] for f in findings)) == {"Major-style": 6, "Minor-style": 3}
    assert {x["finding_id"] for x in actions} == finding_ids
    assert {x["finding_id"] for x in evidence} == {"F-303", "F-308"}
    assert {x["finding_id"] for x in reviews} == {"F-303", "F-308"}

    f_by_id = {x["finding_id"]: x for x in findings}
    a_by_id = {x["capa_id"]: x for x in actions}
    e_by_id = {x["evidence_id"]: x for x in evidence}
    s_by_id = {x["sample_id"]: x for x in samples}

    for row in samples:
        assert row["audit_id"] == "AUD-301"
        assert row["source_ref"] in base_evidence or row["source_ref"] == "MISSING" or (ROOT/row["source_ref"]).is_file()
        if row["result"] == "INDICATIVE FINDING":
            assert row["finding_id"] in finding_ids
        else:
            assert row["result"] == "SCOPED POSITIVE OBSERVATION" and not row["finding_id"]
    assert sum(x["result"] == "INDICATIVE FINDING" for x in samples) == 9

    for row in findings:
        assert row["sample_id"] in sample_ids
        assert s_by_id[row["sample_id"]]["finding_id"] == row["finding_id"]
        assert row["criterion"] == s_by_id[row["sample_id"]]["criterion"]
        assert row["baseline_action_id"] in base_actions
        assert row["baseline_evidence_ref"] in base_evidence or row["baseline_evidence_ref"] == "MISSING" or (ROOT/row["baseline_evidence_ref"]).is_file()
        if row["related_risk"]:
            assert row["related_risk"] in base_risks
        assert row["status"] in ("OPEN - REHEARSAL", "EVIDENCE RECEIVED - FOLLOW-UP OPEN", "ATTENDANCE IMPROVED - FOLLOW-UP OPEN")
        assert len(row["root_cause_hypothesis"]) > 35

    for row in actions:
        assert row["finding_id"] in finding_ids
        assert row["immediate_correction"] and row["root_cause_correction"] and row["effectiveness_test"]
        assert row["closure_authority"] and row["followup_state"] in (
            "OPEN", "EVIDENCE_RECEIVED_NOT_CLOSED", "ATTENDANCE_ONLY_NOT_CLOSED"
        )
        assert row["capa_id"].replace("CAPA", "F") == row["finding_id"]
        assert date.fromisoformat(row["due_date"]) > date(2026, 11, 5)

    for row in evidence:
        assert row["finding_id"] in finding_ids
        p = ROOT / row["source_file"]
        assert p.is_file()
        content = p.read_text(encoding="utf-8").upper()
        assert "SYNTHETIC" in content or "FICTIONAL" in content
        assert date.fromisoformat(row["scenario_date"]) > date.fromisoformat(plans[0]["scenario_date"])
        assert "simulation" in row["confidence"].lower() or "effectiveness" in row["confidence"].lower()

    for row in reviews:
        assert row["review_id"] in review_ids and row["capa_id"] in capa_ids
        assert row["finding_id"] == a_by_id[row["capa_id"]]["finding_id"]
        assert row["finding_id"] == e_by_id[row["new_evidence_id"]]["finding_id"]
        assert row["independent_signoff"] == "NOT OBTAINED"
        assert row["finding_disposition"].startswith("OPEN")
        assert date.fromisoformat(row["review_date"]) >= date.fromisoformat(e_by_id[row["new_evidence_id"]]["scenario_date"])
    assert e_by_id["P3-E01"]["scenario_date"] > a_by_id["CAPA-303"]["due_date"], "Late simulated MFA completion must not be concealed"

    metrics = {row["kpi_id"]: row for row in kpis}
    assert [(metrics[x]["baseline_numerator"], metrics[x]["followup_numerator"]) for x in ("KPI-301","KPI-302")] == [("4","7"), ("16","30")]
    assert (metrics["KPI-303"]["followup_numerator"],metrics["KPI-303"]["denominator"]) == ("5", "9")
    for k in kpis:
        assert k["measure"] and k["interpretation"]
        for ev in k["source_evidence"].split(";"):
            assert ev in base_evidence or ev in ev_ids, f"Unknown KPI evidence {ev}"

    changed = []
    for row in scores:
        base = base_risks[row["risk_id"]]
        assert (row["baseline_likelihood"], row["baseline_impact"],row["baseline_score"]) == (
            base["residual_likelihood"], base["residual_impact"], base["residual_score"]
        )
        l, impact = int(row["followup_likelihood"]), int(row["followup_impact"])
        assert 1 <= l <= 5 and 1 <= impact <= 5
        assert int(row["followup_score"]) == l * impact
        assert row["followup_band"] == band(l * impact)
        assert row["approval_status"] == "NOT APPROVED - SIMULATED"
        new_ids = [x for x in row["new_evidence_ids"].split(";") if x]
        assert all(e in ev_ids for e in new_ids)
        if (l, impact) != (int(base["residual_likelihood"]),int(base["residual_impact"])):
            changed.append(row["risk_id"])
            assert row["risk_id"] == "ISMS-R01" and new_ids == ["P3-E01"]
            assert (l, impact) == (2, 5)
        if row["risk_id"] == "ISMS-R09":
            assert new_ids == ["P3-E02"]
            assert (l, impact) == (3, 3), "Attendance without effectiveness must not change risk"
    assert changed == ["ISMS-R01"]
    assert Counter(x["followup_band"] for x in scores) == {"Critical":1,"High":7,"Medium":2}

    for d in decisions:
        assert d["decision_status"] == "ROLE-PLAY PROPOSAL"
        assert d["no_real_approval"] == "Yes"
        assert d["owner_role"] and d["simulated_direction"] and d["inputs_reviewed"]
        assert date.fromisoformat(d["scenario_meeting_date"]) > date.fromisoformat(plans[0]["scenario_date"])
    assert {x["control_id"] for x in p2_load("soa_applicability_review.csv")
            if x["necessity_decision"]=="Proposed exclusion"} == {"A.7.6","A.8.30"}
    assert len(p2_controls) == 93
    print("PASS Phase 3: 10 audit samples, 9 indicative findings (6 major-style, 3 minor-style), 9 open CAPAs, "
          "2 limited follow-ups, 6 KPIs, 10 linked risks and 7 unsigned role-play proposals.")
    return True

if __name__ == "__main__":
    validate_phase3()
