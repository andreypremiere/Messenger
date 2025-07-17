from fastapi import Depends

from repositories.message_repository import MessageRepository, get_message_repository


class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self.message_repo = message_repository
        print('Message_service создан')

    async def create_message(self, data: dict):
        await self.message_repo.create_message()
        return 'сообщение создано'


async def get_message_service(message_repository: MessageRepository = Depends(get_message_repository)):
    return MessageService(message_repository)