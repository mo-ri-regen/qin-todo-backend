from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

# import os
# from dotenv import load_dotenv

async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task
    
# async def create_task(db):

#     pass
#     load_dotenv()
#     conn = await asyncpg.connect(os.environ['DATABASE_URL'])

#     await conn.execute('''
#         INSERT INTO tasks(
#             task
#             ,user_id 
#             ,sort_key
#             ,due_date
#             ,complete_date
#             ,is_done
#         ) 
#         VALUES (
#             "タスク1"
#             ,12345
#             ,0
#             ,NOW()
#             ,NOW()
#             ,False
#         );
#     ''')
#     await conn.close()
