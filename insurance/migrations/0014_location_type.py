# Generated by Django 3.1.3 on 2020-11-19 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0013_delete_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.locationtype'),
        ),
    ]
