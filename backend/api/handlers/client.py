from pydantic import UUID4
from sqlalchemy import update, delete, select
from sqlalchemy.ext.asyncio import async_sessionmaker

from api.validation.client import Client
from database.connection import DBConnection
from database.models.client import Client as db_client


async def create_client(client: Client) -> None:
    new_client = client.to_db_model()

    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            session.add(new_client)
            await session.commit()

async def get_client(id: UUID4) -> Client:
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            dc_client = await session.get(db_client, {id})
            result = Client.from_db_model(dc_client)
            return result

async def get_all_clients() -> list[Client]:
    stmt = (
        select(db_client)
    )
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            all_clients = await session.scalars(stmt)
            result = [
                Client.from_db_model(client)
                for client in all_clients
            ]
            return result

async def update_client(id: UUID4, client: Client) -> None:
    stmt = (
        update(db_client)
        .where(db_client.id == id)
        .values(**client.__dict__)
    )
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            await session.execute(stmt)

async def delete_client(id: UUID4) -> None:
    stmt = (
        delete(db_client)
        .where(db_client.id == id)
    )
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            await session.execute(stmt)
