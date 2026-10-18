import os
from functools import cache

from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from cartograph_mcp.connection.make_graph_tools import make_graph_tools


@cache
def make_graph_runtime() -> Runtime[AppContext]:
    context = AppContext(
        model=None,
        tools=make_graph_tools(),
        graph_name=os.environ.get("FALKORDB_GRAPH", "cartograph"),
    )
    return Runtime(context=context)
