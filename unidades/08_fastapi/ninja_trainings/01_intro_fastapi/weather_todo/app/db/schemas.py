from pydantic import BaseModel


class WeatherBase(BaseModel):
    city: str
    temperature: int
    day: str
    description: str | None = None


class WeatherCreate(WeatherBase):
    pass


class Weather(WeatherBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    weathers: list[Weather] = []

    class Config:
        orm_mode = True