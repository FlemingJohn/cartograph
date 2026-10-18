from agents.scoring.get_score import get_score


def make_measurement(
    finding: dict, route: list, data_stores: list, actor_count: int, missing: list
):
    return {
        "finding": finding,
        "attack_paths": {
            "result": {"is_reachable": bool(route), "hop_count": len(route) - 1 or None},
            "cypher": "",
            "path": route,
        },
        "blast_radius": {"result": data_stores, "cypher": "", "path": []},
        "actors_for": {
            "result": {"actor_count": actor_count, "actors": []},
            "cypher": "",
            "path": [],
        },
        "detection_gap": [{"result": {"missing_logs": missing}, "cypher": "", "path": []}],
    }


PAYMENTS = make_measurement(
    {"finding_id": "flaw-payments-001", "severity": 6.5, "service_id": "payments-service"},
    ["Internet", "web-gateway", "checkout-service", "payments-service"],
    [{"data_store_id": "customer-cards", "has_personal_data": True, "hop_count": 2}],
    14,
    ["waf-logs"],
)
REPORT = make_measurement(
    {"finding_id": "flaw-report-001", "severity": 9.8, "service_id": "report-generator"},
    [],
    [],
    14,
    [],
)


def test_payments_needs_fixing_now():
    score = get_score(PAYMENTS)
    assert score["total"] == 94
    assert score["status"] == "fix_now"


def test_report_generator_is_capped_and_accepted():
    score = get_score(REPORT)
    assert score["total"] == 39
    assert score["status"] == "accept"


def test_payments_outranks_the_more_severe_report_generator():
    assert get_score(PAYMENTS)["total"] > get_score(REPORT)["total"]
