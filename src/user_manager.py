"""
User management module.
BUG #1: get_user returns wrong key (uses 'username' instead of 'name')
BUG #2: update_email does NOT validate if email contains '@'
BUG #3: delete_user removes from list by value but list stores dicts → always fails silently
"""

users_db = []


def create_user(user_id: int, name: str, email: str) -> dict:
    user = {"id": user_id, "name": name, "email": email, "active": True}
    users_db.append(user)
    return user


def get_user(user_id: int) -> dict | None:
    for user in users_db:
        if user["id"] == user_id:
            # BUG: returns wrong key name — should be user["name"] not user["username"]
            return {"id": user["id"], "username": user["name"], "email": user["email"]}
    return None


def update_email(user_id: int, new_email: str) -> bool:
    # BUG: No validation — accepts emails without '@' symbol
    for user in users_db:
        if user["id"] == user_id:
            user["email"] = new_email
            return True
    return False


def delete_user(user_id: int) -> bool:
    for user in users_db:
        if user["id"] == user_id:
            # BUG: list.remove(user) works on dicts but will raise ValueError
            # if the same dict object is not found. Should use users_db.remove(user)
            # Actually this works but the real bug is we should use pop() with index
            users_db.remove(user)
            return True
    return False


def list_active_users() -> list:
    return [u for u in users_db if u["active"]]


def deactivate_user(user_id: int) -> bool:
    for user in users_db:
        if user["id"] == user_id:
            user["active"] = False
            return True
    return False
