import os

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

from schemas.user import UserCredentials

load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 1
oauth2_scheme = HTTPBearer()


async def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)) -> UserCredentials:
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload is None:
            raise HTTPException(status_code=401)
        user = None
        try:
            user = UserCredentials.model_validate(payload)
        except Exception as e:
            print("Ошибка создания UserCredentials")
        return user
    except JWTError:
        raise HTTPException(status_code=401)
