# Generated by Django 4.1.2 on 2022-11-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieflex", "0004_alter_media_sub_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="sub_category",
            field=models.CharField(
                choices=[
                    ("FANTASY", "Fantasy"),
                    ("ADVENTURE", "Adventure"),
                    ("ACTION", "Action"),
                    ("COMEDY", "Comedy"),
                    ("CRIME", "Crime"),
                    ("DRAMA", "Drama"),
                    ("SCIENCE_FICTION", "Science Fiction"),
                    ("DRAMA", "Drama"),
                    ("HORROR", "Horror"),
                ],
                max_length=250,
            ),
        ),
    ]
