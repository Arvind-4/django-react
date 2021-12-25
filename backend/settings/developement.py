from .base import *

SECRET_KEY = '@ve-_t4@hn%dv8v_z75+33n@kz04wo5rk=tixitqn7ao-yt3p'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1',]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

STATICFILES_DIRS = (
  BASE_DIR, 'assets',
)

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

ADMIN_URL = 'admin/'


WEBPACK_LOADER = {
  'DEFAULT': {
    'CACHE': not DEBUG,
    'BUNDLE_DIR_NAME': './',
    'STATS_FILE': str(BASE_DIR / 'webpack-stats.json'),
  }
}

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'