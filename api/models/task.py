from sqlalchemy import Column, Integer, String, DateTime, Boolean
from api.db import Base

from sqlalchemy.dialects.postgresql import UUID
import uuid

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sort_key = Column(Integer)
    task = Column(String(1024))

    due_date = Column(DateTime)
    complete_date = Column(DateTime)
    is_done = Column(Boolean)
