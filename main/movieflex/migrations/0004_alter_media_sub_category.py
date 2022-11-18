# Generated by Django 4.1.2 on 2022-11-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieflex", "0003_alter_watching_current_watch"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="sub_category",
            field=models.CharField(
                choices=[
                    ("FANTASY", "Fantasy"),
                    ("ACTION", "Action"),
                    ("ACTION", "Action"),
                    ("COMEDY", "Comedy"),
                ],
                max_length=250,
            ),
        ),
    ]
