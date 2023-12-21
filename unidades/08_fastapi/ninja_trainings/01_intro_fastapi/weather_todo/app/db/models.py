from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    weathers = relationship("Weather", back_populates="user")


class Weather(Base):
    __tablename__ = "weathers"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    description = Column(String)
    temperature = Column(Integer)
    day = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="weathers")
