# Generated by Django 4.1.2 on 2022-11-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_alter_audit_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="audit",
            name="celery_task_id",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Celery Task Id"
            ),
        ),
    ]