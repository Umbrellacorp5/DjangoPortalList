#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
 pip install -r ./PortalList/requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate