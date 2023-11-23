import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'weekly_last_news': {
        'task': 'newsapp.tasks.weekly_send_emails',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'options': {'queue': 'weekly_news'},
    },
}

app.autodiscover_tasks()
