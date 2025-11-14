#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

if [ "$ENV" = "production" ]; then
    echo "Starting Gunicorn server..."
    gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
    echo "Starting development server..."
    python manage.py runserver 0.0.0.0:8000
fi