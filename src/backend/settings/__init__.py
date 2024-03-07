from backend.env import config

DJANGO_LIVE = config("DJANGO_LIVE", cast=bool)
DJANGO_DEBUG = config("DJANGO_DEBUG", cast=bool)

if DJANGO_LIVE and not DJANGO_DEBUG:
    print("Using production settings")
    from backend.settings.production import *  # noqa
else:
    print("Using development settings")
    from backend.settings.dev import *  # noqa
