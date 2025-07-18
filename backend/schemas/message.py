import uuid
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class MessageCreate(BaseModel):
    message_id: UUID = Field(default_factory=lambda: uuid.uuid4())
    chat_id: UUID
    sender: UUID
    message: str
    created_at: datetime | None = None
