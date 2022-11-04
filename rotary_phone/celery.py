from __future__ import absolute_import, unicode_literals

from os import environ

from celery import Celery

environ.setdefault("DJANGO_SETTINGS_MODULE", "rotary_phone.settings")
app = Celery(main="rotary_phone")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
