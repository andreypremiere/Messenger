from uuid import UUID

from pydantic import BaseModel, Field
from datetime import datetime, timezone


class Message(BaseModel):
    message_id: UUID
    chat_id: UUID
    sender: UUID
    content: str
    message: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
