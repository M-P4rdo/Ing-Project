from fastapi import APIRouter, Query
from app.schemas import CarCreate
from app import crud

router = APIRouter(prefix="/api/cars", tags=["cars"])

@router.get("/", summary="Obtener lista paginada de autos")
async def get_all_cars(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    cars = await crud.get_all_cars(skip=skip, limit=limit)
    return {
        "data": cars,
        "status": 200,
        "message": "Respuesta ok"
    }

@router.get("/{car_id}", summary="Obtener detalle de un auto")
async def get_car(car_id: str):
    car = await crud.get_car_by_id(car_id)
    return {
        "data": car,
        "status": 200,
        "message": "Respuesta ok"
    }

@router.post("/", summary="Agregar un nuevo auto")
async def create_car(car_data: CarCreate):
    car = await crud.create_car(car_data)
    return {
        "data": car,
        "status": 200,
        "message": "Auto creado correctamente"
    }
