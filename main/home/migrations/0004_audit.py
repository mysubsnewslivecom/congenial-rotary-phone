# Generated by Django 4.1.2 on 2022-10-25 23:15

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_delete_uuidmixin"),
    ]

    operations = [
        migrations.CreateModel(
            name="Audit",
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
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "message",
                    models.CharField(
                        help_text="message", max_length=1000, verbose_name="Message"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]