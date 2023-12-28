from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db import models
from app.db.database import engine, SessionLocal
from app.db import schemas, crud
from app.auth.auth import (
    oauth2_scheme, TokenData, decode_token, Token, verify_password, create_access_token
)

# Create database.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_auth_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
) -> schemas.User:
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    token_data: TokenData = decode_token(token)
    if token_data is None or token_data.username is None:
        raise exception

    user = crud.get_user_by_username(db, token_data.username)
    if user is None:
        raise exception

    return user


@app.get("/")
async def root():
    return {"data": "Bienvenido a mi API"}


@app.get("/add/{n1}/{n2}/")
async def add_two_numbers(n1: int, n2: str):
    addition: int = str(n1) + n2
    return {"data": addition}


@app.get("/users/", response_model=list[schemas.User])
async def read_users(
    # user: Annotated[schemas.User, Depends(get_auth_user)],
    user: schemas.User = Depends(get_auth_user),
    db: Session = Depends(get_db)
):
    users = crud.get_users(db)
    return users


@app.post("/users/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    user_db = crud.get_user_by_username(db, user.username)
    if user_db:
        raise HTTPException(
            status_code=400, 
            detail="Username already registered"
        )

    user_db = crud.create_user(db, user)
    return user_db


@app.post("/auth/login/", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_username(db, form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username and/or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username and/or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return create_access_token(user)