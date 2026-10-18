from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.checkpoint.make_checkpointer import make_checkpointer
from agents.context.make_app_context import make_app_context
from agents.make_triage_graph import make_triage_graph
from api.routes import (
    add_link,
    approve_run,
    get_findings,
    get_route,
    remove_link,
    start_run,
    stream_run,
)
from api.services.app_services import AppServices

DASHBOARD_URLS = ["http://localhost:5180", "http://127.0.0.1:5180"]
ROUTES = [start_run, stream_run, approve_run, get_findings, get_route, add_link, remove_link]


def make_app() -> FastAPI:
    app = FastAPI(title="CartoGraph", lifespan=start_services)
    app.add_middleware(
        CORSMiddleware, allow_origins=DASHBOARD_URLS, allow_methods=["*"], allow_headers=["*"]
    )
    for route in ROUTES:
        app.include_router(route.router)
    return app


@asynccontextmanager
async def start_services(app: FastAPI):
    async with make_app_context() as context:
        checkpointer = make_checkpointer()
        graph = make_triage_graph(checkpointer)
        app.state.services = AppServices(graph=graph, checkpointer=checkpointer, context=context)
        yield


app = make_app()
