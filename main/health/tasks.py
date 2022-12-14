from time import sleep

from celery import current_task, shared_task, states
from celery.exceptions import TaskError
from django.core.management import call_command

from main.utility.functions import LoggingService

log = LoggingService()


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        log.info(i)
        sleep(1)

    return {"status": "completed"}


@shared_task(bind=True, name="trigger_actions")
def trigger_actions(self, *args, **kwargs):
    try:
        log.info("Run trigger health actions")
        message = "Trigger health actions"
        current_task.update_state(state=states.STARTED, meta={"name": "data_dump"})
        call_command("reload_health")
    except Exception as ex:
        log.error(ex)
        self.update_state(
            state=states.FAILURE,
        )
        raise TaskError()

    return {"status": states.SUCCESS, "message": f"{message}. Task completed."}
