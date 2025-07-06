import uuid

from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Annotated
from fastapi import Query
from datetime import datetime


class UserBase(BaseModel):
    unique_nickname: Annotated[str, Query(max_length=80)]
    email: EmailStr
    number_phone: Annotated[str, Query(max_length=16)]


class UserRegister(UserBase):
    pass


class UserRegisterResponse(UserBase):
    user_id: UUID
    displayed_nickname: Annotated[str | None, Query(max_length=140)] = None

    model_config = {
        "from_attributes": True  # заменяет orm_mode
    }


class UserResponse(UserBase):
    user_id: UUID
    displayed_nickname: Annotated[str | None, Query(max_length=140)] = None
    last_enter: datetime

    model_config = {
        "from_attributes": True  # заменяет orm_mode
    }


class UserVerify(BaseModel):
    user_id: str
    code: int

