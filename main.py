from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as bookshelfRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Удаляем существующую базу данных (если она есть)
    await delete_tables()
    print("Дропаем базу базу")

    # Создаем новую базу данных
    await create_tables()
    print("Стартуем базу")

    yield

    # Здесь можно добавить действия при завершении работы приложения (если нужно)
    print("Тушим базу")


# Инициализация FastAPI приложения с использованием lifespan
app = FastAPI(lifespan=lifespan)

# Подключение маршрутизатора
app.include_router(bookshelfRouter)
