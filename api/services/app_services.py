import asyncio
from dataclasses import dataclass, field

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.graph.state import CompiledStateGraph

from agents.context.app_context import AppContext
from api.runs.run_events import RunEvents


@dataclass
class AppServices:
    graph: CompiledStateGraph
    checkpointer: BaseCheckpointSaver
    context: AppContext
    run_events: RunEvents = field(default_factory=RunEvents)
    running_tasks: set[asyncio.Task] = field(default_factory=set)
