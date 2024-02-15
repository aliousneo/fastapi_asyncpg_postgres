from database.connection import Base, DBConnection


async def initial():
    await create_tables()

async def create_tables():
    async with DBConnection().engine.begin() as conn:
        print(Base)
        await conn.run_sync(Base.metadata.create_all)
