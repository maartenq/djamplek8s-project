# djamplek8s/config/wsgi.py

import os
import pathlib

import dotenv
from django.core.wsgi import get_wsgi_application

REPO_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
ENV_FILE_PATH = REPO_DIR / ".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djamplek8s.config.settings")
application = get_wsgi_application()
