from .base import * 
from .developement import *
import os

DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DATABASES['default']['ATOMIC_REQUESTS'] = True

ALLOWED_HOSTS = [str(os.environ.get('YOUR_DOMAIN'))]

STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

ADMIN_URL = str(os.environ.get('ADMIN_URL'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': str(os.environ.get('DB_NAME')),
        'USER': str(os.environ.get('DB_USER')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD')),
        'HOST': int(os.environ.get('DB_HOST')),
    }
}

SERVER_EMAIL = os.environ.get('SERVER_EMAIL')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', '3600'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

WEBPACK_LOADER['DEFAULT']['CACHE'] = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'