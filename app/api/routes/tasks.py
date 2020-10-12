from fastapi import APIRouter, HTTPException

from app.background import celery_app


router = APIRouter()


@router.get("/{task_id}", response_model=dict)
def get_task_result(task_id: str):
    """
    Access to the tasks responsible for parsing stories
    """
    task = celery_app.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {'state': task.state, 'result': None}

    elif task.state != 'FAILURE':
        response = {'state': task.state, 'result': None}
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # Loading task for the first time can takes some time
        if task.info is None:
            # Loading task for the first time can takes some time
            raise HTTPException(status_code=404, detail=f"Task id : {task_id}, doesn't exists "
                                                        f"or the model has to load first")
        else:
            raise HTTPException(status_code=404, detail=task.info)

    return response
