"""
WSGI config for yooablog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from dotenv import load_dotenv
project_folder = os.path.expanduser('~/yooablog')
load_dotenv(os.path.join(project_folder, '.env'))

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yooablog.settings.dev")

application = get_wsgi_application()
