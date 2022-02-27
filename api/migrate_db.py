from sqlalchemy import create_engine
from api.models.task import Base

import os
from dotenv import load_dotenv
load_dotenv()
engine = create_engine(os.environ['DATABASE_URL'], echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()
    