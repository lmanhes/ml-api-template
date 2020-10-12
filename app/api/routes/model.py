from fastapi import APIRouter

from app.background.tasks import ml_task
from app.database import schemas


router = APIRouter()


@router.post("/predict", status_code=202)
async def post_predict(inputs: schemas.MLInput):
    """
    Perform a model inference:

    The process is the following:
        - push job to a redis broker
        - the job will be handle by a free worker
        - the result will be pushed inside the backend redis database
        - go to /tasks/{task_id} to retrieve the state / result
    """
    task = ml_task.delay(inputs.dict())

    response_object = {
        'status': 'accepted',
        'data': {
            'task_id': task.id
        }
    }

    return response_object