from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

CELERY_BROKER_URL = os.getenv("REDIS_URL")
CELERY_RESULT_BACKEND = os.getenv("REDIS_URL")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "DEBUG"},
}
