from pydantic import BaseModel


class ApproveRunRequest(BaseModel):
    is_approved: bool
