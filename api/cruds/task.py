from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import api.models.task as task_model
import api.schemas.task as task_schema

from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result
from uuid import UUID

from datetime import datetime

def task_res_serializer(task:task_model.Task) -> dict:
    return {
        "id": task["id"],
        "task": task["task"],
        "userId": task["user_id"],
        "sortKey": task["sort_key"],
        "dueDate": task["due_date"],
        "completeDate": task["complete_date"],
        "isDone": task["is_done"],
        "createAt": task["create_at"],
        "updateAt": task["update_at"]
    }
def task_cls_res_serializer(task:task_model.Task) -> dict:
    return {
        "id": str(task.id),
        "task": task.task,
        "userId": str(task.user_id),
        "sortKey": task.sort_key,
        "dueDate": task.due_date,
        "completeDate": task.complete_date,
        "isDone": task.is_done,
        "createAt": task.create_at,
        "updateAt": task.update_at
    }

async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> dict:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    task = task_cls_res_serializer(task)
    return task

async def get_tasks_with_done(db: AsyncSession) -> List:
    result: task_model.Task = await (
        db.execute(
            select(
                task_model.Task.id
                ,task_model.Task.task
                ,task_model.Task.user_id
                ,task_model.Task.sort_key
                ,task_model.Task.due_date
                ,task_model.Task.complete_date
                ,task_model.Task.is_done
                ,task_model.Task.create_at
                ,task_model.Task.update_at
            )
        )
    )
    tasks = []
    for task in result.all():
        tasks.append(task_res_serializer(task))
    json_compatible_tasks = jsonable_encoder(tasks)
    return JSONResponse(status_code=200, content=json_compatible_tasks)


async def get_task(db: AsyncSession, task_id: UUID) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

async def update_task(
    db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> dict:
    original.task = task_create.task
    original.sort_key = task_create.sort_key
    original.due_date = task_create.due_date
    original.complete_date = task_create.complete_date
    original.is_done = task_create.is_done
    original.update_at = datetime.now()
    
    db.add(original)
    await db.commit()
    await db.refresh(original)
    task = task_cls_res_serializer(task=original)
    return task