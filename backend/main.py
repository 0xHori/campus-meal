from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI()

# Настройки CORS 
# разрешённые порты ФРОНТЕНДЕРУ ВЕНЕ К ОСМОТРУ:
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Разрешаемые методы(сейчас: все)
    allow_headers=["*"],
)

# Столовая и её структура
class Canteen(BaseModel):
    id: int
    name: str
    address: str

# заглушка вместо бдшки
fake_canteens_db = [
    {"id": 1, "name": "Юнифуд", "address": "ул. Вернадская, 78"},
    {"id": 2, "name": "ИПТИП столовая", "address": "ул. Вернадская, 87"},
]

# Эндпоинты
@app.get("/api/v1/canteens", response_model=List[Canteen])
async def get_canteens():
    # Здесь должен быть запрос к БД
    return fake_canteens_db

# КОМАНДА ДЛЯ ЗАПУСКА:
# python -m uvicorn app.main:app --reload