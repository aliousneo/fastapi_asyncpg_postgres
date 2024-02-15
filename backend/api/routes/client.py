from fastapi import APIRouter
from pydantic import UUID4

from api.handlers.client import (
    create_client,
    delete_client,
    get_client,
    get_all_clients,
    update_client
)
from api.validation.client import Client


clients_router = APIRouter(
    prefix='/clients'
)

@clients_router.get('/', status_code=200)
async def get_all() -> list[Client]:
    client_info = await get_all_clients()
    return client_info

@clients_router.post('/', status_code=201)
async def create(client: Client) -> None:
    await create_client(client)

@clients_router.get('/{id}', status_code=200)
async def get(id: UUID4) -> Client:
    client_info = await get_client(id)
    return client_info

@clients_router.put('/{id}', status_code=200)
async def update(id: UUID4, client: Client) -> None:
    await update_client(id, client)

@clients_router.delete('/{id}', status_code=200)
async def delete(id: UUID4) -> None:
    await delete_client(id)
