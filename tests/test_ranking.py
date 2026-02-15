from app.services.ranking_service import rank_resumes_for_job

def test_ranking_returns_list():
    ranked = rank_resumes_for_job("Python developer with AWS")
    assert isinstance(ranked, list)
