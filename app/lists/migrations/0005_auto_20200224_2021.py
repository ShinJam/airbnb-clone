# Generated by Django 2.2.10 on 2020-02-24 11:21

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20200218_1538'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='list',
            managers=[
                ('objects', core.managers.CustomModelManager()),
            ],
        ),
    ]
