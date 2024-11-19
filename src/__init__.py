from fastapi import FastAPI
from src.book_app.routes import book_router
from src.users.routers import user_router
from contextlib import asynccontextmanager
from src.db.main import init_db, get_session


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server has been started...............")
    await init_db()
    yield
    print("Server has been stopped................")


app = FastAPI(name="CRUDS", lifespan=life_span)

app.include_router(book_router, prefix='/api/book')
app.include_router(user_router, prefix='/api/user')