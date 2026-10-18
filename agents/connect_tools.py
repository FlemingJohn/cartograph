import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from langchain_core.tools import BaseTool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

from agents.tools.list_findings import list_findings

PROJECT_FOLDER = Path(__file__).resolve().parents[1]
CONTRACT_NAME_BY_SERVER_NAME = {
    "check_attack_paths": "attack_paths",
    "check_blast_radius": "blast_radius",
    "check_chokepoints": "chokepoints",
    "check_actors_for": "actors_for",
    "check_detection_gap": "detection_gap",
    "save_decision": "record_decision",
}


@asynccontextmanager
async def connect_tools() -> AsyncIterator[list[BaseTool]]:
    client = MultiServerMCPClient({"cartograph": make_server_connection()})
    async with client.session("cartograph") as session:
        server_tools = await load_mcp_tools(session)
        yield [*[use_contract_name(tool) for tool in server_tools], list_findings]


def make_server_connection() -> dict:
    return {
        "transport": "stdio",
        "command": sys.executable,
        "args": ["-m", "tools.make_server"],
        "cwd": str(PROJECT_FOLDER),
    }


def use_contract_name(tool: BaseTool) -> BaseTool:
    contract_name = CONTRACT_NAME_BY_SERVER_NAME.get(tool.name, tool.name)
    return tool.model_copy(update={"name": contract_name})
