import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

#Postgresを利用 'postgresql://ユーザー名:パスワード@ホスト/DB名'
#ローカルで動かすときのユーザー名、パスワード、ホスト名、DB名は、docker-composeファイルを参照のこと
DB_URL = "postgresql://root:qin@postqresql:5432/postgres"

engine = sqlalchemy.create_engine(DB_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)