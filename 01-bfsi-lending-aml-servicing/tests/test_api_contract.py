from fastapi.testclient import TestClient
from backend.app.main import app
client=TestClient(app)

def test_unknown_entity_is_404():
    r=client.get("/api/lending/records/unknown", headers={"X-User":"analyst1"})
    assert r.status_code == 404

def test_limit_validation():
    r=client.get("/api/lending/records/customers?limit=0", headers={"X-User":"analyst1"})
    assert r.status_code == 422

def test_search_requires_nontrivial_query():
    r=client.get("/api/lending/search?q=a", headers={"X-User":"analyst1"})
    assert r.status_code == 422
