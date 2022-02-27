import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

#Postgresを利用 'postgresql://ユーザー名:パスワード@ホスト/DB名'
#ローカルで動かすときのユーザー名、パスワード、ホスト名、DB名は、docker-composeファイルを参照のこと
ASYNC_DB_URL = "postgresql://root:qin@postqresql:5432/postgres"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)
Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session