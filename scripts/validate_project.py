#!/usr/bin/env python3
"""Standard-library integrity validator for a wholly fictional ISMS portfolio."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    with (ROOT / "data" / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def band(score):
    return "Low" if score <= 4 else "Medium" if score <= 9 else "High" if score <= 16 else "Critical"

def unique(rows, key, expected):
    keys = [row[key] for row in rows]
    assert len(rows) == expected and len(set(keys)) == expected, f"{key}: expected {expected} unique rows"
    return set(keys)

def validate():
    assets = load("asset_inventory.csv")
    risks = load("risk_register.csv")
    actions = load("treatment_plan.csv")
    evidence = load("evidence_register.csv")
    soa = load("statement_of_applicability.csv")
    clauses = load("clauses_gap_assessment.csv")

    asset_ids = unique(assets, "asset_id", 10)
    risk_ids = unique(risks, "risk_id", 10)
    action_ids = unique(actions, "action_id", 10)
    evidence_ids = unique(evidence, "evidence_id", 12)
    control_ids = unique(soa, "control_id", 93)
    clause_ids = unique(clauses, "clause_ref", 24)

    expected_ids = {f"A.{d}.{i}" for d,n in [(5,37),(6,8),(7,14),(8,34)] for i in range(1,n+1)}
    assert control_ids == expected_ids, "Incomplete Annex A control reference coverage"
    review = [s for s in soa if s["project_control_focus"] != "Annex A control reference — review pending"]
    assert len(review) == 23, "Expected 23 selected controls"
    pending = [s for s in soa if s["project_control_focus"] == "Annex A control reference — review pending"]
    assert len(pending) == 70
    for row in soa:
        assert row["theme"] in ("Organizational","People","Physical","Technological")
        assert row["applicability"] in ("Applicable","Undetermined")
        assert row["assessment_status"] in ("Gap","Partial","Not assessed")
        if row["assessment_status"] == "Not assessed":
            assert row["applicability"] == "Undetermined", "Unreviewed control must not be presented as applicable/excluded"
        if row["project_control_focus"] == "Annex A control reference — review pending":
            assert row["assessment_status"] == "Not assessed"
            assert not row["linked_risks"] and not row["action_id"]
        for key in (row["evidence_ids"].split(";") if row["evidence_ids"] else []):
            assert key in evidence_ids, f"Unknown SoA evidence {key}"
        for rid in (row["linked_risks"].split(";") if row["linked_risks"] else []):
            assert rid in risk_ids
        if row["action_id"]:
            assert row["action_id"] in action_ids
    assert len([x for x in soa if x["assessment_status"] == "Gap"]) == 11
    assert len([x for x in soa if x["assessment_status"] == "Partial"]) == 10
    assert len([x for x in soa if x["assessment_status"] == "Not assessed"]) == 72

    for row in evidence:
        if row["file"]:
            p = ROOT / row["file"]
            assert p.is_file(), f"Missing synthetic evidence file {row['file']}"
            assert "SYNTHETIC" in p.read_text(encoding="utf-8").upper() or "FICTIONAL" in p.read_text(encoding="utf-8").upper()
        if row["assurance_level"] == "Missing":
            assert not row["file"]
    assert {a["action_id"] for a in actions} == action_ids
    for a in actions:
        assert a["risk_id"] in risk_ids
        assert a["priority"] in ("P1","P2","P3")
        assert a["status"] in ("Open","Monitoring","Closed")
        for control in a["related_control_ids"].split(";"):
            assert control in control_ids
    for r in risks:
        assert r["asset_id"] in asset_ids
        assert r["action_id"] in action_ids
        assert r["evidence_confidence"] in ("Low","Medium-in-simulation","Missing")
        for prefix in ("inherent","residual"):
            l,i=int(r[f"{prefix}_likelihood"]),int(r[f"{prefix}_impact"])
            assert 1 <= l <= 5 and 1 <= i <= 5
            assert int(r[f"{prefix}_score"]) == l*i, f"Invalid {prefix} arithmetic in {r['risk_id']}"
            assert r[f"{prefix}_band"] == band(l*i)
        assert any(a["action_id"]==r["action_id"] and a["risk_id"]==r["risk_id"] for a in actions)
        for ev in r["evidence_ids"].split(";"):
            if ev: assert ev in evidence_ids
        if r["evidence_confidence"] == "Low":
            assert r["inherent_score"] == r["residual_score"], f"Unsupported reduction: {r['risk_id']}"
        if int(r["residual_score"]) < int(r["inherent_score"]):
            assert r["risk_id"] == "ISMS-R07" and r["evidence_ids"] == "EV-007"
            assert r["evidence_confidence"] == "Medium-in-simulation"
            assert r["verified_existing_control"], "Mitigation needs an explanatory mechanism"
    assert sum(r["residual_band"]=="Critical" for r in risks)==2
    assert sum(r["residual_band"]=="High" for r in risks)==6
    assert sum(r["residual_band"]=="Medium" for r in risks)==2
    assert sum(r["residual_band"]=="Low" for r in risks)==0
    for c in clauses:
        assert c["gap_status"] in ("Gap","Partial","Not assessed")
        if c["action_id"]: assert c["action_id"] in action_ids
        for evid in c["evidence_ids"].split(";"):
            if evid: assert evid in evidence_ids
    assert len([c for c in clauses if c["gap_status"]=="Gap"])==14
    assert len([c for c in clauses if c["gap_status"]=="Partial"])==9
    assert len([c for c in clauses if c["gap_status"]=="Not assessed"])==1
    assert "4.1" in clause_ids and "10.2" in clause_ids
    print("PASS: 10 assets, 10 risks, 10 actions, 12 evidence refs, "
          "24 clause checkpoints, and 93 Annex A refs (23 selected; 70 pending).")
    return True

if __name__=="__main__":
    validate()
