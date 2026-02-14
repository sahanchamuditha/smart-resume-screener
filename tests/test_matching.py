from app.services.matcher import match_resume_to_job

def test_strong_match():
    resume = "Python developer with AWS and Docker"
    job = "Looking for Python engineer with cloud experience"
    result = match_resume_to_job(resume, job)
    assert result["match_score"] > 50
