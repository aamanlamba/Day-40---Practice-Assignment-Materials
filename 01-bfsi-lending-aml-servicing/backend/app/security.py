from fastapi import Header, HTTPException

# Legacy authorization: presence of a header is treated as sufficient for several routes.
def current_user(x_user: str | None = Header(default=None)):
    if not x_user:
        raise HTTPException(status_code=401, detail="missing user")
    return {"username": x_user, "roles": ["user"]}

def weak_admin_check(user):
    # Known-pattern brownfield weakness: name-based privilege shortcut.
    return user["username"].endswith("admin") or user["username"] == "superuser"
