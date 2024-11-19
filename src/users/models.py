from datetime import datetime

from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects import postgresql as pg
from uuid import UUID, uuid4


class UserModel(SQLModel, table=True):
    __tablename__ = "users"

    uuid: UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            nullable=False,
            default=uuid4
        )
    )
    username: str
    first_name: str
    last_name: str
    email: str = Field(max_length=20, unique=True)
    is_verified_user: bool = Field(default=False)
    password_hash: str
    created_at: datetime
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP,
                         default=datetime.now
                         )
    )

    def __repr__(self):
        return self.username
