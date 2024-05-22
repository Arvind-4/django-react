from backend.env import config
from backend.settings.base import *


DEBUG = config("DJANGO_DEBUG", cast=bool)
SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    config("DJANGO_ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])
)


STATIC_URL = "static/"
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]

STATIC_ROOT = BASE_DIR.parent / 'staticfiles_build' / 'static'
MEDIA_ROOT = BASE_DIR.parent / 'mediafiles_build' / 'media'

APPEND_SLASH = True
ADMIN_URL = config("DJANGO_ADMIN_URL", cast=str)
REACT_BASE_TEMPLATE = BASE_DIR / "templates" / "react" / "index.html"

DJANGO_LIVE = config("DJANGO_LIVE", cast=bool)
if DJANGO_LIVE:
    from backend.https import *  # noqa

from backend.email import *  # noqa
from backend.db import *  # noqa
