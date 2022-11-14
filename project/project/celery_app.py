import os

from celery import Celery as AppCelery

# class MyCelery(Celery):
#
#     def gen_task_name(self, name, module):
#         if module.endswith('.tasks'):
#             module = module[:-6]
#         return super().gen_task_name(name, module)
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.prod')

app = AppCelery('project')

app.conf.update(accept_content=['json'])

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()