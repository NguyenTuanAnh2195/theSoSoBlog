from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField, EmailField, FileField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for The So So Blog.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    username = CharField(_("Name of User"), blank=True, null=True, max_length=255)
    first_name = CharField(blank=True, null=True, max_length=100)
    last_name = CharField(blank=True, null=True, max_length=100)
    avatar = FileField(null=True)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    country = CharField(blank=True, null=True, max_length=100)
    city = CharField(blank=True, null=True, max_length=100)
    address = CharField(blank=True, null=True, max_length=255)
    email = EmailField(blank=False, null=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
