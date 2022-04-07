from sqlalchemy import Column, Integer, String, DateTime, Boolean
from api.db import Base

from sqlalchemy.dialects.postgresql import UUID
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Task(Base):
    __tablename__ = "tasks"

    uuid = Column(String, name="uuid", primary_key=True, default=generate_uuid)
    sort_key = Column(Integer)
    task = Column(String(1024))

    due_date = Column(DateTime)
    complete_date = Column(DateTime)
    is_done = Column(Boolean)
