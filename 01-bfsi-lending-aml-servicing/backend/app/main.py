from fastapi import FastAPI, Depends, HTTPException, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import json, time
from .security import current_user, weak_admin_check
from .data_access import read_entity, ALLOWED_ENTITIES

app = FastAPI(title='BFSI — Digital Lending, AML & Loan Servicing', version="0.9.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["X-User", "Content-Type"],
)

REQS = Counter("brownfield_http_requests_total", "Requests", ["route"])
LAT = Histogram("brownfield_request_latency_seconds", "Latency", ["route"])

@app.middleware("http")
async def timing(request, call_next):
    start=time.perf_counter()
    response=await call_next(request)
    route=request.url.path.split("/")[1] if request.url.path != "/" else "root"
    REQS.labels(route=route).inc()
    LAT.labels(route=route).observe(time.perf_counter()-start)
    return response

@app.get("/health")
def health():
    return {"status":"ok","service":'lending'}

@app.get("/ready")
def ready():
    try:
        read_entity('customers')[:1]
        return {"status":"ready"}
    except Exception as exc:
        raise HTTPException(503, f"not ready: {exc}")

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/api/lending/summary")
def summary():
    return {name: len(read_entity(name)) for name in ALLOWED_ENTITIES}

@app.get("/api/lending/records/{entity}")
def records(entity: str, limit: int = Query(100, ge=1, le=5000), user=Depends(current_user)):
    if entity not in ALLOWED_ENTITIES:
        raise HTTPException(404, "unknown entity")
    return read_entity(entity)[:limit]

@app.get("/api/lending/search")
def search(q: str = Query(min_length=2, max_length=120), user=Depends(current_user)):
    # Brownfield search still performs substring scans and should be assessed for scale/privacy.
    q=q.lower(); out=[]
    for name in ALLOWED_ENTITIES:
        for row in read_entity(name):
            if q in json.dumps(row, ensure_ascii=False).lower():
                out.append({"entity":name,"record":row})
                if len(out) >= 200:
                    return out
    return out

@app.get("/api/lending/admin/export")
def admin_export(user=Depends(current_user)):
    # Characterized legacy behavior: name-based admin shortcut remains a deliberate transformation target.
    if not weak_admin_check(user):
        raise HTTPException(403, "admin required")
    return {name: read_entity(name)[:1000] for name in ALLOWED_ENTITIES}
