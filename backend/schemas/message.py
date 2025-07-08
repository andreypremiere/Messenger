from uuid import UUID

from pydantic import BaseModel
from datetime import datetime, timezone

from schemas.user import UserChat


class Message(BaseModel):
    message_id: UUID
    chat_id: UUID
    sender: UserChat
    # content: str  # url на s3 (добавить в дальнейшем
    message: str
    created_at: datetime = lambda: datetime.now(timezone.utc)
