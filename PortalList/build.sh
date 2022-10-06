#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
 pip install -r ./PortalList/requirements.txt

python ./PortalList/manage.py collectstatic --no-input
python ./PortalList/manage.py migrate