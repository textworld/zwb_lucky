#!/bin/bash

# shellcheck disable=SC2016
rm /etc/nginx/sites-enabled/default
envsubst '$STATIC_ROOT' < /webroot/app/nginx_site.conf > /etc/nginx/sites-enabled/django.conf
python manage.py collectstatic
nginx -g "daemon off;"