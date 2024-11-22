from typing import Annotated
from fastapi import APIRouter, Depends
from repository import bookRepository
from schemas import BookAdd

router = APIRouter(prefix="/books")


@router.post("")
async def add_book(book: Annotated[BookAdd, Depends()]):
    book_id = await bookRepository.add_book(book)
    return {"book added": True, "book_id": book_id}


@router.get("")
async def get_book():
    books = await bookRepository.get_all_book()
    return {"books": books}
