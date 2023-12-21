from sqlalchemy.orm import Session

from app.auth.auth import get_password_hash
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_weathers(db: Session, skip: int = 0, limit: int = 100):
    db_weather = models.Weather()
    return db.query(models.Weather).offset(skip).limit(limit).all()


def create_weather(db: Session, weather: schemas.WeatherCreate, user_id: int):
    db_weather = models.Weather(**weather.dict(), user_id=user_id)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather


def delete_weather(db: Session, weather_id: int):
    db_weather = db.get(models.Weather, weather_id)
    if not db_weather:
        return False
    db.delete(db_weather)
    db.commit()
    return True