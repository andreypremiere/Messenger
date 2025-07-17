from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo import DESCENDING
from database import get_mongo


class ChatRepository:
    def __init__(self, mongo_db: AsyncIOMotorDatabase):
        self.db = mongo_db

    async def create_chat(self, chat_dict: dict) -> dict | None:
        result_commit = await self.db['chats'].insert_one(chat_dict)
        return None

    async def get_user_chats(self, user_id: str):
        result = await self.db['chats'].find({
            "participants.user_id": user_id
        }).sort("created_at", DESCENDING).to_list(length=None)
        return result


async def get_chat_repository(mongo: AsyncIOMotorDatabase = Depends(get_mongo)) -> ChatRepository:
    return ChatRepository(mongo)
