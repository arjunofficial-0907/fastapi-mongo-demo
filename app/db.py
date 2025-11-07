from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from .config import get_settings

client: AsyncIOMotorClient | None = None
db: AsyncIOMotorDatabase | None = None

async def connect():
    global client, db
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client[settings.db_name]
    print("✅ MongoDB Connected")

async def disconnect():
    global client
    if client:
        client.close()
        print("✅ MongoDB Disconnected")

def get_db() -> AsyncIOMotorDatabase:
    if db is None:
        raise RuntimeError("❌ Database not initialized. Call connect() first.")
    return db
