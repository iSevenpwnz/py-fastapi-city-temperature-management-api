from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Optional
from models import DBCity, DBTemperature

app = FastAPI(title="Simple City Temperature API")

# Синхронна база даних
SYNC_DATABASE_URL = "sqlite:///./city_temp_sync.db"
sync_engine = create_engine(
    SYNC_DATABASE_URL, connect_args={"check_same_thread": False}
)
SyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=sync_engine
)

# Створити таблиці
from database import Base

Base.metadata.create_all(bind=sync_engine)


# Залежність для отримання сесії
def get_sync_db():
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Схеми
class CityCreate(BaseModel):
    name: str
    additional_info: Optional[str] = None


class City(BaseModel):
    id: int
    name: str
    additional_info: Optional[str] = None

    class Config:
        from_attributes = True


# API endpoints
@app.post("/cities/", response_model=City, status_code=201)
def create_city(city: CityCreate, db: Session = Depends(get_sync_db)):
    # Перевірити чи існує місто
    existing = db.query(DBCity).filter(DBCity.name == city.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="City already exists")

    # Створити місто
    db_city = DBCity(name=city.name, additional_info=city.additional_info)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


@app.get("/cities/")
def get_cities(db: Session = Depends(get_sync_db)):
    return db.query(DBCity).all()


@app.get("/")
def root():
    return {"message": "Simple Sync API works!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
