# Generated by Django 4.1.2 on 2022-11-07 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movflex", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="media",
            options={"ordering": ["-id"], "verbose_name_plural": "Media"},
        ),
        migrations.AlterModelOptions(
            name="watching",
            options={"ordering": ["-id"], "verbose_name_plural": "Watching"},
        ),
    ]
