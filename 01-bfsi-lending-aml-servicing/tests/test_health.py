from fastapi.testclient import TestClient
from backend.app.main import app
client=TestClient(app)

def test_health():
    r=client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_ready():
    assert client.get("/ready").status_code == 200

def test_metrics():
    r=client.get("/metrics")
    assert r.status_code == 200
    assert "brownfield_http_requests_total" in r.text

def test_summary_counts_are_positive():
    r=client.get("/api/lending/summary")
    assert r.status_code == 200
    assert all(v > 0 for v in r.json().values())
