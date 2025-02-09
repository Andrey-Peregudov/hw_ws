from logging.config import listen
from typing import List, Dict
from pydantic import BaseModel
from fastapi import FastAPI, Form, WebSocket
from pony.orm import db_session
from starlette.middleware import Middleware
from starlette.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect
from websockets import ConnectionClosed

# docker stop $(docker ps -qa) && docker rm $(docker ps -qa) && docker rmi -f $(docker images -qa) && docker volume rm $(docker volume ls -q) && docker network rm $(docker network ls -q)

from models import db, User

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


ws_list: List[WebSocket] = []
ws_dict: Dict[int, WebSocket] = {}
online_users: Dict[int, bool] = {}

class StatusUpdate(BaseModel):
    user_id: int
    online: bool

async def broadcast_status(status: StatusUpdate):
    for ws in ws_list:
        try:
            await ws.send_json(status.dict())
        except Exception:
            print("Error sending status update to a client")


@app.websocket("/ws/{id}")
@db_session
async def websocket_endpoint(websocket: WebSocket, id: int):
    user = User.get(id=id)
    if user is None:
        await websocket.close()
        return

    await websocket.accept()
    ws_list.append(websocket)
    ws_dict[id] = websocket
    online_users[id] = True
    await broadcast_status(StatusUpdate(user_id=id, online=True))
    try:
        while True:

            data = await websocket.receive_text()
            user_id=int(data.split('_')[0])
            send_ws = ws_dict.get(user_id)
            if send_ws is not None:
                if send_ws in ws_list:
                    await send_ws.send_text(user.username +' says: '+data.split('_')[1])
            if websocket in ws_list:
               await websocket.send_text('I am says :'+ data.split('_')[1])
               print(user_id)
    except (WebSocketDisconnect, ConnectionClosed):
        ws_list.remove(websocket)
        ws_dict.pop(id)
        online_users[id] = False
    await broadcast_status(StatusUpdate(user_id=id, online=False))






@app.get("/{id}")
async def get_ws(request: Request, id: int):
    return templates.TemplateResponse("websock.html", {"request": request, "id": id})


db.bind(provider='postgres', user='fastapi_jinja2', password='fastapi_jinja2', host='db', database='fastapi_jinja2',
        port='5432')
db.generate_mapping(create_tables=True)

import user

app.include_router(user.router, prefix="/user", tags=["user"])
