# BFSI — Digital Lending, AML & Loan Servicing

## AI FDE Brownfield Transformation Candidate

This is a self-contained workshop repository representing an inherited enterprise system. It is deliberately **runnable but imperfect**: multiple generations of engineering patterns, partial migrations, inconsistent business rules, data-quality variation, incomplete testing, security/authorization debt, legacy interfaces and operational assumptions coexist in the same estate.

The repository does **not** contain a solution pack or facilitator answer key. Participants should discover evidence through the AI FDE production-delivery spine.

## What is included

- FastAPI backend with OpenAPI docs, health/readiness and partial metrics
- Angular 17-style client scaffold with mixed-generation patterns
- Python ETL/batch jobs
- PostgreSQL-oriented SQL plus local SQLite bootstrap
- Legacy/partner adapters
- pytest characterization, API-contract and data smoke tests
- Prometheus/Grafana starter assets
- diverse synthetic domain data including intentional anomalies/edge cases
- inherited legacy notes and a business change request

## Local setup

Requires Python 3.11+.

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/self_check.py
python -m pytest
python scripts/bootstrap_sqlite.py
python -m uvicorn backend.app.main:app --reload
```

API docs: `http://127.0.0.1:8000/docs`

Frontend (optional if Node/npm is available):

```bash
cd frontend
npm install
npm start
```

## Workshop constraints

- Begin with discovery; do not jump directly to refactoring.
- Treat legacy behavior as evidence to characterize, not automatically as correct behavior.
- Do not expose or use real customer/company data; all bundled records are synthetic.
- Do not introduce AI or agent autonomy until Stage 8 qualifies it.
- Keep human-control and deterministic boundaries explicit for high-impact actions.
- No cloud account, Docker, Kubernetes or external service is required for baseline exercises.

See `WORKSHOP_SCENARIO.md` and `CHANGE_REQUEST.md`.
