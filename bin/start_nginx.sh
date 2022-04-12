#!/bin/bash

# shellcheck disable=SC2016
envsubst '$STATIC_ROOT' < /webroot/app/nginx_site.conf > /etc/nginx/conf.d/django.conf
python manage.py collectstatic
nginx -g "daemon off;"