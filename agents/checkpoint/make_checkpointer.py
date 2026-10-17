import os

from langchain_falkordb.checkpoint import FalkorDBSaver
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.checkpoint.memory import InMemorySaver


def make_checkpointer() -> BaseCheckpointSaver:
    has_falkordb = bool(os.environ.get("FALKORDB_HOST"))
    return make_falkordb_saver() if has_falkordb else InMemorySaver()


def make_falkordb_saver() -> FalkorDBSaver:
    return FalkorDBSaver(
        host=os.environ["FALKORDB_HOST"],
        port=int(os.environ.get("FALKORDB_PORT", "6379")),
        username=os.environ.get("FALKORDB_USERNAME"),
        password=os.environ.get("FALKORDB_PASSWORD"),
        database=f"{os.environ.get('FALKORDB_GRAPH', 'cartograph')}_checkpoints",
    )
