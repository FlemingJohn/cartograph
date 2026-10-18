import asyncio
import json
from collections.abc import Awaitable, Callable
from typing import Any

from agents.context.app_context import AppContext
from agents.state.tool_result import ToolResult
from agents.tools.call_tool import call_tool

CachedToolCaller = Callable[[str, dict[str, Any]], Awaitable[ToolResult]]


def make_cached_tool_caller(context: AppContext) -> CachedToolCaller:
    answers_by_question: dict[str, asyncio.Future] = {}

    def call_once(tool_name: str, arguments: dict[str, Any]) -> Awaitable[ToolResult]:
        question = json.dumps([tool_name, arguments], sort_keys=True)
        if question not in answers_by_question:
            answers_by_question[question] = asyncio.ensure_future(
                call_tool(context, tool_name, arguments)
            )
        return answers_by_question[question]

    return call_once
