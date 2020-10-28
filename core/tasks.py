from celery import shared_task

from core.task_modules.send_email import send_email_to_me
from portfolio_api.settings import DEBUG

@shared_task(autoretry_for=(Exception, ), retry_backoff=True, max_retries=5 if not DEBUG else 0)
def send_submission_notice(*args, **kwargs):
    send_email_to_me(*args, **kwargs)

