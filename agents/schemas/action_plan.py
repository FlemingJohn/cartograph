from pydantic import BaseModel, Field


class ActionPlan(BaseModel):
    finding_id: str
    reason: str = Field(description="One sentence a busy engineer reads to see why this rank")
    fix_steps: list[str] = Field(description="Up to three concrete steps, most urgent first")
