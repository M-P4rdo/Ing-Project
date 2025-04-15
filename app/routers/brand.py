from fastapi import APIRouter
from app import crud
from app.schemas import BrandCreate
from beanie import PydanticObjectId

router = APIRouter(prefix="/api/brands", tags=["Brands"])

@router.get("/")
async def list_brands():
    brands = await crud.get_brands()
    return {"data": brands, "status": 200, "message": "Lista de marcas obtenida correctamente"}

@router.get("/{brand_id}")
async def get_brand(brand_id: PydanticObjectId):
    brand = await crud.get_brand_by_id(brand_id)
    return {"data": brand, "status": 200, "message": "Marca obtenida correctamente"}

@router.post("/")
async def create_brand(brand: BrandCreate):
    new_brand = await crud.create_brand(brand)
    return {"data": new_brand, "status": 201, "message": "Marca creada exitosamente"}
