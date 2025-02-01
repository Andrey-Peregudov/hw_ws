from fastapi import FastAPI, Form
from starlette.middleware import Middleware
from starlette.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from models import db, User, City

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware, title='FastAPI Jinja2 Postress Websocket')
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/name")
async def name():
    return {"Hello": "id"}


@app.get("/test/{id}", response_class=HTMLResponse)
async def root(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id})


@app.get("/form", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse('form.html', {'request': request})


@app.post('/disable')
async def disable_cat(cat_name: str = Form(...)):
    print(cat_name.upper())
    return f'{cat_name} category has been disabled.'


db.bind(provider='postgres', user='fastapi_jinja2', password='fastapi_jinja2', host='db', database='fastapi_jinja2',
        port='5432')
db.generate_mapping(create_tables=True)

import user

app.include_router(user.router, prefix="/user", tags=["user"])
