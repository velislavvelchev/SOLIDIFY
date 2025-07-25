from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from SOLIDIFY.accounts.models import Profile
from SOLIDIFY.common.utils import EmailThread

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def handle_user_creation(sender, instance, created, **kwargs):
    if created:
        # 1. Create profile
        Profile.objects.create(user=instance)

        # 2. Send welcome email async using reusable EmailThread
        subject = "Welcome to SOLIDIFY!"
        message = (
            "Thank you for registering with us!\n\n"
            "We're excited to have you on board.\n"
            "Start exploring your account now."
        )

        EmailThread(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email]
        ).start()

        print("📩 Welcome email signal triggered for:", instance.email)

