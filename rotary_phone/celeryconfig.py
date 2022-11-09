import os

import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rotary_phone.settings")
django.setup()

# Celery
accept_content = ["application/json"]
broker_url = getattr(settings, "REDIS_LOCATION")
redis_db = settings.REDIS_DB
redis_host = settings.REDIS_HOST
redis_password = settings.REDIS_PASSWORD
redis_port = settings.REDIS_PORT
redis_username = settings.REDIS_USERNAME
result_accept_content = ["application/json"]
result_backend = "django-db"
result_expires = 0
result_extended = True
task_serializer = "json"
task_track_started = True
timezone = os.environ.get("CELERY_TIMEZONE", "Europe/Zurich")
