from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.shemas.task as task_shema

async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task