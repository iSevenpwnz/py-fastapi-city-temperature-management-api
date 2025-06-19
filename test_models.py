from city.models import DBCity
from temperature.models import DBTemperature
from database import Base, engine, SessionLocal
import asyncio


async def test_models():
    try:
        print("Тестуємо моделі...")

        async with SessionLocal() as session:
            print("Сесія створена успішно")
            print("Тест пройшов!")
    except Exception as e:
        print(f"Помилка: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_models())
