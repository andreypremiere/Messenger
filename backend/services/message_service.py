from datetime import datetime, timezone

from fastapi import Depends

from repositories.message_repository import MessageRepository, get_message_repository
from schemas.message import MessageCreate


class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self.message_repo = message_repository
        print('Message_service создан')

    async def convert_message(self, message: dict):
        message['message_id'] = message['_id']
        del message['_id']

    async def create_message(self, message: MessageCreate):
        message_dict = message.model_dump(mode='json')
        message_dict['_id'] = message_dict['message_id']
        del message_dict['message_id']

        message_dict['created_at'] = datetime.now(timezone.utc)

        try:
            await self.message_repo.create_message(message_dict)
        except Exception as e:
            print('Ошибка при попытке добавить сообщение в базу данных')
            return None

        await self.convert_message(message_dict)

        return MessageCreate.model_validate(message_dict)


async def get_message_service(message_repository: MessageRepository = Depends(get_message_repository)):
    return MessageService(message_repository)