from fastapi import APIRouter, Depends, HTTPException, status
from models.token import Token as TokenModel
from fastapi.security import OAuth2PasswordRequestForm
from services.user import authenticate_user
from datetime import timedelta

ACCESS_TOKEN_EXPIRE_MINUTES = 30

token_router = APIRouter()


@token_router.post('/token', response_model=TokenModel)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
