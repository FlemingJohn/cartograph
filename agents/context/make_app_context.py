import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import truststore
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.connect_tools import connect_tools
from agents.context.app_context import AppContext


@asynccontextmanager
async def make_app_context() -> AsyncIterator[AppContext]:
    load_dotenv()
    truststore.inject_into_ssl()
    async with connect_tools() as tools:
        yield AppContext(
            model=make_model(),
            tools=tools,
            graph_name=os.environ.get("FALKORDB_GRAPH", "cartograph"),
        )


def make_model() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=os.environ.get("MODEL_NAME", "gemini-3.8-flash"),
        temperature=0,
    )
