from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db import crud, models, schemas
from app.db.database import SessionLocal, engine
from app.auth.auth import (
    oauth2_scheme, TokenData, decode_token, Token, verify_password, create_access_token
)

# Create database.
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app.
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


@app.post("/auth/login", response_model=Token)
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


@app.get("/")
async def root():
    return {"data": "Bienvenid@ a mi primer API"}


@app.get("/add/{n1}/{n2}/")
async def add(n1: int, n2: int):
    addition: int = n1 + n2
    return {"data": addition}


@app.get("/users/", response_model=list[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/weathers/", response_model=schemas.Weather)
async def create_weather_for_user(
    user_id: int,
    weather: schemas.WeatherCreate,
    user: Annotated[schemas.User, Depends(get_auth_user)],
    db: Session = Depends(get_db)
):
    return crud.create_weather(db=db, weather=weather, user_id=user_id)


@app.get("/weathers/", response_model=list[schemas.Weather])
async def read_weathers(db: Session = Depends(get_db)):
    users = crud.get_weathers(db)
    return users


@app.delete("/weathers/{weather_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_weather(weather_id: int, db = Depends(get_db)):
    found: bool = crud.delete_weather(db=db, weather_id=weather_id)
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Weather does not exists")