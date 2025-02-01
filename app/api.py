from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette.responses import Response
from starlette.status import HTTP_202_ACCEPTED, HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_201_CREATED, \
    HTTP_406_NOT_ACCEPTABLE, HTTP_405_METHOD_NOT_ALLOWED

from database import get_session
from models import User, Home

#                 Auto, AutoRead, UserCreate, UserRead, UserAndNews, News, MotoRead, Moto, MotoEnum, \
# UserReadOrderBy)


router = APIRouter()


@router.post("/user_add_city/{id}")
def user_add_city(id: int, session: Session = Depends(get_session)):
    user = session.get(User, id)
    home1 = session.get(Home, 1)
    home2 = session.get(Home, 2)

    user.home=[home1,home2]
    session.commit()
    session.refresh(user)

    user = session.get(User, 2)
    home1 = session.get(Home, 1)
    # home2 = session.get(Home, 2)

    user.home = [home1]
    session.commit()
    session.refresh(user)
    return user.home

@router.get("/user_city/{id}")
def user_city(id: int, session: Session = Depends(get_session)):
    user = session.get(User, id)
    return user.home



#
# @router.post('/auto')
# async def auto(data: Auto, session: Session = Depends(get_session)):
#     session.add(data)
#     session.commit()
#     return Response(status_code=HTTP_202_ACCEPTED)
#
#
#
#
#
# @router.get('/list_auto_of_user', response_model=List[AutoRead])
# async def list_auto_of_user(user_id: int, session: Session = Depends(get_session)):
#     user = session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=HTTP_406_NOT_ACCEPTABLE)
#     return user.auto
#
#
# @router.get('/list_moto_of_user', response_model=List[AutoRead])
# async def list_auto_of_user(user_id: int, session: Session = Depends(get_session)):
#     user = session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=HTTP_406_NOT_ACCEPTABLE)
#     return user.moto
#
#
# @router.get('/moto_one_year', response_model=List[MotoRead], summary='мотоциклы 1 года')
# async def moto_one_year(year: int, session: Session = Depends(get_session)):
#     result = session.exec(select(Moto).where(Moto.age == year)).all()
#     return result
#
#
# @router.get('/moto_between_year', response_model=List[MotoRead], summary="Мотоциклы в промежутке")
# async def moto_between_year(year_start: int, year_end: int, session: Session = Depends(get_session)):
#     result = session.exec(select(Moto).where(Moto.age >= year_start).where(Moto.age <= year_end)).all()
#     return result
#
#
# # @router.get('/moto_query', response_model=List[MotoRead], summary="Мотоциклы")
# # async def moto_query(year_start: int, year_end=0, session: Session = Depends(get_session)):
# #     if int(year_end) == 0:
# #         result = session.exec(select(Moto).where(Moto.age == year_start)).all()
# #     else:
# #         result = session.exec(select(Moto).where(Moto.age >= year_start).where(Moto.age <= year_end)).all()
# #     return result
#
# @router.get('/moto_query', response_model=List[MotoRead], summary="Мотоциклы")
# async def moto_query(year_start: int, year_end: int | None = None, session: Session = Depends(get_session)):
#     if year_end is None:
#         result = session.exec(select(Moto).where(Moto.age == year_start)).all()
#     else:
#         result = session.exec(select(Moto).where(Moto.age >= year_start).where(Moto.age <= year_end)).all()
#     return result
#
#
# @router.get('/moto_query_with_model', response_model=List[MotoRead], summary="Мотоциклы и модель")
# async def moto_query(year_start: int, mod: MotoEnum, year_end: int |None=None, session: Session = Depends(get_session)):
#     if year_end is None:
#         result = session.exec(select(Moto).where(Moto.model == mod).where(Moto.age == year_start)).all()
#     else:
#         result = session.exec(
#             select(Moto).where(Moto.model == mod).where(Moto.age >= year_start).where(Moto.age <= year_end)).all()
#     return result
#
#
#
#
# @router.get('/moto_count',)
# def moto_count(session: Session = Depends(get_session)):
#     response= len(session.exec(select(Moto)).all())
#     return response
