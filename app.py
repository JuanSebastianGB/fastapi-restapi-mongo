from fastapi import FastAPI
from routes.user import user_router
from routes.auth import auth_router
from config.db import client

app = FastAPI()

db = client.local


@app.get('/')
def index():
    if client:
        print('Connected to MongoDB!')
    else:
        print('Failed to connect to MongoDB...')


app.include_router(user_router, prefix='/api/v1', tags=['users'])
app.include_router(auth_router, prefix='/api/v1', tags=['secure'])
