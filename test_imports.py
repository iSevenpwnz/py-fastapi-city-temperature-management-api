try:
    print("Тестуємо імпорти...")

    print("1. Основні модулі...")
    from database import Base, engine, SessionLocal

    print("2. City модулі...")
    from city.models import DBCity
    from city.schemas import City, CityCreate
    from city import crud as city_crud
    from city.router import router as city_router

    print("3. Temperature модулі...")
    from temperature.models import DBTemperature
    from temperature.schemas import Temperature, TemperatureCreate
    from temperature import crud as temp_crud
    from temperature.router import router as temp_router

    print("4. Dependencies...")
    from dependencies import get_db

    print("5. Main app...")
    from main import app

    print("Всі імпорти успішні!")

except Exception as e:
    print(f"Помилка імпорту: {e}")
    import traceback

    traceback.print_exc()
