from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from services.user_service import UserService
from models.user_schema import UserCreate, UserLogin, Token
from services.token import generate_token

user_service = UserService()

class UserController:
    def signup(self, user: UserCreate, db: Session):
        """
        Registers a new user and returns an access token.
        """
        db_user = user_service.get_user_by_email(db, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        user_id = user_service.create_user(db, user.email, user.password)
        return {"access_token": generate_token(user.email), "token_type": "bearer"}

    def login(self, user: UserLogin, db: Session):
        db_user = user_service.get_user_by_email(db, user.email)
        if not db_user or db_user.password != user.password:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return {"access_token": generate_token(user.email), "token_type": "bearer"}

    # def generate_token(self, email: str):
    #     access_token_expires = timedelta(minutes=30)
    #     to_encode = {"sub": email, "exp": datetime.utcnow() + access_token_expires}
    #     return jwt.encode(to_encode, "secret_key", algorithm="HS256")

    # def add_post(self, post: PostCreate, token: str, db: Session):
    #     email = self.decode_token(token)
    #     if not email:
    #         raise HTTPException(status_code=401, detail="Invalid token")
    #     return user_service.create_post(db, post.text)

    # def decode_token(self, token: str):
    #     try:
    #         payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
    #         return payload["sub"]
    #     except jwt.ExpiredSignatureError:
    #         return None
    #     except jwt.InvalidTokenError:
    #         return None

    def delete_post(self, post_id: int, token: str, db: Session):
        email = self.decode_token(token)
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        if not user_service.get_post_by_id(db, post_id):
            raise HTTPException(status_code=404, detail="Post not found")
        user_service.delete_post(db, post_id)
        return {"message": "Post deleted successfully"}
