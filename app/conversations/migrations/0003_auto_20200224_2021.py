# Generated by Django 2.2.10 on 2020-02-24 11:21

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20200124_1847'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='conversation',
            managers=[
                ('objects', core.managers.CustomModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='message',
            managers=[
                ('objects', core.managers.CustomModelManager()),
            ],
        ),
    ]
