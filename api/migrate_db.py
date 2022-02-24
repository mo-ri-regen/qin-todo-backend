from sqlalchemy import create_engine

from api.models.task import Base

#Postgresを利用 'postgresql://ユーザー名:パスワード@ホスト/DB名'
#ローカルで動かすときのユーザー名、パスワード、ホスト名、DB名は、docker-composeファイルを参照のこと
DB_URL = "postgresql://root:qin@postqresql:5432/postgres"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
