from backend.env import config
from backend.settings.base import *


SECRET_KEY = config(
    "DJANGO_SECRET",
    cast=str,
    default="@ve-_t4@hn%dv8v_z75+33n@kz04wo5rk=tixitqn7ao-yt3p",
)

DEBUG = config("DJANGO_DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = ["*"]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]

STATIC_ROOT = BASE_DIR.parent / "static-cdn-local"
MEDIA_ROOT = BASE_DIR / "media"

ADMIN_URL = config("DJANGO_ADMIN_URL", default="admin")
APPEND_SLASH = True

REACT_BASE_TEMPLATE = BASE_DIR / "templates" / "react" / "index.html"

from backend.db import *  # noqa
