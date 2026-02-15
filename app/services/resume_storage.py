from app.core.database import SessionLocal
from app.models.resume import ResumeDB

def save_resume(filename: str, text: str, skills: list[str]):
    db = SessionLocal()
    resume = ResumeDB(
        filename=filename,
        text=text,
        skills=", ".join(skills)
    )
    db.add(resume)
    db.commit()
    db.refresh(resume)
    db.close()
    return resume.id

def get_all_resumes():
    db = SessionLocal()
    resumes = db.query(ResumeDB).all()
    db.close()
    return resumes