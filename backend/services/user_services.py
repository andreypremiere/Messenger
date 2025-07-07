from fastapi import Depends

from models.userORM import UserORM
from schemas.token import Token
from schemas.user import UserRegister, UserResponse, UserVerify, UserAuthenticate
from schemas.user import UserRegisterResponse
from repositories.user_repositories import UserRepository, get_user_repo
from services.code_confirmation_service import CodeConfirmationService, get_code_confirmation_service
from utils.email_sending import send_email
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
            result_code = None
            if user_reg_response is not None:
                result_code = await self.code_service.create_temporary_code(str(user_reg_response.user_id))
                if result_code is None:
                    print(f'Код подтверждения не был создан при регистрации. Операция вернула: {result_code}')

            if result_code is not None:
                try:
                    send_email(user_reg_response.email, result_code)
                except Exception as e:
                    print(f'Ошибка при отправке кода клиенту на адрес {user_reg_response.email} с кодом {result_code}'
                          f'Ошибка в user_service.create_user', e)
                    return None
            else:
                print('Код отсутствует. Письмо не отправлено.')
                return None

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

        print('result_comparing', result_comparing)

        if result_comparing:
            user_response = await self.get_user_by_id(user_verify.user_id)

            data = {'user_id': str(user_response.user_id), 'unique_nickname': user_response.unique_nickname,
                    'displayed_nickname': user_response.displayed_nickname}

            token = await create_access_token(data)

            return Token(token=token)
        else:
            return None

    async def authenticate_user_by_any(self, value: UserAuthenticate) -> UserResponse | None:
        user_response = await self.get_user_by_any(value.value)

        if user_response is not None:
            result_code = await self.code_service.create_temporary_code(str(user_response.user_id))
            if result_code is not None:
                try:
                    send_email(user_response.email, result_code)
                except Exception as e:
                    print(f'Ошибка при отправке кода клиенту на адрес {user_response.email} с кодом {result_code}'
                          f'Ошибка в user_service.authenticate_user_by_any', e)
                    return None
                return user_response
            else:
                return None
        else:
            return None

    async def get_user_by_any(self, value: str) -> UserResponse | None:
        user_orm = None

        try:
            user_orm = await self.user_repo.get_user_by_any(value)
            print(f'user_orm в get_user_by_any в user_service: {user_orm}')
        except Exception as e:
            print(f'Ошибка получения пользователя по значению: {value}')
            return None

        if user_orm is None:
            print('Пользователь не найден')
            return user_orm

        try:
            user_response = UserResponse.from_orm(user_orm)
            return user_response
        except Exception as e:
            print(f'Ошибка преобразования модели user_orm {user_orm} в UserResponse в get_user_by_any в user_service.')
            return None


async def get_user_service(
        user_repo: UserRepository = Depends(get_user_repo),
        code_service: CodeConfirmationService = Depends(get_code_confirmation_service)
) -> UserService:
    return UserService(user_repo, code_service)
