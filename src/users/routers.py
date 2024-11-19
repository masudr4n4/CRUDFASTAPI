from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi import APIRouter, Depends, HTTPException,status
from src.users.schema import CreateUser,User
from src.users.service import UserService
from src.db.main import get_session

user_router = APIRouter()
user_service = UserService()


@user_router.post("/signup", status_code= status.HTTP_201_CREATED,response_model=User)
async def create_user(user_data: CreateUser, session:AsyncSession= Depends(get_session)) -> User:
    user = await user_service.create_user(user_data, session)
    if user:
        return User(**user.model_dump())
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already exists")
