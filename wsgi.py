"""
WSGI config for commerce project in root directory.
This is used by Railway deployment.
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add commerce directory to Python path
commerce_dir = os.path.join(os.path.dirname(__file__), 'commerce')
if commerce_dir not in sys.path:
    sys.path.insert(0, commerce_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commerce.settings')

application = get_wsgi_application()