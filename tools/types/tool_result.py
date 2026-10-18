from dataclasses import dataclass
from typing import Any, List


@dataclass
class ToolResult:
    result: Any
    cypher: str
    path: List[str]

    def to_dict(self):
        return {
            "result": self.result,
            "cypher": self.cypher,
            "path": self.path,
        }

