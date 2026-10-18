from langchain_core.tools import BaseTool, StructuredTool

from agents.tools.list_findings import list_findings
from tools.handlers.actors_for import actors_for
from tools.handlers.attack_paths import attack_paths
from tools.handlers.blast_radius import blast_radius
from tools.handlers.chokepoints import chokepoints
from tools.handlers.detection_gap import detection_gap

GRAPH_HANDLERS = [attack_paths, blast_radius, chokepoints, actors_for, detection_gap]


def make_graph_tools() -> list[BaseTool]:
    handler_tools = [
        StructuredTool.from_function(
            func=handler, name=handler.__name__, description=handler.__name__
        )
        for handler in GRAPH_HANDLERS
    ]
    return [*handler_tools, list_findings]
