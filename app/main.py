from fastapi import FastAPI
from app.database import init_db
from app.routers import car
from app.middleware.logging import LogRequestsMiddleware
from app.exceptions.handlers import register_exception_handlers

app = FastAPI()
app.include_router(car.router)
app.add_middleware(LogRequestsMiddleware)
register_exception_handlers(app)

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "API de Gestión de Automóviles"}