from tools.handlers.attack_paths import attack_paths


def test_attack_paths():
    res_payments = attack_paths("payments-service")
    assert res_payments["result"]["is_reachable"] is True
    assert res_payments["result"]["hop_count"] == 3
    assert "payments-service" in res_payments["path"]

    res_report = attack_paths("report-generator")
    assert res_report["result"]["is_reachable"] is False
    assert res_report["result"]["hop_count"] is None
    assert res_report["path"] == []

