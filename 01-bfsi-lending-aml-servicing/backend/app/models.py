from pydantic import BaseModel, Field

class CaseNote(BaseModel):
    entity_id: str = Field(min_length=1, max_length=80)
    note: str = Field(min_length=1, max_length=2000)
    source: str = "manual"
