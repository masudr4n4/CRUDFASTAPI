from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects import postgresql as pg
from datetime import datetime
from uuid import UUID, uuid4


class BookModel(SQLModel, table=True):
    __tablename__ = "books"

    uid: UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            nullable=False,
            default=uuid4
        )
    )
    name: str
    type: str
    page_count: int
    publisher: str
    available: bool
    language: str
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP,
                         default=datetime.now
                         )
    )
    update_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP,
                         default=datetime.now
                         )
    )

    def __repr__(self):
        return self.name
