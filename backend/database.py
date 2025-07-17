import aioboto3
import motor.motor_asyncio
from botocore.config import Config
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

# YANDEX_ENDPOINT = 'https://storage.yandexcloud.net'
# YANDEX_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
# YANDEX_SECRET_KEY = os.getenv('S3_SECRET_KEY')
#
# session = aioboto3.Session()
#
#
# async def get_s3_client():
#     async with session.client(
#             "s3",
#             endpoint_url=YANDEX_ENDPOINT,
#             aws_access_key_id=YANDEX_ACCESS_KEY,
#             aws_secret_access_key=YANDEX_SECRET_KEY,
#             region_name="ru-central1"  # не обязателен, но можно указать
#     ) as s3:
#         yield s3

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "test")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "test")

s3_config = Config(signature_version="s3v4")

session = aioboto3.Session()


async def get_s3_client():
    """
    Возвращает aioboto3-клиент, подключённый к LocalStack.
    """
    async with session.client(
            "s3",
            endpoint_url='http://localhost:4568',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name="us-east-1",  # или любой другой
            use_ssl=False,  # LocalStack обычно на HTTP
            verify=False,  # без проверки сертификата
            config=s3_config
    ) as client:
        yield client



async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


async def get_redis() -> Redis:
    return redis_client


async def get_mongo() -> AsyncIOMotorDatabase:
    return mongo_client['database']
