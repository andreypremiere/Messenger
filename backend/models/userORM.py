import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


Base = declarative_base()


class UserORM(Base):
    __tablename__ = "users"

    user_id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    unique_nickname = Column(String(80), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    number_phone = Column(String(16), nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    last_enter = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    displayed_nickname = Column(String(140), nullable=True)

    def __repr__(self):
        values = ", ".join(f"{column.name}: {getattr(self, column.name)}" for column in self.__table__.columns)
        return f"UserORM = {self.__class__.__name__} ({values})"
