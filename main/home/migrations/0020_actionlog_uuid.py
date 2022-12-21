# Generated by Django 4.1.2 on 2022-12-18 17:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_alter_actionlog_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="actionlog",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
