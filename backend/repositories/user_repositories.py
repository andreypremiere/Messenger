from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from models.userORM import UserORM


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: UserORM) -> UserORM:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        print('UserORM in create_user in UserRepository: ', user)
        return user

    async def get_user_by_id(self, user_id) -> UserORM | None:
        user = await self.session.get(UserORM, user_id)
        return user


async def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)
