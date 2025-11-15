#!/bin/sh

echo "Waiting for PostgreSQL to be ready..."
python << END
import sys
import time
from django.db import connection

for i in range(30):
    try:
        connection.ensure_connection()
        print("PostgreSQL is ready!")
        break
    except Exception:
        print(f"Waiting for PostgreSQL... ({i+1}/30)")
        time.sleep(2)
else:
    print("PostgreSQL not available after 60 seconds")
    sys.exit(1)
END

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Starting application..."
exec "$@"