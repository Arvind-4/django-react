from backend.env import config
from backend.settings.base import BASE_DIR

DJANGO_VERCEL = config("DJANGO_VERCEL", default=True, cast=bool)

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if DJANGO_VERCEL:
    DATABASES = {}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
