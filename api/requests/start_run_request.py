from pydantic import BaseModel


class StartRunRequest(BaseModel):
    scan_id: str
