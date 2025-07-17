from fastapi import FastAPI
from starlette.websockets import WebSocket

from routers import user, code_confirmation, chat, avatar, web_socket
from fastapi.middleware.cors import CORSMiddleware

from utils.jwt_util import get_current_user_from_token

app = FastAPI()

app.include_router(user.router, tags=['user'])
app.include_router(code_confirmation.router, tags=['code_confirmation'])
app.include_router(chat.router, tags=['chat'])
app.include_router(avatar.router, tags=['avatar'])
app.include_router(web_socket.router, tags=['web-socket'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],          # Все методы: GET, POST, PUT и т.д.
    allow_headers=["*"],          # Все заголовки
)





