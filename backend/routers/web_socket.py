from fastapi import APIRouter
from starlette.websockets import WebSocket
from utils.jwt_util import get_current_user_from_token

router = APIRouter()

connections = {}


@router.websocket('/ws')
async def web_socket(websocket: WebSocket):
    # Получаем токен из query параметров
    token = websocket.query_params.get('token')
    if not token:
        await websocket.close(code=1008)  # policy violation
        return

    try:
        user = get_current_user_from_token(token)  # функция декодирования токена
    except Exception:
        await websocket.close(code=1008)
        return

    await websocket.accept()

    connections[user.user_id] = websocket

    while True:
        data = await websocket.receive_text()
        print(data)

