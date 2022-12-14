import json
import sys
from os import getenv
from typing import Optional

import requests
import urllib3
from bs4 import BeautifulSoup as BS
from django.conf import settings
from loguru import logger
from requests import request

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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


class Ipify:
    def __init__(
        self,
        url: Optional[str] = getenv("IPIFY_BASEURL"),
        **kwargs,
    ):
        super().__init__()
        self.url = url
        assert self.url, "IPIFY_BASEURL is not provided"

    def get_ipify(self):

        resp = request(method="GET", url=str(self.url))
        if resp.status_code == 200:
            return resp.json()
        else:
            return json.dumps(
                {"statuscode": resp.status_code, "statusmessage": resp.text}, indent=4
            )


class WebScrapping:
    def __init__(
        self, url: Optional[str] = None, features: Optional[str] = "html.parser"
    ):
        self.url = url
        self.features = features

    def get_soup(self):
        content = requests.get(self.url).content
        soup = BS(content, features=self.features)
        return soup

    def get_soup_text(self):
        content = requests.get(self.url).text
        soup = BS(content, features=self.features)
        return soup
