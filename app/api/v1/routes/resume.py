from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import parse_resume

router = APIRouter(prefix="/resume", tags=["Resume"])

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    parsed_data = parse_resume(content)
    return parsed_data
