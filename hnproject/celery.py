from __future__ import absolute_import, unicode_literals

import os
from celery.schedules import crontab
from time import timezone
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hnproject.settings')

app = Celery('hnproject')
app.config_from_object('django.conf:settings', namespace='CELERY')

# celerybeat schedule
app.conf.beat_schedule = {
  
}

# set time zone
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Lagos')

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')