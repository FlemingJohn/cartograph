import asyncio

from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.evidence.make_evidence import make_evidence
from agents.prompts.make_attacker_checker_prompt import make_attacker_checker_prompt
from agents.schemas.attacker_verdicts import AttackerVerdicts
from agents.state.checker_input import CheckerInput
from agents.tools.call_tool import call_tool
from agents.verdicts.make_checker_verdict import make_checker_verdict
from agents.verdicts.pair_verdicts import pair_verdicts

AGENT = "check_attackers"


async def check_attackers(state: CheckerInput, runtime: Runtime[AppContext]) -> dict:
    model = runtime.context.model.with_structured_output(AttackerVerdicts)
    answer = await model.ainvoke(make_attacker_checker_prompt(state["measurements"]))
    verdicts = [verdict for _, verdict in pair_verdicts(state["measurements"], answer.verdicts)]
    actor_answers = await asyncio.gather(
        *[
            call_tool(runtime.context, "actors_for", {"technique_ids": verdict.technique_ids})
            for verdict in verdicts
        ]
    )
    pairs = list(zip(verdicts, actor_answers))
    return {
        "verdicts": [
            make_checker_verdict(AGENT, verdict, actor_count=actors["result"]["actor_count"])
            for verdict, actors in pairs
        ],
        "evidence": [
            make_evidence(verdict.finding_id, AGENT, "actors_for", actors, verdict.explanation)
            for verdict, actors in pairs
        ],
    }
