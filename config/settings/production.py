"""Production settings."""

from .base import *  # NOQA
from .base import env

# Base
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

"""
# Databases
DATABASES["default"] = env.db("DATABASE_URL")  # NOQA
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # NOQA
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # NOQA
"""
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
            "SOCKET_CONNECT_TIMEOUT": 5,  # seconds
            "SOCKET_TIMEOUT": 1800,  # seconds
        },
        "TIMEOUT": None,
    }
}

SELECT2_CACHE_BACKEND = "default"
