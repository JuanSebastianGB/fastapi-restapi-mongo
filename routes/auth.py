from fastapi import APIRouter
from config.db import client
from models.user import User as UserModel
from services import user as user_service
auth_router = APIRouter()


@auth_router.post('/login')
def login(user: UserModel):
    result = user_service.authenticate_user(user)
    if  not result:
        return {"message": "Invalid credentials"}
    return {"message": "login"}


@auth_router.post('/register')
def register():
    return {"message": "register"}
