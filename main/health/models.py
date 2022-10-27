from django.db import models
from django.urls import reverse

from main.utility.mixins import ActiveStatusMixin, PrimaryIdMixin, TimestampMixin


class Rule(PrimaryIdMixin, ActiveStatusMixin, TimestampMixin):
    name = models.JSONField(
        help_text="Name of the rule(JSON)", verbose_name="Rule Name"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Rules"

    def __str__(self) -> str:
        return "".join(
            str(self.name),
        )

    def get_absolute_url(self):
        # return reverse("git:git_detail_view", kwargs={"id": str(self.id)})
        return reverse("health:health_list_view", args=[self.id])
