# from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()

@router.get("/todo/{id}")
async def get_task():
    pass

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)

@router.put("/todo/{id}")
async def edit_task():
    pass

@router.delete("/todo/{id}")
async def delete_task():
    pass
