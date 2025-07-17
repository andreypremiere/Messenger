from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket, WebSocketDisconnect

from schemas.user import UserCredentials
from services.message_service import get_message_service, MessageService
from utils.connection_manager import ConnectionManager
from utils.jwt_util import get_current_user_from_token

router = APIRouter()

connection_manager = ConnectionManager()


@router.websocket('/ws')
async def web_socket(websocket: WebSocket, message_service: MessageService = Depends(get_message_service)):
    token = websocket.query_params.get('token')
    if not token:
        await websocket.close(code=1008)
        return

    user: UserCredentials = await get_current_user_from_token(token)

    await websocket.accept()

    await connection_manager.connect(str(user.user_id), websocket)

    try:
        while True:
            data = await websocket.receive_json()
            await connection_manager.process_request(str(user.user_id), data, message_service)
    except WebSocketDisconnect:
        print(f"Пользователь {user.user_id} отключился")
    except Exception as e:
        print(f"Ошибка в WebSocket у пользователя {user.user_id}: {e}")
    finally:
        await connection_manager.disconnect(str(user.user_id))

