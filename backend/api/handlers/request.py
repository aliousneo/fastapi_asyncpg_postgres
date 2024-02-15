from pydantic import UUID4
from sqlalchemy import update, delete, select
from sqlalchemy.ext.asyncio import async_sessionmaker

from api.validation.request import Request
from database.connection import DBConnection
from database.models.request import Request as db_request


async def create_request(client: Request) -> None:
    new_client = client.to_db_model()

    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            session.add(new_client)
            await session.commit()

async def get_request(id: UUID4) -> Request:
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            dc_client = await session.get(db_request, {id})
            result = Request.from_db_model(dc_client)
            return result

async def get_all_requests() -> list[Request]:
    stmt = (
        select(db_request)
    )
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            all_clients = await session.scalars(stmt)
            result = [
                Request.from_db_model(client)
                for client in all_clients
            ]
            return result

async def update_request(id: UUID4, client: Request) -> None:
    stmt = (
        update(db_request)
        .where(db_request.id == id)
        .values(**client.__dict__)
    )
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            await session.execute(stmt)

async def delete_request(id: UUID4) -> None:
    stmt = (
        delete(db_request)
        .where(db_request.id == id)
    )
    async_session = async_sessionmaker(DBConnection().engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            await session.execute(stmt)
