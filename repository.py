from sqlalchemy import select
from database import BookShelfOrm, new_session
from schemas import BooksGet


class bookRepository:
    @classmethod
    async def add_book(cls, data: BooksGet) -> int:
        async with new_session() as session:
            book_dict = data.model_dump  # приводим полученные данные к типу - словарь

            book = BookShelfOrm(**book_dict)  # создаем обьект с помощью ОРМ из полученных данных
            session.add(book)
            await session.flush()
            await session.commit()
            return book.id

    async def delete_book(cls):
        pass

    async def get_all_book(cls):
        async with new_session() as session:
            query = select(BookShelfOrm)
            result = await session.execute(query)
            task_models = result.scalar_all()  # погуглять про скаляр
            return task_models
