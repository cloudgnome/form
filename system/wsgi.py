"""
WSGI config for igrushec project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/usr/local/lib/python3.5/site-packages/django/')
sys.path.append('/home/form/form/')
sys.path.append('/usr/local/lib/python3.5/site-packages/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")

application = get_wsgi_application()