from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship


# class CarEnum(str, Enum):
#     FORD = 'FORD'
#     VAZ = 'VAZ'
#     JEEP = 'JEEP'
#     VW = 'VW'
#
#
# class MotoEnum(str, Enum):
#     TOYOTA = 'TOYOTA'
#     HONDA = 'HONDA'
#     KAWASAKI = 'KAWASAKI'
class UserHomeLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='user.id')
    home_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='home.id')

class UserBase(SQLModel):
    pass





class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field()
    password: Optional[str] = Field()
    # is_active: Optional[bool] = Field(default=True)
    # is_superuser: Optional[bool] = Field(default=True)
    email: Optional[str] = Field()

    home: list["Home"]= Relationship(back_populates="user", link_model=UserHomeLink)
    # data_ostroiki: Optional[datetime] = Field(default=datetime.now())

    # auto: List["Auto"] = Relationship(back_populates="user",
    #                                   sa_relationship_kwargs={"cascade": "all,delete,delete-orphan"}, )
    # moto: List["Moto"] = Relationship(back_populates="user",
    #                                   sa_relationship_kwargs={"cascade": "all,delete,delete-orphan"}, )

#
# class UserUpdate(UserBase):
#     username: str | None = None
#     email: str | None = None
#
#
#
# class UserRead(UserBase):
#     # id: Optional[int]
#     username: Optional[str]
#     password: Optional[str]
#     # is_active: Optional[bool]
#     # is_superuser: Optional[bool]
#     email: Optional[str]
#     # data_ostroiki: Optional[datetime]
#
#     # auto: List["Auto"]
#     # moto: List["Moto"]
#
# class UserReadOrderBy(UserBase):
#     username: Optional[str]
#     email: Optional[str]
#
#
# class UserCreate(UserBase):
#     username: str
#     password: str
#     email: Optional[str]
#

class HomeBase(SQLModel):
    pass

class Home(HomeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    city: Optional[str]
    user: list["User"]=Relationship(back_populates="home", link_model=UserHomeLink)



#
#
# class AutoBase(SQLModel):
#     pass
#
#
# class Auto(AutoBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     model: Optional[CarEnum] = Field(default=CarEnum.FORD)
#     age: Optional[int] = Field(default=2024, ge=2000, le=2025)
#
#     user_id: Optional[int] = Field(default=None, foreign_key="user.id")
#     user: Optional[User] = Relationship(back_populates="auto")
#
#
# class AutoCreate(AutoBase):
#     age: Optional[int]
#     user_id: Optional[int]
#
#
# class AutoRead(AutoBase):
#     model: Optional[CarEnum]
#     age: Optional[int]
#
#
# class MotoBase(SQLModel):
#     pass
#
#
# class Moto(MotoBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     model: Optional[MotoEnum] = Field(default=MotoEnum.KAWASAKI)
#     age: Optional[int] = Field(default=2024, ge=2000, le=2025)
#
#     user_id: Optional[int] = Field(default=None, foreign_key="user.id")
#     user: Optional[User] = Relationship(back_populates="moto")
#
#
# class MotoCreate(MotoBase):
#     age: Optional[int]
#     user_id: Optional[int]
#
#
# class MotoRead(MotoBase):
#     model: Optional[MotoEnum]
#     age: Optional[int]
#
#
# class NewsBase(SQLModel):
#     pass
#
#
# class News(NewsBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     text: Optional[str] = Field()
#     nums: Optional[int] = Field(ge=1, le=100)
#
#
# class UserAndNews(BaseModel):
#     user: UserRead
#     news: List["News"]
