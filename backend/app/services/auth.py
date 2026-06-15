import jwt
from datetime import datetime, timedelta

SECRET = "supersecret"

def create_token(user_id: int):

    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=1)
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")
