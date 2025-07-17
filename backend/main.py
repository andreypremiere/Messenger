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
# app.include_router(web_socket.router, tags=['web-socket'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],          # Все методы: GET, POST, PUT и т.д.
    allow_headers=["*"],          # Все заголовки
)


# @app.websocket('/ws')
# async def web_socket(websocket: WebSocket):
#     # Получаем токен из query параметров
#     token = websocket.query_params.get('token')
#     if not token:
#         await websocket.close(code=1008)  # policy violation
#         return
#
#     try:
#         user = get_current_user_from_token(token)  # функция декодирования токена
#     except Exception:
#         await websocket.close(code=1008)
#         return
#
#     await websocket.accept()
#
#     while True:
#         data = await websocket.receive_text()
#         print(data)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("⏳ Запрос на соединение пришёл")  # ← даже если токен неверный, это должно выводиться

    await websocket.accept()
    print("✅ Соединение принято")

    while True:
        data = await websocket.receive_text()
        print(f"📩 Получено сообщение: {data}")
        await websocket.send_text("pong")
