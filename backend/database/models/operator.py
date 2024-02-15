from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from database.connection import Base


class Operator(Base):
    __tablename__ = 'operator'

    id = Column(UUID, primary_key=True, unique=True, default=uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
