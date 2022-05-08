from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from api.router import tasks

app = FastAPI()

load_dotenv()

ASYNC_DB_URL = os.environ['DATABASE_URL']
if ASYNC_DB_URL and ASYNC_DB_URL.startswith("postgres://"):
    ASYNC_DB_URL = ASYNC_DB_URL.replace("postgres://", "postgresql://", 1)
ASYNC_DB_URL = ASYNC_DB_URL.replace('postgresql', 'postgresql+asyncpg')

if not os.environ['DATABASE_URL'] == "postgres://":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=os.environ['ORIGINS'],

        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        max_age=60,
    )

app.include_router(tasks.router)

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}