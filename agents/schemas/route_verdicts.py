from pydantic import BaseModel

from agents.schemas.route_verdict import RouteVerdict


class RouteVerdicts(BaseModel):
    verdicts: list[RouteVerdict]
