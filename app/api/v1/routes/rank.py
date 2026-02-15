from fastapi import APIRouter, HTTPException
from fastapi import Depends
from app.services.job_storage import get_job
from app.services.ranking_service import rank_resumes_for_job
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/rank", tags=["Ranking"])


@router.get("/job/{job_id}")
def rank_resumes(job_id: int, user: str = Depends(get_current_user)):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    ranked_resumes = rank_resumes_for_job(job.description)
    return {
        "job_id": job_id,
        "job_title": job.title,
        "candidates": ranked_resumes
    }
