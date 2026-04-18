from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True, max_retries=3)
def send_welcome_email_task(self, user_email):
    subject = 'Welcome to SkillShare Pro'
    message = 'Hi, thank you for registering on our platform. We are glad to have you!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    try:
        # Email Seand in Fucnction
        send_mail(subject, message, email_from, recipient_list)
        return f"Email sent to {user_email}"
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)