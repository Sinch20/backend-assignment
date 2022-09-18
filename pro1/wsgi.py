"""
WSGI config for pro1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from wsgiref.util import application_uri
import whitenoise 

from django.core.wsgi import get_wsgi_application
from whitenoise import DjangoWhiteNoise 
application = DjangoWhiteNoise(application_uri)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')

application = get_wsgi_application()
