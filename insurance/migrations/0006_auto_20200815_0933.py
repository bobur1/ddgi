# Generated by Django 2.2.6 on 2020-08-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0005_auto_20200814_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gridcols',
            name='field',
        ),
        migrations.RemoveField(
            model_name='gridcols',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='gridcols',
            name='headerClass',
        ),
        migrations.RemoveField(
            model_name='gridcols',
            name='headerName',
        ),
        migrations.RemoveField(
            model_name='gridcols',
            name='hide',
        ),
        migrations.RemoveField(
            model_name='gridcols',
            name='resizable',
        ),
        migrations.RemoveField(
            model_name='gridcols',
            name='rowDrag',
        ),
        migrations.RemoveField(
            model_name='gridcols',
            name='sortable',
        ),
        migrations.AddField(
            model_name='gridcols',
            name='className',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='gridcols',
            name='data',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='gridcols',
            name='defaultContent',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='gridcols',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='gridcols',
            name='orderable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gridcols',
            name='searchable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gridcols',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='gridcols',
            name='type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
