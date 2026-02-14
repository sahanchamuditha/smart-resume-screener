from app.services.embedding_service import calculate_similarity


def match_resume_to_job(resume_text: str, job_description: str):
    similarity = calculate_similarity(resume_text, job_description)

    score_percentage = round(similarity * 100, 2)

    if score_percentage >= 75:
        verdict = "Strong Match"
    elif score_percentage >= 50:
        verdict = "Good Match"
    else:
        verdict = "Weak Match"

    return {
        "match_score": score_percentage,
        "verdict": verdict
    }
