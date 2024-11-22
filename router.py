import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from repository import BookRepository
from schemas import BookAdd, BookId, BooksGet

# Создание экземпляра маршрутизатора
router = APIRouter(
    prefix="/books",
    tags=["Bookshelf"],
)


# Маршрут для добавления новой книги
@router.post("", response_model=BookId, status_code=status.HTTP_201_CREATED)
async def add_book(book: Annotated[BooksGet, Depends()]) -> BookId:
    try:
        book_id = await BookRepository.add_book(book)  # Добавляем книгу в базу данных и получаем её ID
        logging.info(f"Добавлена книга с ID: {book_id}")
        return {"book added": True, "book_id": book_id}  # Возвращаем статус и ID добавленной книги
    except Exception as e:
        logging.error(f"Ошибка при добавлении книги: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка при добавлении книги")


# Маршрут для получения всех книг
@router.get("", response_model=list[BookAdd])
async def get_book() -> list[BookAdd]:
    try:
        books = await BookRepository.get_all_books()  # Получаем список всех книг
        logging.info("Получен список всех книг")
        return books  # Возвращаем список книг
    except Exception as e:
        logging.error(f"Ошибка при получении книг: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка при получении книг")
