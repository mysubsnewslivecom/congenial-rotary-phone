# Generated by Django 4.1.2 on 2022-10-29 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_user_state"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="address2",
            new_name="address_2",
        ),
    ]