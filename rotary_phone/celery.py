from __future__ import absolute_import, unicode_literals

from os import environ

from celery import Celery

from rotary_phone import celeryconfig

environ.setdefault("DJANGO_SETTINGS_MODULE", "rotary_phone.settings")
app = Celery(main="rotary_phone")

# app.config_from_object("django.conf:settings", namespace="CELERY")
app.config_from_object("django.conf:settings", namespace="celery")
app.config_from_object(celeryconfig)

app.autodiscover_tasks()

# print(f"{ app.conf.accept_content  = }")
# print(f"{ app.conf.broker_url  = }")
# print(f"{ app.conf.redis_db  = }")
# print(f"{ app.conf.redis_host  = }")
# print(f"{ app.conf.redis_password  = }")
# print(f"{ app.conf.redis_port  = }")
# print(f"{ app.conf.redis_username  = }")
# print(f"{ app.conf.result_accept_content  = }")
# print(f"{ app.conf.result_backend  = }")
# print(f"{ app.conf.result_expires  = }")
# print(f"{ app.conf.result_extended  = }")
# print(f"{ app.conf.task_serializer  = }")
# print(f"{ app.conf.task_track_started = }")
# print(f"{ app.conf.timezone  = }")


@app.task(
    bind=True,
)
def debug_task(self):
    print(f"Request: {self.request!r}")
