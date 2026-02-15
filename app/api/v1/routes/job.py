from fastapi import APIRouter
from pydantic import BaseModel
from app.services.job_storage import save_job

router = APIRouter(prefix="/job", tags=["Job"])


class JobCreate(BaseModel):
    title: str
    description: str


@router.post("/")
def create_job(job: JobCreate):
    job_id = save_job(job.title, job.description)
    return {"job_id": job_id}
