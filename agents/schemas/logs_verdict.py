from pydantic import BaseModel, Field


class LogsVerdict(BaseModel):
    finding_id: str
    explanation: str = Field(
        description="Two sentences on whether an attack through this flaw would be spotted, "
        "and which missing logs would hide it"
    )
    logs_to_add: list[str] = Field(description="Log sources to turn on, most useful first")
