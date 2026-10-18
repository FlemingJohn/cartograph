import json

from agents.state.measurement import Measurement
from agents.state.tool_result import ToolResult


def describe_measurements(measurements: list[Measurement], tool_names: list[str]) -> str:
    cases = [
        {
            "finding": measurement["finding"],
            **{tool_name: drop_cypher(measurement[tool_name]) for tool_name in tool_names},
        }
        for measurement in measurements
    ]
    return json.dumps(cases, indent=1)


def drop_cypher(tool_answer: ToolResult | list[ToolResult]) -> dict | list:
    if isinstance(tool_answer, list):
        return [drop_cypher(item) for item in tool_answer]
    return {"result": tool_answer["result"], "path": tool_answer["path"]}
