# Generated by Django 4.1.2 on 2022-10-20 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_uuidmixin"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UUIDMixin",
        ),
    ]
