from fastapi import Depends

from repositories.chat_repository import ChatRepository, get_chat_repository
from schemas.chat import Chat


class ChatService:
    def __init__(self, chat_repo: ChatRepository):
        self.chat_repo = chat_repo

    async def create_chat(self, chat: Chat) -> Chat | None:
        chat_dict = chat.model_dump(mode='json')
        chat_dict['_id'] = chat_dict['chat_id']
        del chat_dict['chat_id']

        try:
            await self.chat_repo.create_chat(chat_dict)
        except Exception as e:
            print('Ошибка создания чата.')
            return None
        return chat


async def get_chat_service(chat_repo: ChatRepository = Depends(get_chat_repository)) -> ChatService:
    return ChatService(chat_repo)
