# Generated by Django 4.1.2 on 2022-10-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_user_address_user_address2_user_city_user_country_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="state",
            field=models.CharField(max_length=300, null=True),
        ),
    ]