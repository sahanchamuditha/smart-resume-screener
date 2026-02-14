from app.services.nlp_service import extract_skills, extract_experience_sentences
from app.services.resume_storage import save_resume
from io import BytesIO
import pdfplumber
from docx import Document


def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with pdfplumber.open(BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def extract_text_from_docx(file_bytes: bytes) -> str:
    document = Document(BytesIO(file_bytes))
    return "\n".join(p.text for p in document.paragraphs).strip()


def parse_resume(file_bytes: bytes, filename: str):
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_bytes)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file type")

    skills = extract_skills(text)
    experience = extract_experience_sentences(text)

    resume_id = save_resume(filename, text, skills)

    return {
        "resume_id": resume_id,
        "skills": skills,
        "experience_sentences": experience[:5]
    }
