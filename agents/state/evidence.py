from typing import TypedDict


class Evidence(TypedDict):
    id: str
    finding_id: str
    agent: str
    tool: str
    cypher: str
    path: list[str]
    claim: str
