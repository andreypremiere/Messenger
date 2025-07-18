from starlette.websockets import WebSocket

from services.message_service import MessageService


class ConnectionManager:
    def __init__(self):
        self.connections = {}
        print('Менеджер соединений инициализирован')

    async def connect(self, user_id: str, websocket: WebSocket):
        self.connections[user_id] = websocket
        print(f'Пользователь {user_id} присоединился')

    async def disconnect(self, user_id: str):
        if user_id in self.connections:
            del self.connections[user_id]
