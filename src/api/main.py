from common.database import engine
from config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo import models
from todo.routers import router as todo_router

app = FastAPI()

app.include_router(todo_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize database on startup
@app.on_event("startup")
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
