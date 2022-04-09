from sqlalchemy import Column, Integer, String, DateTime, Boolean
from api.db import Base

import uuid
from sqlalchemy_utils import UUIDType

# def generate_uuid():
#     return str(uuid.uuid4())

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    sort_key = Column(Integer)
    user_id = Column(UUIDType(binary=False), default=uuid.uuid4)
    task = Column(String(1024))

    due_date = Column(DateTime)
    complete_date = Column(DateTime)
    is_done = Column(Boolean)
