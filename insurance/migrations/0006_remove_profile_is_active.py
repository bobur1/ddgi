# Generated by Django 3.0 on 2020-11-17 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0005_profile_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_active',
        ),
    ]
