import pdfplumber
from docx import Document
from io import BytesIO


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
    text = "\n".join([para.text for para in document.paragraphs])
    return text.strip()


def parse_resume(file_bytes: bytes, filename: str):
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_bytes)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file type")

    return {
        "filename": filename,
        "text_length": len(text),
        "extracted_text": text[:1000]  # preview only
    }
