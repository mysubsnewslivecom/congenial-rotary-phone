import sys
from os import getenv
from typing import Optional

from django.conf import settings
from loguru import logger
from requests import request


class LoggingService:
    def __init__(
        self,
        debug: Optional[bool] = settings.DEBUG,
        **kwargs,
    ):
        super().__init__()
        logger.remove()
        self.set_log_level()

    def set_log_level(self):
        level = "DEBUG" if settings.DEBUG else "INFO"
        format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> |"
            "<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:"
            "<cyan>{line}</cyan> - <level>{message}</level>"
        )
        logger.add(sink=sys.stderr, format=format, level=level)
        # logger.add(sink=sys.stderr, level=level)

    def info(self, message):
        logger.info(message)

    def warn(self, message):
        logger.warning(message)

    def debug(self, message):
        logger.debug(message)

    def error(self, message):
        logger.error(message)


class OpenWeather:
    def __init__(
        self,
        open_weather_key: Optional[str] = getenv("OPEN_WEATHER_API_KEY"),
        open_weather_url: Optional[str] = getenv("OPEN_WEATHER_BASEURL"),
        **kwargs,
    ):
        super().__init__()
        # self.open_weather_key = settings.OPEN_WEATHER_API_KEY
        # self.open_weather_url = settings.OPEN_WEATHER_BASEURL
        self.open_weather_key = open_weather_key
        self.open_weather_url = open_weather_url
        self.log = LoggingService()

        assert self.open_weather_key, "OPEN_WEATHER_API_KEY is not provided"
        assert self.open_weather_url, "OPEN_WEATHER_BASEURL is not provided"

    def get_weather(self, location: str = "Krakow"):

        OPEN_WEATHER_URL = "".join(
            [
                str(self.open_weather_url),
                location,
                "&appid=",
                str(self.open_weather_key),
            ]
        )

        resp = request(url=OPEN_WEATHER_URL, method="GET")

        return resp.json()
