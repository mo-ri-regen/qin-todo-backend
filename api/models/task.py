from sqlalchemy import Column, Integer, String, DateTime, Boolean
from api.db import Base

import uuid
from sqlalchemy_utils import UUIDType

from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    sort_key = Column(Integer)
    # TODO: firebaseに登録されているユーザIDを登録する
    user_id = Column(UUIDType(binary=False), default=uuid.uuid4)
    task = Column(String(1024))

    due_date = Column(DateTime)
    complete_date = Column(DateTime)
    is_done = Column(Boolean)

    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now)
    