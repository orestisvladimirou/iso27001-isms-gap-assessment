#!/usr/bin/env python3
"""Review dashboard source-of-truth, cross-phase traceability and document links.

Every record is fictional. Validation is a consistency check, not an ISO
conformity opinion, internal audit, approval, or certification.
"""
import csv
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

from validate_project import ROOT, load, band
from validate_phase2 import p2_load
from validate_phase3 import p3_load, validate_phase3

P4 = ROOT / "phase4" / "data"

def p4_load(name):
    with (P4 / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def validate_links():
    broken = []
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for file in ROOT.rglob("*.md"):
        if any(p in (".git", "__pycache__") for p in file.parts):
            continue
        for raw in pattern.findall(file.read_text(encoding="utf-8")):
            # GitHub Markdown may contain an optional link title.
            dest = raw.strip().split(" ", 1)[0].strip("<>")
            if not dest or dest.startswith(("#", "http://", "https://", "mailto:", "data:")):
                continue
            relative = unquote(dest.split("#", 1)[0].split("?", 1)[0])
            if relative and not (file.parent / relative).exists():
                broken.append(f"{file.relative_to(ROOT)} -> {relative}")
    assert not broken, "Broken local Markdown links:\n" + "\n".join(broken)
    return True

def validate_portfolio():
    validate_phase3()
    old = {r["risk_id"]: r for r in load("risk_register.csv")}
    new = {r["risk_id"]: r for r in p3_load("risk_follow_up.csv")}
    evo = p4_load("risk_evolution.csv")
    metrics = p4_load("dashboard_indicators.csv")
    crosswalk = p4_load("audit_action_crosswalk.csv")
    soa = p2_load("soa_applicability_review.csv")
    clauses = load("clauses_gap_assessment.csv")
    findings = {r["finding_id"]: r for r in p3_load("audit_findings.csv")}
    actions = {r["finding_id"]: r for r in p3_load("corrective_actions.csv")}
    inputs = p3_load("management_review_inputs.csv")
    kpis = {r["kpi_id"]: r for r in p3_load("kpi_snapshot.csv")}
    proposals = p3_load("management_decisions.csv")
    tests = p3_load("audit_samples.csv")
    assert set(old) == set(new) and len(evo) == 10
    assert len({r["risk_id"] for r in evo}) == 10
    assert len(metrics) == len({r["metric_id"] for r in metrics}) == 14
    assert len(inputs) == len({r["input_id"] for r in inputs}) == 8
    assert len(crosswalk) == 9 and len({r["finding_id"] for r in crosswalk}) == 9

    baseline, followup = Counter(), Counter()
    changed = []
    for r in evo:
        rid = r["risk_id"]
        assert rid in old
        a, b = old[rid], new[rid]
        assert r["asset_id"] == a["asset_id"] and r["risk_owner"] == a["risk_owner"]
        assert (r["baseline_likelihood"], r["baseline_impact"], r["baseline_residual_score"], r["baseline_band"]) == (
            a["residual_likelihood"], a["residual_impact"], a["residual_score"], a["residual_band"]
        )
        assert (r["followup_likelihood"], r["followup_impact"], r["followup_residual_score"], r["followup_band"]) == (
            b["followup_likelihood"], b["followup_impact"], b["followup_score"], b["followup_band"]
        )
        assert int(r["score_change"]) == int(b["followup_score"]) - int(a["residual_score"])
        assert int(r["followup_residual_score"]) == int(r["followup_likelihood"])*int(r["followup_impact"])
        assert r["followup_band"] == band(int(r["followup_residual_score"]))
        assert r["new_evidence_ids"] == b["new_evidence_ids"]
        assert r["risk_approval_status"] == "NOT APPROVED - SIMULATED"
        baseline[r["baseline_band"]] += 1
        followup[r["followup_band"]] += 1
        if r["score_change"] != "0":
            changed.append((rid, int(r["score_change"])))
    assert baseline == {"Critical":2, "High":6, "Medium":2}
    assert followup == {"Critical":1, "High":7, "Medium":2}
    assert changed == [("ISMS-R01", -10)], "Only the scoped privileged-access scenario may change"

    control_counts = Counter(s["implementation_status"] for s in soa)
    assert len(soa) == 93 and control_counts == {
        "Gap":11, "Partial":10, "Not verified":70,
        "Not applicable if assumption confirmed":2
    }
    assert sum(s["necessity_decision"] == "Necessary - provisional" for s in soa) == 91
    assert len(clauses) == 24 and Counter(c["gap_status"] for c in clauses) == {
        "Gap":14, "Partial":9, "Not assessed":1
    }

    for row in crosswalk:
        fid = row["finding_id"]
        assert fid in findings and fid in actions
        f, a = findings[fid], actions[fid]
        assert (row["sample_id"], row["severity_training_only"], row["criterion"], row["finding_status"]) == (
            f["sample_id"], f["indicative_severity"], f["criterion"], f["status"]
        )
        assert (row["capa_id"], row["responsible_role"], row["capa_followup_state"]) == (
            a["capa_id"], a["owner_role"], a["followup_state"]
        )
        assert row["related_risk"] == f["related_risk"]
        assert row["independent_closure"] == "NOT OBTAINED"
        assert a["followup_state"] in ("OPEN", "EVIDENCE_RECEIVED_NOT_CLOSED", "ATTENDANCE_ONLY_NOT_CLOSED")

    all_metrics = {m["metric_id"]: m for m in metrics}
    values = {
        "K01": ("2","1"), "K02": ("6","7"), "K03": ("2","2"),
        "K04": ("n/a","93"), "K05": ("n/a","91"), "K06": ("n/a","70"),
        "K07": ("n/a","2"), "K08": ("n/a","9"), "K09": ("n/a","9"),
        "K10": ("n/a","7"), "K11": ("4","7"), "K12": ("16","30"),
        "K13": ("5","5"), "K14": ("n/a","24")
    }
    for mid, v in values.items():
        assert (all_metrics[mid]["baseline"], all_metrics[mid]["followup"]) == v, mid
        for source in all_metrics[mid]["source_files"].split(";"):
            assert (ROOT / source).is_file(), f"Missing source for {mid}: {source}"
    assert (kpis["KPI-301"]["baseline_numerator"], kpis["KPI-301"]["followup_numerator"]) == ("4","7")
    assert (kpis["KPI-302"]["baseline_numerator"], kpis["KPI-302"]["followup_numerator"]) == ("16","30")
    assert len(tests) == 10 and len(findings) == len(actions) == 9
    assert len(proposals) == 7 and all(x["no_real_approval"] == "Yes" for x in proposals)

    for inp in inputs:
        assert inp["status"] == "DRAFT_FOR_FICTIONAL_REVIEW"
        source = inp["source_reference"]
        assert (ROOT/source).is_file(), f"Stale management-review input: {inp['input_id']} -> {source}"
    mri = {r["input_id"]: r for r in inputs}
    assert mri["MRI-302"]["source_reference"] == "phase3/data/audit_findings.csv"
    assert "Nine indicative findings" in mri["MRI-302"]["scenario_observation"]
    assert "Nine open" in mri["MRI-306"]["scenario_observation"]
    assert mri["MRI-303"]["source_reference"] == "phase3/data/risk_follow_up.csv"

    validate_links()
    print("PASS portfolio: dashboard and risk history match source records; 93 provisional controls, 9 open CAPAs, "
          "8 valid management inputs, 14 indicators and all local Markdown links.")
    return True

if __name__ == "__main__":
    validate_portfolio()
