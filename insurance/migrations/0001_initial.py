# Generated by Django 3.1.3 on 2020-11-24 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128, verbose_name='Наименования банка')),
                ('branchName', models.CharField(default=None, max_length=128, null=True, verbose_name='Наименования филиала')),
                ('inn', models.CharField(max_length=20, null=True)),
                ('mfo', models.CharField(default=None, max_length=6, null=True)),
                ('phone_number', models.CharField(default=None, max_length=14, null=True, verbose_name='Номер телефона')),
                ('address', models.CharField(default=None, max_length=1024, verbose_name='Адрес')),
                ('checking_account', models.CharField(default=None, max_length=30, null=True, verbose_name='Расчётный счёт')),
                ('is_exist', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BasicTariffRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('sum', models.BigIntegerField(verbose_name='Сумма')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_client_title', models.CharField(default=None, help_text='This field should be set if beneficiary is legal client', max_length=128, null=True, verbose_name='Наименование')),
                ('address', models.CharField(default=None, help_text='This field should be set if beneficiary is legal client', max_length=1024, null=True, verbose_name='Адрес')),
                ('phone', models.CharField(default=None, help_text='This field should be set if beneficiary is legal client', max_length=14, null=True, verbose_name='Номер телефона')),
                ('fax_number', models.CharField(max_length=64, null=True)),
                ('checking_account', models.CharField(max_length=64, null=True)),
                ('inn', models.CharField(max_length=20, null=True)),
                ('mfo', models.CharField(blank=True, default=None, max_length=6, null=True)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beneficiary_bank', to='insurance.bank')),
            ],
        ),
        migrations.CreateModel(
            name='ClientRequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Название')),
                ('description', models.CharField(max_length=2048, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Код валюты')),
                ('is_exist', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Dt_Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeName', models.CharField(max_length=128, unique=True)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('dataPath', models.CharField(blank=True, max_length=512, null=True)),
                ('draw', models.IntegerField(blank=True, default=1, null=True)),
                ('keys', models.BooleanField(default=True)),
                ('colReorder', models.BooleanField(default=True)),
                ('fixedHeader', models.BooleanField(default=True)),
                ('responsive', models.BooleanField(default=True)),
                ('autoFill', models.BooleanField(default=True)),
                ('serverSide', models.BooleanField(default=True)),
                ('processing', models.BooleanField(default=True)),
                ('scrollY', models.CharField(default='70vh', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default=None, max_length=14, verbose_name='Номер телефона')),
                ('first_name', models.CharField(default=None, max_length=128, verbose_name='Имя')),
                ('last_name', models.CharField(default=None, max_length=128, verbose_name='Фамилия')),
                ('middle_name', models.CharField(default=None, max_length=128, verbose_name='Отчество')),
                ('address', models.CharField(default=None, max_length=1024, verbose_name='Адрес')),
                ('passport_series', models.CharField(default=None, max_length=3, verbose_name='Паспортная серия')),
                ('passport_number', models.CharField(default=None, max_length=10, verbose_name='Паспортная серия')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(default='AAA', max_length=10, verbose_name='Серии')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('contact', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Contact')),
                ('location', models.CharField(default='', max_length=1024, verbose_name='Местонахождение')),
                ('founded_date', models.DateField(null=True, verbose_name='Основан')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('up_on', models.DateTimeField(auto_now=True)),
                ('is_exist', models.BooleanField(default=True)),
                ('bank', models.ManyToManyField(blank=True, default=None, max_length=3, to='insurance.Bank')),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='office_cr_by', to=settings.AUTH_USER_MODEL)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insurance_director', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Название')),
                ('description', models.CharField(max_length=2048, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('up_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('up_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permission_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fax_number', models.CharField(max_length=32)),
                ('checking_account', models.CharField(max_length=32)),
                ('inn', models.CharField(max_length=20, null=True)),
                ('mfo', models.CharField(max_length=6, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.bank')),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.human')),
            ],
        ),
        migrations.CreateModel(
            name='PoliciesIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_number', models.CharField(max_length=128, unique=True, verbose_name='Номер акта')),
                ('act_date', models.DateTimeField(verbose_name='Дата акта')),
                ('policy_number_from', models.PositiveIntegerField(default=1, verbose_name='Номер полиса с')),
                ('policy_number_to', models.PositiveIntegerField(default=2, verbose_name='Номер полиса до')),
                ('is_free_policy', models.BooleanField(default=False, verbose_name='Свободный')),
                ('document', models.FileField(blank=True, default=None, null=True, upload_to='policies_income', verbose_name='Документ')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policies_income_cr_by', to=settings.AUTH_USER_MODEL)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policies_income_up_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Поступления полис',
                'verbose_name_plural': 'Поступления полисы',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free_generated', models.BooleanField(default=False, verbose_name='Свободный')),
                ('policy_number', models.PositiveIntegerField(verbose_name='Номер')),
                ('client_type', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('date_from', models.DateField(blank=True, default=None, null=True)),
                ('date_to', models.DateField(blank=True, default=None, null=True)),
                ('goal', models.CharField(blank=True, default=None, max_length=2048, null=True)),
                ('zone', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('beneficiary', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.beneficiary')),
                ('income_session', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policiesincome', verbose_name='Policies income session')),
                ('pledger', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.pledger')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('is_exist', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должность',
            },
        ),
        migrations.CreateModel(
            name='ProductTypeCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, verbose_name='Класс')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.CharField(max_length=6000, verbose_name='Описание')),
                ('is_exist', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userrole_created_by', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.role')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Тел')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users', verbose_name='Фото')),
                ('passport_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Паспорт номер')),
                ('passport_series', models.CharField(blank=True, max_length=50, null=True, verbose_name='Паспортная серия')),
                ('passport_given_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи паспорта')),
                ('passport_given_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Паспорт выдан')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('document', models.FileField(blank=True, null=True, upload_to='user/documents', verbose_name='Document')),
                ('created_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_created_by', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.position', verbose_name='Должность')),
                ('updated_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('client_type', models.PositiveIntegerField(choices=[(1, 'Физическое лицо'), (2, 'Юридик лицо')], default=(2, 'Юридик лицо'), max_length=50, verbose_name='Тип клиента')),
                ('has_beneficiary', models.BooleanField(default=False, verbose_name='Has beneficiary')),
                ('has_pledger', models.BooleanField(default=False, verbose_name='Has pledger')),
                ('min_acceptable_amount', models.FloatField(default=0, verbose_name='Minimum acceptable amount')),
                ('max_acceptable_amount', models.FloatField(default=9999, verbose_name='Minimum acceptable amount')),
                ('is_exist', models.BooleanField(default=True)),
                ('classes', models.ManyToManyField(blank=True, default=[], max_length=3, to='insurance.ProductTypeCode')),
            ],
        ),
        migrations.CreateModel(
            name='ProductField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
                ('input_type', models.PositiveIntegerField(choices=[(1, 'Text'), (2, 'Number'), (3, 'Single selection'), (4, 'Multi selection'), (5, 'Currency')], default=(1, 'Text'), max_length=128)),
                ('is_required', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128)),
                ('value', models.CharField(blank=True, default=None, max_length=4096, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyTransfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policy_transfers_cr_by', to=settings.AUTH_USER_MODEL)),
                ('policy', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policy')),
                ('to_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policy_transfer_to_office', to='insurance.insuranceoffice')),
            ],
        ),
        migrations.CreateModel(
            name='PolicySeriesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=24, verbose_name='Код')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policy_series_cr_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Серии полиса',
                'verbose_name_plural': 'Серии полисов',
            },
        ),
        migrations.CreateModel(
            name='PolicyRetransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policy_retransfer_cr_by', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='policy_retransfer_transfer_parent', to='insurance.policytransfers')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=128, null=True)),
                ('value', models.CharField(blank=True, default=None, max_length=4096, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.producttype')),
            ],
        ),
        migrations.AddField(
            model_name='policy',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.producttype'),
        ),
        migrations.AddField(
            model_name='policy',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policyseriestype'),
        ),
        migrations.AddField(
            model_name='policiesincome',
            name='policy_series',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policyseriestype', verbose_name='Серии полиса'),
        ),
        migrations.CreateModel(
            name='PermissionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant', models.BooleanField(default=False)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissionuser_created_by', to=settings.AUTH_USER_MODEL)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant', models.BooleanField(default=True)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.role')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeWorkers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('up_on', models.DateTimeField(auto_now=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='office_workers_cr_by', to=settings.AUTH_USER_MODEL)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='office_workers_office', to='insurance.insuranceoffice')),
                ('up_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='office_workers_up_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='office_workers_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(default=None, max_length=10)),
                ('name', models.CharField(max_length=512)),
                ('is_active', models.BooleanField(default=True)),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.locationtype')),
            ],
        ),
        migrations.CreateModel(
            name='LegalClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('mfo', models.CharField(blank=True, default=None, max_length=6, null=True, verbose_name='MFO')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('up_on', models.DateTimeField(auto_now_add=True)),
                ('is_exist', models.BooleanField(default=True)),
                ('cr_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('up_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='legal_client_up_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fax_number', models.CharField(max_length=32)),
                ('checking_account', models.CharField(max_length=32)),
                ('bank_name', models.CharField(max_length=256, null=True)),
                ('inn', models.CharField(max_length=20, null=True)),
                ('mfo', models.CharField(max_length=6, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.human')),
            ],
        ),
        migrations.AddField(
            model_name='insuranceoffice',
            name='office_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.officetype'),
        ),
        migrations.AddField(
            model_name='insuranceoffice',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.insuranceoffice'),
        ),
        migrations.AddField(
            model_name='insuranceoffice',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.location'),
        ),
        migrations.AddField(
            model_name='insuranceoffice',
            name='up_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='office_up_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='IndividualClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('up_on', models.DateTimeField(auto_now_add=True)),
                ('is_exist', models.BooleanField(default=True)),
                ('cr_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.human')),
                ('up_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='individual_client_up_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GridCols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('data', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('type', models.CharField(blank=True, max_length=128, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('searchable', models.BooleanField(default=True)),
                ('orderable', models.BooleanField(default=True)),
                ('className', models.CharField(blank=True, max_length=128, null=True)),
                ('defaultContent', models.CharField(blank=True, max_length=1024, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('order_num', models.IntegerField(blank=True, null=True)),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='insurance.dt_option')),
            ],
            options={
                'ordering': ['order_num'],
            },
        ),
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
        migrations.AddField(
            model_name='beneficiary',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.human'),
        ),
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.DateField(verbose_name='From date')),
                ('to_time', models.DateField(verbose_name='To date')),
                ('contract_type', models.PositiveIntegerField(choices=[(1, 'Leasing'), (2, 'Loan')], default=(2, 'Loan'), max_length=20)),
                ('beneficiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.beneficiary')),
                ('fields', models.ManyToManyField(blank=True, null=True, to='insurance.ProductField')),
                ('individual_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.individualclient')),
                ('legal_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.legalclient')),
                ('pledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.pledger')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='insurance.producttype')),
            ],
        ),
    ]
