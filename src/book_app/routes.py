from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from typing import List
from .schema import BookSchema, CreateBookSchema, UpdateBookSchema
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.book_app.service import BookService

book_router = APIRouter()
book_service = BookService()


@book_router.get("/get_books", response_model=List[BookSchema])
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_book(session=session)
    return [BookSchema(**book.model_dump()) for book in books]


@book_router.get("/{book_id}", response_model=BookSchema)
async def get_book(book_id: str, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_id, session=session)
    if book:
        return BookSchema(**book.model_dump())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=BookSchema)
async def create_book(book_data: CreateBookSchema, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data=book_data, session=session)
    return BookSchema(**new_book.model_dump())


@book_router.patch("/{book_id}", response_model=BookSchema)
async def update_book(book_id: str, update_book_data: UpdateBookSchema,
                      session: AsyncSession = Depends(get_session)) -> BookSchema:
    updated_book = await book_service.update_book(book_id, update_book_data, session)
    if updated_book:
        return BookSchema(**updated_book.model_dump())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found with given ID")


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str, session=Depends(get_session)) -> None:
    result = await book_service.delete_book(book_id, session=session)
    if result:
        return None
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found with given ID")
