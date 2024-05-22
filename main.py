import os
import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

PATHS = [str(BASE_DIR / "src"),]

sys.path.extend(PATHS)

os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"

import django

django.setup()

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
