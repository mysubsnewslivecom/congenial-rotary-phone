from os import getenv, path
from pathlib import Path

import dj_database_url

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
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    "django_celery_results",
    "crispy_forms",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rest_framework",
]

LOCAL_APPS = [
    "main.home.apps.HomeConfig",
    "main.api.apps.ApiConfig",
    "main.gitsvn.apps.GitsvnConfig",
    "main.health.apps.HealthConfig",
    "main.movieflex.apps.MovieflexConfig",
    "main.tasks.apps.TasksConfig",
    "main.system.apps.SystemConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
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
                "rotary_phone.context_processor.export_variables",
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
            "TEST": {
                # "ENGINE": "django.db.backends.sqlite3",
                # 'NAME': path.join(BASE_DIR, "db.sqlite3"),
                "NAME": "test",  # test database name
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
            "TEST": {
                # "ENGINE": "django.db.backends.sqlite3",
                # "NAME": BASE_DIR / "db.sqlite3",
                "NAME": "test",  # test database name
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

# CACHES = {
#     "default": {
#         "BACKEND": REDIS_BACKEND,
#         "LOCATION": REDIS_LOCATION,
#         "OPTIONS": {"CLIENT_CLASS": REDIS_CLIENT_CLASS},
#         "KEY_PREFIX": REDIS_KEY_PREFIX,
#     }
# }

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

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    path.join(BASE_DIR, "static"),
    "/var/www/static/",
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = path.join(BASE_DIR, "media")

FILE_DIR = path.join(BASE_DIR, "files")
DATA_DIR = path.join(BASE_DIR, "data")
BACKUP_DIR = path.join(getenv("BACKUP_DIR", DATA_DIR), "backup")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DJANGO_SU_EMAIL = getenv("DJANGO_SU_EMAIL")
DJANGO_SU_NAME = getenv("DJANGO_SU_NAME")
DJANGO_PORT = getenv("DJANGO_PORT", 8000)

log.debug(f"DJANGO_SU_EMAIL: {DJANGO_SU_EMAIL}")
log.debug(f"DJANGO_SU_NAME: {DJANGO_SU_NAME}")

# Auth model
AUTH_USER_MODEL = "home.User"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# login
LOGIN_REDIRECT_URL = "home:home_list_view"
LOGOUT_REDIRECT_URL = "/login"

CSRF_COOKIE_SECURE = True

# SLASH

APPEND_SLASH = False

# DJANGO REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    # General
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
    # Pagination
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": int(getenv("DJANGO_PAGINATION_LIMIT", 10)),
    # Render
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    # Permission/Authentication
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # Throttling
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/day", "user": "100000/day"},
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Rotary Phone API",
    "DESCRIPTION": "Timepass project on django",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}


TASK_DEFAULT_QUEUE = getenv("TASK_DEFAULT_QUEUE", "na")
log.info(REDIS_LOCATION)
log.info(INSTALLED_APPS)
