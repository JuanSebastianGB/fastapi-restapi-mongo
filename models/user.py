from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    username: str
    email: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "John Doe",
                "email": " email@gmail.com"
            }
        }
