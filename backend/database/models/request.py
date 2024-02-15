import enum
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column

from database.connection import Base


class RequestStatusChoices(enum.Enum):
    Pending = 'Pending'
    Completed = 'Completed'
    Rejected = 'Rejected'


class Request(Base):
    __tablename__ = 'request'

    id = Column(UUID, primary_key=True, unique=True, default=uuid4)
    body = Column(String, nullable=False)
    status = Column(
        Enum(RequestStatusChoices),
        default=RequestStatusChoices.Pending.value,
        nullable=False
    )
    processed_by = mapped_column(ForeignKey('operator.id'), nullable=False)
