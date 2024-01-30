#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry instal
pip install -r requeriments.txt
python manage.py collectstatic --no-input
python manage.py migrate