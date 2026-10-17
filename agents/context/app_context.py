from dataclasses import dataclass

from langchain_core.language_models import BaseChatModel
from langchain_core.tools import BaseTool


@dataclass
class AppContext:
    model: BaseChatModel
    tools: list[BaseTool]
    graph_name: str
