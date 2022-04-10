from typing import Optional

from pydantic import BaseModel, Field
from uuid import UUID
import datetime
from datetime import date

class TaskBase(BaseModel):
    task: Optional[str] = Field(None, example="クリーニング")
    sort_key:int =Field(0, example=0)
    due_date:date =Field(None, example="2022-04-01")
    complete_date:date = Field(None, example="2022-04-28")
    is_done:bool =Field(False, example=False)
    
class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    task: Optional[str] = Field(None, example="クリーニングを取りに行く!!")
    update_at:str = Field(str(datetime.datetime.now()), example="2021-02-03T10:01:48.206968")
    class Config:
        orm_mode = True
            
class Task(TaskBase):
    id:UUID
    sort_key=Field(0, example=0)
    task: Optional[str] = Field(None, example="クリーニングを取りに行く",description="タスク内容")
    
    user_id:UUID
    
    is_done: bool = Field(False, description="完了フラグ")
    create_at:date = Field(None, example="2022-04-28")
    update_at:date = Field(None, example="2022-04-28")

    class Config:
        orm_mode = True