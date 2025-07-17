from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from database import get_mongo


class MessageRepository:
    def __init__(self, mongo_db: AsyncIOMotorDatabase):
        self.mongo_db = mongo_db

    async def create_message(self):
        pass


async def get_message_repository(mongo: AsyncIOMotorDatabase = Depends(get_mongo)):
    return MessageRepository(mongo)
