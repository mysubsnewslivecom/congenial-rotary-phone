# Generated by Django 4.1.2 on 2022-11-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("health", "0010_dailytracker"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailytracker",
            name="date",
            field=models.DateField(auto_now=True, verbose_name="Date"),
        ),
    ]