from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, items
from .db import connect, disconnect

app = FastAPI(
    title="FastAPI + MongoDB Demo",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(users.router)
app.include_router(items.router)

@app.on_event("startup")
async def startup_event():
    await connect()

@app.on_event("shutdown")
async def shutdown_event():
    await disconnect()

@app.get("/", tags=["root"])
async def root():
    return {"message": "FastAPI MongoDB demo is running"}
