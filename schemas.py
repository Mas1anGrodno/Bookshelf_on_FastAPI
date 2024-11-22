from typing import Optional
from pydantic import BaseModel


# Схема для получения данных о книге
class BooksGet(BaseModel):
    name: str  # Название книги
    author: str  # Автор книги
    description: Optional[str] = None  # Описание книги, поле является необязательным


# Схема для добавления книги, наследует BooksGet
class BookAdd(BooksGet):
    id: int  # Добавляется поле id, которое является идентификатором книги


# Схема для возвращаемого результата при добавлении книги
class BookId(BaseModel):
    ok: bool = True  # Поле ок, по умолчанию значение True
    book_id: int  # Поле book_id, идентификатор книги
