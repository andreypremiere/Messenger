from pydantic import BaseModel


class Token(BaseModel):
    type: str = 'Bearer'
    token: str
