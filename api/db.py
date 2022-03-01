from sqlalchemy.orm import sessionmaker, declarative_base
import asyncio
import asyncpg

Base = declarative_base()

async def run():
    conn = await asyncpg.connect(user='root', password='qin',
                                 database='postgres', host='postqresql:5432')
    values = await conn.fetch(
        'SELECT * FROM done WHERE id = $1',
        10,
    )
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

if __name__ == '__main__':
    run()
