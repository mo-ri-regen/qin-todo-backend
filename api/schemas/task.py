from typing import Optional

from pydantic import BaseModel, Field
import datetime

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    
class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    task: Optional[str] = Field(None, example="クリーニングを取りに行く!!")
    update_at:str = Field(str(datetime.datetime.now()), example="2021-02-03T10:01:48.206968")
    class Config:
        orm_mode = True
            
class Task(TaskBase):
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True