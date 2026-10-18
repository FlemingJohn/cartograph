from tools.handlers.record_decision import record_decision


def test_record_decision():
    res = record_decision(
        finding_id="flaw-payments-001",
        status="fix_now",
        score=95,
        reason="Reachable, near card data, missing Sysmon log",
        evidence_ids=[],
    )
    result = res["result"]
    assert "decision_id" in result
    assert result["decision_id"].startswith("dec-")

