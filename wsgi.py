"""
WSGI config for commerce project.
This is used by Railway deployment with Nixpacks.
"""

import os
import sys
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent

# Configure Python path to find Django apps - same as manage.py
commerce_dir = str(BASE_DIR / 'commerce')
if commerce_dir not in sys.path:
    sys.path.insert(0, commerce_dir)

# Set Django settings module to root settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Explicitly define WSGI_APPLICATION for Nixpacks detection
WSGI_APPLICATION = 'wsgi.application'