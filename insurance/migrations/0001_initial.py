# Generated by Django 2.2.6 on 2020-08-02 13:45

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
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('mfo', models.CharField(max_length=8, verbose_name='МФО банка')),
                ('inn', models.CharField(max_length=10, verbose_name='ИНН')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('checking_account', models.CharField(max_length=30, verbose_name='Расчётный счёт')),
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
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='ClientPhysical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middlename', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('checking_account', models.CharField(max_length=30, verbose_name='Расчётный счёт')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('code', models.CharField(max_length=4, verbose_name='Код валюты')),
            ],
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeName', models.CharField(max_length=128, unique=True)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('dataPath', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.IntegerField(verbose_name='Номер договора')),
                ('contract_date', models.DateTimeField(verbose_name='Дата договора')),
                ('client_id', models.BigIntegerField()),
                ('client_type', models.CharField(max_length=1, verbose_name='Тип клиента')),
                ('loan_agreement', models.CharField(max_length=150, verbose_name='Кредитный договор')),
                ('property_name', models.CharField(max_length=100, verbose_name='Имя имущества')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('insurance_cost', models.BigIntegerField(verbose_name='Страховая стоимость')),
                ('insurance_sum', models.BigIntegerField(verbose_name='Страховая сумма')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('franchise', models.CharField(max_length=100, verbose_name='Франшиза')),
                ('original', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='LegalClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
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
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должность',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
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
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.Role')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.BigIntegerField()),
                ('client_type', models.CharField(max_length=1, verbose_name='Тип клиента')),
                ('sum', models.BigIntegerField(verbose_name='Сумма')),
                ('time', models.DateField(auto_now_add=True)),
                ('client_checking_account', models.CharField(max_length=30, verbose_name='Расчётный счёт клиента')),
                ('comments', models.TextField()),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.Bank')),
                ('bank_checking_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.CompanyBankAccount', verbose_name='Расчётный счёт')),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.InsuranceContract')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Тел')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users', verbose_name='Фото')),
                ('passport', models.CharField(blank=True, max_length=50, null=True, verbose_name='Паспорт')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.Position', verbose_name='Должность')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.IntegerField(verbose_name='Номер договора')),
                ('property_name', models.CharField(max_length=100, verbose_name='Имя имущества')),
                ('loan_agreement', models.CharField(max_length=150, verbose_name='Кредитный договор')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('insurance_case', models.CharField(max_length=100, verbose_name='Страховой случае')),
                ('insurance_sum', models.BigIntegerField(verbose_name='Страховая сумма')),
                ('franchise', models.CharField(max_length=100, verbose_name='Франшиза')),
                ('total_prize', models.BigIntegerField(verbose_name=' Общая страховая премия')),
                ('paid_insurance_prize', models.BigIntegerField(verbose_name='Оплаченная страховая премия')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('policy_date', models.DateField(verbose_name='Дата полиса')),
                ('issue_date', models.DateField(verbose_name='Дата выдачи')),
                ('original', models.TextField()),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.InsuranceContract')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant', models.BooleanField(default=False)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissionuser_created_by', to=settings.AUTH_USER_MODEL)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.Permission')),
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
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.Role')),
            ],
        ),
        migrations.CreateModel(
            name='GridCols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headerName', models.CharField(blank=True, max_length=512, null=True)),
                ('field', models.CharField(blank=True, max_length=512, null=True)),
                ('sortable', models.BooleanField(default=False)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('grid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colDefs', to='insurance.Grid')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('property_name', models.CharField(max_length=100, verbose_name='Имя имущества')),
                ('client_id', models.BigIntegerField()),
                ('client_type', models.CharField(max_length=1, verbose_name='Тип клиента')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('insurance_cost', models.BigIntegerField(verbose_name='Страховая стоимость')),
                ('insurance_sum', models.BigIntegerField(verbose_name='Страховая сумма')),
                ('anti_fire_stuff', models.SmallIntegerField(verbose_name='Наличие пожарной сигнализации и средств пожаротушения')),
                ('security_stuff', models.SmallIntegerField(verbose_name='Наличие охранной сигнализации и средств защиты')),
                ('payment_type', models.CharField(max_length=1, verbose_name='Вид оплаты')),
                ('payment_currency', models.CharField(max_length=4, verbose_name='Валюта оплаты')),
                ('insurer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Страхователь')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
