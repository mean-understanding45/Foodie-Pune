# Generated by Django 3.1.7 on 2021-03-18 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20210314_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 4, 17, 23, 555896)),
        ),
    ]
