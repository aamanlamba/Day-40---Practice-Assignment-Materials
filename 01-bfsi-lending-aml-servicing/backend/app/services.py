from decimal import Decimal

# Two competing calculation paths are intentionally retained.
def normalized_amount(value):
    try:
        return round(float(value), 2)
    except Exception:
        return 0.0

def normalized_amount_v2(value):
    try:
        return Decimal(str(value)).quantize(Decimal("0.01"))
    except Exception:
        return Decimal("0.00")
