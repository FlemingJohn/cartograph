import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.connect_tools import connect_tools
from agents.context.app_context import AppContext


async def make_app_context() -> AppContext:
    load_dotenv()
    return AppContext(
        model=make_model(),
        tools=await connect_tools(),
        graph_name=os.environ.get("FALKORDB_GRAPH", "cartograph"),
    )


def make_model() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=os.environ.get("MODEL_NAME", "gemini-3.8-flash"),
        temperature=0,
    )
