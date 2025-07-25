from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from threading import Thread
from SOLIDIFY.accounts.models import Profile

UserModel = get_user_model()


def send_welcome_email(user_email):
    """Threaded function to send welcome email."""
    subject = "Welcome to SOLIDIFY!"
    message = (
        "Thank you for registering with us!\n\n"
        "We're excited to have you on board.\n"
        "Start exploring your account now."
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Set this in settings.py
        [user_email],
        fail_silently=False,
    )


@receiver(post_save, sender=UserModel)
def handle_user_creation(sender, instance, created, **kwargs):
    if created:
        # 1. Create profile (existing logic)
        Profile.objects.create(user=instance)

        # 2. Send welcome email in a background thread
        email_thread = Thread(
            target=send_welcome_email,
            args=(instance.email,)
        )
        email_thread.start()  # Runs async