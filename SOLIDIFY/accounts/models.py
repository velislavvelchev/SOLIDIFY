from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy  as _

from SOLIDIFY.accounts.managers import AppUserManager


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    # authentication logic here
    # ask for as few things as possible
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    # django admin will not work without this field
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    # vital for authentication
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    # first credential
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # used upon sending e-mails
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

class Profile(models.Model):
    # additional fields that are not vital for authentication

    user = models.OneToOneField(
        to = 'accounts.AppUser',
        on_delete=models.CASCADE,
        related_name = 'profile',
    )

    age = models.IntegerField()

    first_name = models.CharField(
        max_length = 30,
    )

    last_name = models.CharField(
        max_length=30,
    )
    # will not a direct join on the two tables

