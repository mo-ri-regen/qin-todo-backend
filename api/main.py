from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from api.router import tasks

app = FastAPI()

load_dotenv()
ASYNC_DB_URL = (os.environ['DATABASE_URL']).replace('postgresql', 'postgresql+asyncpg')

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ['ORIGINS'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=60,
)

app.include_router(tasks.router)
