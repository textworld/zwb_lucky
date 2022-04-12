
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zwb_lucky.settings.dev')

app = Celery('zwb_lucky')
app.config_from_object(os.environ.get('DJANGO_SETTINGS_MODULE'), namespace='CELERY')
app.autodiscover_tasks()
platforms.C_FORCE_ROOT = True

app.conf.beat_schedule = {
    'make_lucky': {
        'task': 'home.tasks.make_lucky',
        'schedule': crontab( minute='0', hour='10', day_of_week='0,2,4')
    },
    'echo_hello': {
        'task': 'home.tasks.echo_hello',
        'schedule': crontab(minute='*', hour='0-23') 
    }
}
