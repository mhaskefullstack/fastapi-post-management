from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from services.post_service import PostService
from models.post_scehema import Post,PostCreate
from services.token import generate_token,decode_token

post_service = PostService()

class PostController:
    
    def add_post(self, post: PostCreate, token: str, db: Session):
        email = decode_token(token)
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        return post_service.create_post(db, post.text)
    
    def delete_post(self, post_id: int, token: str, db: Session):
        email = decode_token(token)
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        if not post_service.get_post_by_id(db, post_id):
            raise HTTPException(status_code=404, detail="Post not found")
        post_service.delete_post(db, post_id)
        return {"message": "Post deleted successfully"}
    
    def get_posts(self, db: Session) -> list[Post]:
        return post_service.get_posts(db)