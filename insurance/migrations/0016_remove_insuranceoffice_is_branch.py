# Generated by Django 3.1.3 on 2020-11-19 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0015_auto_20201119_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insuranceoffice',
            name='is_branch',
        ),
    ]
