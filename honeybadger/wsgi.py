# This file is a part of HoneyBadger https://github.com/honeybadger/HoneyBadger
# See the file 'LICENSE' for copying permission.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "honeybadger.settings")

application = get_wsgi_application()
