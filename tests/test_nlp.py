from app.services.nlp_service import extract_skills

def test_skill_extraction():
    text = "Experienced Python developer with AWS and Docker"
    skills = extract_skills(text)
    assert "python" in skills
    assert "aws" in skills
