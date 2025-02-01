from pydantic import BaseModel
from typing import Optional as Opt


class CityView(BaseModel):
    id: int
    name: str


class UserView(BaseModel):
    id: int
    username: str
    address: str
