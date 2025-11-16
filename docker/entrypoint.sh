#!/bin/sh

echo "Applying database migrations..."
/venv/bin/python manage.py migrate --noinput

echo "Starting application..."
exec /venv/bin/$@
