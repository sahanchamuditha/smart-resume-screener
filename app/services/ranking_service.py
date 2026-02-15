from app.services.embedding_service import calculate_similarity
from app.services.resume_storage import get_all_resumes


def rank_resumes_for_job(job_description: str):
    resumes = get_all_resumes()
    ranked = []

    for resume in resumes:
        similarity = calculate_similarity(resume.text, job_description)
        score = round(similarity * 100, 2)

        ranked.append({
            "resume_id": resume.id,
            "filename": resume.filename,
            "skills": resume.skills.split(", "),
            "match_score": score
        })

    ranked.sort(key=lambda x: x["match_score"], reverse=True)
    return ranked
