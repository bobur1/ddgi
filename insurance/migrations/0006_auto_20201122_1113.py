# Generated by Django 3.1.3 on 2020-11-22 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0005_productfield_input_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationform',
            name='beneficiary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.beneficiary'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='pledger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.pledger'),
        ),
        migrations.AddField(
            model_name='productfield',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producttype',
            name='max_acceptable_amount',
            field=models.FloatField(default=9999, verbose_name='Minimum acceptable amount'),
        ),
        migrations.AddField(
            model_name='producttype',
            name='min_acceptable_amount',
            field=models.FloatField(default=0, verbose_name='Minimum acceptable amount'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='contract_type',
            field=models.CharField(choices=[(1, 'Leasing'), (2, 'Loan')], default=(2, 'Loan'), max_length=20),
        ),
    ]
