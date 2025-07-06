from fastapi import Depends
from redis.asyncio import Redis

from database import get_redis


class CodeConfirmationRepository:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def create_temporary_code(self, user_id: str, code: int):
        await self.redis.set(user_id, code, ex=180)

    async def get_temporary_code(self, user_id: str) -> int:
        return await self.redis.get(user_id)


async def get_code_repo(redis: Redis = Depends(get_redis)) -> CodeConfirmationRepository:
    return CodeConfirmationRepository(redis)
