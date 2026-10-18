from dotenv import load_dotenv

from cartograph_mcp.make_server import make_server

if __name__ == "__main__":
    load_dotenv()
    make_server().run(transport="stdio")
