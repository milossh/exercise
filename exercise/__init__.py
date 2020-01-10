# This will make sure the Celery app is always imported when
# Django starts so that task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)