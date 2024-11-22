from typing import Optional
from pydantic import BaseModel


class BooksGet(BaseModel):
    name: str
    author: str
    description: Optional[str] = None


class BookAdd(BooksGet):
    id: int


class BookId(BaseModel):
    ok: bool = True
    book_id: int
