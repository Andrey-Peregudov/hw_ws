# -*- coding:utf-8 -*-
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Query
from pydantic import EmailStr

from models import *
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordRequestForm

security = HTTPBasic()


@db_session
def get_cur_user(
        credentials: HTTPBasicCredentials = Depends(security),
):
    a = credentials.username

    print("Username is {}".format(credentials.username))
    print("Password is {}".format(credentials.password))
    user = User.get(username = a)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not register",
            headers={"WWW-Authenticate": "Basic"},
        )
    correct_username = secrets.compare_digest(a, str(user.username))
    correct_password = check_password_hash(user.password_hash, credentials.password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    print(user)
    print('--------')
    return user


