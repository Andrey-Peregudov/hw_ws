from typing import List

from fastapi import Depends, APIRouter, HTTPException
from starlette.responses import Response
from starlette.status import HTTP_202_ACCEPTED


from pydantic_read import  UserView
from pydantic_create import UserCreate
from models import *

router = APIRouter()



@router.post("/new_user", summary="Регистрация нового пользователя")
@db_session
def new_user(*, base: UserCreate):
    a = base.dict()
    # b = a.pop('password')
    # a['password_hash'] = generate_password_hash(b)
    # a['city'] = 1
    a = User(**a)
    commit()
    return Response(status_code=HTTP_202_ACCEPTED)
