from models.user import User as UserModel
from models.token import TokenData
from config.db import client
from schemas.user import user_schema
from bson.objectid import ObjectId
from utils.encrypt_verify import verify_password
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi import status, HTTPException
from jose import JWTError, jwt
from utils.jwt import SECRET_KEY, ALGORITHM


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_users():
    users = client.fast.users.find()
    return [user_schema(user) for user in users]


def create_user(user: UserModel):
    userDict = user.dict()
    del userDict["id"]
    id = client.fast.users.insert_one(userDict).inserted_id
    created_user = user_schema(client.fast.users.find_one({"_id": id}))
    return UserModel(**created_user)


def get_user_by_id(id: str):
    user = client.fast.users.find_one({"_id": ObjectId(id)})
    if not user:
        return None
    return UserModel(**user_schema(user))


def update_user(id: str, user: UserModel):
    user_dictionary = user.dict()
    if user_dictionary.get("id"):
        del user_dictionary["id"]
    user_updated = client.fast.users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": user_dictionary}, return_document=True)
    return None if user_updated is None else UserModel(**user_schema(user_updated))


def delete_user(id: str):
    response = client.fast.users.find_one_and_delete({"_id": ObjectId(id)})
    return None if response is None else UserModel(**user_schema(response))


def authenticate_user(user: UserModel) -> bool | UserModel:
    user_db = client.fast.users.find_one({"username": user.username})
    if not user_db:
        return False
    if not verify_password(user_db["password"], user.password):
        return False
    return UserModel(**user_schema(user_db))


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = client.fast.users.find_one({"username": token_data.username})
    if user is None:
        raise credential_exception
    return UserModel(**user_schema(user))


async def get_current_active_user(current_user: UserModel = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
