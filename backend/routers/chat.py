from fastapi import APIRouter, Depends

from schemas.chat import Chat
from schemas.user import UserCredentials
from services.chat_service import get_chat_service, ChatService
from utils.jwt_util import get_current_user

router = APIRouter()


@router.post('/create_chat', response_model=Chat | None)
async def create_chat(chat: Chat, user: UserCredentials = Depends(get_current_user),
                      chat_service: ChatService = Depends(get_chat_service)):
    new_chat = await chat_service.create_chat(chat, user)
    return new_chat


@router.get('/get_user_chats', response_model=list[Chat] | None)
async def get_user_chats(user: UserCredentials = Depends(get_current_user),
                         chat_service: ChatService = Depends(get_chat_service)):
    list_chats = await chat_service.get_user_chats(user)
    return list_chats
