import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone as tz


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


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
        help_text="Created Timestamp",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
        help_text="Updated Timestamp",
    )

    class Meta:
        """Setting up the abstract model class"""

        abstract = True


class ActiveStatusMixin(models.Model):
    is_active = models.BooleanField(
        default=True, verbose_name="Is active", help_text="is active"
    )

    class Meta:
        """Setting up the abstract model class"""

        abstract = True


class PrimaryIdMixin(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        """Setting up the abstract model class"""

        abstract = True


class UUIDMixin(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        """Setting up the abstract model class"""

        abstract = True
