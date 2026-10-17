from typing import Any

from agents.context.app_context import AppContext
from agents.state.tool_result import ToolResult
from agents.tools.read_tool_output import read_tool_output


async def call_tool(context: AppContext, tool_name: str, arguments: dict[str, Any]) -> ToolResult:
    tool = next(tool for tool in context.tools if tool.name == tool_name)
    output = await tool.ainvoke(arguments)
    return read_tool_output(output)
