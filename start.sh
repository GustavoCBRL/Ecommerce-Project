#!/usr/bin/env bash
# Railway startup script

set -e

echo "🚀 Starting Railway deployment..."

# Navigate to the Django project directory
cd commerce

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