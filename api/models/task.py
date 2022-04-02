from sqlalchemy import Column, Integer, String, DateTime, Boolean
from api.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    sort_key = Column(Integer)
    task = Column(String(1024))

    due_date = Column(DateTime)
    complete_date = Column(DateTime)
    is_done = Column(Boolean)
