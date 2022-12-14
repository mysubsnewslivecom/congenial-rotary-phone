# Generated by Django 4.1.4 on 2022-12-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemProperty',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created Timestamp', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated Timestamp', verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='is active', verbose_name='Is active')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name', max_length=250, verbose_name='Name')),
                ('value', models.JSONField(help_text='Value', verbose_name='Value')),
            ],
            options={
                'verbose_name_plural': 'SystemProperties',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
    ]
