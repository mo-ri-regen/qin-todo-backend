from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.task as task_schema
import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks(db)

@router.get("/task/{task_id}", response_model=task_schema.Task)
async def list_tasks(task_id: int, db: AsyncSession = Depends(get_db)):
    return await task_crud.get_task(db, task_id)

@router.post("/task", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_crud.create_task(db, task_body)

@router.put("/task/{task_id}", response_model=task_schema.TaskCreateResponse)
async def create_task(task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await task_crud.update_task(db, task_id, task_body)
    print(task)
    return task

@router.delete("/task/{task_id}", response_model=None)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await task_crud.delete_task(db, task_id)