import os

from dotenv import load_dotenv
from falkordb import FalkorDB

load_dotenv()


def get_database():
    return FalkorDB(
        host=os.environ["FALKORDB_HOST"],
        port=int(os.environ["FALKORDB_PORT"]),
        username=os.environ.get("FALKORDB_USERNAME", "falkordb"),
        password=os.environ["FALKORDB_PASSWORD"],
    )

