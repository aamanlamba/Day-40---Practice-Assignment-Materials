from fastapi.testclient import TestClient
from backend.app.main import app
client=TestClient(app)

def test_records_requires_user_header():
    assert client.get("/api/lending/records/customers").status_code == 401

def test_existing_header_access_characterization():
    # Existing behavior captured for safe refactoring; it is not a security endorsement.
    r=client.get("/api/lending/records/customers", headers={"X-User":"analyst1"})
    assert r.status_code == 200

def test_admin_name_shortcut_characterization():
    # Deliberately records the inherited behavior so a later secure redesign can prove change.
    r=client.get("/api/lending/admin/export", headers={"X-User":"ops_admin"})
    assert r.status_code == 200
