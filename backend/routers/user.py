from fastapi import APIRouter, Depends

from schemas.token import Token
from schemas.user import UserRegisterResponse, UserRegister, UserResponse, UserVerify
from services.user_services import UserService, get_user_service

router = APIRouter()


@router.post('/create_user', response_model=UserRegisterResponse)
async def create_user(user: UserRegister, user_service: UserService = Depends(get_user_service)):
    user_response = await user_service.create_user(user)
    return user_response


@router.get('/get_user_by_id/{user_id}', response_model=UserResponse)
async def get_user_by_id(user_id: str, user_service: UserService = Depends(get_user_service)):
    user_response = await user_service.get_user_by_id(user_id)
    return user_response


@router.post('/verify_user_by_id', response_model=Token)
async def verify_user_by_id(user_verify: UserVerify, user_service: UserService = Depends(get_user_service)):
    token = await user_service.verify_user_by_id(user_verify)
    return token


