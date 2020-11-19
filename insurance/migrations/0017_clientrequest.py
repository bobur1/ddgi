# Generated by Django 3.1.3 on 2020-11-19 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insurance', '0016_remove_insuranceoffice_is_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=100)),
                ('policy_series', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=4000, verbose_name='Причина увеличения лимитов')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='client_requests', verbose_name='Документ')),
                ('comment', models.CharField(max_length=4000, verbose_name='Комментарий')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Одобрено')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('up_on', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Назначен')),
                ('request_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.clientrequesttype', verbose_name='Тип запроса')),
                ('up_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_request_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
