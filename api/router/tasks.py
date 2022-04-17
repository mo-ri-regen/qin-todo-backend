# from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List
from uuid import UUID
import api.schemas.task as task_schema
import api.cruds.task as task_crud
import api.models.task as task_model
from api.db import get_db

router = APIRouter()

class TaskIn(BaseModel):
    task: str = Field(None, example="クリーニング")
    sortKey: int = Field(0, example=0)
    dueDate: date = Field(None, example="2022-04-01")
    completeDate: date = Field(None, example="2022-04-28")
    isDone: bool = Field(False, example=False)
    
class TaskOut(BaseModel):
    id: str
    task: str
    userId: str
    sortKey: int
    dueDate: str
    completeDate: str
    isDone: bool
    createAt: datetime
    updateAt: datetime

def task_cls_req_serializer(task:TaskIn) -> task_schema.TaskCreate:
    retuen_task = task_schema.TaskCreate()
    retuen_task.task = str(task.task)
    retuen_task.sort_key = int(task.sortKey)
    retuen_task.due_date = task.dueDate
    retuen_task.complete_date = task.completeDate
    retuen_task.is_done = task.isDone
    return retuen_task
    
@router.get("/todo/{id}", response_model=TaskOut)
async def get_task():
    pass

@router.get("/tasks", response_model=List[TaskOut])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)

@router.post("/tasks")
async def create_task(
    task_body: TaskIn, db: AsyncSession = Depends(get_db)
):
    task:task_schema.TaskCreate = task_cls_req_serializer(task_body)
    return await task_crud.create_task(db, task)

@router.put("/todo/{id}")
async def edit_task(
    task_id: UUID, task_body: TaskIn, db: AsyncSession = Depends(get_db)
):
    task_in: task_schema.TaskCreate = task_cls_req_serializer(task_body)
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, task_in, original=task)

@router.delete("/todo/{id}")
async def delete_task():
    pass





