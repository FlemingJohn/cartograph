from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.evidence.make_evidence import make_evidence
from agents.prompts.make_route_checker_prompt import make_route_checker_prompt
from agents.schemas.route_verdict import RouteVerdict
from agents.state.checker_input import CheckerInput

AGENT = "check_routes"


async def check_routes(state: CheckerInput, runtime: Runtime[AppContext]) -> dict:
    measurement = state["measurement"]
    finding_id = measurement["finding"]["finding_id"]
    model = runtime.context.model.with_structured_output(RouteVerdict)
    verdict = await model.ainvoke(make_route_checker_prompt(measurement))
    return {
        "verdicts": [{"finding_id": finding_id, "agent": AGENT, "answer": verdict.model_dump()}],
        "evidence": [
            make_evidence(finding_id, AGENT, tool, measurement[tool], verdict.explanation)
            for tool in ["attack_paths", "blast_radius"]
        ],
    }
