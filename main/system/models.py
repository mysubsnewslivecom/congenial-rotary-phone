from django.db import models

from main.utility.mixins import ActiveStatusMixin, PrimaryIdMixin, TimestampMixin


class SystemProperty(PrimaryIdMixin, ActiveStatusMixin, TimestampMixin):
    name = models.CharField(
        max_length=250,
        verbose_name="Name",
        help_text="Name",
    )
    value = models.JSONField(
        verbose_name="Value",
        help_text="Value",
    )

    class Meta:
        unique_together = ["name"]
        ordering = ["-id"]
        verbose_name_plural = "SystemProperties"

    def __str__(self) -> str:
        return "| ".join([str(self.name)])
