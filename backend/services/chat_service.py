from uuid import UUID

from fastapi import Depends

from repositories.chat_repository import ChatRepository, get_chat_repository
from schemas.chat import Chat
from schemas.user import UserCredentials


class ChatService:
    def __init__(self, chat_repo: ChatRepository):
        self.chat_repo = chat_repo

    async def convert_chat(self, chat: dict):
        chat['chat_id'] = chat['_id']
        del chat['_id']
        return chat

    async def convert_chats(self, chats: list):
        return [await self.convert_chat(chat) for chat in chats]

    async def create_chat(self, chat: Chat, creator: UserCredentials) -> Chat | None:
        checking_creator = False

        for user in chat.participants:
            if creator.user_id == user.user_id:
                checking_creator = True
                break

        if not checking_creator:
            print('Пользователь создает чужой чат')
            return None

        chat_dict = chat.model_dump(mode='json')
        chat_dict['_id'] = chat_dict['chat_id']
        del chat_dict['chat_id']

        try:
            await self.chat_repo.create_chat(chat_dict)
        except Exception as e:
            print('Ошибка создания чата.')
            return None
        return chat

    async def get_user_chats(self, user: UserCredentials):
        result = None
        try:
            result = await self.chat_repo.get_user_chats(str(user.user_id))
        except Exception as e:
            print('Ошибка запроса чатов для пользователя')
            return None

        try:
            result = await self.convert_chats(result)
            result = [Chat.model_validate(chat) for chat in result]
        except Exception as e:
            print('Ошибка преобразования типов данных')
            return None

        return result

    async def get_chat_by_chat_id(self, chat_id: UUID):
        pass

    async def get_participants_by_chat_id(self, chat_id: UUID):
        result = None
        try:
            result = await self.chat_repo.get_chat_by_chat_id(chat_id)
        except Exception as e:
            print('Ошибка получения чата по id чата', e)

        if result is None:
            return None

        participants_id = [user['user_id'] for user in result['participants']]

        return participants_id







async def get_chat_service(chat_repo: ChatRepository = Depends(get_chat_repository)) -> ChatService:
    return ChatService(chat_repo)
