#!/bin/bash

set -o errexit
set -o nounset

echoerr() { echo "$@" 1>&2; }

python manage.py migrate

gunicorn -c  gunicorn_config.py