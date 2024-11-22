from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Дропаем базу базу")
    await create_tables()
    print("Стартуем базу")
    yield
    print("Тушим базу")


app = FastAPI(lifespan=lifespan)


class BooksGet(BaseModel):
    name: str
    author: str
    description: str | None


class BookAdd(BooksGet):
    id: int


bookShelf = []


@app.post("/books")
async def add_book(book: Annotated[BookAdd, Depends()]):
    bookShelf.append(book)
    return {"book added": True}


# @app.get("/books")
# def get_book():
#     book1 = BooksGet(name="123", author="456", description="hfhfhfhfhhf")
#     return {"data": book1}
