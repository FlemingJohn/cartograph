from typing import TypedDict

from agents.state.finding import Finding
from agents.state.tool_result import ToolResult


class Measurement(TypedDict):
    finding: Finding
    attack_paths: ToolResult
    blast_radius: ToolResult
    actors_for: ToolResult
    detection_gap: list[ToolResult]
