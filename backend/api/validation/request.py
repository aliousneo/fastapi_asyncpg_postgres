from typing import Optional, Self

from pydantic import BaseModel, UUID4

from database.models.request import (
    Request as db_request,
    RequestStatusChoices
)


class Request(BaseModel):
    id: Optional[UUID4] = None
    body: str
    status: RequestStatusChoices
    processed_by: UUID4

    def to_db_model(self) -> db_request:
        return db_request(**self.__dict__)

    @classmethod
    def from_db_model(cls: type[Self], db_instance: db_request) -> Self:
        return cls(
            id=db_instance.id,
            body=db_instance.body,
            status=db_instance.status,
            processed_by=db_instance.processed_by
        )
