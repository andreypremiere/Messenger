import random
from fastapi import Depends
from repositories.code_confirmation_repository import CodeConfirmationRepository, get_code_repo


class CodeConfirmationService:
    def __init__(self, code_confirmation_repository: CodeConfirmationRepository):
        self.code_repo = code_confirmation_repository

    async def generate_code(self) -> int:
        return random.randint(100000, 999999)

    async def create_temporary_code(self, user_id: str) -> bool:
        code = await self.generate_code()

        try:
            await self.code_repo.create_temporary_code(user_id, code)
            print(f'Код был создан успешно. {code}')
            return True
        except Exception as e:
            print('Ошибка при попытке установить код для клиента.')
            return False

    async def get_temporary_code(self, user_id: str) -> int | None:
        try:
            code = await self.code_repo.get_temporary_code(user_id)
            print(f'Полученный код в get_temporary_code {code}')
            return code
        except Exception as e:
            print(f'Ошибка при попытке получить код по id {user_id}')
            return None

    async def compare_code_confirmation(self, user_id: str, code: int) -> bool:
        true_code = await self.get_temporary_code(user_id)

        if true_code is None:
            return False

        # print(f'Истинный код: {true_code} тип {type(true_code)}, код пользователя {code} тип {type(code)}')
        return int(true_code) == code


async def get_code_confirmation_service(code_repo: CodeConfirmationRepository = Depends(get_code_repo)) \
        -> CodeConfirmationService:
    return CodeConfirmationService(code_repo)
