from typing import Annotated
from fastapi import APIRouter, Depends
from repository import BookRepository
from schemas import BookAdd, BookId, BooksGet

router = APIRouter(
    prefix="/books",
    tags=["Bookshelf"],
)


@router.post("")
async def add_book(book: Annotated[BooksGet, Depends()]) -> BookId:
    book_id = await BookRepository.add_book(book)
    return {"book added": True, "book_id": book_id}


@router.get("")
async def get_book() -> list[BookAdd]:
    books = await BookRepository.get_all_books()
    return books
