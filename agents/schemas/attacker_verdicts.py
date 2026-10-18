from pydantic import BaseModel

from agents.schemas.attacker_verdict import AttackerVerdict


class AttackerVerdicts(BaseModel):
    verdicts: list[AttackerVerdict]
