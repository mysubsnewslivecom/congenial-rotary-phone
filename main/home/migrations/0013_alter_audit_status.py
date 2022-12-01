# Generated by Django 4.1.2 on 2022-11-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_alter_audit_status_alter_user_education_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audit",
            name="status",
            field=models.CharField(
                choices=[
                    ("ERROR", "ERROR"),
                    ("SUCCESS", "SUCCESS"),
                    ("IN_PROGRESS", "IN-PROGRESS"),
                    ("CREATED", "CREATED"),
                    ("COMPLETED", "COMPLETED"),
                    ("SKIPPED", "SKIPPED"),
                    ("INFO", "INFO"),
                    ("DEBUG", "DEBUG"),
                ],
                max_length=15,
                verbose_name="Status",
            ),
        ),
    ]