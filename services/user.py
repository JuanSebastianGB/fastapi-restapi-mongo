from models.user import User as UserModel
from config.db import client
from schemas.user import user_schema
from bson.objectid import ObjectId


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

# print(f"user--------------------------{user}")


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
