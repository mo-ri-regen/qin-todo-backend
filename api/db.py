from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

#Postgresを利用 'postgresql://ユーザー名:パスワード@ホスト/DB名'
#ローカルで動かすときのユーザー名、パスワード、ホスト名、DB名は、docker-composeファイルを参照のこと
ASYNC_DB_URL = "postgresql+asyncpg://root:qin@postqresql:5432/postgres"

engine = create_async_engine(ASYNC_DB_URL, echo=True)
Session = scoped_session(
            sessionmaker(
                autocommit = False,
                autoflush = False,
                bind = engine,
                class_=AsyncSession))

Base = declarative_base()


async def get_db():
    async with Session() as session:
        yield session