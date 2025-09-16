"""
WSGI config for happyshowchoir project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'happyshowchoir.settings')

application = get_wsgi_application()


