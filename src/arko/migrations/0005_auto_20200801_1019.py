# Generated by Django 3.0.8 on 2020-08-01 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arko', '0004_auto_20200726_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='lastSeen',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 10, 19, 10, 817696)),
        ),
        migrations.AlterField(
            model_name='device',
            name='seenAgo',
            field=models.CharField(default=datetime.datetime(2020, 8, 1, 10, 19, 10, 817696), max_length=20),
        ),
    ]