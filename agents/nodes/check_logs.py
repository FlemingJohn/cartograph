from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.evidence.make_evidence import make_evidence
from agents.prompts.make_logs_checker_prompt import make_logs_checker_prompt
from agents.schemas.logs_verdicts import LogsVerdicts
from agents.state.checker_input import CheckerInput
from agents.verdicts.make_checker_verdict import make_checker_verdict
from agents.verdicts.pair_verdicts import pair_verdicts

AGENT = "check_logs"


async def check_logs(state: CheckerInput, runtime: Runtime[AppContext]) -> dict:
    model = runtime.context.model.with_structured_output(LogsVerdicts)
    answer = await model.ainvoke(make_logs_checker_prompt(state["measurements"]))
    pairs = pair_verdicts(state["measurements"], answer.verdicts)
    return {
        "verdicts": [make_checker_verdict(AGENT, verdict) for _, verdict in pairs],
        "evidence": [
            make_evidence(verdict.finding_id, AGENT, "detection_gap", gap, verdict.explanation)
            for measurement, verdict in pairs
            for gap in measurement["detection_gap"][:1]
        ],
    }
