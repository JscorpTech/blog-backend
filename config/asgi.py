import os

from django.core.asgi import get_asgi_application

asgi_application = get_asgi_application()
from config.env import env  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("DJANGO_SETTINGS_MODULE"))


application = asgi_application

