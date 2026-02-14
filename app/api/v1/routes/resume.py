from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.resume_parser import parse_resume
from app.utils.file_handler import validate_file_type

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if not validate_file_type(file.filename):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported"
        )

    file_bytes = await file.read()
    parsed_data = parse_resume(file_bytes, file.filename)

    return parsed_data
