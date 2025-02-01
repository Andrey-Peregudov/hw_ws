from fastapi import FastAPI
from sqlmodel import SQLModel, Session, select
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from seed import seed
from database import engine
from models import User

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     if session.get(User, 1) is None:
    #         a=User(role='LLLLL')
    #         session.add(a)
    #         session.commit()


app = FastAPI(middleware=middleware, title='Python424 group', description='Our first fastapi project', version='1')

import auth, api, users

app.include_router(users.router, tags=["Users | users.py"], prefix="/api")
app.include_router(auth.router, tags=["Auth | auth.py"], prefix="/auth")
app.include_router(api.router, tags=["API | api.py"], prefix="/api")


create_db_and_tables()

with Session(engine) as session:
    results = session.exec(select(User)).all()
    if not results: seed()
