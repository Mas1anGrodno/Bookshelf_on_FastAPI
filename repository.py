from sqlalchemy import select
from database import BookShelfOrm, new_session
from schemas import BooksGet


class BookRepository:
    @classmethod
    async def add_book(cls, data: BooksGet) -> int:
        async with new_session() as session:
            book_dict = data.model_dump()  # вызываем метод, чтобы получить словарь

            book = BookShelfOrm(**book_dict)  # создаем объект с помощью ОРМ из полученных данных
            session.add(book)
            await session.flush()
            await session.commit()
            return book.id

    # async def delete_book(cls):
    #     pass

    @classmethod
    async def get_all_books(cls) -> list[BooksGet]:
        async with new_session() as session:
            query = select(BookShelfOrm)
            result = await session.execute(query)
            book_models = result.scalars().all()  # используем scalars() для получения всех результатов
            book_schemas = [BooksGet.model_validate(book_models) for books_model in book_schemas]
            return book_schemas
