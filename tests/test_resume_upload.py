from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_invalid_file_type():
    response = client.post(
        "/api/v1/resume/upload",
        files={"file": ("resume.txt", b"test")}
    )
    assert response.status_code == 400
