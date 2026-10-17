from pydantic import BaseModel

from agents.schemas.action_plan import ActionPlan


class ActionPlans(BaseModel):
    plans: list[ActionPlan]
