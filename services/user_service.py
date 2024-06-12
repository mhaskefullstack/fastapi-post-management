from sqlalchemy.orm import Session
# from models.user_schema import User, Post
from database import get_db,engine,SessionLocal,Base,User,Post

class UserService:
    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db: Session, email: str, password: str):
        user = User(email=email, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.id

