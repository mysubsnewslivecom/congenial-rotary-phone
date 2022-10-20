from django.db import models
from django.urls import reverse

from main.home.models import ActiveStatusMixin, PrimaryIdMixin, TimestampMixin


class ProjectDetail(PrimaryIdMixin, TimestampMixin, ActiveStatusMixin):
    GIT_CHOICES = [("gitlab", "Gitlab"), ("github", "Github")]
    name = models.CharField(
        max_length=50, help_text="Project Name", verbose_name="Project Name"
    )
    project_id = models.IntegerField(help_text="Project id", verbose_name="Project id")
    url = models.URLField(max_length=300, help_text="Git URL", verbose_name="Git URL")
    git = models.CharField(
        choices=GIT_CHOICES,
        max_length=200,
        verbose_name="Git",
        help_text="Git",
        default="Github",
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> str:
        return "".join(
            str(self.name),
        )

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"id": str(self.id)})

    def as_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "git": self.git,
            "project_id": self.project_id,
            "id": self.id,
        }
