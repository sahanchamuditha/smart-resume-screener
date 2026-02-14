from pydantic import BaseModel
from typing import List

#postgre part
from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Resume(BaseModel):
    name: str | None
    skills: List[str] = []
    experience_years: int | None

#postgre part
class ResumeDB(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    skills = Column(Text)