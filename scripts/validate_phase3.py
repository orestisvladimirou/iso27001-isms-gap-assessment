#!/usr/bin/env python3
"""Validate a MOCK internal audit and a DRAFT management review in the fictional ISMS."""
import csv
from collections import Counter
from datetime import date
from pathlib import Path

from validate_phase2 import ROOT, p2_load, validate_phase2
from validate_project import load

P3 = ROOT / "phase3" / "data"

def p3_load(name):
    with (P3 / name).open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def unique(rows, key):
    keys = [r[key] for r in rows]
    assert len(set(keys)) == len(keys), "Duplicate " + key
    return {r[key]: r for r in rows}

def validate_phase3():
    validate_phase2()  # Phase 1 and 2 remain the source of earlier conclusions
    risks = unique(load("risk_register.csv"), "risk_id")
    actions = unique(load("treatment_plan.csv"), "action_id")
    evidence = unique(load("evidence_register.csv"), "evidence_id")
    soa = unique(p2_load("soa_applicability_review.csv"), "control_id")
    samples = unique(p3_load("mock_audit_samples.csv"), "sample_id")
    findings = unique(p3_load("mock_audit_findings.csv"), "finding_id")
    capas = unique(p3_load("corrective_actions.csv"), "capa_id")
    inputs = unique(p3_load("management_review_inputs.csv"), "input_id")
    proposals = unique(p3_load("management_review_proposals.csv"), "proposal_id")

    assert len(samples) == 9 and len(findings) == len(capas) == 8
    assert len(inputs) == 8 and len(proposals) == 6
    assert Counter(s["sample_result"] for s in samples.values()) == {
        "Gap": 6, "Partial": 2, "Limited positive observation": 1
    }
    assert Counter(f["severity"] for f in findings.values()) == {
        "Major - simulated": 5, "Minor - simulated": 3
    }
    assert len({f["sample_id"] for f in findings.values()}) == 8
    assert {f["sample_id"] for f in findings.values()} == {
        s["sample_id"] for s in samples.values()
        if s["sample_result"] != "Limited positive observation"
    }
    assert len([s for s in samples.values() if s["sample_result"] == "Limited positive observation"]) == 1

    for s in samples.values():
        assert s["soa_control_id"] in soa
        assert s["risk_id"] in risks
        assert s["review_method"] and s["limitations"] and s["independence_note"]
        if s["baseline_evidence_id"]:
            assert s["baseline_evidence_id"] in evidence
        assert "Fictional" in s["independence_note"]
    for f in findings.values():
        sample = samples[f["sample_id"]]
        assert sample["sample_result"] in ("Gap", "Partial")
        assert f["criterion"] == sample["criterion"]
        assert f["soa_control_id"] == sample["soa_control_id"]
        assert f["linked_risk_id"] == sample["risk_id"]
        assert f["evidence_id"] == sample["baseline_evidence_id"]
        assert f["finding_type"] == "Nonconformity - mock"
        assert f["status"] == "OPEN"
        assert f["finding_statement"] and f["verification_limitation"]

    assert {c["finding_id"] for c in capas.values()} == set(findings)
    for c in capas.values():
        f = findings[c["finding_id"]]
        assert c["linked_treatment_id"] in actions
        assert actions[c["linked_treatment_id"]]["risk_id"] == f["linked_risk_id"]
        assert len(c["root_cause_hypothesis"]) >= 20
        assert all(c[k] for k in ("immediate_containment","systemic_corrective_action",
                                  "evidence_for_closure","owner"))
        assert c["status"] == "OPEN" and c["approval_status"] == "NOT_APPROVED"
        assert date.fromisoformat(c["target_date"]) >= date(2026, 12, 8)
        assert date.fromisoformat(c["independent_follow_up_date"]) > date.fromisoformat(c["target_date"])

    for x in inputs.values():
        assert x["status"] == "DRAFT_FOR_FICTIONAL_REVIEW"
        assert x["management_question"] and x["scenario_observation"]
        assert (ROOT / x["source_reference"]).is_file(), "Missing input source"
    for p in proposals.values():
        assert p["input_id"] in inputs
        assert p["status"] == "PROPOSED_ONLY" and p["authorization"] == "NONE"
        assert p["responsible_role"] and p["proposed_management_direction"]
        assert date.fromisoformat(p["requested_date"]) >= date(2026, 12, 8)
        related = p["related_capa_ids"].split(";")
        assert related and all(x in capas for x in related)
    assert all(r["decision_review_status"].startswith("Awaiting") for r in soa.values())
    print("PASS Phase 3: 9 synthetic samples, 8 OPEN mock findings, 8 unapproved CAPAs, "
          "8 review inputs and 6 unapproved proposals; no evidence or approval invented.")
    return True

if __name__ == "__main__":
    validate_phase3()
