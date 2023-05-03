from fastapi import APIRouter, status
from services import user as user_service
from models.user import User as UserModel
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token):
    return UserModel(
        username=token + "fakedecoded", email="john@example.com"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@user_router.get('/users/me', status_code=status.HTTP_200_OK)
def get_users(current_user: Annotated[str, Depends(get_current_user)]):
    """ Get all users """
    return current_user


@user_router.get('/users', status_code=status.HTTP_200_OK)
def get_users(token: Annotated[str, Depends(oauth2_scheme)]):
    """ Get all users """
    return user_service.get_users()


@user_router.get('/users/{user_id}', status_code=status.HTTP_200_OK)
def get_user(user_id: str):
    """ Get user by id """
    user_db = user_service.get_user_by_id(user_id)
    if not user_db:
        return {"message": "user not found"}
    return user_db


@user_router.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(user: UserModel):
    """ Create user"""
    created_user = user_service.create_user(user)
    return created_user


@user_router.put('/users/{user_id}', status_code=status.HTTP_200_OK)
def update_user(user_id: str, user: UserModel):
    """ Update user by id """
    updated_user = user_service.update_user(id=user_id, user=user)
    return updated_user


@user_router.delete('/users/{user_id}', status_code=status.HTTP_200_OK)
def delete_user(user_id: str):
    """ Delete user by id """
    return user_service.delete_user(id=user_id)
