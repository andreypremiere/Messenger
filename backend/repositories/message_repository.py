from motor.motor_asyncio import AsyncIOMotorDatabase


class MessageRepository:
    def __init__(self, mongo_db: AsyncIOMotorDatabase):
        self.mongo_db = mongo_db

    def create_message(self):
        pass
