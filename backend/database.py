import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os
import redis.asyncio as redis
from redis.asyncio.client import Redis


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

REDIS_URL = os.getenv('REDIS_URL')
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

MONGO_URL = os.getenv('MONGO_URL')
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


async def get_redis() -> Redis:
    return redis_client


async def get_mongo() -> AsyncIOMotorDatabase:
    return mongo_client['database']
