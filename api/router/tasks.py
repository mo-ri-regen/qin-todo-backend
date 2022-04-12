# from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
import api.schemas.task as task_schema
import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()

@router.get("/todo/{id}")
async def get_task():
    pass

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
    task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)
@router.put("/todo/{id}")
async def edit_task(
   task_id: UUID, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, task_body, original=task)    

@router.delete("/todo/{id}")
async def delete_task():
    pass
