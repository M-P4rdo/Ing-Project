from pydantic import BaseModel, Field, validator
from typing import Optional

class CarCreate(BaseModel):
    model: str = Field(..., max_length=30)
    description: Optional[str] = Field(None, max_length=100)
    price: float = Field(..., gt=0)
    mileage: int = Field(..., ge=0)
    brand_id: str

    @validator("model")
    def validar_modelo(cls, value):
        if any(char in value for char in [";", "'", "--", "$", "{", "}"]):
            raise ValueError("El modelo contiene caracteres no permitidos.")
        return value

    @validator("description")
    def validar_descripcion(cls, value):
        if value and any(char in value for char in [";", "'", "--", "$", "{", "}"]):
            raise ValueError("La descripción contiene caracteres no permitidos.")
        return value

class BrandCreate(BaseModel):
    name: str = Field(..., max_length=20)