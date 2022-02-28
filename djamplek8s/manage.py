#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import pathlib
import sys

import dotenv

REPO_DIR = pathlib.Path(__file__).resolve().parent.parent
ENV_FILE_PATH = REPO_DIR / ".env"


def main():
    """Run administrative tasks."""
    dotenv.read_dotenv(str(ENV_FILE_PATH))
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "djamplek8s.config.settings"
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
