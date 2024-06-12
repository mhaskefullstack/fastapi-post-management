from fastapi import FastAPI, HTTPException, Depends, Response,Request
from pydantic import BaseModel
from typing import Any
import jwt
from datetime import datetime, timedelta
from functools import lru_cache
from fastapi.middleware.cors import CORSMiddleware

from database import get_db,engine,SessionLocal,Base
from routes import user_route,post_route


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    """
    Middleware function that creates a new database session for each incoming HTTP request and
    closes the session once the request is completed.
    """
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(user_route.router)
app.include_router(post_route.router)
