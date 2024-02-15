
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.base import main_router
from api.routes.client import clients_router
from api.routes.requests import requests_router
from database.migrations.executor import run_migrations, drop_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await run_migrations()
    yield
    await drop_tables()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']

)
app.include_router(main_router)
app.include_router(clients_router)
app.include_router(requests_router)
