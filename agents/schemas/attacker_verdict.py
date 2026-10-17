from pydantic import BaseModel, Field


class AttackerVerdict(BaseModel):
    technique_ids: list[str] = Field(
        description="MITRE ATT&CK technique ids this flaw enables, such as T1190, "
        "including any the scanner did not link"
    )
    explanation: str = Field(
        description="Two sentences on which attack methods the flaw opens and who uses them"
    )
