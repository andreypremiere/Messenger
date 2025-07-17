from fastapi import APIRouter, Depends

from schemas.token import Token
from schemas.user import UserRegisterResponse, UserRegister, UserResponse, UserVerify, UserAuthenticate
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


@router.post('/authenticate_user_by_any', response_model=UserResponse)
async def authenticate_user_by_any(value: UserAuthenticate, user_service: UserService = Depends(get_user_service)):
    user_response = await user_service.authenticate_user_by_any(value)
    print(f'Полученный результат в verify_user: {user_response}')
    return user_response


@router.post('/find_users_by_value', response_model=list[UserResponse] | None)
async def find_users_by_value(value: UserAuthenticate, user_service: UserService = Depends(get_user_service)):
    response = await user_service.find_users_by_value(value)
    return response
