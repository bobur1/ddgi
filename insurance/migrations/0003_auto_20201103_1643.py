# Generated by Django 3.0 on 2020-11-03 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20201103_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.Human'),
        ),
        migrations.AddField(
            model_name='pledger',
            name='person',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.Human'),
        ),
        migrations.AlterField(
            model_name='human',
            name='address',
            field=models.CharField(default=None, max_length=1024),
        ),
        migrations.AlterField(
            model_name='human',
            name='first_name',
            field=models.CharField(default=None, max_length=128),
        ),
        migrations.AlterField(
            model_name='human',
            name='last_name',
            field=models.CharField(default=None, max_length=128),
        ),
        migrations.AlterField(
            model_name='human',
            name='middle_name',
            field=models.CharField(default=None, max_length=128),
        ),
        migrations.AlterField(
            model_name='human',
            name='phone',
            field=models.CharField(default=None, max_length=14, verbose_name='Phone'),
        ),
    ]
