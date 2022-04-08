import asyncio
import asyncpg
import os
from dotenv import load_dotenv
load_dotenv()

# HACK:一つの関数に機能を持たせすぎているので、クラスにして分ける
async def definition_db():
   
    conn = await asyncpg.connect(os.environ['DATABASE_URL'])

    # TODO: テーブルを消すのではなくaltertableで定義する
    await conn.execute('''
        DROP TABLE if exists tasks
    ''')
    await conn.execute('''
        CREATE TABLE tasks(
            id               uuid,
            task             text,
            user_id          UUID NOT NULL,
            sort_key         int NOT NULL default 0,
            due_date         date DEFAULT NULL,
            complete_date    date DEFAULT NULL,
            is_done          boolean DEFAULT False,
            create_at        timestamp NOT NULL DEFAULT NOW(),
            update_at        timestamp NOT NULL DEFAULT NOW(),
            primary key (id)
        );
    ''')
    await conn.close()
 
if __name__ == "__main__":
 
    asyncio.run(definition_db())
    