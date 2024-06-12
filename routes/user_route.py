from fastapi import FastAPI, HTTPException, Depends, Response,APIRouter
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.user_controller import UserController
from database import get_db,engine,SessionLocal,Base
from models.user_schema import UserCreate, UserLogin, Token
from services.token import get_token

user_controller = UserController()
router = APIRouter(tags=['User'])



@router.post("/signup", response_model=Token)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to sign up a new user.

    Args:
        user (UserCreate): The details of the user to be signed up.
        db (Session): SQLAlchemy database session.

    Returns:
        TokenResponse: Response containing access token and token type.
    """
    
    return user_controller.signup(user, db)

@router.post("/login", response_model=Token)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Endpoint to log in a user.

    Args:
        user (UserLogin): The credentials of the user attempting to log in.
        db (Session): SQLAlchemy database session.

    Returns:
        TokenResponse: Response containing access token and token type upon successful login.
    """
    return user_controller.login(user, db)

