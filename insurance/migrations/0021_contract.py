# Generated by Django 3.1.3 on 2020-11-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0020_auto_20201120_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
