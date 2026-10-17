from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.evidence.make_evidence import make_evidence
from agents.prompts.make_attacker_checker_prompt import make_attacker_checker_prompt
from agents.schemas.attacker_verdict import AttackerVerdict
from agents.state.checker_input import CheckerInput
from agents.tools.call_tool import call_tool

AGENT = "check_attackers"


async def check_attackers(state: CheckerInput, runtime: Runtime[AppContext]) -> dict:
    measurement = state["measurement"]
    finding_id = measurement["finding"]["finding_id"]
    model = runtime.context.model.with_structured_output(AttackerVerdict)
    verdict = await model.ainvoke(make_attacker_checker_prompt(measurement))
    actors = await call_tool(
        runtime.context, "actors_for", {"technique_ids": verdict.technique_ids}
    )
    answer = {**verdict.model_dump(), "actor_count": actors["result"]["actor_count"]}
    return {
        "verdicts": [{"finding_id": finding_id, "agent": AGENT, "answer": answer}],
        "evidence": [make_evidence(finding_id, AGENT, "actors_for", actors, verdict.explanation)],
    }
