from fastapi import Depends

from models.userORM import UserORM
from schemas.token import Token
from schemas.user import UserRegister, UserResponse, UserVerify
from schemas.user import UserRegisterResponse
from repositories.user_repositories import UserRepository, get_user_repo
from services.code_confirmation_service import CodeConfirmationService, get_code_confirmation_service
from utils.jwt_util import create_access_token


class UserService:
    def __init__(self, user_repo: UserRepository,
                 code_confirmation_service: CodeConfirmationService):
        self.user_repo = user_repo
        self.code_service = code_confirmation_service

    async def create_user(self, user: UserRegister) -> UserRegisterResponse | None:
        user_dict = user.dict()
        print(f'user.dict() in create_user in UserService: {user_dict}')
        user_orm = UserORM(**user_dict, displayed_nickname=user_dict['unique_nickname'])

        try:
            user_orm_updated = await self.user_repo.create_user(user_orm)
        except Exception as e:
            print('Ошибка создания пользователя в UserService в create_user.')
            return None

        try:
            user_reg_response = UserRegisterResponse.from_orm(user_orm_updated)
            if user_reg_response is not None:
                result_creating_code = await self.code_service.create_temporary_code(str(user_reg_response.user_id))
                if result_creating_code is None:
                    print(f'Код подтверждения не был создан при регистрации. Операция вернула: {result_creating_code}')
            print('Пользователь создан')
            return user_reg_response
        except Exception as e:
            print('Ошибка преобразования модели ORM в pydantic.')

    async def get_user_by_id(self, user_id: str) -> UserResponse | None:
        user_orm = None

        try:
            user_orm = await self.user_repo.get_user_by_id(user_id)
            print(f'user_orm в get_user_by_id в user_service: {user_orm}')
        except Exception as e:
            print(f'Ошибка получения пользователя по id: {user_id}')
            return None

        try:
            user_response = UserResponse.from_orm(user_orm)
            return user_response
        except Exception as e:
            print(f'Ошибка преобразования модели user_orm {user_orm} в UserResponse в get_user_by_id в user_service.')
            return None

    async def verify_user_by_id(self, user_verify: UserVerify) -> Token | None:
        result_comparing = self.code_service.compare_code_confirmation(user_verify.user_id, user_verify.code)

        if result_comparing:
            user_response = await self.get_user_by_id(user_verify.user_id)

            data = {'user_id': str(user_response.user_id), 'unique_nickname': user_response.unique_nickname,
                    'displayed_nickname': user_response.displayed_nickname}

            token = await create_access_token(data)

            return Token(token=token)
        else:
            return None


async def get_user_service(
        user_repo: UserRepository = Depends(get_user_repo),
        code_service: CodeConfirmationService = Depends(get_code_confirmation_service)
) -> UserService:
    return UserService(user_repo, code_service)
