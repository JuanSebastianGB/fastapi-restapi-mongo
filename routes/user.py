from fastapi import APIRouter, status
from services import user as user_service
from models.user import User as UserModel

user_router = APIRouter()


@user_router.get('/users', status_code=status.HTTP_200_OK)
def get_users():
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
