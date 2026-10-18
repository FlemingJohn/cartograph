from tools.handlers.actors_for import actors_for


def test_actors_for():
    res = actors_for(["T1190"], limit=5)
    result = res["result"]
    assert result["actor_count"] > 0
    assert len(result["actors"]) <= 5
    assert all("id" in a and "name" in a for a in result["actors"])

