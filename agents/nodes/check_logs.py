from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.evidence.make_evidence import make_evidence
from agents.prompts.make_logs_checker_prompt import make_logs_checker_prompt
from agents.schemas.logs_verdict import LogsVerdict
from agents.state.checker_input import CheckerInput

AGENT = "check_logs"


async def check_logs(state: CheckerInput, runtime: Runtime[AppContext]) -> dict:
    measurement = state["measurement"]
    finding_id = measurement["finding"]["finding_id"]
    model = runtime.context.model.with_structured_output(LogsVerdict)
    verdict = await model.ainvoke(make_logs_checker_prompt(measurement))
    return {
        "verdicts": [{"finding_id": finding_id, "agent": AGENT, "answer": verdict.model_dump()}],
        "evidence": [
            make_evidence(finding_id, AGENT, "detection_gap", gap, verdict.explanation)
            for gap in measurement["detection_gap"][:1]
        ],
    }
