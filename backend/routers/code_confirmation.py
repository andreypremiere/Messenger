from fastapi import APIRouter, Depends

from services.code_confirmation_service import CodeConfirmationService, get_code_confirmation_service
from services.user_services import UserService, get_user_service

router = APIRouter()


@router.post('/create_code')
async def create_code_by_user_id(user_id: str,
                                 code_service: CodeConfirmationService = Depends(get_code_confirmation_service)):
    result = await code_service.create_temporary_code(user_id)

    if result:
        return True
    else:
        return False


@router.get('/compare_code')
async def compare_code(user_id: str, code: int,
                       code_service: CodeConfirmationService = Depends(get_code_confirmation_service)):
    result = await code_service.compare_code_confirmation(user_id, code)
    return result
