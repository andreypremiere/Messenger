import uuid
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.user import UserChat


class TypeChat(str, Enum):
    type1 = 'personal'
    type2 = 'group'


class Chat(BaseModel):
    chat_id: UUID = Field(default_factory=lambda: uuid.uuid4())
    participants: list[UserChat]
    type_chat: TypeChat = TypeChat('personal')
    admin: UserChat | None = None
    name: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# class ChatCreate(BaseModel):
