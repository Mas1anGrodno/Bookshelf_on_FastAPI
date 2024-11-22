from typing import Optional
import logging
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.exc import SQLAlchemyError

# Создание асинхронного движка для SQLite
db_engine = create_async_engine("sqlite+aiosqlite:///Bookshelf.db")  # адрес к базе

# Создание асинхронной сессии
new_session = async_sessionmaker(db_engine, expire_on_commit=False)


# Базовый класс для моделей ORM
class Model(DeclarativeBase):
    pass


# Модель для таблицы Bookshelf
class BookShelfOrm(Model):
    __tablename__ = "Bookshelf"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author: Mapped[str]
    description: Mapped[Optional[str]]  # str | None  == Optional [str]


# Функция для создания таблиц в базе данных
async def create_tables():
    try:
        async with db_engine.begin() as conn:
            await conn.run_sync(Model.metadata.create_all)
    except SQLAlchemyError as e:
        logging.error(f"Ошибка при создании таблиц: {e}")


# Функция для удаления таблиц из базы данных
async def delete_tables():
    try:
        async with db_engine.begin() as conn:
            await conn.run_sync(Model.metadata.drop_all)
    except SQLAlchemyError as e:
        logging.error(f"Ошибка при удалении таблиц: {e}")
