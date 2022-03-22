# from fastapi import APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.task as task_schema
import api.cruds.task as task_crud
# from api.db import get_db

router = APIRouter()

@router.get("/todo/{id}")
async def get_task():
    pass

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
    # task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, **task_body.dict())

@router.put("/todo/{id}")
async def edit_task():
    pass

@router.delete("/todo/{id}")
async def delete_task():
    pass
