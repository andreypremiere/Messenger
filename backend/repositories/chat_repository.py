from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from database import get_mongo
from schemas.chat import Chat


class ChatRepository:
    def __init__(self, mongo_db: AsyncIOMotorDatabase):
        self.db = mongo_db

    async def create_chat(self, chat_dict: dict) -> dict | None:
        result_commit = await self.db['chats'].insert_one(chat_dict)
        return None


async def get_chat_repository(mongo: AsyncIOMotorDatabase = Depends(get_mongo)) -> ChatRepository:
    return ChatRepository(mongo)
