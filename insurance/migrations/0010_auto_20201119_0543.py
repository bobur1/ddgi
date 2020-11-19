# Generated by Django 3.1.3 on 2020-11-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0009_insuranceoffice_parent_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Название')),
                ('description', models.CharField(max_length=2048, verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='officetype',
            name='description',
            field=models.CharField(max_length=2048, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='officetype',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='Название'),
        ),
    ]