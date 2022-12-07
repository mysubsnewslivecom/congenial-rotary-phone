from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone as tz
from django.utils.translation import gettext_lazy as _

from main.utility.mixins import (
    ActiveStatusMixin,
    PrimaryIdMixin,
    StatusMixin,
    TimestampMixin,
    UUIDMixin,
)


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
    skills = models.JSONField(_("Skills"), default=dict)
    notes = models.TextField(_("Notes"))
    education = models.JSONField(_("Education"), default=dict)


class Audit(PrimaryIdMixin, TimestampMixin, UUIDMixin, StatusMixin):
    message = models.CharField(
        max_length=1000,
        verbose_name="Message",
        help_text="message",
    )
    task_id = models.CharField(_("Task Id"), blank=True, null=True, max_length=50)
    celery_task_id = models.CharField(
        _("Celery Task Id"), blank=True, null=True, max_length=50
    )

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Audit"

    def __str__(self) -> str:
        return "| ".join([str(self.id), str(self.message)])


class Category(PrimaryIdMixin, TimestampMixin, ActiveStatusMixin):
    category = models.CharField(
        max_length=250,
        verbose_name="Category",
        help_text="Category",
    )
    sub_category = models.CharField(
        max_length=250,
        verbose_name="Category",
        help_text="Category",
    )

    class Meta:
        unique_together = ["category", "sub_category"]
        ordering = ["-id"]

    def __str__(self) -> str:
        return "| ".join([str(self.category), str(self.sub_category)])
