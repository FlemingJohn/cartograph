from tools.handlers.chokepoints import chokepoints


def test_chokepoints():
    res = chokepoints(limit=5)
    points = res["result"]
    assert len(points) > 0
    assert any(p["service_id"] == "checkout-service" for p in points)
    assert points[0]["betweenness"] >= points[-1]["betweenness"]

