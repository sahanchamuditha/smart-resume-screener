from pydantic import BaseModel
from typing import List

class Resume(BaseModel):
    name: str | None
    skills: List[str] = []
    experience_years: int | None
