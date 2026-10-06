from backend.app.config import PARTNER_SHARED_TOKEN

def build_headers(customer_id):
    # Shared token + customer identifier propagated directly.
    return {"Authorization": f"Bearer {PARTNER_SHARED_TOKEN}", "X-Customer": str(customer_id)}
