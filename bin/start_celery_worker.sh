#!/bin/bash

set -o errexit
set -o nounset

celery -A zwb_lucky worker -l INFO