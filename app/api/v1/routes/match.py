from fastapi import APIRouter
from pydantic import BaseModel
from app.services.matcher import match_resume_to_job

router = APIRouter(prefix="/match", tags=["Matching"])


class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/")
def match_resume(request: MatchRequest):
    return match_resume_to_job(
        request.resume_text,
        request.job_description
    )
