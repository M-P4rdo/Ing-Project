from app.models import Car
from app.schemas import CarCreate
from fastapi import HTTPException

async def get_all_cars(skip: int = 0, limit: int = 10):
    return await Car.find_all().skip(skip).limit(limit).to_list()

async def get_car_by_id(car_id: str):
    car = await Car.get(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return car

async def create_car(car_data: CarCreate):
    car = Car(**car_data.dict())
    await car.insert()
    return car
