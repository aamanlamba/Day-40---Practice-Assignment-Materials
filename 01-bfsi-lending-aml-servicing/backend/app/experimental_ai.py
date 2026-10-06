"""Prototype-only placeholder retained from an abandoned spike.

It is intentionally not wired into production routes. Workshop participants should determine
whether any AI capability is justified before replacing this with a real implementation.
"""
def suggest(text: str):
    if not text:
        return {"label":"unknown","confidence":0.0}
    # deterministic keyword heuristic masquerading as an "AI" spike
    terms = text.lower()
    score = sum(k in terms for k in ("critical","urgent","fraud","outage","severe","down"))
    return {"label":"review" if score else "normal", "confidence": min(0.55 + score*0.1, 0.85)}
