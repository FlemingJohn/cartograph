from typing import Any, TypedDict


class ToolResult(TypedDict):
    result: Any
    cypher: str
    path: list[str]
