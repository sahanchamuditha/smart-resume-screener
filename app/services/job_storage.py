from app.core.database import SessionLocal
from app.models.job import JobDB


def save_job(title: str, description: str):
    db = SessionLocal()
    job = JobDB(title=title, description=description)
    db.add(job)
    db.commit()
    db.refresh(job)
    db.close()
    return job.id


def get_job(job_id: int):
    db = SessionLocal()
    job = db.query(JobDB).filter(JobDB.id == job_id).first()
    db.close()
    return job
