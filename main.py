from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from schemas import BookAdd


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Дропаем базу базу")
    await create_tables()
    print("Стартуем базу")
    yield
    print("Тушим базу")


app = FastAPI(lifespan=lifespan)


bookShelf = []
