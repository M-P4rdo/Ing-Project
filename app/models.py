from beanie import Document
from typing import Optional
from pydantic import Field
from uuid import uuid4

class Brand(Document):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    name: str = Field(..., max_length=20)

    class Settings:
        collection = "brands"

class Car(Document):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    model: str = Field(..., max_length=30)
    description: Optional[str] = Field(None, max_length=100)
    price: float = Field(..., gt=0)
    mileage: int = Field(..., ge=0)
    brand_id: str = Field(...)

    class Settings:
        collection = "cars"