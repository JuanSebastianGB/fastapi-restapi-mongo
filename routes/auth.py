from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.post('/login')
def login():
    return {"message": "login"}


@auth_router.post('/register')
def register():
    return {"message": "register"}
