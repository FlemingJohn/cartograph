from typing import Any

from pydantic import BaseModel

from agents.state.checker_verdict import CheckerVerdict


def make_checker_verdict(agent: str, verdict: BaseModel, **extra: Any) -> CheckerVerdict:
    answer = {**verdict.model_dump(exclude={"finding_id"}), **extra}
    return {"finding_id": verdict.finding_id, "agent": agent, "answer": answer}
