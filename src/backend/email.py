from backend.env import config

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = config("DJANGO_EMAIL_PORT", cast=int, default=587)
EMAIL_USE_TLS = config("DJANGO_EMAIL_USE_TLS", cast=bool, default=True)
EMAIL_HOST_USER = config("DJANGO_EMAIL_HOST_USER", cast=str)
EMAIL_HOST_PASSWORD = config("DJANGO_EMAIL_HOST_PASSWORD", cast=str)
