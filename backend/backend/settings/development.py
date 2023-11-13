import os

from .common import *


SECRET_KEY = os.getenv("DJANGO_DEVELOPMENT_SECRET_KEY")

ALLOWED_HOSTS = os.getenv("DEVELOPMENT_ALLOWED_HOSTS").split(",")

INTERNAL_IPS = os.getenv("DEBUG_HOSTS").split(",")

DEBUG = True

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

INSTALLED_APPS += ["debug_toolbar"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "PORT": os.getenv("DB_PORT"),
    }
}
