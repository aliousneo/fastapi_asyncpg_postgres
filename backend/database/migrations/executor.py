from database.connection import DBConnection, Base
from database.migrations.initial import initial


async def run_migrations():
    migrations = (
        initial,
    )
    for migration in migrations:
        await migration()


async def drop_tables():
    async with DBConnection().engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
