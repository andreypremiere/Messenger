from uuid import UUID

from fastapi import Depends
from starlette.websockets import WebSocket

from schemas.message import MessageCreate
from services.chat_service import ChatService, get_chat_service
from services.message_service import get_message_service, MessageService


class SocketDispatcher:
    def __init__(self, message_service: MessageService,
                 chat_service: ChatService):
        self.message_service = message_service
        self.chat_service = chat_service
        self.connection_manager = None

    async def process_message(self, received_data: dict):
        message_create: MessageCreate
        try:
             message_create = MessageCreate.model_validate(received_data)
        except Exception as e:
            print('Ошибка валидации поступившего сообщения')
            return None

        id_participants: list | None = None
        # Получить участников чата/проверить существование чата
        try:
            id_participants = await self.chat_service.get_participants_by_chat_id(message_create.chat_id)
        except Exception as e:
            print('Ошибка выполнения id_participants: list = '
                  'await self.chat_service.get_participants_by_chat_id(message_create.chat_id)')

        if id_participants is not None:
            # id_participants.remove(str(message_create.sender))
            pass
        else:
            print('id_participants оказался None')
            return None

        # Отправить в сервис создание сообщения
        message_create = await self.message_service.create_message(message_create)

        if message_create is None:
            print('Метод создания сообщения вернул None')
            return None

        # Отправить всем участникам чата его
        for user_id in id_participants:
            if await self.check_is_online(user_id):
                await self.perform_response(user_id, message_create)

    async def perform_response(self, user_id: str, message: MessageCreate):
        socket: WebSocket
        try:
            socket = self.connection_manager.connections[user_id]
        except Exception as e:
            print(f'Cоединение c {user_id} не найдено')
            return None
        await socket.send_json(message.model_dump(mode="json"))

    async def check_is_online(self, user_id: str):
        return user_id in self.connection_manager.connections


async def get_socket_dispatcher(message_service: MessageService = Depends(get_message_service),
                                chat_service: ChatService = Depends(get_chat_service)) -> SocketDispatcher:
    return SocketDispatcher(message_service, chat_service)
