#!/usr/bin/env bash
# Railway startup script

set -e

echo "🚀 Starting Railway deployment..."

# Get the current directory and find the Django project
CURRENT_DIR=$(pwd)
echo "📁 Current directory: $CURRENT_DIR"

# Check if we're in the right directory structure
if [ -f "commerce/manage.py" ]; then
    echo "✅ Found manage.py in commerce/ subdirectory"
    cd commerce
elif [ -f "manage.py" ]; then
    echo "✅ Found manage.py in current directory"
else
    echo "❌ Cannot find manage.py. Directory structure:"
    ls -la
    if [ -d "commerce" ]; then
        echo "Contents of commerce directory:"
        ls -la commerce/
    fi
    exit 1
fi

DJANGO_DIR=$(pwd)
echo "📁 Django project directory: $DJANGO_DIR"

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

echo "🔍 Checking Django configuration..."
python manage.py check --deploy

echo "✅ Starting Gunicorn server..."
exec gunicorn commerce.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers ${WEB_CONCURRENCY:-3} \
    --worker-class gevent \
    --worker-connections ${WORKER_CONNECTIONS:-1000} \
    --timeout ${TIMEOUT:-120} \
    --keep-alive ${KEEP_ALIVE:-2} \
    --max-requests ${MAX_REQUESTS:-1000} \
    --max-requests-jitter ${MAX_REQUESTS_JITTER:-100} \
    --log-level ${LOG_LEVEL:-info} \
    --access-logfile - \
    --error-logfile -