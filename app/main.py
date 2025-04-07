from fastapi import FastAPI
from app.database import init_db
from app.routers import car

app = FastAPI()
app.include_router(car.router)

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "API de Gestión de Automóviles"}