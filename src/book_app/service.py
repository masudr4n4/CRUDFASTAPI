from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .schema import UpdateBookSchema, CreateBookSchema
from .models import BookModel


class BookService:
    async def get_all_book(self, session: AsyncSession):
        statement = select(BookModel).order_by(BookModel.created_at)
        result = await session.exec(statement=statement)
        return result.all()

    async def get_book(self, book_id: str, session: AsyncSession):
        statement = select(BookModel).where(book_id == BookModel.uid)
        result = await session.exec(statement=statement)
        result = result.first()
        if result:
            return result
        else:
            return None

    async def create_book(self, book_data: CreateBookSchema, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = BookModel(**book_data_dict)
        session.add(new_book)
        await session.commit()
        return new_book

    async def update_book(self, book_id: str, book_data: UpdateBookSchema, session: AsyncSession):
        book_to_update = await self.get_book(book_id=book_id, session=session)
        if book_to_update:
            updated_data = book_data.model_dump()
            for key, value in updated_data.items():
                setattr(book_to_update, key, value)
            await session.commit()
            return await self.get_book(book_id, session)
        else:
            return None

    async def delete_book(self, book_id: str, session: AsyncSession):
        book_to_delete = await self.get_book(book_id=book_id, session=session)
        if book_to_delete:
            await session.delete(book_to_delete)
            await session.commit()
            return True
        else:
            return None
