from pydantic import BaseModel

from agents.schemas.logs_verdict import LogsVerdict


class LogsVerdicts(BaseModel):
    verdicts: list[LogsVerdict]
