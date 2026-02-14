from app.services.resume_storage import save_resume

def test_save_resume():
    resume_id = save_resume(
        "test.pdf",
        "Python developer",
        ["python"]
    )
    assert resume_id is not None
