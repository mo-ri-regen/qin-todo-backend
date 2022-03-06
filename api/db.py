from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base


DB_URL = '{}://{}:{}@{}:{}/{}'.format("postgresql+asyncpg", "admin", "password", "db", "5432", "async_db")
engine = create_async_engine(DB_URL, echo=True)
Session = scoped_session(
            sessionmaker(
                autocommit = False,
                autoflush = False,
                bind = engine,
                class_=AsyncSession))

Base = declarative_base()

async def get_db():
    async with Session() as session:
        try:
            yield session
        finally:
            session.close()