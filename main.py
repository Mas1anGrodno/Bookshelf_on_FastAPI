from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as bookshelfRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Дропаем базу базу")
    await create_tables()
    print("Стартуем базу")
    yield
    print("Тушим базу")


app = FastAPI(lifespan=lifespan)
app.include_router(bookshelfRouter)
