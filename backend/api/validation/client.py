from typing import Optional, Self

from pydantic import BaseModel, UUID4
from pydantic_extra_types.phone_numbers import PhoneNumber

from database.models.client import Client as db_client


class Client(BaseModel):
    id: Optional[UUID4] = None
    first_name: str
    last_name: str
    phone: PhoneNumber

    def to_db_model(self) -> db_client:
        return db_client(**self.__dict__)

    @classmethod
    def from_db_model(cls: type[Self], db_instance: db_client) -> Self:
        return cls(
            id=db_instance.id,
            first_name=db_instance.first_name,
            last_name=db_instance.last_name,
            phone=db_instance.phone
        )
