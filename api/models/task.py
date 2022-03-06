from sqlalchemy import Column, Integer, String, ForeignKey

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

