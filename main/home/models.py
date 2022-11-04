from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone as tz

from main.utility.mixins import PrimaryIdMixin, TimestampMixin, UUIDMixin


class User(AbstractUser):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(null=True, blank=True, default="default.jpg")
    bio = models.TextField(blank=True)
    headline = models.CharField(max_length=300)
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    friends = models.IntegerField(default=0)
    articles = models.IntegerField(default=0)
    # profile_picture = models.URLField(blank=True)
    date_of_birth = models.DateField(default="1990-01-01")
    is_admin = models.BooleanField(default=False)
    last_modified = models.DateTimeField(
        default=tz.now,
        verbose_name="Blog updated on",
        help_text="Updated Timestamp",
    )
    address = models.CharField(max_length=300, null=True)
    address_2 = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=300, null=True)
    country = models.CharField(max_length=300, null=True)
    zip = models.CharField(max_length=300, null=True)


class Audit(PrimaryIdMixin, TimestampMixin, UUIDMixin):
    message = models.CharField(
        max_length=1000,
        verbose_name="Message",
        help_text="message",
    )
