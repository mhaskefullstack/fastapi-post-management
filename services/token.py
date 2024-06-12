import jwt
from datetime import datetime, timedelta

from fastapi import HTTPException

#Function to generate token
def generate_token(email: str):
    access_token_expires = timedelta(minutes=30)
    to_encode = {"sub": email, "exp": datetime.utcnow() + access_token_expires}
    return jwt.encode(to_encode, "secret_key", algorithm="HS256")

#Function to decode token
def decode_token(token: str):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

#Function to get token from header
def get_token(authorization: str):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")
    token = authorization.split()[1]
    return token