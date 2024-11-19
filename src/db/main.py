from sqlmodel import create_engine, text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.config import Config
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

engine = AsyncEngine(
    create_engine(url=Config.DATABASE_URL, echo=True)
)


async def init_db():
    async with engine.begin() as conn:
        from src.book_app.models import BookModel
        from src.users.models import UserModel
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    s = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with s() as session:
        yield session
