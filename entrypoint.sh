#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

APP_PORT=${PORT:-8000}

if [ "$ENV" = "production" ]; then
    echo "Starting Gunicorn server..."
    gunicorn config.wsgi:application --bind 0.0.0.0:$APP_PORT
else
    echo "Starting development server..."
    python manage.py runserver 0.0.0.0:$APP_PORT
fi