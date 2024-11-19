from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import UserModel
from .schema import CreateUser
from .utils import generate_password_hash


class UserService:
    async def get_user_by_email(self, user_email: str, session: AsyncSession) -> UserModel:
        statement = select(UserModel).where(UserModel.email == user_email)
        result = await session.execute(statement)
        return result.scalars().first()

    async def user_exist(self, email: str, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)
        return user is not None

    async def create_user(self, user_data: CreateUser, session: AsyncSession):
        if not await self.user_exist(user_data.email, session):
            setattr(user_data, 'password_hash', generate_password_hash(user_data.password))
            user = UserModel(**user_data.model_dump())
            session.add(user)
            await session.commit()
            return user
        else:
            return None
