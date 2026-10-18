from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.evidence.make_evidence import make_evidence
from agents.prompts.make_route_checker_prompt import make_route_checker_prompt
from agents.schemas.route_verdicts import RouteVerdicts
from agents.state.checker_input import CheckerInput
from agents.verdicts.make_checker_verdict import make_checker_verdict
from agents.verdicts.pair_verdicts import pair_verdicts

AGENT = "check_routes"
TOOLS = ["attack_paths", "blast_radius"]


async def check_routes(state: CheckerInput, runtime: Runtime[AppContext]) -> dict:
    model = runtime.context.model.with_structured_output(RouteVerdicts)
    answer = await model.ainvoke(make_route_checker_prompt(state["measurements"]))
    pairs = pair_verdicts(state["measurements"], answer.verdicts)
    return {
        "verdicts": [make_checker_verdict(AGENT, verdict) for _, verdict in pairs],
        "evidence": [
            make_evidence(verdict.finding_id, AGENT, tool, measurement[tool], verdict.explanation)
            for measurement, verdict in pairs
            for tool in TOOLS
        ],
    }
