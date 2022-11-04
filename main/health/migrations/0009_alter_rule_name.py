# Generated by Django 4.1.2 on 2022-10-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("health", "0008_alter_rule_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rule",
            name="name",
            field=models.JSONField(
                help_text="Name of the rule(JSON)", verbose_name="Rule Name"
            ),
        ),
    ]
