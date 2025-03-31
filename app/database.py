import os
from app.models import Car, Brand
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URL)
    database = client.get_database()
    await init_beanie(database=database, document_models=[Car, Brand])

    