from pydantic import BaseModel


class LinkRequest(BaseModel):
    source_id: str = "web-gateway"
    target_id: str = "report-generator"
