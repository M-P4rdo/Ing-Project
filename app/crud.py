from app.models import Car, Brand
from app.schemas import CarCreate, BrandCreate
from app.exceptions.custom import NotFoundError

async def get_all_cars(skip: int = 0, limit: int = 10):
    return await Car.find_all().skip(skip).limit(limit).to_list()

async def get_car_by_id(car_id: str):
    car = await Car.get(car_id)
    if not car:
        raise NotFoundError("Auto no encontrado")
    return car

async def create_car(car_data: CarCreate):
    car = Car(**car_data.dict())
    await car.insert()
    return car

async def get_brands():
    return await Brand.find_all().to_list()

async def get_brand_by_id(brand_id: str):
    brand = await Brand.get(brand_id)
    if not brand:
        raise NotFoundError("Marca no encontrada")
    return brand

async def create_brand(brand_data: BrandCreate):
    brand = Brand(**brand_data.dict())
    await brand.insert()
    return brand