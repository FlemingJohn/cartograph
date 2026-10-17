import json
from typing import Any

from agents.state.tool_result import ToolResult


def read_tool_output(output: Any) -> ToolResult:
    is_already_read = isinstance(output, dict)
    return output if is_already_read else json.loads(get_text(output))


def get_text(output: str | list) -> str:
    is_text = isinstance(output, str)
    return output if is_text else "".join(block["text"] for block in output if "text" in block)
