from celery import Celery

from app.background.tasks import ml_task
import settings


celery_app = Celery(
        "celery_app",
        backend=settings.REDIS_URL,
        broker=settings.REDIS_URL
    )

celery_app.tasks.register(ml_task)

celery_app.conf.task_routes = {
    'app.background.tasks.ml_task': 'main-queue'
}