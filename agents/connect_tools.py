from langchain_core.tools import BaseTool

from agents.fakes.make_fake_tools import make_fake_tools


async def connect_tools() -> list[BaseTool]:
    return make_fake_tools()
