#!/usr/bin/env bash
# Render build script
set -o errexit  # Exit on any error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata seed_data.json
python manage.py createsuperuser --noinput || true