from pathlib import Path
from os import getenv, path
from loguru import logger
import dj_database_url
import sys
from main.utility.functions import LoggingService

DEBUG = bool(getenv("DJANGO_DEBUG", "True") == "True")

log = LoggingService()

# SECURITY WARNING: don't run with debug turned on in production!

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = path.dirname(path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("DJANGO_SECRET_KEY", None)

DEFAULT_HOST = ["127.0.0.1"]
DJANGO_ALLOWED_HOST = getenv("DJANGO_ALLOWED_HOST", default="127.0.0.1").split(",")
ALLOWED_HOSTS = list(DEFAULT_HOST) + [
    host for host in DJANGO_ALLOWED_HOST if host not in DEFAULT_HOST
]

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    "main.home.apps.HomeConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rotary_phone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            path.join(BASE_DIR, "templates"),
            path.join(
                BASE_DIR,
                "templates",
                "base",
            ),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rotary_phone.wsgi.application"

DB_SRC = getenv("DB_SRC", "local")
DJANGO_SCHEMA_NAME = getenv("DJANGO_SCHEMA_NAME")
DJANGO_CUSTOM_SCHEMA = getenv("DJANGO_CUSTOM_SCHEMA", "custom")
DJANGO_DB_ENGINE = getenv("DJANGO_DB_ENGINE", "NA")
DJANGO_DB_NAME = getenv("DJANGO_DB_NAME")
DJANGO_DB_USER = getenv("DJANGO_DB_USER")
DJANGO_DB_PASSWORD = getenv("DJANGO_DB_PASSWORD")
DJANGO_DB_HOST = getenv("DJANGO_DB_HOST")
DJANGO_DB_PORT = int(getenv("DJANGO_DB_PORT", default=5432))

if not DEBUG or DB_SRC == "PG":
    DATABASES = {
        "default": {
            "ENGINE": DJANGO_DB_ENGINE,
            "NAME": DJANGO_DB_NAME,
            "USER": DJANGO_DB_USER,
            "PASSWORD": DJANGO_DB_PASSWORD,
            "HOST": DJANGO_DB_HOST,
            "PORT": DJANGO_DB_PORT,
            "OPTIONS": {
                "connect_timeout": 5,
                "options": f"-c search_path={DJANGO_SCHEMA_NAME}",
            },
        },
        "custom": {
            "ENGINE": DJANGO_DB_ENGINE,
            "NAME": DJANGO_DB_NAME,
            "USER": DJANGO_DB_USER,
            "PASSWORD": DJANGO_DB_PASSWORD,
            "HOST": DJANGO_DB_HOST,
            "PORT": DJANGO_DB_PORT,
            "OPTIONS": {
                "connect_timeout": 5,
                "options": f"-c search_path={DJANGO_CUSTOM_SCHEMA}",
            },
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

DATABASE_URL = None
# DATABASE_URL = f"postgresql://{username}:{password}@{POSTGRES_HOST}:5432/adminlte?sslmode=disable"
DATABASE_URL = getenv("DATABASE_URL", DATABASE_URL)
if DATABASE_URL is not None:
    db_from_env = dj_database_url.config(
        default=DATABASE_URL, conn_max_age=500, ssl_require=True
    )
    DATABASES["default"].update(db_from_env)

CACHE_TTL = 60 * int(getenv("CACHE_TTL_SECS", 1500))

REDIS_HOST = getenv("REDIS_HOST")
REDIS_PORT = int(getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = getenv("REDIS_PASSWORD")
REDIS_CLIENT_CLASS = getenv("REDIS_CLIENT_CLASS")
REDIS_BACKEND = getenv("REDIS_BACKEND")
REDIS_USERNAME = getenv("REDIS_USERNAME", "default")
REDIS_KEY_PREFIX = getenv("REDIS_KEY_PREFIX", ROOT_URLCONF.split(".")[0])
REDIS_DB = getenv("REDIS_DB", 1)
REDIS_LOCATION = (
    f"redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
)

CACHES = {
    "default": {
        "BACKEND": REDIS_BACKEND,
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {"CLIENT_CLASS": REDIS_CLIENT_CLASS},
        "KEY_PREFIX": REDIS_KEY_PREFIX,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DJANGO_SU_EMAIL = getenv("DJANGO_SU_EMAIL")
DJANGO_SU_NAME = getenv("DJANGO_SU_NAME")

log.debug(f"DJANGO_SU_EMAIL: {DJANGO_SU_EMAIL}")
log.debug(f"DJANGO_SU_NAME: {DJANGO_SU_NAME}")
