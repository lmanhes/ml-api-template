from fastapi import APIRouter

from app.api.routes import model, tasks

api_router = APIRouter()
api_router.include_router(model.router, tags=["model"], prefix="/model")
api_router.include_router(tasks.router, tags=["tasks"], prefix="/tasks")