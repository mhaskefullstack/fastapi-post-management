from fastapi import FastAPI, HTTPException, Depends, Response,APIRouter
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Any
import jwt
from datetime import datetime, timedelta
from functools import lru_cache
from controllers.post_controller import PostController
from services.token import get_token
from database import get_db
from models.post_scehema import Post,PostCreate

from services.token import decode_token
from functools import lru_cache

post_controller = PostController()
router = APIRouter(tags=['Post'])



@router.post("/add_post", response_model=int)
async def add_post(post: PostCreate, token: str = Depends(get_token), db: Session = Depends(get_db)):
    """
    Endpoint to add a new post.

    Args:
        post (PostCreate): The details of the post to be created.
        token (str): JWT token for authorization.
        db (Session): SQLAlchemy database session.

    Returns:
        PostResponse: Response containing the ID of the newly created post.
    """
    return post_controller.add_post(post, token, db)

@router.delete("/delete_post/{post_id}")
async def delete_post(post_id: int, token: str = Depends(get_token), db: Session = Depends(get_db)):
    """
    Endpoint to delete a post.

    Args:
        post_id (int): The ID of the post to be deleted.
        token (str): JWT token for authorization.
        db (Session): SQLAlchemy database session.

    Returns:
        dict: A dictionary indicating the success of the deletion.
    """
    return post_controller.delete_post(post_id, token, db)

@router.get("/get_posts", response_model=list[Post])
@lru_cache(maxsize=128)
def get_posts(token: str = Depends(get_token), db: Session = Depends(get_db)):
    """
    Endpoint to get all user's posts.

    Args:
        token (str): JWT token for authentication.
        db (Session): SQLAlchemy database session.

    Returns:
        list[Post]: List of all user's posts.
    """
    # Check if the token is valid
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")

    email = decode_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Fetch posts from the database
    return post_controller.get_posts(db)
