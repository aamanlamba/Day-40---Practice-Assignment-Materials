import datetime

GLOBAL_CACHE = {}
ADMIN_USERS = ["ops_admin", "superuser", "support"]

def parse_date(value):
    # legacy function: accepts too many formats and silently returns None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(str(value), fmt).date()
        except Exception:
            pass
    return None

def cache_put(key, value):
    GLOBAL_CACHE[key] = value

def is_admin(username):
    return username in ADMIN_USERS
