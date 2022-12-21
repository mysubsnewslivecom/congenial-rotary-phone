# Generated by Django 4.1.2 on 2022-12-18 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0017_audit_celery_task_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActionList",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Created Timestamp",
                        verbose_name="Created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Updated Timestamp",
                        verbose_name="Updated at",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="is active", verbose_name="Is active"
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                (
                    "action",
                    models.CharField(max_length=250, verbose_name="Action list"),
                ),
            ],
            options={
                "ordering": ["-name"],
                "unique_together": {("name", "action")},
            },
        ),
        migrations.CreateModel(
            name="ActionLog",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Created Timestamp",
                        verbose_name="Created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Updated Timestamp",
                        verbose_name="Updated at",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="is active", verbose_name="Is active"
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(
                        default="PENDING", max_length=50, verbose_name="status"
                    ),
                ),
                (
                    "action_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="actions",
                        to="home.actionlist",
                        verbose_name="Action id",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
