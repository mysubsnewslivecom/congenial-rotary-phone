import datetime

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone as tz

from main.utility.mixins import ActiveStatusMixin, PrimaryIdMixin, TimestampMixin


class Rule(PrimaryIdMixin, ActiveStatusMixin, TimestampMixin):
    name = models.JSONField(
        help_text="Name of the rule(JSON)",
        verbose_name="Rule Name",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Rules"

    def __str__(self) -> str:
        return "| ".join(
            [str(self.id), str(self.name)],
        )

    def get_absolute_url(self):
        # return reverse("git:git_detail_view", kwargs={"id": str(self.id)})
        return reverse("health:health_list_view", args=[self.id])


class DailyTrackerManager(models.Manager):
    # def title_count(self, keyword):
    #     return self.filter(title__icontains=keyword).count()
    date_today = datetime.date.today()

    def get_daily_status(self):
        # date_today = datetime.date.today()

        # rule_ids = Rule.objects.values_list("id", flat=True)

        # for rule_id in rule_ids.iterator():
        #     rule = Rule.objects.get(id=rule_id)

        daily_st = self.filter(date=self.date_today)
        completed = daily_st.filter(status=True).values_list("rule_id", flat=True)
        pending = daily_st.filter(status=False).values_list("rule_id", flat=True)

        result = {
            "count": {"pending": pending.count(), "completed": completed.count()},
            "pending": Rule.objects.filter(id__in=pending).values_list("name", flat=True),
            "completed": Rule.objects.filter(id__in=completed).values_list("name", flat=True),
        }
        return result

    # def get_daily_status(self):
    #     query = super(DailyTrackerManager, self).get_queryset().filter(date=self.date_today).all()
    #     return query


class DailyTracker(PrimaryIdMixin, ActiveStatusMixin, TimestampMixin):
    rule_id = models.ForeignKey(
        "health.Rule",
        verbose_name=_("rule id"),
        on_delete=models.CASCADE,
        related_name="rules"
    )
    status = models.BooleanField(_("Completed"))
    date = models.DateField(_("Date"), default=tz.localdate)
    objects = DailyTrackerManager()

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "DailyTrackers"
        unique_together = ["date", "rule_id"]

    def __str__(self) -> str:
        name = str(self.rule_id.name["name"])
        completion = "Completed" if self.status else "Pending"
        return "| ".join([str(self.rule_id), str(self.date), name, completion])

    def get_absolute_url(self):
        # return reverse("git:git_detail_view", kwargs={"id": str(self.id)})
        return reverse("health:health_list_view", args=[self.id])

    def get_daily_status(self):
        date_today = datetime.date.today() - datetime.timedelta(days=1)

        # rule = Rule.objects.all()
        daily_st = DailyTracker.objects.filter(date=date_today)
        completed = daily_st.filter(status=True)
        pending = daily_st.filter(status=False)
        result = {
            "count": {"pending": pending.count(), "completed": completed.count()},
            "pending": pending,
            "completed": completed,
        }
        return result
