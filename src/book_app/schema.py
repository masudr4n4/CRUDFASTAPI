from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class BookSchema(BaseModel):
    name: str
    type: str
    page_count: int
    publisher: str
    uid: UUID


class CreateBookSchema(BaseModel):
    name: str
    type: str
    page_count: int
    publisher: str
    available: bool
    language: str
    create_at: datetime
    updated_at: datetime


class UpdateBookSchema(BaseModel):
    name: str
    type: str
    page_count: int
    available: bool
