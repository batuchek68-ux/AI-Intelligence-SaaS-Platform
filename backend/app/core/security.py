import jwt
from datetime import datetime, timedelta

def create_token(data):
    payload = {
        "data": data,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }

    return jwt.encode(payload, "SECRET", algorithm="HS256")
