
"""
WSGI config for Proyecto_Sysforum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/opt/bitnami/apps/django/django_projects/Proyecto_Sysforum')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/Proyecto_Sysforum/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proyecto_Sysforum.settings")
from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
