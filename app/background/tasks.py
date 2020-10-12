from celery import Task

from core.model import BadassModel
import settings


class MLTask(Task):

    def __init__(self):
        super().__init__()
        self.model = None

        # dynamically adding a name to the task object
        self.name = f"{__name__}.ml_task"

    def initialize(self):
        from_s3 = settings.FROM_S3 == "True"
        self.model = BadassModel(from_s3=from_s3)

    def run(self, inputs):
        if self.model is None:
            self.initialize()

        return {"result": self.model.predict(**inputs)}


ml_task = MLTask()