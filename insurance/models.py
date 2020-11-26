from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

from insurance.enum import ContractType, InputType, ClientType, ApplicationFormStatus


class Position(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50)
    is_exist = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name='Тел', max_length=15, null=True, blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='users', null=True, blank=True)
    passport_number = models.CharField(verbose_name='Паспорт номер', max_length=50, null=True, blank=True)
    passport_series = models.CharField(verbose_name='Паспортная серия', max_length=50, null=True, blank=True)
    passport_given_date = models.DateField(verbose_name='Дата выдачи паспорта', blank=True, null=True)
    passport_given_by = models.CharField(verbose_name='Паспорт выдан', blank=True, null=True, max_length=128)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    document = models.FileField(upload_to='user/documents', null=True, blank=True, verbose_name='Document')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True,
                                   related_name='profile_created_by')

    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True,
                                   related_name='profile_updated_by')

    def __str__(self):
        return self.user.username


# signal receiver. when User changed or created, Profile also updated or created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Permission(models.Model):
    code_name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                              related_name='permission_updated_by')
    up_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code_name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userrole_created_by', null=True, blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.role.title)


class PermissionRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    grant = models.BooleanField(default=True)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} {}'.format(self.role.title, self.permission.title, self.grant)


class PermissionUser(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grant = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permissionuser_created_by', null=True,
                              blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.permission.__str__() + ' ' + self.user.__str__()


class ProductTypeCode(models.Model):
    code = models.CharField(verbose_name="Класс", max_length=15)
    name = models.CharField(verbose_name="Наименование", max_length=255)
    description = models.CharField(verbose_name="Описание", max_length=6000)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PolicySeriesType(models.Model):
    code = models.CharField(verbose_name="Код", max_length=24)

    cr_on = models.DateTimeField(auto_now_add=True)

    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policy_series_cr_by')

    class Meta:
        verbose_name = "Серии полиса"
        verbose_name_plural = 'Серии полисов'

    def __str__(self):
        return self.code


class PoliciesIncome(models.Model):
    act_number = models.CharField(verbose_name="Номер акта", max_length=128, unique=True)
    act_date = models.DateTimeField(verbose_name="Дата акта")

    policy_series = models.ForeignKey(PolicySeriesType,
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True, default=None,
                                      verbose_name="Серии полиса")

    policy_number_from = models.PositiveIntegerField(verbose_name="Номер полиса с", default=1)
    policy_number_to = models.PositiveIntegerField(verbose_name="Номер полиса до", default=2)
    is_free_policy = models.BooleanField(verbose_name="Свободный", default=False)

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name="policies_income_up_by")

    document = models.FileField(verbose_name="Документ", upload_to='policies_income', blank=True, null=True,
                                default=None)

    cr_on = models.DateTimeField(auto_now_add=True)

    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policies_income_cr_by')

    class Meta:
        verbose_name = 'Поступления полис'
        verbose_name_plural = 'Поступления полисы'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.act_number + " " + self.cr_by.__str__()


class ProductType(models.Model):
    code = models.CharField(verbose_name="Код", max_length=15, null=True, blank=False)

    name = models.CharField(verbose_name="Наименование", max_length=255)

    client_type = models.PositiveIntegerField(verbose_name='Тип клиента', choices=ClientType.__list__,
                                              default=ClientType.LEGAL_PERSON)

    classes = models.ManyToManyField(ProductTypeCode, default=[], blank=True, max_length=3)

    has_beneficiary = models.BooleanField(verbose_name='Has beneficiary', default=False)

    has_pledger = models.BooleanField(verbose_name='Has pledger', default=False, )

    min_acceptable_amount = models.FloatField(verbose_name="Minimum acceptable amount", default=0, blank=False,
                                              null=False)
    max_acceptable_amount = models.FloatField(verbose_name="Minimum acceptable amount", default=9999, blank=False,
                                              null=False)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name, self.code}'

    def _code_(self):
        code = self.classes[0].code
        return f'{self.code}{code}'


class Human(models.Model):
    phone = models.CharField(verbose_name="Номер телефона", max_length=14, default=None)
    first_name = models.CharField(verbose_name="Имя", max_length=128, default=None)
    last_name = models.CharField(verbose_name="Фамилия", max_length=128, default=None)
    middle_name = models.CharField(verbose_name="Отчество", max_length=128, default=None)
    address = models.CharField(verbose_name="Адрес", max_length=1024, default=None)
    passport_series = models.CharField(verbose_name='Паспортная серия', max_length=3, default=None)
    passport_number = models.CharField(verbose_name='Паспортная серия', max_length=10, default=None)
    passport_given_date = models.DateField(verbose_name='Дата выдачи паспорта', blank=True, null=True)
    passport_given_by = models.CharField(verbose_name='Паспорт выдан', blank=True, null=True, max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.passport_series}|{self.passport_number}'


class Bank(models.Model):
    name = models.CharField(verbose_name="Наименования банка", max_length=128, default=None)
    branchName = models.CharField(verbose_name="Наименования филиала", max_length=128, default=None, null=True)
    inn = models.CharField(max_length=20, null=True)
    mfo = models.CharField(max_length=6, null=True, default=None)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=14, default=None, null=True)
    address = models.CharField(verbose_name="Адрес", max_length=1024, default=None)
    checking_account = models.CharField(verbose_name="Расчётный счёт", max_length=30, default=None, null=True)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.name, self.mfo)


class LocationType(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Location(models.Model):
    series = models.CharField(max_length=10, default=None, blank=False)
    name = models.CharField(max_length=512)
    type = models.ForeignKey(LocationType, on_delete=models.SET_NULL, blank=False, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.series} - {self.name}'


class OfficeType(models.Model):
    title = models.CharField(verbose_name='Название', max_length=1024)
    description = models.CharField(verbose_name='Описание', max_length=2048)

    def __str__(self):
        return self.title


class InsuranceOffice(models.Model):
    series = models.CharField(verbose_name="Серии", max_length=10, default="AAA")

    name = models.CharField(verbose_name="Наименование", max_length=255)

    director = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='insurance_director')

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    contact = models.CharField(verbose_name='Contact', max_length=50, null=True, blank=True, default=None)

    bank = models.ManyToManyField(Bank, blank=True, default=None, max_length=3)

    office_type = models.ForeignKey(OfficeType, on_delete=models.SET_NULL, null=True, blank=True)

    location = models.CharField(verbose_name="Местонахождение", max_length=1024, default='')

    region = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    founded_date = models.DateField(verbose_name="Основан", blank=False, null=True)

    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='office_cr_by')
    up_on = models.DateTimeField(auto_now=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='office_up_by')
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OfficeWorkers(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='office_workers_user')
    office = models.ForeignKey(InsuranceOffice, on_delete=models.DO_NOTHING, related_name='office_workers_office')
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='office_workers_cr_by')
    up_on = models.DateTimeField(auto_now=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='office_workers_up_by')

    def __str__(self):
        return self.user.username + ' works at ' + self.office.name


class Currency(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=50)
    code = models.CharField(verbose_name="Код валюты", max_length=4, unique=True)
    is_exist = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.code


class BasicTariffRate(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    sum = models.BigIntegerField(verbose_name="Сумма")


class LegalClient(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    address = models.CharField(verbose_name="Адрес", max_length=150)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15)

    checking_account = models.CharField(max_length=32)

    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True)

    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='legal_client_up_by')
    up_on = models.DateTimeField(auto_now_add=True)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class IndividualClient(Human):
    checking_account = models.CharField(max_length=32)

    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True)

    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='individual_client_up_by')
    up_on = models.DateTimeField(auto_now_add=True)
    is_exist = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Beneficiary(models.Model):
    individual = models.ForeignKey(IndividualClient, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='beneficiary_individual')

    legal = models.ForeignKey(LegalClient, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='legal')

    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    cr_on = models.DateTimeField(default=timezone.now)

    up_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='beneficiary_up_by')

    up_on = models.DateTimeField(default=timezone.now)

    is_exist = models.BooleanField(default=True)

    def __str__(self):
        left_text = self.individual.__str__()
        if self.individual is None:
            left_text = self.legal.name
        return left_text + ' ' + self.legal.inn


class Policy(models.Model):
    series = models.ForeignKey(PolicySeriesType, on_delete=models.SET_NULL, null=True, blank=True)

    is_free_generated = models.BooleanField(default=False, verbose_name="Свободный")

    policy_number = models.PositiveIntegerField(verbose_name="Номер")

    product = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    client_type = models.CharField(max_length=64, null=True, blank=True, default=None)

    date_from = models.DateField(null=True, blank=True, default=None)

    date_to = models.DateField(null=True, blank=True, default=None)

    goal = models.CharField(max_length=2048, null=True, blank=True, default=None)

    zone = models.CharField(max_length=256, null=True, blank=True, default=None)

    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    pledger = models.ForeignKey(LegalClient, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    income_session = models.ForeignKey(PoliciesIncome, verbose_name="Policies income session",
                                       on_delete=models.SET_NULL,
                                       default=None, null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name="Active", null=False, blank=False)

    def __str__(self):
        return self.series.__str__() + '|' + self.policy_number.__str__()


class PolicyTransfers(models.Model):
    to_office = models.ForeignKey(InsuranceOffice, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name='policy_transfer_to_office')
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policy_transfers_cr_by')

    def __str__(self):
        return self.to_office.__str__()


class PolicyRetransfer(models.Model):
    transfer = models.ForeignKey(PolicyTransfers, on_delete=models.DO_NOTHING, null=False, blank=False,
                                 related_name='policy_retransfer_transfer_parent')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='policy_retransfer_cr_by')

    def __str__(self):
        return self.transfer.__str__()


class Dt_Option(models.Model):
    codeName = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=512, null=True, blank=True)
    dataPath = models.CharField(max_length=512, null=True, blank=True)
    draw = models.IntegerField(default=1, null=True, blank=True)
    keys = models.BooleanField(default=True)
    colReorder = models.BooleanField(default=True)
    fixedHeader = models.BooleanField(default=True)
    responsive = models.BooleanField(default=True)
    autoFill = models.BooleanField(default=True)
    serverSide = models.BooleanField(default=True)
    processing = models.BooleanField(default=True)
    scrollY = models.CharField(max_length=128, default='70vh')

    def __str__(self):
        return self.codeName


class GridCols(models.Model):
    table = models.ForeignKey(Dt_Option, on_delete=models.CASCADE, related_name='columns', null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    data = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    type = models.CharField(max_length=128, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    searchable = models.BooleanField(default=True)
    orderable = models.BooleanField(default=True)
    className = models.CharField(max_length=128, null=True, blank=True)
    defaultContent = models.CharField(max_length=1024, null=True, blank=True)
    visible = models.BooleanField(default=True)
    order_num = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['order_num']

    def __str__(self):
        return self.title


class ProductField(models.Model):
    product = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    input_type = models.PositiveIntegerField(choices=InputType.__list__, default=InputType.TEXT)
    is_required = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=4096, null=True, blank=True, default=None)

    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class PolicyFields(models.Model):
    product = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=128, null=True)
    value = models.CharField(max_length=4096, null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class ClientRequestType(models.Model):
    title = models.CharField(verbose_name='Название', max_length=1024)
    description = models.CharField(verbose_name='Описание', max_length=2048)

    def __str__(self):
        return self.title


class ClientRequest(models.Model):
    request_type = models.ForeignKey(ClientRequestType, verbose_name='Тип запроса', on_delete=models.SET_NULL,
                                     null=True, blank=True)
    policy_number = models.CharField(max_length=100, null=False, blank=False)
    policy_series = models.CharField(max_length=100, null=False, blank=False)
    reason = models.CharField(verbose_name='Причина увеличения лимитов', max_length=4000)
    file = models.FileField(verbose_name="Документ", upload_to='client_requests', blank=True, null=True, default=None)
    comment = models.CharField(verbose_name='Комментарий', max_length=4000)

    is_approved = models.BooleanField(verbose_name='Одобрено', default=False)

    assigned_to = models.ForeignKey(User, verbose_name='Назначен', on_delete=models.SET_NULL, default=None, null=True,
                                    blank=True)

    cr_on = models.DateTimeField(auto_now_add=True)
    up_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                              related_name='client_request_updated_by')
    up_on = models.DateTimeField(auto_now_add=True)


class ApplicationForm(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING, blank=False, null=False)

    legal_client = models.ForeignKey(LegalClient, on_delete=models.CASCADE, blank=True, null=True)

    individual_client = models.ForeignKey(IndividualClient, on_delete=models.CASCADE, blank=True, null=True)

    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='application_form_beneficiary')

    pledger = models.ForeignKey(LegalClient, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='application_form_pledger')

    from_time = models.DateField(verbose_name='From date')

    to_time = models.DateField(verbose_name='To date')

    contract_type = models.PositiveIntegerField(choices=ContractType.__list__,
                                                default=ContractType.CONTRACT)

    form_status = models.PositiveIntegerField(choices=ApplicationFormStatus.__list__,
                                              default=ApplicationFormStatus.ACTIVE)

    cr_on = models.DateTimeField(verbose_name='created on', default=timezone.now)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, default=None,
                                   related_name='application_form_created_by')

    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, default=None,
                                  related_name='application_form_edited_by')


class ProductApplicationField(ProductField):
    application_id = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE)
