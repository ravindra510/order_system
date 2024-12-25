from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_system.settings')

app = Celery('order_system')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app = Celery('order_system')

app.conf.beat_schedule = {
    'daily-task': {
        'task': 'order_system.tasks.daily_task',
        'schedule': crontab(minute=30, hour=14),
    },
}