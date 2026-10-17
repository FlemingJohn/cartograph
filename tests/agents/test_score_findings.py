import asyncio

from agents.connect_tools import connect_tools
from agents.context.app_context import AppContext
from agents.fakes.fake_findings import make_fake_findings
from agents.nodes.measure_findings import measure_findings
from agents.nodes.score_findings import score_findings


def get_scored_state() -> dict:
    context = AppContext(model=None, tools=asyncio.run(connect_tools()), graph_name="test")
    runtime = type("FakeRuntime", (), {"context": context})()
    state = {"scan_id": "scan-test", "findings": make_fake_findings("scan-test")}
    measured = asyncio.run(measure_findings(state, runtime))
    return score_findings(measured)


def test_payments_lands_near_the_top():
    scored = get_scored_state()
    assert scored["scores"]["F-0001"]["status"] == "fix_now"
    assert scored["shortlist"].index("F-0001") < 5


def test_report_generator_lands_in_accept():
    scored = get_scored_state()
    assert scored["scores"]["F-0002"]["total"] == 39
    assert scored["scores"]["F-0002"]["status"] == "accept"
