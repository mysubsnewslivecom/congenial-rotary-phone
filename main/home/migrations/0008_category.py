# Generated by Django 4.1.2 on 2022-11-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_rename_address2_user_address_2"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "category",
                    models.CharField(
                        help_text="Category", max_length=250, verbose_name="Category"
                    ),
                ),
                (
                    "sub_category",
                    models.CharField(
                        help_text="Category", max_length=250, verbose_name="Category"
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
                "unique_together": {("category", "sub_category")},
            },
        ),
    ]
