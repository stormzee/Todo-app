# Generated by Django 3.0.6 on 2020-11-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20201115_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
