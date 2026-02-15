from fastapi import APIRouter, HTTPException
from app.services.job_storage import get_job
from app.services.ranking_service import rank_resumes_for_job

router = APIRouter(prefix="/rank", tags=["Ranking"])


@router.get("/job/{job_id}")
def rank_resumes(job_id: int):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    ranked_resumes = rank_resumes_for_job(job.description)
    return {
        "job_id": job_id,
        "job_title": job.title,
        "candidates": ranked_resumes
    }
