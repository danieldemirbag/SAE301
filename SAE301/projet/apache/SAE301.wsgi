import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'SAE301.settings'

path = '/var/www/SAE301'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
