#!/bin/bash

set -o errexit
set -o nounset

if [ -f './celerybeat.pid' ]; then
  rm -f './celerybeat.pid'
fi

celery -A zwb_lucky beat -l INFO