from pydantic import BaseModel
import os

class Settings(BaseModel):
    mongo_uri: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    db_name: str = os.getenv("DB_NAME", "demo_db")

settings = Settings()

def get_settings():
    return settings
