from uuid import uuid4

from main.home.models import Audit
from main.utility.common import Status
from main.utility.functions import LoggingService


class AuditMixins:

    # def dispatch(self, request, *args, **kwargs):
    #     dispatch = super().dispatch(request, *args, **kwargs)
    #     self.log.info(f"{dispatch = }")
    #     payload = {
    #         "message": "dispatch",
    #         "status": "COMPLETED"
    #     }
    #     # audit = Audit(**payload)
    #     # audit.save()

    #     return dispatch

    def error(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.ERROR.value
        self.payload(**kwargs)

    def success(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.SUCCESS.value
        self.payload(**kwargs)

    def in_progress(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.IN_PROGRESS.value
        self.payload(**kwargs)

    def created(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.CREATED.value
        self.payload(**kwargs)

    def completed(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.COMPLETED.value
        self.payload(**kwargs)

    def skip(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.SKIPPED.value
        self.payload(**kwargs)

    def info(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.INFO.value
        self.payload(**kwargs)

    def debug(self, message=None, *args, **kwargs):
        if message is not None:
            kwargs["message"] = message
        kwargs["status"] = Status.DEBUG.value
        print(f"{kwargs = }")

        self.payload(**kwargs)

    def generate_uuid(self):
        task_id = uuid4()
        return str(task_id)

    def payload(self, *args, **kwargs):
        print(f"{kwargs = }")
        self.log = LoggingService()

        message = kwargs["message"]
        status = kwargs["status"]

        if status == "DEBUG":
            self.log.debug(message=message)
        elif status == "ERROR":
            self.log.error(message=message)
        else:
            self.log.info(message=message)

        audit = Audit(**kwargs)
        # audit.message = message
        # audit.status = status
        # audit.task_id = kwargs["task_id"] if 'task_id' in kwargs.keys() else None
        audit.save()
        # self.info("saved")
