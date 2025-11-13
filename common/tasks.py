import sentry_sdk
from celery import shared_task


@shared_task
def log_event_to_sentry(event_type: str, message: str):
    sentry_sdk.logger.info(f"{event_type}: {message}")
