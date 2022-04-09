from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

from typing import List, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result

async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
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
            # select(
            #     task_model.Task.id,
            #     task_model.Done.id.isnot(None).label("done"),
            # ).outerjoin(task_model.Done)
        )
    )
    return result.all()
