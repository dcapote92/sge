#!/bin/sh

python manage.py migrate --noinput

# Execute the command on Dockerfile CMD
exec "$@"