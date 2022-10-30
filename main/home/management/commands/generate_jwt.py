import jwt
import subprocess
from main.home.models import User
import datetime
from main.utility.functions import LoggingService
from django.conf import settings


log = LoggingService()


class GenerateJwt:
    def __init__(self) -> None:
        self.cmd = "openssl rand -hex 32"
        # self.SECRET_KEY = subprocess.getoutput(cmd=self.cmd)
        self.SECRET_KEY = settings.SECRET_KEY

    def generate_jwt(self, username: str):
        user = User.objects.get(username=username)
        payload = {
            "name": user.get_full_name(),
            "username": user.username,
            "email": user.email,
            "exp": round((datetime.datetime.now() + datetime.timedelta(1)).timestamp()),
            "iss": "Portal",
            "iat": round(datetime.datetime.now().timestamp()),
        }

        log.info(payload)
        token = jwt.encode(payload=payload, key=self.SECRET_KEY, algorithm="HS256")
        log.info(token)


def generate_jwt(username: str):
    user = User.objects.get(username=username)
    payload = {
        "name": user.get_full_name(),
        "username": user.username,
        "email": user.email,
        "exp": round(datetime.datetime.now().timestamp() + 24 * 60 * 60),
        "iss": "Portal",
        "iat": round(datetime.datetime.now().timestamp()),
    }
    log.info(payload)
