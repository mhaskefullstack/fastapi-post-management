from sqlalchemy.orm import Session
from database import get_db,engine,SessionLocal,Base,Post

class PostService:
   
    def create_post(self, db: Session, text: str):
        post = Post(text=text)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post.id

    def get_post_by_id(self, db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()

    def delete_post(self, db: Session, post_id: int):
        post = self.get_post_by_id(db, post_id)
        db.delete(post)
        db.commit()
    def get_posts(self, db: Session) -> list[Post]:
        return db.query(Post).all()