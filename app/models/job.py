from sqlalchemy import Column, Integer, Text, String
from app.core.database import Base

class JobDB(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
