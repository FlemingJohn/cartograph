from typing import Any, TypedDict


class CheckerVerdict(TypedDict):
    finding_id: str
    agent: str
    answer: dict[str, Any]
