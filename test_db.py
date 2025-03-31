import asyncio
from app.database import init_db
from app.models import Car, Brand

async def test_db():
    await init_db()
    
    # Crear una nueva marca
    brand = Brand(name="Toyota")
    await brand.insert()
    print(f"Marca insertada: {brand}")

    # Crear un nuevo automóvil
    car = Car(model="Corolla", description="Sedán compacto", price=15000, mileage=50000, brand_id=brand.id)
    await car.insert()
    print(f"Auto insertado: {car}")

asyncio.run(test_db())
