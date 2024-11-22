from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

db_engine = create_async_engine("sqlite+aiosqlite:///Bookshelf.db")  # адрес к базе

new_session = async_sessionmaker(db_engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class BookShelfOrm(Model):
    __tablename__ = "Bookshelf"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author: Mapped[str]
    description: Mapped[Optional[str]]  # str | None  == Optional [str]


async def create_tables():
    async with db_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with db_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
