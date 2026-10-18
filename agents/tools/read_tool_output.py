import json
from typing import Any

from agents.state.tool_result import ToolResult


def read_tool_output(output: Any) -> ToolResult:
    is_already_read = isinstance(output, dict)
    return output if is_already_read else read_text_output(get_text(output))


def read_text_output(text: str) -> ToolResult:
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise RuntimeError(text) from error


def get_text(output: str | list) -> str:
    is_text = isinstance(output, str)
    return output if is_text else "".join(block["text"] for block in output if "text" in block)
