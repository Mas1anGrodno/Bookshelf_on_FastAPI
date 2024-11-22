import logging
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from database import BookShelfOrm, new_session
from schemas import BookAdd, BooksGet

logging.basicConfig(level=logging.INFO)


class BookRepository:
    @classmethod
    async def add_book(cls, data: BooksGet) -> int:
        async with new_session() as session:
            try:
                book_dict = data.model_dump()  # Приводим полученные данные к типу - словарь

                book = BookShelfOrm(**book_dict)  # Создаем объект с помощью ORM из полученных данных
                session.add(book)  # Добавляем объект в сессию
                await session.flush()  # Фиксируем изменения в сессии
                await session.commit()  # Сохраняем изменения в базе данных

                logging.info(f"Книга добавлена: {book}")
                return book.id  # Возвращаем ID добавленной книги

            except SQLAlchemyError as e:
                logging.error(f"Ошибка при добавлении книги: {e}")
                await session.rollback()  # Откатываем изменения в случае ошибки
                raise e

    @classmethod
    async def get_all_books(cls) -> list[BookAdd]:
        async with new_session() as session:
            try:
                query = select(BookShelfOrm)  # Создаем запрос для выбора всех записей из таблицы BookShelfOrm
                result = await session.execute(query)  # Выполняем запрос
                book_models = result.scalars().all()  # Используем scalars() для получения всех результатов
                book_schemas = [BookAdd.model_validate(book.__dict__) for book in book_models]  # Преобразуем объекты ORM в схемы Pydantic

                logging.info("Все книги получены")
                return book_schemas  # Возвращаем список схем Pydantic

            except SQLAlchemyError as e:
                logging.error(f"Ошибка при получении книг: {e}")
                raise e
