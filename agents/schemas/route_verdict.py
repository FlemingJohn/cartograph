from pydantic import BaseModel, Field


class RouteVerdict(BaseModel):
    explanation: str = Field(
        description="Two sentences: how an attacker from the internet gets to this service, "
        "or why they cannot, and what data sits nearby"
    )
    is_exposed: bool = Field(description="True when the route and the nearby data make it urgent")
