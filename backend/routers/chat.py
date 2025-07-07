from fastapi import APIRouter, Depends

from schemas.chat import Chat
from services.chat_service import get_chat_service, ChatService

router = APIRouter()


@router.post('/create_chat', response_model=Chat | None)
async def create_chat(chat: Chat, chat_service: ChatService = Depends(get_chat_service)):
    new_chat = await chat_service.create_chat(chat)
    return new_chat
