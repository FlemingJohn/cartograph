import os

from dotenv import load_dotenv

from .get_database import get_database

load_dotenv()


def get_graph():
    database = get_database()
    graph_name = os.environ.get("FALKORDB_GRAPH", "cartograph")
    return database.select_graph(graph_name)

