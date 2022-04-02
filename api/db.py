import asyncpg
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

# async_engine = create_async_engine(os.environ['DATABASE_URL'], echo=True)
# async_session = sessionmaker(
#     autocommit=False, autoflush=False, bind=connect_db.async_engine, class_=AsyncSession
# )
Base = declarative_base()

async def connect_db():
    return await asyncpg.connect(os.environ['DATABASE_URL'])
async def disconnect_db(conn):
    return await conn.close()
# async def get_db():
#     async with async_session() as session:
#         yield session
        