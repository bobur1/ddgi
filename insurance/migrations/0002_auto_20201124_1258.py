# Generated by Django 3.1.3 on 2020-11-24 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationform',
            name='fields',
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='cr_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 12, 58, 20, 823932, tzinfo=utc), verbose_name='created on'),
        ),
    ]
