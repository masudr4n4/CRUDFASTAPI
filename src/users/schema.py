from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    email: str = Field(max_length=30)
    username: str
    first_name: str
    last_name: str
    password: str
    is_active: bool = False

    class Config:
        extra = "allow"


class User(BaseModel):
    email: str = Field(max_length=30)
    username: str
    first_name: str
    last_name: str
