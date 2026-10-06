from pathlib import Path
from fastapi.testclient import TestClient
from backend.app.main import app
ROOT=Path(__file__).resolve().parents[1]
client=TestClient(app)

def test_baseline_metrics_present():
    p=ROOT/'data'/'baseline_metrics.csv'
    assert p.exists() and p.stat().st_size > 1000

def test_local_frontend_cors_preflight():
    r=client.options('/api/lending/search',headers={'Origin':'http://127.0.0.1:4200','Access-Control-Request-Method':'GET','Access-Control-Request-Headers':'X-User'})
    assert r.status_code == 200
    assert r.headers.get('access-control-allow-origin') == 'http://127.0.0.1:4200'
