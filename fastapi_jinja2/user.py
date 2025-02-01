from typing import List

from fastapi import Depends, APIRouter, HTTPException, Form
from starlette.responses import Response, HTMLResponse
from starlette.status import HTTP_202_ACCEPTED
from starlette.requests import Request

from auth import get_cur_user
from pydantic_read import CityView, UserView
from pydantic_create import UserCreate
from models import *

router = APIRouter()


@router.post("/login", summary="Авторизация", response_model=UserView )
async def maid_login(user: User = Depends(get_cur_user)):

    return user


@router.post("/new_city", summary="Регистрация нового города", )
@db_session
def new_city(*, name: str):
    gorod = City(name=name)
    commit()
    return Response(status_code=HTTP_202_ACCEPTED)


@router.get("/list_city", response_model=CityView, summary="Список городов",)
@db_session
def list_city():
    result = City.get(id=1)
    print(result)

    return result


@router.get("/user_forms", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse('user_form.html', {'request': request})


@router.post("/new_user", summary="Регистрация нового пользователя")
@db_session
def new_user(username: str = Form(...), password_hash: str = Form(...)):
    user = User(username=username, password_hash=password_hash)
    commit()
    return Response(status_code=HTTP_202_ACCEPTED)

