from fastapi import APIRouter
from pydantic import UUID4

from api.handlers.request import (
    create_request,
    delete_request,
    get_request,
    get_all_requests,
    update_request
)
from api.validation.request import Request


requests_router = APIRouter(
    prefix='/requests'
)

@requests_router.get('/', status_code=200)
async def get_all() -> list[Request]:
    client_info = await get_all_requests()
    return client_info

@requests_router.post('/', status_code=201)
async def create(client: Request) -> None:
    await create_request(client)

@requests_router.get('/{id}', status_code=200)
async def get(id: UUID4) -> Request:
    client_info = await get_request(id)
    return client_info

@requests_router.put('/{id}', status_code=200)
async def update(id: UUID4, client: Request) -> None:
    await update_request(id, client)

@requests_router.delete('/{id}', status_code=200)
async def delete(id: UUID4) -> None:
    await delete_request(id)
