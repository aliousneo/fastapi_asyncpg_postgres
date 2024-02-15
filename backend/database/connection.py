import os
from typing import ClassVar, Self

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DBConnection:
    db_address: str
    engine: AsyncEngine
    session_factory: async_sessionmaker[AsyncSession]
    instance: ClassVar[Self|None] = None

    __slots__ = (
        'db_address',
        'engine',
        'session_factory'
    )

    @classmethod
    def __new__(cls: type[Self], *args, **kwargs) -> Self:
        if cls.instance is not None:
            return cls.instance
        return object.__new__(cls)

    def __init__(self) -> None:
        if self.__class__.instance is not None:
            return
        self.db_address = os.environ['DATABASE_ADDRESS']
        self.engine = create_async_engine(self.db_address)
        self.session_factory = async_sessionmaker(self.engine, expire_on_commit=True)
        self.__class__.instance = self
