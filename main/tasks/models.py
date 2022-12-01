from django.db import models

from main.utility.mixins import PrimaryIdMixin, TimestampMixin, ActiveStatusMixin
from django.utils.translation import gettext_lazy as _


class Todo(PrimaryIdMixin, TimestampMixin, ActiveStatusMixin):
    name = models.CharField(_("Task Name"), max_length=50)
    status = models.BooleanField(_("Status"), default=False)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Todo"

    def __str__(self) -> str:
        return "".join(str(self.name))
