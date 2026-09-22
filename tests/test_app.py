from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health(): assert client.get("/health").status_code == 200

def test_grounded_query():
    r = client.post("/ask", json={"question":"Gold specialist copay"})
    assert r.status_code == 200
    assert "50" in r.json()["answer"]

def test_redaction():
    r = client.post("/ask", json={"question":"My email is test@example.com what is the Gold deductible?"})
    assert r.json()["audit"]["pii_redacted"] is True
