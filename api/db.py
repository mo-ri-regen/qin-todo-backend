import asyncpg

async def get_db():
    async with async_session() as session:
        yield session
async def connect_db():
    return await asyncpg.connect(os.environ['DATABASE_URL'])
async def disconnect_db(conn):
    return await conn.close()
        