from tools.handlers.detection_gap import detection_gap


def test_detection_gap():
    res = detection_gap("payments-service", "T1190")
    result = res["result"]
    assert "log-security" in result["written_logs"]
    assert "log-sysmon" in result["needed_logs"]
    assert "log-sysmon" in result["missing_logs"]

