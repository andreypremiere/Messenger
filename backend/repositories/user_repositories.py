from fastapi import Depends
from sqlalchemy import select, or_
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

    async def get_user_by_any(self, value) -> UserORM | None:
        stmt = select(UserORM).where(
            or_(
                UserORM.email == value,
                UserORM.number_phone == value,
                UserORM.unique_nickname == value
            )
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def find_users_by_value(self, value):
        stmt = select(UserORM).where(
            or_(
                UserORM.number_phone.ilike(f"%{value}%"),
                UserORM.unique_nickname.ilike(f"%{value}%"),
                UserORM.displayed_nickname.ilike(f"%{value}%")
            )
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()


async def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)
