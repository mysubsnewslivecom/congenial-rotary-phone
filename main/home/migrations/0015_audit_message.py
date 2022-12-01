# Generated by Django 4.1.2 on 2022-11-20 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_alter_audit_task_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="audit",
            name="message",
            field=models.CharField(
                default="", help_text="message", max_length=1000, verbose_name="Message"
            ),
            preserve_default=False,
        ),
    ]