from pydantic import BaseModel


class BooksGet(BaseModel):
    name: str
    author: str
    description: str | None


class BookAdd(BooksGet):
    id: int
