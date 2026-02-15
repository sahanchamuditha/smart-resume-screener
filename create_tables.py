from app.core.database import engine
from app.models.resume import ResumeDB
from app.models.job import JobDB
from app.models.user import UserDB

ResumeDB.metadata.create_all(bind=engine)
JobDB.metadata.create_all(bind=engine)

print("Tables created successfully")
