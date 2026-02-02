"""
Django settings for Railway Nixpacks deployment.
This file imports the original settings and ensures WSGI_APPLICATION is properly configured.
"""

import os
import sys
from pathlib import Path

# Add commerce directory to path
BASE_DIR = Path(__file__).resolve().parent
commerce_dir = str(BASE_DIR / 'commerce')
if commerce_dir not in sys.path:
    sys.path.insert(0, commerce_dir)

# Import all settings from the original commerce.settings
from commerce.settings import *

# Explicitly define WSGI_APPLICATION for Nixpacks
WSGI_APPLICATION = 'wsgi.application'

# Ensure the commerce directory is in INSTALLED_APPS path
import django
from django.conf import settings