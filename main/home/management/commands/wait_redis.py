import time

from django.core.management.base import BaseCommand
from django_redis import get_redis_connection
from main.utility.functions import LoggingService
import redis
from django.conf import settings


log = LoggingService()

class Command(BaseCommand):
    def handle(self, *args, **options):
        log.debug("Waiting for Redis...")
        conn = None
        sleep_timer = 3
        conn_string = settings.REDIS_LOCATION
        while not conn:
            try:
                conn = redis.Redis.from_url(conn_string)
                conn.ping()
            except Exception as e:
                msg = f"{str(e)}. Waiting {sleep_timer} second..."
                log.error((msg))
                conn = None
                time.sleep(sleep_timer)

        log.info("Redis available!")
