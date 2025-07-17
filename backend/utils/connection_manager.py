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

    async def process_request(self, user_id: str, data: dict, service_message: MessageService):
        if data['type'] == 'create_message':
            result = await service_message.create_message(data)
            data = {'result': result}
            await self.send_to_user(user_id, data)

    async def send_to_user(self, user_id: str, data: dict):
        socket: WebSocket
        try:
            socket = self.connections[user_id]
        except Exception as e:
            print('соединение не найдено')
        print('Соединение найдено')
        await socket.send_json(data)





